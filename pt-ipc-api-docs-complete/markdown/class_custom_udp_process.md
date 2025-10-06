# Cisco Packet Tracer Extensions API: CustomUdpProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_custom_udp_process.html

---

[CustomUdpProcess](class_custom_udp_process.html "CustomUdpProcess is the process that manipulates the custom UDP process.") is the process that manipulates the custom UDP process. [More...](class_custom_udp_process.html#details)

##  Public Member Functions  
  
---  
bool | [start](class_custom_udp_process.html#a9d8b81842133c46a85a8c03990a57fb0) (int)  
| Starts the custom UDP process on the specified port number. [More...](class_custom_udp_process.html#a9d8b81842133c46a85a8c03990a57fb0)  
  
bool | [stop](class_custom_udp_process.html#a2fad6c8b387f466ba68537df6a6e4b9e) ()  
| Stops the custom UDP process. [More...](class_custom_udp_process.html#a2fad6c8b387f466ba68537df6a6e4b9e)  
  
bool | [isStarted](class_custom_udp_process.html#ad24bad7240472cde1e1ff0cbb1b6c2bb) ()  
| Returns true if the custom UDP process was started, otherwise false. [More...](class_custom_udp_process.html#ad24bad7240472cde1e1ff0cbb1b6c2bb)  
  
int | [getPortNumber](class_custom_udp_process.html#a2bc455069ba2f2b69e02eb4569d1f189) ()  
| Returns the port number of this custom UDP process. [More...](class_custom_udp_process.html#a2bc455069ba2f2b69e02eb4569d1f189)  
  
bool | [sendData](class_custom_udp_process.html#a91e8a6212c5f0f0dd0690b56332521c5) (QString, QString, int, [FrameInstance](class_frame_instance.html), [Port](class_port.html))  
| Sends data over this custom UDP process to the specified destination IP address and port number. [More...](class_custom_udp_process.html#a91e8a6212c5f0f0dd0690b56332521c5)  
  
bool | [sendDataWithPduInfo](class_custom_udp_process.html#a3c1877f3f2dee63b2a03c82316c0e9c1) (QString, QString, int, [FrameInstance](class_frame_instance.html), [Port](class_port.html), QString, QString, QString)  
| Sends data over this custom UDP process to the specified destination IP address and port number, along with PDU info. [More...](class_custom_udp_process.html#a3c1877f3f2dee63b2a03c82316c0e9c1)  
  
bool | [processData](class_custom_udp_process.html#ade4d511d73f3332d0c608f66389d0e33) (QString, ip, int, [FrameInstance](class_frame_instance.html), [Port](class_port.html))  
| This delegate processes the incoming data and returns true if successful, otherwise false. [More...](class_custom_udp_process.html#ade4d511d73f3332d0c608f66389d0e33)  
  
[FrameInstance](class_frame_instance.html) | [createFrameInstance](class_custom_udp_process.html#a35a3cf7c56f9b8c4c84d3c03e1eb96dc) (int, QString)  
| Creates a frame instance. [More...](class_custom_udp_process.html#a35a3cf7c56f9b8c4c84d3c03e1eb96dc)  
  
void | [finalizeFrameInstance](class_custom_udp_process.html#a736b45015d9d6c40b9372b8ad46771fc) ([FrameInstance](class_frame_instance.html))  
| Finalizes a frame instance. [More...](class_custom_udp_process.html#a736b45015d9d6c40b9372b8ad46771fc)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[CustomUdpProcess](class_custom_udp_process.html "CustomUdpProcess is the process that manipulates the custom UDP process.") is the process that manipulates the custom UDP process. 

## Member Function Documentation

## ◆ createFrameInstance()

[FrameInstance](class_frame_instance.html) CustomUdpProcess::createFrameInstance  | ( | int  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Creates a frame instance. 

Parameters
     color,the| color for this frame instance.   
---|---  
dstStr,the| destination IP address for this frame instance.  
  
Returns
    [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc."), a [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") object. 

## ◆ finalizeFrameInstance()

void CustomUdpProcess::finalizeFrameInstance  | ( | [FrameInstance](class_frame_instance.html) | | ) |   
---|---|---|---|---|---  
  
Finalizes a frame instance. 

Parameters
     frameInstance,the| frame instance of interest to finalize.   
---|---  
  
## ◆ getPortNumber()

int CustomUdpProcess::getPortNumber  | ( | | ) |   
---|---|---|---|---  
  
Returns the port number of this custom UDP process. 

Returns
    int, the port number of this custom UDP process. 

## ◆ isStarted()

bool CustomUdpProcess::isStarted  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the custom UDP process was started, otherwise false. 

Returns
    bool, true if the custom UDP process was started, otherwise false. 

## ◆ processData()

bool CustomUdpProcess::processData  | ( | QString  | ,   
---|---|---|---  
|  | ip  | ,   
|  | int  | ,   
|  | [FrameInstance](class_frame_instance.html) | ,   
|  | [Port](class_port.html) |   
| ) | |   
  
This delegate processes the incoming data and returns true if successful, otherwise false. 

  * data, the data that was processed. 
  * srcIp, the source IP address. 
  * srcPort, the source port number. 
  * frameInstance, the [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") object. 
  * inPort, the incoming [Port](class_port.html "Port holds and manipulates the ports on devices.") object.



Returns
    bool, true if successful, otherwise false. 

## ◆ sendData()

bool CustomUdpProcess::sendData  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | int  | ,   
|  | [FrameInstance](class_frame_instance.html) | ,   
|  | [Port](class_port.html) |   
| ) | |   
  
Sends data over this custom UDP process to the specified destination IP address and port number. 

Parameters
     data,the| data to send to the destination.   
---|---  
dstIp,the| IP address of the destination.   
dstPort,the| port number of the destination.   
frameInstance,the| [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") object. Use [createFrameInstance()](class_custom_udp_process.html#a35a3cf7c56f9b8c4c84d3c03e1eb96dc "Creates a frame instance.") to create the [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") object.   
outPort,the| [Port](class_port.html "Port holds and manipulates the ports on devices.") object where this data will be sent out of from the source device.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ sendDataWithPduInfo()

bool CustomUdpProcess::sendDataWithPduInfo  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | int  | ,   
|  | [FrameInstance](class_frame_instance.html) | ,   
|  | [Port](class_port.html) | ,   
|  | QString  | ,   
|  | QString  | ,   
|  | QString  |   
| ) | |   
  
Sends data over this custom UDP process to the specified destination IP address and port number, along with PDU info. 

Parameters
     data,the| data to send to the destination.   
---|---  
dstIp,the| IP address of the destination.   
dstPort,the| port number of the destination.   
frameInstance,the| [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") object. Use [createFrameInstance()](class_custom_udp_process.html#a35a3cf7c56f9b8c4c84d3c03e1eb96dc "Creates a frame instance.") to create the [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") object.   
outPort,the| [Port](class_port.html "Port holds and manipulates the ports on devices.") object where this data will be sent out of from the source device.   
customProtocol,the| custom protocol name   
customPduType,the| custom PDU type   
jsonFields,the| fields in JSON string representation:  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ start()

bool CustomUdpProcess::start  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Starts the custom UDP process on the specified port number. 

Parameters
     int,the| port number.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ stop()

bool CustomUdpProcess::stop  | ( | | ) |   
---|---|---|---|---  
  
Stops the custom UDP process. 

Returns
    bool, true if successful, otherwise false. 

* * *

The documentation for this class was generated from the following file:

  * [CCustomUdpProcess.pki](_c_custom_udp_process_8pki.html)


