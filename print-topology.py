#!/usr/bin/env python3
"""
Print Network Topology from Packet Tracer

This script connects to a Packet Tracer instance and prints out the network topology,
including all devices and their connections (links).

Uses binary encoding and cleartext authentication for simplicity.
Verified working with PT 8.2.2
"""

import uuid
import time
import socket
import struct

# Constants
PTMP_IDENTIFIER = "PTMP"
PTMP_VERSION = 1
DEFAULT_IPC_PORT = 39000
TEXT_ENCODING = 1
BINARY_ENCODING = 2
ENCRYPTION_NONE = 1
COMPRESSION_NONE = 1
AUTHENTICATION_CLEARTEXT = 1
KEEP_ALIVE_PERIOD = 60

# Connection settings
SERVER_ADDRESS = ('192.168.1.18', DEFAULT_IPC_PORT)
USERNAME = "net.ihitc.ptmptest"  # Replace with your registered ExApp ID
PASSWORD = "cisco"  # Replace with your ExApp key


def send_negotiation(sock):
    """Send PTMP negotiation request."""
    print("Sending negotiation request...")
    timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
    app_id = str(uuid.uuid4())
    reserved = ":PTVER8.0.0.0000"

    negotiation_string = f"{PTMP_IDENTIFIER}\0{PTMP_VERSION}\0{app_id}\0{BINARY_ENCODING}\0{ENCRYPTION_NONE}\0{COMPRESSION_NONE}\0{AUTHENTICATION_CLEARTEXT}\0{timestamp}\0{KEEP_ALIVE_PERIOD}\0{reserved}\0"
    encoded_value = negotiation_string.encode('utf-8') + b'\0'
    msg_type = str(0).encode('utf-8') + b'\0'
    length = str(len(msg_type + encoded_value)).encode('utf-8') + b'\0'
    request = length + msg_type + encoded_value

    sock.sendall(request)
    receive_response(sock)


def authenticate(sock):
    """Authenticate with Packet Tracer."""
    # Send authentication request
    print("Sending authentication request...")
    encoded_value = USERNAME.encode('utf-8') + b'\0'
    request = struct.pack('!i', 2) + encoded_value
    length = len(request)
    request = struct.pack('!i', length) + request
    sock.sendall(request)
    receive_response(sock)

    # Send authentication response
    print("Sending authentication response...")
    reserved = ""
    auth_response = f"{USERNAME}\0{PASSWORD}\0{reserved}\0"
    encoded_value = auth_response.encode('utf-8')
    request = struct.pack('!i', 4) + encoded_value
    length = len(request)
    request = struct.pack('!i', length) + request
    sock.sendall(request)
    receive_response(sock)


def receive_response(sock):
    """Receive and consume response data."""
    try:
        while True:
            data = sock.recv(1024)
            if not data:
                break
    except socket.timeout:
        pass


def send_ipc_call(sock, call_id, call_name, debug=False):
    """Send an IPC API call and return the response."""
    encoded_call = call_name.encode('utf-8')
    request = struct.pack('!i', 100) + struct.pack('!i', call_id) + encoded_call
    request = request + bytes([0])
    length = len(request)
    request = struct.pack('!i', length) + request

    sock.sendall(request)

    # Receive response
    try:
        data = sock.recv(4096)
        if debug:
            print(f"  DEBUG - Call ID {call_id}: Received {len(data)} bytes")
            print(f"  DEBUG - Raw response: {data[:100]}")  # First 100 bytes
            print(f"  DEBUG - Hex: {data[:100].hex()}")
        return data
    except socket.timeout:
        return None


def get_object_property(sock, call_id, uuid, property_name):
    """Call a method on an object identified by UUID."""
    # Format: "getObjectByUuid\0\0<method>\0" with UUID as argument
    call_name = f"getObjectByUuid\0\0{property_name}\0"
    encoded_call = call_name.encode('utf-8')
    request = struct.pack('!i', 100) + struct.pack('!i', call_id) + encoded_call

    # Add UUID as QString argument
    arg_type = 9  # QString
    uuid_arg = f"{uuid}\0"
    encoded_uuid = uuid_arg.encode('utf-8')
    request = request + struct.pack('!b', arg_type) + encoded_uuid
    request = request + bytes([0])

    length = len(request)
    request = struct.pack('!i', length) + request
    sock.sendall(request)

    try:
        data = sock.recv(4096)
        # Parse QString response
        if len(data) > 13:
            offset = 13  # Skip length, type, call_id, result_type
            result = data[offset:].decode('utf-8', errors='ignore').split('\0')[0]
            return result
    except socket.timeout:
        pass
    return None


