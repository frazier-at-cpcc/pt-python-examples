# Cisco Packet Tracer Extensions API: EmailClient Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_email_client.html

---

[EmailClient](class_email_client.html "EmailClient is the process that handles the email client.") is the process that handles the email client. [More...](class_email_client.html#details)

##  Public Member Functions  
  
---  
[EmailUser](class_email_user.html) | [getEmailUser](class_email_client.html#aea1d20e20ac83fa466c78c8676980b6e) ()  
| Returns email user for this email client. [More...](class_email_client.html#aea1d20e20ac83fa466c78c8676980b6e)  
  
[SmtpClient](class_smtp_client.html) | [getSmtpClient](class_email_client.html#a9ac16a8aade35c991ce3fd709c482444) ()  
| Returns SMTP client for this email client. [More...](class_email_client.html#a9ac16a8aade35c991ce3fd709c482444)  
  
[Pop3Client](class_pop3_client.html) | [getPop3Client](class_email_client.html#aeb6de8ebfe09854448c84fbd13186a6c) ()  
| Returns POP3 client for this email client. [More...](class_email_client.html#aeb6de8ebfe09854448c84fbd13186a6c)  
  
  
## Detailed Description

[EmailClient](class_email_client.html "EmailClient is the process that handles the email client.") is the process that handles the email client. 

## Member Function Documentation

## ◆ getEmailUser()

[EmailUser](class_email_user.html) EmailClient::getEmailUser  | ( | | ) |   
---|---|---|---|---  
  
Returns email user for this email client. 

Returns
    [EmailUser](class_email_user.html "EmailUser holds and manipulates the email user."), the [EmailUser](class_email_user.html "EmailUser holds and manipulates the email user.") object for this email client. 

## ◆ getPop3Client()

[Pop3Client](class_pop3_client.html) EmailClient::getPop3Client  | ( | | ) |   
---|---|---|---|---  
  
Returns POP3 client for this email client. 

Returns
    [Pop3Client](class_pop3_client.html "Pop3Client handles and manipulates POP3 clients."), the [Pop3Client](class_pop3_client.html "Pop3Client handles and manipulates POP3 clients.") object for this email client. 

## ◆ getSmtpClient()

[SmtpClient](class_smtp_client.html) EmailClient::getSmtpClient  | ( | | ) |   
---|---|---|---|---  
  
Returns SMTP client for this email client. 

Returns
    [SmtpClient](class_smtp_client.html "SmtpClient handles and manipulates the SMTP client."), the [SmtpClient](class_smtp_client.html "SmtpClient handles and manipulates the SMTP client.") object for this email client. 

* * *

The documentation for this class was generated from the following file:

  * [CEmailClient.pki](_c_email_client_8pki.html)


