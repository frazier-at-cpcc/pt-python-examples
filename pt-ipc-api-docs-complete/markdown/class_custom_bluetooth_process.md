# Cisco Packet Tracer Extensions API: CustomBluetoothProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_custom_bluetooth_process.html

---

[CustomBluetoothProcess](class_custom_bluetooth_process.html "CustomBluetoothProcess is the process that manipulates the custom Bluetooth process.") is the process that manipulates the custom Bluetooth process. [More...](class_custom_bluetooth_process.html#details)

##  Public Member Functions  
  
---  
bool | [start](class_custom_bluetooth_process.html#aae272bf04752a1cba8dffdd6d4024e00) (uuid)  
| Starts the custom bluetooth process on the specified service uuid. [More...](class_custom_bluetooth_process.html#aae272bf04752a1cba8dffdd6d4024e00)  
  
bool | [connect](class_custom_bluetooth_process.html#afb17336b2737037ba12d0482552439b5) (mac, uuid)  
bool | [stop](class_custom_bluetooth_process.html#aa2fbbb34dfb972b3150746e64c381ccf) ()  
| Stops the custom bluetooth process. [More...](class_custom_bluetooth_process.html#aa2fbbb34dfb972b3150746e64c381ccf)  
  
bool | [isStarted](class_custom_bluetooth_process.html#aaac7f3d06d9f5a6a5d1e9fbddeb1f791) ()  
| Returns true if the custom bluetooth process was started, otherwise false. [More...](class_custom_bluetooth_process.html#aaac7f3d06d9f5a6a5d1e9fbddeb1f791)  
  
uuid | [getServiceUuid](class_custom_bluetooth_process.html#a6584cab956b417bfa7cd13369e281fb6) ()  
| Returns the service uuid of this custom Bluetooth process. [More...](class_custom_bluetooth_process.html#a6584cab956b417bfa7cd13369e281fb6)  
  
mac | [getDstMac](class_custom_bluetooth_process.html#a38f5b2faf3de5bda60c7b9228c307b99) ()  
uuid | [getDstServiceUuid](class_custom_bluetooth_process.html#a95f0c3723b842bf007595f54305492b1) ()  
bool | [sendData](class_custom_bluetooth_process.html#a31fa0f25ecb303572190e9130ef5c7dd) (QString, mac, uuid, [FrameInstance](class_frame_instance.html), [Port](class_port.html))  
| Sends data over this custom Bluetooth process to the specified destination MAC address and service uuid. [More...](class_custom_bluetooth_process.html#a31fa0f25ecb303572190e9130ef5c7dd)  
  
bool | [sendDataToConnected](class_custom_bluetooth_process.html#a5dd141449d27887945547dbc9ba08b68) (QString, [FrameInstance](class_frame_instance.html), [Port](class_port.html))  
| Sends data over this custom Bluetooth process to the connected destination MAC address and service uuid. [More...](class_custom_bluetooth_process.html#a5dd141449d27887945547dbc9ba08b68)  
  
bool | [processData](class_custom_bluetooth_process.html#a65d0089b41ab368afccd808e341b564d) (QString, mac, uuid, mac, uuid, [FrameInstance](class_frame_instance.html), [Port](class_port.html))  
| This delegate processes the incoming data and returns true if successful, otherwise false. [More...](class_custom_bluetooth_process.html#a65d0089b41ab368afccd808e341b564d)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[CustomBluetoothProcess](class_custom_bluetooth_process.html "CustomBluetoothProcess is the process that manipulates the custom Bluetooth process.") is the process that manipulates the custom Bluetooth process. 

## Member Function Documentation

## ◆ connect()

bool CustomBluetoothProcess::connect  | ( | mac  | ,   
---|---|---|---  
|  | uuid  |   
| ) | |   
  
## ◆ getDstMac()

mac CustomBluetoothProcess::getDstMac  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getDstServiceUuid()

uuid CustomBluetoothProcess::getDstServiceUuid  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getServiceUuid()

uuid CustomBluetoothProcess::getServiceUuid  | ( | | ) |   
---|---|---|---|---  
  
Returns the service uuid of this custom Bluetooth process. 

Returns
    uuid, the service uuid of this custom Bluetooth process. 

## ◆ isStarted()

bool CustomBluetoothProcess::isStarted  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the custom bluetooth process was started, otherwise false. 

Returns
    bool, true if the custom bluetooth process was started, otherwise false. 

## ◆ processData()

bool CustomBluetoothProcess::processData  | ( | QString  | ,   
---|---|---|---  
|  | mac  | ,   
|  | uuid  | ,   
|  | mac  | ,   
|  | uuid  | ,   
|  | [FrameInstance](class_frame_instance.html) | ,   
|  | [Port](class_port.html) |   
| ) | |   
  
This delegate processes the incoming data and returns true if successful, otherwise false. 

  * data, the data that was processed. 
  * srcMac, the source MAC address. 
  * srcService, the source service uuid. 
  * dstMac, the destination MAC address. 
  * dstService, the destination service uuid. 
  * frameInstance, the [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") object. 
  * inPort, the incoming [Port](class_port.html "Port holds and manipulates the ports on devices.") object.



Returns
    bool, true if successful, otherwise false. 

## ◆ sendData()

bool CustomBluetoothProcess::sendData  | ( | QString  | ,   
---|---|---|---  
|  | mac  | ,   
|  | uuid  | ,   
|  | [FrameInstance](class_frame_instance.html) | ,   
|  | [Port](class_port.html) |   
| ) | |   
  
Sends data over this custom Bluetooth process to the specified destination MAC address and service uuid. 

Parameters
     data,the| data to send to the destination.   
---|---  
dstMac,the| MAC address of the destination.   
dstService,the| service uuid of the destination.   
frameInstance,the| [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") object. Use createFrameInstance() to create the [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") object.   
outPort,the| [Port](class_port.html "Port holds and manipulates the ports on devices.") object where this data will be sent out of from the source device.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ sendDataToConnected()

bool CustomBluetoothProcess::sendDataToConnected  | ( | QString  | ,   
---|---|---|---  
|  | [FrameInstance](class_frame_instance.html) | ,   
|  | [Port](class_port.html) |   
| ) | |   
  
Sends data over this custom Bluetooth process to the connected destination MAC address and service uuid. 

Parameters
     data,the| data to send to the destination.   
---|---  
frameInstance,the| [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") object. Use createFrameInstance() to create the [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") object.   
outPort,the| [Port](class_port.html "Port holds and manipulates the ports on devices.") object where this data will be sent out of from the source device.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ start()

bool CustomBluetoothProcess::start  | ( | uuid  | | ) |   
---|---|---|---|---|---  
  
Starts the custom bluetooth process on the specified service uuid. 

Parameters
     uuid,the| service uuid.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ stop()

bool CustomBluetoothProcess::stop  | ( | | ) |   
---|---|---|---|---  
  
Stops the custom bluetooth process. 

Returns
    bool, true if successful, otherwise false. 

* * *

The documentation for this class was generated from the following file:

  * [CCustomBluetoothProcess.pki](_c_custom_bluetooth_process_8pki.html)