def parse_device_count_response(data):
    """Parse the device count from the response."""
    if not data or len(data) < 13:
        return 0
    try:
        # Response format: length(4) + type(4) + call_id(4) + result_type(1) + result
        offset = 12  # Skip length, type, call_id

        # Read the result type byte
        result_type = data[offset]
        offset += 1

        # Type 4 = int32
        if result_type == 4:
            count = struct.unpack('!i', data[offset:offset+4])[0]
            return count

        # Type 9 = QString
        elif result_type == 9:
            result_str = data[offset:].decode('utf-8', errors='ignore').split('\0')[0]
            if result_str.isdigit():
                return int(result_str)

        return 0
    except Exception as e:
        print(f"  DEBUG - Error parsing count: {e}")
        return 0


def parse_device_response(data):
    """Parse device information from response - extracts UUID from object reference."""
    if not data or len(data) < 12:
        return None

    try:
        # Skip length, type, call_id (12 bytes total)
        offset = 12

        # Read the result type byte
        result_type = data[offset]
        offset += 1

        # Read the rest as null-terminated strings
        device_info = data[offset:].decode('utf-8', errors='ignore')
        parts = [p for p in device_info.split('\0') if p]  # Filter empty strings

        if len(parts) >= 2:
            # parts[0] is object type (e.g., "Router", "Switch")
            # parts[1] is the UUID reference like "IPC Cache entry: {uuid}"
            uuid_str = parts[1]
            if "IPC Cache entry:" in uuid_str:
                # Extract UUID from "IPC Cache entry: {uuid}"
                uuid = uuid_str.split("{")[1].split("}")[0] if "{" in uuid_str else None
                return {
                    'type': parts[0],
                    'uuid': uuid
                }
    except Exception as e:
        print(f"  DEBUG - Error parsing device: {e}")
    return None


def parse_link_response(data):
    """Parse link information from response - extracts UUID from object reference."""
    if not data or len(data) < 12:
        return None

    try:
        # Skip length, type, call_id (12 bytes total)
        offset = 12

        # Read the result type byte
        result_type = data[offset]
        offset += 1

        # Read the rest as null-terminated strings
        link_info = data[offset:].decode('utf-8', errors='ignore')
        parts = [p for p in link_info.split('\0') if p]  # Filter empty strings

        if len(parts) >= 2:
            # parts[0] is object type (e.g., "Cable", "Link")
            # parts[1] is the UUID reference
            uuid_str = parts[1]
            if "IPC Cache entry:" in uuid_str:
                # Extract UUID from "IPC Cache entry: {uuid}"
                uuid = uuid_str.split("{")[1].split("}")[0] if "{" in uuid_str else None
                return {
                    'type': parts[0],
                    'uuid': uuid
                }
    except Exception as e:
        print(f"  DEBUG - Error parsing link: {e}")
    return None


def get_link_details(sock, call_id_start, link_uuid):
    """Get link connection details using the link UUID."""
    details = {}

    # Get source device name
    call_id = call_id_start
    src_device_uuid = get_object_property(sock, call_id, link_uuid, 'getSourceDeviceUuid')
    if src_device_uuid:
        call_id += 1
        details['sourceDevice'] = get_object_property(sock, call_id, src_device_uuid, 'getName') or 'Unknown'
    else:
        details['sourceDevice'] = 'Unknown'

    # Get source port
    call_id += 1
    details['sourcePort'] = get_object_property(sock, call_id, link_uuid, 'getSourcePortName') or ''

    # Get destination device name
    call_id += 1
    dst_device_uuid = get_object_property(sock, call_id, link_uuid, 'getDestDeviceUuid')
    if dst_device_uuid:
        call_id += 1
        details['destinationDevice'] = get_object_property(sock, call_id, dst_device_uuid, 'getName') or 'Unknown'
    else:
        details['destinationDevice'] = 'Unknown'

    # Get destination port
    call_id += 1
    details['destinationPort'] = get_object_property(sock, call_id, link_uuid, 'getDestPortName') or ''

    return details, call_id


