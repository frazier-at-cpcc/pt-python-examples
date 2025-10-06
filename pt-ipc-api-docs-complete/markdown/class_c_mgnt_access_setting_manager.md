# Cisco Packet Tracer Extensions API: CMgntAccessSettingManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_c_mgnt_access_setting_manager.html

---

[CMgntAccessSettingManager](class_c_mgnt_access_setting_manager.html "CMgntAccessSettingManager is the asa object storage manager class that is used to store and retrieve ...") is the asa object storage manager class that is used to store and retrieve asa object. [More...](class_c_mgnt_access_setting_manager.html#details)

##  Public Member Functions  
  
---  
bool | [deleteIpv4MgntAccessSetting](class_c_mgnt_access_setting_manager.html#a3c9262a83e8c6de86588c9903cdb21aa) (AccessProtocol, ip, ip, string)  
| Delete the access configuration that matches protocol, allowed ip address, allowed mask and nameIf. [More...](class_c_mgnt_access_setting_manager.html#a3c9262a83e8c6de86588c9903cdb21aa)  
  
bool | [deleteIpv6MgntAccessSetting](class_c_mgnt_access_setting_manager.html#a0c9c160f6c462673f1267589f12822c2) (AccessProtocol, ip, int, string)  
| Delete the access configuration that matches protocol, allowed ip address, allowed prefix and nameIf. [More...](class_c_mgnt_access_setting_manager.html#a0c9c160f6c462673f1267589f12822c2)  
  
bool | [addMgntAccessSetting](class_c_mgnt_access_setting_manager.html#af4694160c7fcddea24eb8e8f3996262f) (AccessProtocol, ip, ip, string)  
| Add the access configuration that matches protocol, allowed ip address, allowed mask and nameIf. [More...](class_c_mgnt_access_setting_manager.html#af4694160c7fcddea24eb8e8f3996262f)  
  
[CMgntAccessSetting](class_c_mgnt_access_setting.html) | [getMgntAccessSettingAt](class_c_mgnt_access_setting_manager.html#a329741661f544ad31854f9a34fb87de4) (int)  
| Returns the access setting a specified index. [More...](class_c_mgnt_access_setting_manager.html#a329741661f544ad31854f9a34fb87de4)  
  
int | [getMgntAccessSettingCount](class_c_mgnt_access_setting_manager.html#a08b1d5ada4553532a21b16772963a39c) ()  
| Return the number of access setting. [More...](class_c_mgnt_access_setting_manager.html#a08b1d5ada4553532a21b16772963a39c)  
  
void | [setSshTimeout](class_c_mgnt_access_setting_manager.html#aec9e0554cd63174c3926dfe838ea3149) (int)  
| Set the ssh timeout for ssh connection. [More...](class_c_mgnt_access_setting_manager.html#aec9e0554cd63174c3926dfe838ea3149)  
  
int | [getSshTimeout](class_c_mgnt_access_setting_manager.html#acc569de52d7d041fe9c725376d11142a) ()  
| Return the ssh timeout. [More...](class_c_mgnt_access_setting_manager.html#acc569de52d7d041fe9c725376d11142a)  
  
void | [setTelnetTimeout](class_c_mgnt_access_setting_manager.html#a2592751e551075a13b2cde519b485ca0) (int)  
| Set the telnet timeout for telnet connection. [More...](class_c_mgnt_access_setting_manager.html#a2592751e551075a13b2cde519b485ca0)  
  
int | [getTelnetTimeout](class_c_mgnt_access_setting_manager.html#a4c6b48d9de8ebd8e07720fbdd19efc5a) ()  
| Return the Telnet timeout. [More...](class_c_mgnt_access_setting_manager.html#a4c6b48d9de8ebd8e07720fbdd19efc5a)  
  
bool | [allow](class_c_mgnt_access_setting_manager.html#a193aba98e1daf95632a333dbb3d49924) (AccessProtocol, ip, string)  
| Check to see if the traffic that matches protocol, ipAddress into srcNameIf allowed or not. [More...](class_c_mgnt_access_setting_manager.html#a193aba98e1daf95632a333dbb3d49924)  
  
  
## Detailed Description

[CMgntAccessSettingManager](class_c_mgnt_access_setting_manager.html "CMgntAccessSettingManager is the asa object storage manager class that is used to store and retrieve ...") is the asa object storage manager class that is used to store and retrieve asa object. 

## Member Function Documentation

## ◆ addMgntAccessSetting()

bool CMgntAccessSettingManager::addMgntAccessSetting  | ( | AccessProtocol  | ,   
---|---|---|---  
|  | ip  | ,   
|  | ip  | ,   
|  | string  |   
| ) | |   
  
Add the access configuration that matches protocol, allowed ip address, allowed mask and nameIf. 

Parameters
     protocol,ssh/telnet/http|   
---|---  
allowedIp,ip| address   
allowedMask,mask|   
srcNameIf,nameIf| of the interface that allow remote access  
  
Returns
    bool, value is true if the add was successful, false if not. 

## ◆ allow()

bool CMgntAccessSettingManager::allow  | ( | AccessProtocol  | ,   
---|---|---|---  
|  | ip  | ,   
|  | string  |   
| ) | |   
  
Check to see if the traffic that matches protocol, ipAddress into srcNameIf allowed or not. 

Parameters
     protocol,ssh/telnet/http|   
---|---  
ipAddress,source| ip address of the host   
srcNameIf,the| nameif of the interface in which the host is trying to gain access into  
  
Returns
    bool, value is true if the traffic that matches protocol, ipAddress into srcNameIf allowed, false if not. 

## ◆ deleteIpv4MgntAccessSetting()

bool CMgntAccessSettingManager::deleteIpv4MgntAccessSetting  | ( | AccessProtocol  | ,   
---|---|---|---  
|  | ip  | ,   
|  | ip  | ,   
|  | string  |   
| ) | |   
  
Delete the access configuration that matches protocol, allowed ip address, allowed mask and nameIf. 

Parameters
     protocol,ssh/telnet/http|   
---|---  
allowedIp,ip| address   
allowedMask,mask|   
srcNameIf,nameIf| of the interface that allow remote access  
  
Returns
    bool, value is true if the delete was successful, false if not. 

## ◆ deleteIpv6MgntAccessSetting()

bool CMgntAccessSettingManager::deleteIpv6MgntAccessSetting  | ( | AccessProtocol  | ,   
---|---|---|---  
|  | ip  | ,   
|  | int  | ,   
|  | string  |   
| ) | |   
  
Delete the access configuration that matches protocol, allowed ip address, allowed prefix and nameIf. 

Parameters
     protocol,ssh/telnet/http|   
---|---  
allowedIp,ip| address   
allowedPrefix,ipv6| prefix   
srcNameIf,nameIf| of the interface that allow remote access  
  
Returns
    bool, value is true if the delete was successful, false if not. 

## ◆ getMgntAccessSettingAt()

[CMgntAccessSetting](class_c_mgnt_access_setting.html) CMgntAccessSettingManager::getMgntAccessSettingAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the access setting a specified index. 

Parameters
     index,index| to retrive the access setting from. Range (0, [getMgntAccessSettingCount()](class_c_mgnt_access_setting_manager.html#a08b1d5ada4553532a21b16772963a39c "Return the number of access setting.")).  
---|---  
  
Returns
    [CMgntAccessSetting](class_c_mgnt_access_setting.html "CMgntAccessSetting is used to control telnet and ssh access into the asa."), value is the access setting a specified index. 

## ◆ getMgntAccessSettingCount()

int CMgntAccessSettingManager::getMgntAccessSettingCount  | ( | | ) |   
---|---|---|---|---  
  
Return the number of access setting. 

Returns
    int, value is the number of access settings. 

## ◆ getSshTimeout()

int CMgntAccessSettingManager::getSshTimeout  | ( | | ) |   
---|---|---|---|---  
  
Return the ssh timeout. 

Returns
    int, value is the ssh timeout. 

## ◆ getTelnetTimeout()

int CMgntAccessSettingManager::getTelnetTimeout  | ( | | ) |   
---|---|---|---|---  
  
Return the Telnet timeout. 

Returns
    int, value is the Telnet timeout. 

## ◆ setSshTimeout()

void CMgntAccessSettingManager::setSshTimeout  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Set the ssh timeout for ssh connection. 

Parameters
     timeout,in| minutes   
---|---  
  
## ◆ setTelnetTimeout()

void CMgntAccessSettingManager::setTelnetTimeout  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Set the telnet timeout for telnet connection. 

Parameters
     timeout,in| minutes   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CMgntAccessSettingManager.pki](_c_mgnt_access_setting_manager_8pki.html)


