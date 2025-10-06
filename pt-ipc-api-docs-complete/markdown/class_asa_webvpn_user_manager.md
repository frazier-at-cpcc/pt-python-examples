# Cisco Packet Tracer Extensions API: AsaWebvpnUserManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_asa_webvpn_user_manager.html

---

[AsaWebvpnUserManager](class_asa_webvpn_user_manager.html "AsaWebvpnUserManager manages clientless VPN users on ASA devices.") manages clientless VPN users on [ASA](class_a_s_a.html "ASA is the base class for all ASA devices.") devices. [More...](class_asa_webvpn_user_manager.html#details)

##  Public Member Functions  
  
---  
[AsaWebvpnUserInfo](class_asa_webvpn_user_info.html) | [addClientlessVpnUser](class_asa_webvpn_user_manager.html#a04e8ededfdacfc9d94e7089aaa6ac21e) (string, string, string, string, string)  
| Adds a clientless VPN user with the specified username, profile, group policy, and bookmark. [More...](class_asa_webvpn_user_manager.html#a04e8ededfdacfc9d94e7089aaa6ac21e)  
  
[AsaWebvpnUserInfo](class_asa_webvpn_user_info.html) | [getClientlessVpnUser](class_asa_webvpn_user_manager.html#a13ddffdbc04d821ca241bb8a1f4c603b) (string)  
| Returns the clientless VPN user with the specified username. [More...](class_asa_webvpn_user_manager.html#a13ddffdbc04d821ca241bb8a1f4c603b)  
  
void | [removeClientlessVpnUser](class_asa_webvpn_user_manager.html#a5d150312056e8a891b47a3e9c9a51a22) (string)  
| Removes the clientless VPN user with the specified username. [More...](class_asa_webvpn_user_manager.html#a5d150312056e8a891b47a3e9c9a51a22)  
  
int | [getClientlessVpnUserCount](class_asa_webvpn_user_manager.html#a7f7dbc966ba857e7c68640dc10943127) ()  
| Returns the number of clientless VPN users. [More...](class_asa_webvpn_user_manager.html#a7f7dbc966ba857e7c68640dc10943127)  
  
[AsaWebvpnUserInfo](class_asa_webvpn_user_info.html) | [getClientlessVpnUserAt](class_asa_webvpn_user_manager.html#a5037d590a3e8f3412af24fa2587f20e7) (int)  
| Returns the clientless VPN user at the specified index. [More...](class_asa_webvpn_user_manager.html#a5037d590a3e8f3412af24fa2587f20e7)  
  
  
## Detailed Description

[AsaWebvpnUserManager](class_asa_webvpn_user_manager.html "AsaWebvpnUserManager manages clientless VPN users on ASA devices.") manages clientless VPN users on [ASA](class_a_s_a.html "ASA is the base class for all ASA devices.") devices. 

## Member Function Documentation

## ◆ addClientlessVpnUser()

[AsaWebvpnUserInfo](class_asa_webvpn_user_info.html) AsaWebvpnUserManager::addClientlessVpnUser  | ( | string  | ,   
---|---|---|---  
|  | string  | ,   
|  | string  | ,   
|  | string  | ,   
|  | string  |   
| ) | |   
  
Adds a clientless VPN user with the specified username, profile, group policy, and bookmark. 

/param username, the username for the clientless VPN user. /param profileName, the name of the profile. /param policyName, the name of the group policy. /param bookmarkName, the title of the bookmark. /param urlName, the URL of the bookmark.

Returns
    [AsaWebvpnUserInfo](class_asa_webvpn_user_info.html "AsaWebvpnUserInfo manipulates clientless VPN users on ASA devices."), the [AsaWebvpnUserInfo](class_asa_webvpn_user_info.html "AsaWebvpnUserInfo manipulates clientless VPN users on ASA devices.") object. 

## ◆ getClientlessVpnUser()

[AsaWebvpnUserInfo](class_asa_webvpn_user_info.html) AsaWebvpnUserManager::getClientlessVpnUser  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the clientless VPN user with the specified username. 

/param username, the username of the clientless VPN user of interest.

Returns
    [AsaWebvpnUserInfo](class_asa_webvpn_user_info.html "AsaWebvpnUserInfo manipulates clientless VPN users on ASA devices."), the [AsaWebvpnUserInfo](class_asa_webvpn_user_info.html "AsaWebvpnUserInfo manipulates clientless VPN users on ASA devices.") object. 

## ◆ getClientlessVpnUserAt()

[AsaWebvpnUserInfo](class_asa_webvpn_user_info.html) AsaWebvpnUserManager::getClientlessVpnUserAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the clientless VPN user at the specified index. 

/param index, the index of the clientless VPN user of interest.

Returns
    [AsaWebvpnUserInfo](class_asa_webvpn_user_info.html "AsaWebvpnUserInfo manipulates clientless VPN users on ASA devices."), the [AsaWebvpnUserInfo](class_asa_webvpn_user_info.html "AsaWebvpnUserInfo manipulates clientless VPN users on ASA devices.") object. 

## ◆ getClientlessVpnUserCount()

int AsaWebvpnUserManager::getClientlessVpnUserCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of clientless VPN users. 

Returns
    int, the number of clientless VPN users. 

## ◆ removeClientlessVpnUser()

void AsaWebvpnUserManager::removeClientlessVpnUser  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes the clientless VPN user with the specified username. 

/param username, the username of the clientless VPN user of interest. 

* * *

The documentation for this class was generated from the following file:

  * [CWebvpnUserManager.pki](_c_webvpn_user_manager_8pki.html)


