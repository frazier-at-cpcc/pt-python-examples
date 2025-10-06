# Cisco Packet Tracer Extensions API: SmtpClient Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_smtp_client.html

---

[SmtpClient](class_smtp_client.html "SmtpClient handles and manipulates the SMTP client.") handles and manipulates the SMTP client. [More...](class_smtp_client.html#details)

##  Public Member Functions  
  
---  
void | [mailSent](class_smtp_client.html#a073062025310008f8b83f2199946e8d3) (string, string, QString, SmtpResponseType)  
| This event is emitted when an email is sent. [More...](class_smtp_client.html#a073062025310008f8b83f2199946e8d3)  
  
bool | [sendMail](class_smtp_client.html#a4fbfb53d24c6b58e5b0688509e729265) (string, string, string, QString, string, string)  
| This event is emitted when an email is sent. [More...](class_smtp_client.html#a4fbfb53d24c6b58e5b0688509e729265)  
  
void | [cancelSend](class_smtp_client.html#a51f980150eec5a512c6dd3a28e385ade) ()  
| Intervene with mail sending. [More...](class_smtp_client.html#a51f980150eec5a512c6dd3a28e385ade)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[SmtpClient](class_smtp_client.html "SmtpClient handles and manipulates the SMTP client.") handles and manipulates the SMTP client. 

## Member Function Documentation

## ◆ cancelSend()

void SmtpClient::cancelSend  | ( | | ) |   
---|---|---|---|---  
  
Intervene with mail sending. 

## ◆ mailSent()

void SmtpClient::mailSent  | ( | string  | ,   
---|---|---|---  
|  | string  | ,   
|  | QString  | ,   
|  | SmtpResponseType  |   
| ) | |   
  
This event is emitted when an email is sent. 

Parameters
     dest,the| email recipient.   
---|---  
subject,the| email subject.   
body,the| email body.   
responseType,the| response type. Response types: eSmtpRequest = 1, eSmtpResponseSuccess = 2, eSmtpRequestForward = 3, eSmtpRemoteReceieverDoesNotExist = 4, eSmtpResponseError = 5, eSmtpTimeout = 6, eSmtpPeerReset = 7, eSmtpDnsServerNotFound = 8, eSmtpDnsUnResolvedHostName = 9, eSmtpProtocolError = 10, eSmtpUserNotFound = 11, eSmtpServerDomainError = 12, eSmtpServerNotFound = 13  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ sendMail()

bool SmtpClient::sendMail  | ( | string  | ,   
---|---|---|---  
|  | string  | ,   
|  | string  | ,   
|  | QString  | ,   
|  | string  | ,   
|  | string  |   
| ) | |   
  
This event is emitted when an email is sent. 

Parameters
     fromEmailId,the| sender's email.   
---|---  
toEmailId,the| recipient's email.   
subject,tthe| email subject.   
contents,the| email contents.   
  
password,the| smtp user password.   
ipAddr,the| outgoing email server address   
  
* * *

The documentation for this class was generated from the following file:

  * [CSmtpClient.pki](_c_smtp_client_8pki.html)


