# Cisco Packet Tracer Extensions API: EmailServer Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_email_server.html

---

[EmailServer](class_email_server.html "EmailServer is the process that handles the email server.") is the process that handles the email server. [More...](class_email_server.html#details)

##  Public Member Functions  
  
---  
bool | [addUser](class_email_server.html#a49f60acd5d61af084cc02023ef2ad6ac) (string, string)  
| Adds an email user with the specified username and password. [More...](class_email_server.html#a49f60acd5d61af084cc02023ef2ad6ac)  
  
bool | [deleteUser](class_email_server.html#a9f7f8810602be6753ccfdc336769b630) (string)  
| Removes the email user with the specified username. [More...](class_email_server.html#a9f7f8810602be6753ccfdc336769b630)  
  
void | [changePassword](class_email_server.html#a9d241b0a2f70726a4f856c7a94068712) (string, string)  
| Changes the password of the email user with the specifed username. [More...](class_email_server.html#a9d241b0a2f70726a4f856c7a94068712)  
  
[EmailUser](class_email_user.html) | [getEmailUser](class_email_server.html#a07d0dcd272fc996b33a7b47ac824f3ed) (string)  
| Returns the email user with specified username. [More...](class_email_server.html#a07d0dcd272fc996b33a7b47ac824f3ed)  
  
vector< string > | [getAllEmailAcctAsStrings](class_email_server.html#a0f5649202e4f4222a5e1df067baf5b2a) ()  
| Adds an email user with the specified username and password. [More...](class_email_server.html#a0f5649202e4f4222a5e1df067baf5b2a)  
  
void | [updateAllAccounts](class_email_server.html#a7781a994d04ef7d30b0d9029b9c72326) (string)  
| Updates passwords and adds user accounts based on the given formatted string.   
Format each entry as "name:password;". So two entries would be formated as "name1:password1;name2:password2;" If a username exists, the password will be set. If a username doesn't exist, the entry will be added. [More...](class_email_server.html#a7781a994d04ef7d30b0d9029b9c72326)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[EmailServer](class_email_server.html "EmailServer is the process that handles the email server.") is the process that handles the email server. 

## Member Function Documentation

## ◆ addUser()

bool EmailServer::addUser  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Adds an email user with the specified username and password. 

Parameters
     name,the| username for the email user.   
---|---  
password,the| password for the email user.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ changePassword()

void EmailServer::changePassword  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Changes the password of the email user with the specifed username. 

Parameters
     name,the| username of the email user of interest.   
---|---  
newpassword,the| new password for the email user.   
  
## ◆ deleteUser()

bool EmailServer::deleteUser  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes the email user with the specified username. 

Parameters
     name,the| username of the email user of interest.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ getAllEmailAcctAsStrings()

vector< string > EmailServer::getAllEmailAcctAsStrings  | ( | | ) |   
---|---|---|---|---  
  
Adds an email user with the specified username and password. 

Returns
    vector<string>, Return is all email accounts. Each entry is in the format "name:password", like "jitu:jituPass". 

## ◆ getEmailUser()

[EmailUser](class_email_user.html) EmailServer::getEmailUser  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the email user with specified username. 

Parameters
     username,the| username of the email user of interest.  
---|---  
  
Returns
    [EmailUser](class_email_user.html "EmailUser holds and manipulates the email user."), the [EmailUser](class_email_user.html "EmailUser holds and manipulates the email user.") object with the specified username. 

## ◆ updateAllAccounts()

void EmailServer::updateAllAccounts  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Updates passwords and adds user accounts based on the given formatted string.   
Format each entry as "name:password;". So two entries would be formated as "name1:password1;name2:password2;" If a username exists, the password will be set. If a username doesn't exist, the entry will be added. 

* * *

The documentation for this class was generated from the following file:

  * [CEmailServer.pki](_c_email_server_8pki.html)