def print_topology():
    """Connect to Packet Tracer and print the network topology."""
    print(f"Connecting to Packet Tracer at {SERVER_ADDRESS}...")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(SERVER_ADDRESS)
        sock.settimeout(1)
        print("Connected.\n")

        # Negotiate and authenticate
        send_negotiation(sock)
        authenticate(sock)

        print("\n" + "="*60)
        print("NETWORK TOPOLOGY")
        print("="*60 + "\n")

        # Get device count
        call_id = 1
        call_name = "network\0\0getDeviceCount\0"
        print(f"Calling {call_name.strip(chr(0))}...")
        response = send_ipc_call(sock, call_id, call_name, debug=True)
        device_count = parse_device_count_response(response)

        print(f"Total Devices: {device_count}\n")

        # Get each device
        devices = []
        print("DEVICES:")
        print("-" * 60)
        for i in range(device_count):
            call_id += 1
            call_name = f"network\0\0getDeviceAt\0"

            # Send call with index argument
            encoded_call = call_name.encode('utf-8')
            request = struct.pack('!i', 100) + struct.pack('!i', call_id) + encoded_call
            # Add integer argument as int type (not QString!)
            arg_type = 4  # int type
            request = request + struct.pack('!b', arg_type) + struct.pack('!i', i)
            request = request + bytes([0])
            length = len(request)
            request = struct.pack('!i', length) + request
            sock.sendall(request)

            response = None
            try:
                response = sock.recv(4096)
                if i == 0:  # Debug first device only
                    print(f"  DEBUG - Device {i}: Received {len(response)} bytes")
                    print(f"  DEBUG - Raw response: {response[:200]}")
                    print(f"  DEBUG - Hex: {response[:200].hex()}")
            except socket.timeout:
                pass

            device = parse_device_response(response)
            if device and device.get('uuid'):
                # Get device name using UUID
                call_id += 1
                device_name = get_object_property(sock, call_id, device['uuid'], 'getName')
                device['name'] = device_name if device_name else device['uuid']
                devices.append(device)
                print(f"  [{i}] {device['name']} ({device['type']})")
            elif device:
                devices.append(device)
                print(f"  [{i}] Unknown ({device.get('type', 'Device')})")

        # Get link count
        call_id += 1
        call_name = "network\0\0getLinkCount\0"
        print(f"\nCalling {call_name.strip(chr(0))}...")
        response = send_ipc_call(sock, call_id, call_name, debug=True)
        link_count = parse_device_count_response(response)

        print(f"\nTotal Links: {link_count}\n")

        # Get each link
        print("LINKS:")
        print("-" * 60)
        for i in range(link_count):
            call_id += 1
            call_name = f"network\0\0getLinkAt\0"

            # Send call with index argument
            encoded_call = call_name.encode('utf-8')
            request = struct.pack('!i', 100) + struct.pack('!i', call_id) + encoded_call
            # Add integer argument as int type (not QString!)
            arg_type = 4  # int type
            request = request + struct.pack('!b', arg_type) + struct.pack('!i', i)
            request = request + bytes([0])
            length = len(request)
            request = struct.pack('!i', length) + request
            sock.sendall(request)

            response = None
            try:
                response = sock.recv(4096)
                if i == 0:  # Debug first link only
                    print(f"  DEBUG - Link {i}: Received {len(response)} bytes")
                    print(f"  DEBUG - Raw response: {response[:200]}")
                    print(f"  DEBUG - Hex: {response[:200].hex()}")
            except socket.timeout:
                pass

            link = parse_link_response(response)
            if link and link.get('uuid'):
                # Get link details using UUID
                link_details, call_id = get_link_details(sock, call_id + 1, link['uuid'])
                print(f"  [{i}] {link_details['sourceDevice']}:{link_details['sourcePort']} <--> "
                      f"{link_details['destinationDevice']}:{link_details['destinationPort']}")
            elif link:
                print(f"  [{i}] Unknown link")

        print("\n" + "="*60)
        print("Topology printed successfully!")
        print("="*60)


if __name__ == "__main__":
    try:
        print_topology()
    except ConnectionRefusedError:
        print(f"ERROR: Could not connect to Packet Tracer at {SERVER_ADDRESS}")
        print("Make sure Packet Tracer is running and IPC is enabled.")
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
