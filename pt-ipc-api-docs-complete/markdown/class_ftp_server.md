# Cisco Packet Tracer Extensions API: FtpServer Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_ftp_server.html

---

[FtpServer](class_ftp_server.html "FtpServer is the process that handles the FTP service.") is the process that handles the FTP service. [More...](class_ftp_server.html#details)

##  Public Member Functions  
  
---  
void | [setEnabled](class_ftp_server.html#a4910537f53efb1572348b422e158c25c) (bool)  
| Enables or disables the FTP service. [More...](class_ftp_server.html#a4910537f53efb1572348b422e158c25c)  
  
bool | [isEnabled](class_ftp_server.html#adff67485e2b526937f5f4fab0becf945) ()  
| Returns true if the FTP service is enabled, otherwise false. [More...](class_ftp_server.html#adff67485e2b526937f5f4fab0becf945)  
  
[FtpUserAccountManager](class_ftp_user_account_manager.html) | [getFtpUserAccountManager](class_ftp_server.html#a744c3ba2e35936608be9f02ad610a63c) ()  
| Returns the FTP user account manager. [More...](class_ftp_server.html#a744c3ba2e35936608be9f02ad610a63c)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[FtpServer](class_ftp_server.html "FtpServer is the process that handles the FTP service.") is the process that handles the FTP service. 

## Member Function Documentation

## ◆ getFtpUserAccountManager()

[FtpUserAccountManager](class_ftp_user_account_manager.html) FtpServer::getFtpUserAccountManager  | ( | | ) |   
---|---|---|---|---  
  
Returns the FTP user account manager. 

Returns
    [FtpUserAccountManager](class_ftp_user_account_manager.html "FtpUserAccountManager manages user accounts for FTP servers."), the [FtpUserAccountManager](class_ftp_user_account_manager.html "FtpUserAccountManager manages user accounts for FTP servers.") object. 

## ◆ isEnabled()

bool FtpServer::isEnabled  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the FTP service is enabled, otherwise false. 

Returns
    bool, true if the FTP service is enabled, otherwise false. 

## ◆ setEnabled()

void FtpServer::setEnabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables the FTP service. 

Parameters
     bEnable,true| to enable the FTP service, false to disable it.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CFtpServerProcess.pki](_c_ftp_server_process_8pki.html)


