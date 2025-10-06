# Cisco Packet Tracer Extensions API: FtpUserAccountManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_ftp_user_account_manager.html

---

[FtpUserAccountManager](class_ftp_user_account_manager.html "FtpUserAccountManager manages user accounts for FTP servers.") manages user accounts for FTP servers. [More...](class_ftp_user_account_manager.html#details)

##  Public Member Functions  
  
---  
void | [addFtpUser](class_ftp_user_account_manager.html#a910492b0e7b326fddb6c7599db2a290c) (string, string, string)  
| Adds an FTP user account with the specified username, password, and permissions. [More...](class_ftp_user_account_manager.html#a910492b0e7b326fddb6c7599db2a290c)  
  
void | [removeFtpUser](class_ftp_user_account_manager.html#abea7db43ab527f402506d85d5d20c1ac) (string)  
| Removes the specified FTP user account. [More...](class_ftp_user_account_manager.html#abea7db43ab527f402506d85d5d20c1ac)  
  
bool | [isExistingUser](class_ftp_user_account_manager.html#a631125beef419b28015674aba15dfdd9) (string)  
| Returns true if the specified username already exists, otherwise false. [More...](class_ftp_user_account_manager.html#a631125beef419b28015674aba15dfdd9)  
  
int | [getUsersCount](class_ftp_user_account_manager.html#a4870d5c6cc4593b58c1506795c56ac08) ()  
| Returns the number of users accounts. [More...](class_ftp_user_account_manager.html#a4870d5c6cc4593b58c1506795c56ac08)  
  
string | [getUsernameAt](class_ftp_user_account_manager.html#ae2cc5477ab3e4bf019963007180bf34b) (int)  
| Returns the username at given index. [More...](class_ftp_user_account_manager.html#ae2cc5477ab3e4bf019963007180bf34b)  
  
string | [getPasswordAt](class_ftp_user_account_manager.html#ad323151bf92daa6ee60edc7f8bbc11e3) (int)  
| Returns the password at given index. [More...](class_ftp_user_account_manager.html#ad323151bf92daa6ee60edc7f8bbc11e3)  
  
string | [getPermissionAt](class_ftp_user_account_manager.html#a510e1432ef0833c649252e6543b3a0e9) (int)  
| Returns the permission at given index. [More...](class_ftp_user_account_manager.html#a510e1432ef0833c649252e6543b3a0e9)  
  
  
## Detailed Description

[FtpUserAccountManager](class_ftp_user_account_manager.html "FtpUserAccountManager manages user accounts for FTP servers.") manages user accounts for FTP servers. 

## Member Function Documentation

## ◆ addFtpUser()

void FtpUserAccountManager::addFtpUser  | ( | string  | ,   
---|---|---|---  
|  | string  | ,   
|  | string  |   
| ) | |   
  
Adds an FTP user account with the specified username, password, and permissions. 

Parameters
     username,the| username for the account.   
---|---  
password,the| password for the account.   
perms,the| permissions for the account. Permissions: R - Read W - Write N - Rename L - List D - Delete Example: "RW" will permit read and write operations   
  
## ◆ getPasswordAt()

string FtpUserAccountManager::getPasswordAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the password at given index. 

Parameters
     i,index| of the user.  
---|---  
  
Returns
    string, the password at given index. 

## ◆ getPermissionAt()

string FtpUserAccountManager::getPermissionAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the permission at given index. 

Parameters
     i,index| of the user.  
---|---  
  
Returns
    string, the permission at given index. 

## ◆ getUsernameAt()

string FtpUserAccountManager::getUsernameAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the username at given index. 

Parameters
     i,index| of the user.  
---|---  
  
Returns
    string, the username at given index. 

## ◆ getUsersCount()

int FtpUserAccountManager::getUsersCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of users accounts. 

Returns
    int, the number of users accounts. 

## ◆ isExistingUser()

bool FtpUserAccountManager::isExistingUser  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns true if the specified username already exists, otherwise false. 

Parameters
     username,the| username of the account of interest.  
---|---  
  
Returns
    bool, true if the specified username already exists, otherwise false. 

## ◆ removeFtpUser()

void FtpUserAccountManager::removeFtpUser  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes the specified FTP user account. 

Parameters
     username,the| username of the account of interest.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CFtpUserAccountManager.pki](_c_ftp_user_account_manager_8pki.html)


