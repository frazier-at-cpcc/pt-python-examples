# Cisco Packet Tracer Extensions API: VtpProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_vtp_process.html

---

[VtpProcess](class_vtp_process.html "VtpProcess handles and manipulates the VTP process.") handles and manipulates the VTP process. [More...](class_vtp_process.html#details)

##  Public Member Functions  
  
---  
void | [setDomainName](class_vtp_process.html#a74369ee1b27c59b9ab360875707d6618) (string)  
| Sets the VTP domain name. [More...](class_vtp_process.html#a74369ee1b27c59b9ab360875707d6618)  
  
string | [getDomainName](class_vtp_process.html#aa66fa6fe4f5b52847f10f5c7f936f43d) ()  
| Returns the VTP domain name. [More...](class_vtp_process.html#aa66fa6fe4f5b52847f10f5c7f936f43d)  
  
void | [setMode](class_vtp_process.html#a070a31c2cac5e63b825559cb6bb89aa3) (VtpMode)  
| Sets the VTP mode. [More...](class_vtp_process.html#a070a31c2cac5e63b825559cb6bb89aa3)  
  
VtpMode | [getMode](class_vtp_process.html#a450b22e88dcff01c31609e53e9f09e85) ()  
| Returns the VTP mode. [More...](class_vtp_process.html#a450b22e88dcff01c31609e53e9f09e85)  
  
void | [setVersion](class_vtp_process.html#a1793da662e3cf5c7802d7b282ff27ec6) (byte)  
| Sets the VTP version. [More...](class_vtp_process.html#a1793da662e3cf5c7802d7b282ff27ec6)  
  
byte | [getVersion](class_vtp_process.html#aa848bf63b8af79d2ba187f403a46e20e) ()  
| Returns the VTP version. [More...](class_vtp_process.html#aa848bf63b8af79d2ba187f403a46e20e)  
  
void | [setPassword](class_vtp_process.html#ae8a3b511b59d681f4f616b157d5edc8a) (string)  
| Sets the VTP password. [More...](class_vtp_process.html#ae8a3b511b59d681f4f616b157d5edc8a)  
  
string | [getPassword](class_vtp_process.html#a5d5cb91908c03027dd9449508f218b63) ()  
| Returns the VTP password. [More...](class_vtp_process.html#a5d5cb91908c03027dd9449508f218b63)  
  
int | [getConfigRevision](class_vtp_process.html#a7fa64e0b7a9354953cb08da1a95c87ab) ()  
| Returns the configuration revision number. [More...](class_vtp_process.html#a7fa64e0b7a9354953cb08da1a95c87ab)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[VtpProcess](class_vtp_process.html "VtpProcess handles and manipulates the VTP process.") handles and manipulates the VTP process. 

## Member Function Documentation

## ◆ getConfigRevision()

int VtpProcess::getConfigRevision  | ( | | ) |   
---|---|---|---|---  
  
Returns the configuration revision number. 

Returns
    int, the configuration revision number. 

## ◆ getDomainName()

string VtpProcess::getDomainName  | ( | | ) |   
---|---|---|---|---  
  
Returns the VTP domain name. 

Returns
    string, the domain name. 

## ◆ getMode()

VtpMode VtpProcess::getMode  | ( | | ) |   
---|---|---|---|---  
  
Returns the VTP mode. 

Returns
    enum<VtpMode>, the VTP mode. VTP modes: eVtpServer = 0, eVtpClient = 1, eVtpTransparent = 2 

## ◆ getPassword()

string VtpProcess::getPassword  | ( | | ) |   
---|---|---|---|---  
  
Returns the VTP password. 

Parameters
     string,the| VTP version.   
---|---  
  
## ◆ getVersion()

byte VtpProcess::getVersion  | ( | | ) |   
---|---|---|---|---  
  
Returns the VTP version. 

Returns
    byte, the VTP version. 

## ◆ setDomainName()

void VtpProcess::setDomainName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the VTP domain name. 

Parameters
     domainName,the| domain name.   
---|---  
  
## ◆ setMode()

void VtpProcess::setMode  | ( | VtpMode  | | ) |   
---|---|---|---|---|---  
  
Sets the VTP mode. 

Parameters
     type,the| VTP mode. VTP modes: eVtpServer = 0, eVtpClient = 1, eVtpTransparent = 2   
---|---  
  
## ◆ setPassword()

void VtpProcess::setPassword  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the VTP password. 

Parameters
     password,the| VTP version.   
---|---  
  
## ◆ setVersion()

void VtpProcess::setVersion  | ( | byte  | | ) |   
---|---|---|---|---|---  
  
Sets the VTP version. 

Parameters
     version,the| VTP version.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CVtpProcess.pki](_c_vtp_process_8pki.html)


