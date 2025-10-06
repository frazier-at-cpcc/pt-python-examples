# Cisco Packet Tracer Extensions API: AsaWebvpnUserInfo Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_asa_webvpn_user_info.html

---

[AsaWebvpnUserInfo](class_asa_webvpn_user_info.html "AsaWebvpnUserInfo manipulates clientless VPN users on ASA devices.") manipulates clientless VPN users on [ASA](class_a_s_a.html "ASA is the base class for all ASA devices.") devices. [More...](class_asa_webvpn_user_info.html#details)

##  Public Member Functions  
  
---  
bool | [addBookmark](class_asa_webvpn_user_info.html#a94f49fd3eb6af7975d3c5bc3cf016448) (string, string)  
| Adds a bookmark with the specified name and URL. [More...](class_asa_webvpn_user_info.html#a94f49fd3eb6af7975d3c5bc3cf016448)  
  
void | [setProfileName](class_asa_webvpn_user_info.html#a2efffd8ad01af6f92fcac0364f8664f4) (string)  
| Sets the name of the profile. [More...](class_asa_webvpn_user_info.html#a2efffd8ad01af6f92fcac0364f8664f4)  
  
void | [setPolicyName](class_asa_webvpn_user_info.html#a8c9ce71f318519f4fbfb2fabe0066930) (string)  
| Sets the name of the group policy. [More...](class_asa_webvpn_user_info.html#a8c9ce71f318519f4fbfb2fabe0066930)  
  
void | [setBookmarkName](class_asa_webvpn_user_info.html#a3f1dced61eff78f23f6693d1393bf7a8) (string)  
| Sets the title of the bookmark. [More...](class_asa_webvpn_user_info.html#a3f1dced61eff78f23f6693d1393bf7a8)  
  
void | [setUrlName](class_asa_webvpn_user_info.html#a15f05b70f702b03fcbfba3716553b24f) (string)  
| Sets the URL of the bookmark. [More...](class_asa_webvpn_user_info.html#a15f05b70f702b03fcbfba3716553b24f)  
  
string | [getUserName](class_asa_webvpn_user_info.html#ad0f911ebc8a9de4ee78eefec0109a6cb) ()  
| Returns the username of this clientless VPN user. [More...](class_asa_webvpn_user_info.html#ad0f911ebc8a9de4ee78eefec0109a6cb)  
  
string | [getProfileName](class_asa_webvpn_user_info.html#aa41991930e4b2ed03afb40078c7345c9) ()  
| Returns the profile name of this clientless VPN user. [More...](class_asa_webvpn_user_info.html#aa41991930e4b2ed03afb40078c7345c9)  
  
string | [getPolicyName](class_asa_webvpn_user_info.html#a83584b06a2198c80a8d559a74ecaf591) ()  
| Returns the group policy name of this clientless VPN user. [More...](class_asa_webvpn_user_info.html#a83584b06a2198c80a8d559a74ecaf591)  
  
string | [getBookmarkName](class_asa_webvpn_user_info.html#a0c23bf70cc945b34577c9cc22c2fef39) ()  
| Returns the title of the bookmark of this clientless VPN user. [More...](class_asa_webvpn_user_info.html#a0c23bf70cc945b34577c9cc22c2fef39)  
  
string | [getUrlName](class_asa_webvpn_user_info.html#a7b48bdcc3c53c9b073da0d681db62976) ()  
| Returns the URL of the bookmark of this clientless VPN user. [More...](class_asa_webvpn_user_info.html#a7b48bdcc3c53c9b073da0d681db62976)  
  
  
## Detailed Description

[AsaWebvpnUserInfo](class_asa_webvpn_user_info.html "AsaWebvpnUserInfo manipulates clientless VPN users on ASA devices.") manipulates clientless VPN users on [ASA](class_a_s_a.html "ASA is the base class for all ASA devices.") devices. 

## Member Function Documentation

## ◆ addBookmark()

bool AsaWebvpnUserInfo::addBookmark  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Adds a bookmark with the specified name and URL. 

/param bookmarkName, the title of the bookmark. /param url, the URL of the bookmark.

Returns
    bool, true if the bookmark was added successfully, otherwise false. 

## ◆ getBookmarkName()

string AsaWebvpnUserInfo::getBookmarkName  | ( | | ) |   
---|---|---|---|---  
  
Returns the title of the bookmark of this clientless VPN user. 

Returns
    string, the title of the bookmark of this clientless VPN user. 

## ◆ getPolicyName()

string AsaWebvpnUserInfo::getPolicyName  | ( | | ) |   
---|---|---|---|---  
  
Returns the group policy name of this clientless VPN user. 

Returns
    string, the group policy name of this clientless VPN user. 

## ◆ getProfileName()

string AsaWebvpnUserInfo::getProfileName  | ( | | ) |   
---|---|---|---|---  
  
Returns the profile name of this clientless VPN user. 

Returns
    string, the profile name of this clientless VPN user. 

## ◆ getUrlName()

string AsaWebvpnUserInfo::getUrlName  | ( | | ) |   
---|---|---|---|---  
  
Returns the URL of the bookmark of this clientless VPN user. 

Returns
    string, the URL of the bookmark of this clientless VPN user. 

## ◆ getUserName()

string AsaWebvpnUserInfo::getUserName  | ( | | ) |   
---|---|---|---|---  
  
Returns the username of this clientless VPN user. 

Returns
    string, the username of this clientless VPN user. 

## ◆ setBookmarkName()

void AsaWebvpnUserInfo::setBookmarkName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the title of the bookmark. 

/param title, the title of the bookmark. 

## ◆ setPolicyName()

void AsaWebvpnUserInfo::setPolicyName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the name of the group policy. 

/param name, the name of the group policy. 

## ◆ setProfileName()

void AsaWebvpnUserInfo::setProfileName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the name of the profile. 

/param name, the name of the profile. 

## ◆ setUrlName()

void AsaWebvpnUserInfo::setUrlName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the URL of the bookmark. 

/param url, the URL of the bookmark. 

* * *

The documentation for this class was generated from the following file:

  * [CWebvpnUserInfo.pki](_c_webvpn_user_info_8pki.html)


