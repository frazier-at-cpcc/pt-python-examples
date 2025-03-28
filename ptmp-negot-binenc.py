# This sample python script successfully connects, negotiates, and authenticates with Packet Tracer then sends two sample API calls
# Note this uses a password in cleartext instead of challenge based authentication it uses binary encoding and no encryption
# Just a sample for shwoing the basics of using PTMP
# Verifies working with PT 8.2.2 on 2025-03-28

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
AUTHENTICATION_SIMPLE = 2
AUTHENTICATION_MD5 = 4
KEEP_ALIVE_PERIOD = 60  # seconds, note not implemented in this example, keep alives are PTMP message type 6

server_address = ('127.0.0.1', DEFAULT_IPC_PORT)
username = "net.ihitc.ptmptest"  # Replace with your registered ExApp ID
password = "cisco"  # Replace with your ExApp key

print(f"Connecting to {server_address}...")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(server_address)
    sock.settimeout(1) #timeout waiting for data after 1 second
    print("Connected.")

    # 1. Connection Negotiation - must use text encoding for this
    print("Sending negotiation request...")
    timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
    app_id = str(uuid.uuid4())
    reserved = ":PTVER8.0.0.0000"  # Example version
    negotiation_string = f"{PTMP_IDENTIFIER}\0{PTMP_VERSION}\0{app_id}\0{BINARY_ENCODING}\0{ENCRYPTION_NONE}\0{COMPRESSION_NONE}\0{AUTHENTICATION_CLEARTEXT}\0{timestamp}\0{KEEP_ALIVE_PERIOD}\0{reserved}\0"
    encoded_value = negotiation_string.encode('utf-8') + b'\0'
    type = str(0).encode('utf-8') + b'\0' # type is 0 for negotiation request message
    length = str(len(type+encoded_value)).encode('utf-8') + b'\0'
    request = length+type+encoded_value
    print(request)
    sock.sendall(request)
    print("Negotiation request sent.")
    print("Receiving negotiation response...")
    """Receives a text-encoded message from the socket."""
    try:
        while True:
            data = sock.recv(1024)
            if not data:
                break
            print(f"Received: {data}")
    except socket.timeout:
        pass
    # 2. Authentication - now using binary struct encoding
    print("Sending authentication request...")
    username = "net.ihitc.ptmptest"  # Replace with your registered ExApp ID
    authentication_request_string = f"{username}"
    encoded_value = authentication_request_string.encode('utf-8') + b'\0'
    request = struct.pack('!i',2) + encoded_value # type is 2 for authentication request message
    length = len(request)
    request = struct.pack('!i',length) + request
    print(request)
    sock.sendall(request)
    print("Authentication request sent.")
    print("Receiving authentication challenge...")
    try:
        while True:
            data = sock.recv(1024)
            if not data:
                break
            print(f"Received: {data}")
    except socket.timeout:
        pass
    print("Sending authentication response...")
    password = "cisco"  # Replace with your ExApp key
    reserved = "" # currently unused
    authentication_response_string = f"{username}\0{password}\0{reserved}\0"
    encoded_value = authentication_response_string.encode('utf-8')
    request = struct.pack('!i',4) + encoded_value # type is 4 for authentication response message
    length = len(request)
    request = struct.pack('!i',length) + request
    print(request)
    sock.sendall(request)
    print("Authentication response sent.")
    print("Receiving authentication status...")
    try:
        while True:
            data = sock.recv(1024)
            if not data:
                break
            print(f"Received: {data}")
    except socket.timeout:
        pass
    # 3. Send a basic IPC API request without any arguments/parameters
    type = 100 # PTMP message type is between 100 and 199 for IPC call messages
    call_id = 1 # int number to differentiate responses
    call_name = f"appWindow\0\0getVersion\0" # IPC call ipc.appWindow().getVersion(), note the strange formatting
    encoded_value = call_name.encode('utf-8')
    request = struct.pack('!i',type) + struct.pack('!i',call_id) + encoded_value
    request = request + bytes([0])
    length = len(request)
    request = struct.pack('!i',length) + request
    print("IPC Call sent.")
    print(request)
    sock.sendall(request)
    print("Receiving IPC Response...")
    try:
        while True:
            data = sock.recv(1024)
            if not data:
                break
            print(f"Received: {data}")
    except socket.timeout:
        pass
    # 4. Send an IPC API request with an argument/parameter (in this case write to the IPC log in PT)
    type = 100 # PTMP messag etype is between 100 and 199 for IPC call messages
    call_id = 2 # int number to differentiate responses
    call_name = f"appWindow\0\0writeToPT\0" # IPC call ipc.appWindow().0writeToPT()
    encoded_value = call_name.encode('utf-8')
    request = struct.pack('!i',type) + struct.pack('!i',call_id) + encoded_value
    arg_type = 9 # Qstring type is 9
    args = "Hello World - Sent With Binary Encoding!\0" # Qstring text to send to the IPC log in PT, all strings must terminate in \0
    encoded_args = args.encode('utf-8')
    request = request + struct.pack('!b',arg_type) + encoded_args
    request = request + bytes([0])
    length = len(request)
    request = struct.pack('!i',length) + request
    print("IPC Call sent.")
    print(request)
    sock.sendall(request)
    print("Receiving IPC Response...")
    try:
        while True:
            data = sock.recv(1024)
            if not data:
                break
            print(f"Received: {data}")
    except socket.timeout:
        pass