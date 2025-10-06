# Cisco Packet Tracer Extensions API: CustomTcpProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_custom_tcp_process.html

---

[CustomTcpProcess](class_custom_tcp_process.html "CustomTcpProcess is the process that manipulates the custom TCP process.") is the process that manipulates the custom TCP process. [More...](class_custom_tcp_process.html#details)

##  Public Member Functions  
  
---  
[TcpConnection](class_tcp_connection.html) | [getConnection](class_custom_tcp_process.html#a8ac2d002d3f7ba8515e8b62e0256e933) ()  
void | [connectionChanged](class_custom_tcp_process.html#aa27ded4b752bf8a71cc26badf4c62371) ([TcpConnection](class_tcp_connection.html), TcpEvent)  
| [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. [More...](class_custom_tcp_process.html#aa27ded4b752bf8a71cc26badf4c62371)  
  
bool | [sendData](class_custom_tcp_process.html#a51151f926168bcba0b97d2af8fcc204f) (QString, [TcpConnection](class_tcp_connection.html), [FrameInstance](class_frame_instance.html))  
| Sends data over this custom TCP process to the specified TCP connection. [More...](class_custom_tcp_process.html#a51151f926168bcba0b97d2af8fcc204f)  
  
bool | [sendDataWithPduInfo](class_custom_tcp_process.html#a42d2b2d6cd65b3e5ca9a9d99f69ab0d3) (QString, [TcpConnection](class_tcp_connection.html), [FrameInstance](class_frame_instance.html), QString, QString, QString)  
| Sends data over this custom TCP process to the specified TCP connection. [More...](class_custom_tcp_process.html#a42d2b2d6cd65b3e5ca9a9d99f69ab0d3)  
  
bool | [processData](class_custom_tcp_process.html#a8581116717c64c831d082c33b2c24d89) (QString, [TcpConnection](class_tcp_connection.html), [FrameInstance](class_frame_instance.html))  
| This delegate processes the incoming data and returns true if successful, otherwise false. [More...](class_custom_tcp_process.html#a8581116717c64c831d082c33b2c24d89)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[CustomTcpProcess](class_custom_tcp_process.html "CustomTcpProcess is the process that manipulates the custom TCP process.") is the process that manipulates the custom TCP process. 

## Member Function Documentation

## ◆ connectionChanged()

void CustomTcpProcess::connectionChanged  | ( | [TcpConnection](class_tcp_connection.html) | ,   
---|---|---|---  
|  | TcpEvent  |   
| ) | |   
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

eConnectionActive = 0, eConnectionTimeout = 1, eConnectionRequest = 2, ePeerClose = 3, ePeerReset = 4, eSendUserTraffic = 5 

## ◆ getConnection()

[TcpConnection](class_tcp_connection.html) CustomTcpProcess::getConnection  | ( | | ) |   
---|---|---|---|---  
  
## ◆ processData()

bool CustomTcpProcess::processData  | ( | QString  | ,   
---|---|---|---  
|  | [TcpConnection](class_tcp_connection.html) | ,   
|  | [FrameInstance](class_frame_instance.html) |   
| ) | |   
  
This delegate processes the incoming data and returns true if successful, otherwise false. 

  * data, the data that was processed. 
  * connection, the TCP connection. 
  * frameInstance, the [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") object.



Returns
    bool, true if successful, otherwise false. 

## ◆ sendData()

bool CustomTcpProcess::sendData  | ( | QString  | ,   
---|---|---|---  
|  | [TcpConnection](class_tcp_connection.html) | ,   
|  | [FrameInstance](class_frame_instance.html) |   
| ) | |   
  
Sends data over this custom TCP process to the specified TCP connection. 

Parameters
     data,the| data to send to the destination. 

  * connection, the TCP connection. 

  
---|---  
frameInstance,the| [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") object. Use createFrameInstance() to create the [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") object.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ sendDataWithPduInfo()

bool CustomTcpProcess::sendDataWithPduInfo  | ( | QString  | ,   
---|---|---|---  
|  | [TcpConnection](class_tcp_connection.html) | ,   
|  | [FrameInstance](class_frame_instance.html) | ,   
|  | QString  | ,   
|  | QString  | ,   
|  | QString  |   
| ) | |   
  
Sends data over this custom TCP process to the specified TCP connection. 

Parameters
     data,the| data to send to the destination. 

  * connection, the TCP connection. 

  
---|---  
frameInstance,the| [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") object. Use createFrameInstance() to create the [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") object.   
customProtocol,the| custom protocol name   
customPduType,the| custom PDU type   
jsonFields,the| fields in JSON string representation:  
  
Returns
    bool, true if successful, otherwise false. 

* * *

The documentation for this class was generated from the following file:

  * [CCustomTcpProcess.pki](_c_custom_tcp_process_8pki.html)


