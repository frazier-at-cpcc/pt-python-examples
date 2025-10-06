# Cisco Packet Tracer Extensions API: CMgntAccessSetting Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_c_mgnt_access_setting.html

---

[CMgntAccessSetting](class_c_mgnt_access_setting.html "CMgntAccessSetting is used to control telnet and ssh access into the asa.") is used to control telnet and ssh access into the asa. [More...](class_c_mgnt_access_setting.html#details)

##  Public Member Functions  
  
---  
AccessProtocol | [getAccessProtocol](class_c_mgnt_access_setting.html#a683e1daa8a41605ca83b64b476261e3e) ()  
| Return the access protocol eTelnet =0, eSsh, eHttp. [More...](class_c_mgnt_access_setting.html#a683e1daa8a41605ca83b64b476261e3e)  
  
ip | [getAllowedIp](class_c_mgnt_access_setting.html#a9eceae5a938f1cfa23addc60df728f4d) ()  
| Return the ip address that is allowed to access the asa. [More...](class_c_mgnt_access_setting.html#a9eceae5a938f1cfa23addc60df728f4d)  
  
ip | [getAllowedMask](class_c_mgnt_access_setting.html#a90b8c5a11f63b553313b08d545c6b26f) ()  
| Return the mask address of the host that is allowed to access the asa. [More...](class_c_mgnt_access_setting.html#a90b8c5a11f63b553313b08d545c6b26f)  
  
int | [getAllowedPrefix](class_c_mgnt_access_setting.html#a96c7a6e7969e4d96c20aa906e5dc2f83) ()  
| Return the prefix of the host that is allowed to access the asa. [More...](class_c_mgnt_access_setting.html#a96c7a6e7969e4d96c20aa906e5dc2f83)  
  
string | [getSrcNameIf](class_c_mgnt_access_setting.html#a83652e73d22113de0de7c370cadc86c3) ()  
| Return the nameif at which the host can access into. [More...](class_c_mgnt_access_setting.html#a83652e73d22113de0de7c370cadc86c3)  
  
int | [getTimeout](class_c_mgnt_access_setting.html#a132e39a9e41f0bc8da0d5847ab719e9c) ()  
| Return the timeout of the connection. [More...](class_c_mgnt_access_setting.html#a132e39a9e41f0bc8da0d5847ab719e9c)  
  
void | [setTimeout](class_c_mgnt_access_setting.html#afc765dff28a883a0d573ede730af5f9b) (int)  
| Set the timeout for the connection. [More...](class_c_mgnt_access_setting.html#afc765dff28a883a0d573ede730af5f9b)  
  
string | [toString](class_c_mgnt_access_setting.html#ac34fd07841e3c1c7c237b387a45c152c) ()  
| Return the configuration in string. [More...](class_c_mgnt_access_setting.html#ac34fd07841e3c1c7c237b387a45c152c)  
  
void | [setIpv4](class_c_mgnt_access_setting.html#ab1b079bfa8240e56d01fcd09b6335590) (bool)  
| set the access setting to ipv4 when it permits an ipv4 address [More...](class_c_mgnt_access_setting.html#ab1b079bfa8240e56d01fcd09b6335590)  
  
bool | [isIpv4](class_c_mgnt_access_setting.html#a38b0451af404417edaeb5b53ea25e73c) ()  
| Return true if the setting allows ipv4 address and false if the setting allows ipv6 address. [More...](class_c_mgnt_access_setting.html#a38b0451af404417edaeb5b53ea25e73c)  
  
bool | [isActive](class_c_mgnt_access_setting.html#a885ad55d1c16baeae2d8f654a4e0d650) ()  
| Return true if the setting has all of the required configuration for example (ip address is set on the nameif interface) [More...](class_c_mgnt_access_setting.html#a885ad55d1c16baeae2d8f654a4e0d650)  
  
void | [setActive](class_c_mgnt_access_setting.html#ad6708659add74986f997561adc95a359) (bool)  
| Set the setting to be active or inactive. [More...](class_c_mgnt_access_setting.html#ad6708659add74986f997561adc95a359)  
  
  
## Detailed Description

[CMgntAccessSetting](class_c_mgnt_access_setting.html "CMgntAccessSetting is used to control telnet and ssh access into the asa.") is used to control telnet and ssh access into the asa. 

## Member Function Documentation

## ◆ getAccessProtocol()

AccessProtocol CMgntAccessSetting::getAccessProtocol  | ( | | ) |   
---|---|---|---|---  
  
Return the access protocol eTelnet =0, eSsh, eHttp. 

## ◆ getAllowedIp()

ip CMgntAccessSetting::getAllowedIp  | ( | | ) |   
---|---|---|---|---  
  
Return the ip address that is allowed to access the asa. 

Returns
    ip, value is the ip address that is allowed to access the asa. 

## ◆ getAllowedMask()

ip CMgntAccessSetting::getAllowedMask  | ( | | ) |   
---|---|---|---|---  
  
Return the mask address of the host that is allowed to access the asa. 

Returns
    ip, value is the mask address of the host that is allowed to access the asa. 

## ◆ getAllowedPrefix()

int CMgntAccessSetting::getAllowedPrefix  | ( | | ) |   
---|---|---|---|---  
  
Return the prefix of the host that is allowed to access the asa. 

Returns
    int, value is the the prefix of the host that is allowed to access the asa. 

## ◆ getSrcNameIf()

string CMgntAccessSetting::getSrcNameIf  | ( | | ) |   
---|---|---|---|---  
  
Return the nameif at which the host can access into. 

Returns
    string, value is the nameif at which the host can access into. 

## ◆ getTimeout()

int CMgntAccessSetting::getTimeout  | ( | | ) |   
---|---|---|---|---  
  
Return the timeout of the connection. 

Returns
    int, value is the timeout of the connection. 

## ◆ isActive()

bool CMgntAccessSetting::isActive  | ( | | ) |   
---|---|---|---|---  
  
Return true if the setting has all of the required configuration for example (ip address is set on the nameif interface) 

Returns
    bool, value is true if the setting has all of the required configuration. 

## ◆ isIpv4()

bool CMgntAccessSetting::isIpv4  | ( | | ) |   
---|---|---|---|---  
  
Return true if the setting allows ipv4 address and false if the setting allows ipv6 address. 

Returns
    bool, value is true if the setting allows ipv4 address and false if the setting allows ipv6 address. 

## ◆ setActive()

void CMgntAccessSetting::setActive  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Set the setting to be active or inactive. 

Parameters
     isActive,true| to set to active, false to inactive.   
---|---  
  
## ◆ setIpv4()

void CMgntAccessSetting::setIpv4  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
set the access setting to ipv4 when it permits an ipv4 address 

Parameters
     isIpv4| \- true if ipv4; false if ipv6   
---|---  
  
## ◆ setTimeout()

void CMgntAccessSetting::setTimeout  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Set the timeout for the connection. 

Parameters
     timeout| \- time in minutes   
---|---  
  
## ◆ toString()

string CMgntAccessSetting::toString  | ( | | ) |   
---|---|---|---|---  
  
Return the configuration in string. 

Returns
    string, value is the configuration string. 

* * *

The documentation for this class was generated from the following file:

  * [CMgntAccessSetting.pki](_c_mgnt_access_setting_8pki.html)


