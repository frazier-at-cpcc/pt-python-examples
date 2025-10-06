# Cisco Packet Tracer Extensions API: Pop3Client Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_pop3_client.html

---

[Pop3Client](class_pop3_client.html "Pop3Client handles and manipulates POP3 clients.") handles and manipulates POP3 clients. [More...](class_pop3_client.html#details)

##  Public Member Functions  
  
---  
void | [mailReceived](class_pop3_client.html#ac5f7f9d7b8c780fc33b5eebe04ddd4df) (string, string, QString, QString)  
| This event is emitted when the POP3 client receives an email. [More...](class_pop3_client.html#ac5f7f9d7b8c780fc33b5eebe04ddd4df)  
  
void | [errorReceivingMail](class_pop3_client.html#a321c84e97f3dccfee32707900119c600) (Pop3ResponseType)  
| This event is emitted when the POP3 client had an error retrieving email. [More...](class_pop3_client.html#a321c84e97f3dccfee32707900119c600)  
  
bool | [getMailIpc](class_pop3_client.html#a8fb0bcd2bbcf8b96bb625b70a9f91163) ()  
| Gets mail. [More...](class_pop3_client.html#a8fb0bcd2bbcf8b96bb625b70a9f91163)  
  
void | [cancelReceive](class_pop3_client.html#a1d23f3eee1e2a9a595ca76036d7e9e99) ()  
| Cancels receive. [More...](class_pop3_client.html#a1d23f3eee1e2a9a595ca76036d7e9e99)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[Pop3Client](class_pop3_client.html "Pop3Client handles and manipulates POP3 clients.") handles and manipulates POP3 clients. 

## Member Function Documentation

## ◆ cancelReceive()

void Pop3Client::cancelReceive  | ( | | ) |   
---|---|---|---|---  
  
Cancels receive. 

## ◆ errorReceivingMail()

void Pop3Client::errorReceivingMail  | ( | Pop3ResponseType  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when the POP3 client had an error retrieving email. 

  * responseType, the response type. Response types: ePop3Request = 1, ePop3ResponseSuccess = 2, ePop3ResponseError = 3, ePop3Timeout = 4, ePop3PeerReset = 5, ePop3DnsServerNotFound = 6, ePop3DnsUnResolvedHostName = 7, ePop3ProtocolError = 8, ePop3UserNotFound = 9



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ getMailIpc()

bool Pop3Client::getMailIpc  | ( | | ) |   
---|---|---|---|---  
  
Gets mail. 

Returns
    bool, always returns true. 

## ◆ mailReceived()

void Pop3Client::mailReceived  | ( | string  | ,   
---|---|---|---  
|  | string  | ,   
|  | QString  | ,   
|  | QString  |   
| ) | |   
  
This event is emitted when the POP3 client receives an email. 

  * sender, the sender of the email. 
  * subject, the subject of the email. 
  * dateTime, the date time. 
  * body, the body of the email.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

* * *

The documentation for this class was generated from the following file:

  * [CPop3Client.pki](_c_pop3_client_8pki.html)


