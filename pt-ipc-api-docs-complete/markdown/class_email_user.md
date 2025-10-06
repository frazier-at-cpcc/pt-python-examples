# Cisco Packet Tracer Extensions API: EmailUser Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_email_user.html

---

[EmailUser](class_email_user.html "EmailUser holds and manipulates the email user.") holds and manipulates the email user. [More...](class_email_user.html#details)

##  Public Member Functions  
  
---  
string | [getUser](class_email_user.html#a9163c4b0b5fbf00ad8036fcf1cdb1c4c) ()  
| Returns the username of the email user. [More...](class_email_user.html#a9163c4b0b5fbf00ad8036fcf1cdb1c4c)  
  
string | [getName](class_email_user.html#a4bb53f404748e0e591298c02c4b911e7) ()  
| Returns the name of the email user. [More...](class_email_user.html#a4bb53f404748e0e591298c02c4b911e7)  
  
void | [setUser](class_email_user.html#ac3189a180c19f67a3cd352f1b399b3a8) (string)  
| Sets the username for the email user. [More...](class_email_user.html#ac3189a180c19f67a3cd352f1b399b3a8)  
  
void | [setName](class_email_user.html#a2ac44be7b66426ce34379f1ba3d0df24) (string)  
| Sets the name for the email user. [More...](class_email_user.html#a2ac44be7b66426ce34379f1ba3d0df24)  
  
string | [getMailId](class_email_user.html#a89b8807cfa83baba82cb943475eb18aa) ()  
| Returns the email address of the email user. [More...](class_email_user.html#a89b8807cfa83baba82cb943475eb18aa)  
  
string | [getPassword](class_email_user.html#ac011829734cfaf1763f60713feb0c7cb) ()  
| Returns the password of the email user. [More...](class_email_user.html#ac011829734cfaf1763f60713feb0c7cb)  
  
void | [setMailId](class_email_user.html#a11231f40c323c3ab1639ba3ced1783de) (string)  
| Sets the email address for the email user. [More...](class_email_user.html#a11231f40c323c3ab1639ba3ced1783de)  
  
void | [setPassword](class_email_user.html#a7f0e5e1cc9b2332cda85e6a870dac162) (string)  
| Sets the password for the email user. [More...](class_email_user.html#a7f0e5e1cc9b2332cda85e6a870dac162)  
  
string | [getSmtpServer](class_email_user.html#ae14f355bf62d4d46fbe5cc8d0c0f41a4) ()  
| Returns the SMTP server of the email user. [More...](class_email_user.html#ae14f355bf62d4d46fbe5cc8d0c0f41a4)  
  
string | [getPop3Server](class_email_user.html#a7ccad002a85adcf76f0749f69a430bbc) ()  
| Returns the POP3 server of the email user. [More...](class_email_user.html#a7ccad002a85adcf76f0749f69a430bbc)  
  
void | [setSmtpServer](class_email_user.html#af030e71a97b617ebde71dacfe888153f) (string)  
| Sets the SMTP server for the email user. [More...](class_email_user.html#af030e71a97b617ebde71dacfe888153f)  
  
void | [setPop3Server](class_email_user.html#a3cf9b5c3ccf8f1d48b076d62c2418393) (string)  
| Sets the POP3 server for the email user. [More...](class_email_user.html#a3cf9b5c3ccf8f1d48b076d62c2418393)  
  
[MailBox](class_mail_box.html) | [getMailBox](class_email_user.html#af65b278f19d80428b96e7fdb287a7a03) ()  
| Returns the mailbox of the email user. [More...](class_email_user.html#af65b278f19d80428b96e7fdb287a7a03)  
  
  
## Detailed Description

[EmailUser](class_email_user.html "EmailUser holds and manipulates the email user.") holds and manipulates the email user. 

## Member Function Documentation

## ◆ getMailBox()

[MailBox](class_mail_box.html) EmailUser::getMailBox  | ( | | ) |   
---|---|---|---|---  
  
Returns the mailbox of the email user. 

Returns
    string, the mailbox of the email user. Through the object, emails can be added, accessed, removed. 

## ◆ getMailId()

string EmailUser::getMailId  | ( | | ) |   
---|---|---|---|---  
  
Returns the email address of the email user. 

Returns
    string, the email address of the email user. 

## ◆ getName()

string EmailUser::getName  | ( | | ) |   
---|---|---|---|---  
  
Returns the name of the email user. 

Returns
    string, the name of the email user. 

## ◆ getPassword()

string EmailUser::getPassword  | ( | | ) |   
---|---|---|---|---  
  
Returns the password of the email user. 

Returns
    string, the password of the email user. 

## ◆ getPop3Server()

string EmailUser::getPop3Server  | ( | | ) |   
---|---|---|---|---  
  
Returns the POP3 server of the email user. 

Returns
    string, the POP3 server of the email user. 

## ◆ getSmtpServer()

string EmailUser::getSmtpServer  | ( | | ) |   
---|---|---|---|---  
  
Returns the SMTP server of the email user. 

Returns
    string, the SMTP server of the email user. 

## ◆ getUser()

string EmailUser::getUser  | ( | | ) |   
---|---|---|---|---  
  
Returns the username of the email user. 

Returns
    string, the username of the email user. 

## ◆ setMailId()

void EmailUser::setMailId  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the email address for the email user. 

Parameters
     mailid,the| email address for the email user.   
---|---  
  
## ◆ setName()

void EmailUser::setName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the name for the email user. 

Parameters
     name,the| name for the email user.   
---|---  
  
## ◆ setPassword()

void EmailUser::setPassword  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the password for the email user. 

Parameters
     password,the| password for the email user.   
---|---  
  
## ◆ setPop3Server()

void EmailUser::setPop3Server  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the POP3 server for the email user. 

Parameters
     server,the| SMTP server for the email user.   
---|---  
  
## ◆ setSmtpServer()

void EmailUser::setSmtpServer  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the SMTP server for the email user. 

Parameters
     server,the| SMTP server for the email user.   
---|---  
  
## ◆ setUser()

void EmailUser::setUser  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the username for the email user. 

Parameters
     user,the| username for the email user.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CEmailUser.pki](_c_email_user_8pki.html)


