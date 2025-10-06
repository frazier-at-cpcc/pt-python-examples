# Cisco Packet Tracer Extensions API: TftpServer Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_tftp_server.html

---

[TftpServer](class_tftp_server.html "TftpServer handles and manipulates the TFTP service.") handles and manipulates the TFTP service. [More...](class_tftp_server.html#details)

##  Public Member Functions  
  
---  
void | [setEnabled](class_tftp_server.html#a3a77bd8964cc05941b7f20fdc5b75a4f) (bool)  
| Enables or disables the TFTP service. [More...](class_tftp_server.html#a3a77bd8964cc05941b7f20fdc5b75a4f)  
  
bool | [isEnabled](class_tftp_server.html#a7a199a1cf4ad6f7aa04a11e362ad20bf) ()  
| Returns true if the TFTP service is enabled, otherwise false. [More...](class_tftp_server.html#a7a199a1cf4ad6f7aa04a11e362ad20bf)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[TftpServer](class_tftp_server.html "TftpServer handles and manipulates the TFTP service.") handles and manipulates the TFTP service. 

## Member Function Documentation

## ◆ isEnabled()

bool TftpServer::isEnabled  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the TFTP service is enabled, otherwise false. 

Returns
    bool, true if the TFTP service is enabled, otherwise false. 

## ◆ setEnabled()

void TftpServer::setEnabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables the TFTP service. 

Parameters
     bEnable,true| to enable the TFTP service, false to disable it.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CTftpServer.pki](_c_tftp_server_8pki.html)


