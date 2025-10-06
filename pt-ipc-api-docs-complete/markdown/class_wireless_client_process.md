# Cisco Packet Tracer Extensions API: WirelessClientProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_wireless_client_process.html

---

[WirelessClientProcess](class_wireless_client_process.html "WirelessClientProcess handles and manipulates wireless clients.") handles and manipulates wireless clients. [More...](class_wireless_client_process.html#details)

##  Public Member Functions  
  
---  
bool | [addProfile](class_wireless_client_process.html#a819325cbf3272cc7a52a6349c68afd6d) (string, string, WirelessNetworkType, mac, WirelessAuthenType, WirelessEncryptType, string, string, string, bool, bool, ip, ip, ip, ip)  
| Adds a wireless profile. [More...](class_wireless_client_process.html#a819325cbf3272cc7a52a6349c68afd6d)  
  
bool | [deleteProfile](class_wireless_client_process.html#a5e14ebfa398bc70a5f00fa767b6beaa0) (string)  
| Deletes the wireless profile with the specified name. [More...](class_wireless_client_process.html#a5e14ebfa398bc70a5f00fa767b6beaa0)  
  
[WirelessProfile](struct_wireless_profile.html) | [getProfile](class_wireless_client_process.html#a2f226ce21d00f5da558b17c38cf4ff61) (string)  
| Returns the wireless profile with the specified name. [More...](class_wireless_client_process.html#a2f226ce21d00f5da558b17c38cf4ff61)  
  
int | [getProfileCount](class_wireless_client_process.html#ad4428e4a6c9b9576d11bbceb7ea2922a) ()  
| Returns the number of wireless profiles. [More...](class_wireless_client_process.html#ad4428e4a6c9b9576d11bbceb7ea2922a)  
  
[WirelessProfile](struct_wireless_profile.html) | [getProfileAt](class_wireless_client_process.html#ab3ed26b81c7a42f0d76bc8ad37fd7b41) (int)  
| Returns the wireless profile at the specified index. [More...](class_wireless_client_process.html#ab3ed26b81c7a42f0d76bc8ad37fd7b41)  
  
[WirelessProfile](struct_wireless_profile.html) | [getCurrentProfile](class_wireless_client_process.html#ae56d7931518e122706b291618e608ca6) ()  
| Returns the current wireless profile. [More...](class_wireless_client_process.html#ae56d7931518e122706b291618e608ca6)  
  
bool | [setCurrentProfile](class_wireless_client_process.html#abfebf75213af56a7f0e799aa56398d04) (string, string, WirelessNetworkType, mac, WirelessAuthenType, WirelessEncryptType, string, string, string, bool, bool, ip, ip, ip, ip)  
| Sets the current wireless profile with the specified settings. [More...](class_wireless_client_process.html#abfebf75213af56a7f0e799aa56398d04)  
  
bool | [setCurrentProfileStringIPs](class_wireless_client_process.html#a5434759975c7b5fa9ab06804ffa43f5e) (string, string, WirelessNetworkType, string, WirelessAuthenType, WirelessEncryptType, string, string, string, bool, bool, string, string, string, string)  
int | [getCurrentNetworkCount](class_wireless_client_process.html#a78167a6472e8a77df598e115da01defe) ()  
| Returns the number of current network wireless profiles. [More...](class_wireless_client_process.html#a78167a6472e8a77df598e115da01defe)  
  
[WirelessProfile](struct_wireless_profile.html) | [getCurrentNetworkAt](class_wireless_client_process.html#a17bfbd8d84fea1e2f38566fdf1057fba) (int)  
| Returns the current network wireless profile at the specified index. [More...](class_wireless_client_process.html#a17bfbd8d84fea1e2f38566fdf1057fba)  
  
mac | [getCurrentApMac](class_wireless_client_process.html#abbd34b110bbc1b7b7fb05a6845dbe2f1) ()  
| Returns the MAC address of the current access point. [More...](class_wireless_client_process.html#abbd34b110bbc1b7b7fb05a6845dbe2f1)  
  
Public Member Functions inherited from [WirelessCommon](class_wireless_common.html)  
WirelessAuthenType | [getAuthenType](class_wireless_common.html#a73da1817e0194e42055f2d11325e1ec1) ()  
| Returns the authentication type. [More...](class_wireless_common.html#a73da1817e0194e42055f2d11325e1ec1)  
  
void | [setAuthenType](class_wireless_common.html#a55b6c0bb0be61fae37d57b9ca647d3d4) (WirelessAuthenType)  
void | [setSsid](class_wireless_common.html#aa77261561b1a910cc29213a51647f179) (string)  
| Sets the SSID. [More...](class_wireless_common.html#aa77261561b1a910cc29213a51647f179)  
  
string | [getSsid](class_wireless_common.html#a3407cc8e38b0762bf57f66baaac5c205) ()  
| Returns the SSID. [More...](class_wireless_common.html#a3407cc8e38b0762bf57f66baaac5c205)  
  
WirelessNetworkType | [getNetworkType](class_wireless_common.html#a24ef5bbbc91040285a9efe0053e34b46) ()  
| Returns the network type. [More...](class_wireless_common.html#a24ef5bbbc91040285a9efe0053e34b46)  
  
void | [setNetworkType](class_wireless_common.html#a1956bc3e9f762bac3b2650eb1b109432) (WirelessNetworkType)  
bool | [setPort](class_wireless_common.html#aecafc76dd3db544d51c44dd404d246cc) (string)  
| Sets the wireless port with the specified port. [More...](class_wireless_common.html#aecafc76dd3db544d51c44dd404d246cc)  
  
[Port](class_port.html) | [getPort](class_wireless_common.html#acf6ed21c09269c4492738b14b01e5066) ()  
| Returns the wireless port. [More...](class_wireless_common.html#acf6ed21c09269c4492738b14b01e5066)  
  
[WEPProcess](class_w_e_p_process.html) | [getWepProcess](class_wireless_common.html#a3f410c65baa2b5304d97b444beddb26a) ()  
| Returns the WEP process. [More...](class_wireless_common.html#a3f410c65baa2b5304d97b444beddb26a)  
  
void | [resetAllAssociations](class_wireless_common.html#a44f9435c843f296d41123dca98846b00) ()  
| Resets all wireless associations. [More...](class_wireless_common.html#a44f9435c843f296d41123dca98846b00)  
  
WirelessEncryptType | [getEncryptType](class_wireless_common.html#a3c6da8ef9e79c1999c3a16ea1de48854) ()  
| Get encryption type. [More...](class_wireless_common.html#a3c6da8ef9e79c1999c3a16ea1de48854)  
  
void | [setEncryptType](class_wireless_common.html#a453e59c57cc3c044738e220fb875c258) (WirelessEncryptType)  
| Set encryption type \para type, enum<WirelessEncryptType> eEncryptNull = 0, eEncryptWep_64bit = 1, eEncryptWep_128bit = 2, eEncryptTKIP = 3, //Arun wpa eEncryptAES = 4. [More...](class_wireless_common.html#a453e59c57cc3c044738e220fb875c258)  
  
void | [setStandardChannel](class_wireless_common.html#adeb4b681e9fb72ba38fa308144693e2a) (StandardChannel)  
| Set standard channel \para type, enum<StandardChannel>   
eStandardChannel_1 = 0, // channel: 1 - 2.412GHz eStandardChannel_2 = 1, // channel: 2 - 2.417GHz eStandardChannel_3 = 2, // channel: 3 - 2.422GHz eStandardChannel_4 = 3, // channel: 4 - 2.427GHz eStandardChannel_5 = 4, // channel: 5 - 2.432GHz eStandardChannel_6 = 5, // channel: 6 - 2.437GHz eStandardChannel_7 = 6, // channel: 7 - 2.442GHz eStandardChannel_8 = 7, // channel: 8 - 2.447GHz eStandardChannel_9 = 8, // channel: 9 - 2.452GHz eStandardChannel_10 = 9, // channel: 10 - 2.457GHz eStandardChannel_11 = 10 // channel: 11 - 2.462GHz. [More...](class_wireless_common.html#adeb4b681e9fb72ba38fa308144693e2a)  
  
StandardChannel | [getStandardChannel](class_wireless_common.html#ad9b3cf7631b50b15f70c7a1d9de0697e) ()  
| Get standard channel. [More...](class_wireless_common.html#ad9b3cf7631b50b15f70c7a1d9de0697e)  
  
void | [setWideChannel](class_wireless_common.html#a1ccadd79b5931e03802b3c29cf1305bb) (WideChannel)  
| Set wide channel. [More...](class_wireless_common.html#a1ccadd79b5931e03802b3c29cf1305bb)  
  
WideChannel | [getWideChannel](class_wireless_common.html#ad96be35c35495432c570fafa93567809) ()  
| Get wide channel. [More...](class_wireless_common.html#ad96be35c35495432c570fafa93567809)  
  
WirelessRadioBand | [getRadioBand](class_wireless_common.html#a3b45b59413f71c18b72676d8d4cd4c8d) ()  
| Get radio band. [More...](class_wireless_common.html#a3b45b59413f71c18b72676d8d4cd4c8d)  
  
void | [setRadioBand](class_wireless_common.html#a9311a28f95c9c58b7db57f3d0d7d0ed8) (WirelessRadioBand)  
| Set radio band. [More...](class_wireless_common.html#a9311a28f95c9c58b7db57f3d0d7d0ed8)  
  
[WPAProcess](class_w_p_a_process.html) | [getWpaProcess](class_wireless_common.html#a4a2d2e1e942a839d14b617d2600a4c63) ()  
| Get Wpa [Process](class_process.html "Process is the base class for all device processes."). [More...](class_wireless_common.html#a4a2d2e1e942a839d14b617d2600a4c63)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[WirelessClientProcess](class_wireless_client_process.html "WirelessClientProcess handles and manipulates wireless clients.") handles and manipulates wireless clients. 

## Member Function Documentation

## ◆ addProfile()

bool WirelessClientProcess::addProfile  | ( | string  | ,   
---|---|---|---  
|  | string  | ,   
|  | WirelessNetworkType  | ,   
|  | mac  | ,   
|  | WirelessAuthenType  | ,   
|  | WirelessEncryptType  | ,   
|  | string  | ,   
|  | string  | ,   
|  | string  | ,   
|  | bool  | ,   
|  | bool  | ,   
|  | ip  | ,   
|  | ip  | ,   
|  | ip  | ,   
|  | ip  |   
| ) | |   
  
Adds a wireless profile. 

Parameters
     name,the| name for the wireless profile.   
---|---  
ssid,the| SSID of the access point.   
netType,the| network type. [Network](class_network.html "Network is the entry point for all device configurations in the network. It retrieves devices.") types: eWirelessDisabled = 0x0, eWirelessB = 0x1, eWirelessG = 0x2, eWirelessBGMixed = 0x3, eWirelessN = 0x4, eWirelessA = 0x5, eWirelessMixed = 0x7   
macAddress,the| MAC address of the access point.   
authType,the| authentication type. Authentication types: eAuthenNull = 0, eAuthenWep = 1, eAuthenWPA1_PSK = 2, eAuthenWPA1_EAP = 3, eAuthenWPA2_PSK = 4, eAuthenWPA2_EAP = 5, eAuthenOpen = 6   
encryptType,the| encryption type. Encryption types: eEncryptNull = 0, eEncryptWep_64bit = 1, eEncryptWep_128bit = 2, eEncryptTKIP = 3, eEncryptAES = 4   
wepKey,the| WEP key.   
userid,the| user ID for WPA enterprise.   
password,the| password for WPA enterprise.   
bDHCPOn,true| to enable DHCP, false to disable DHCP.   
bDHCPv6On,true| to enable DHCPv6, false to disable DHCPv6.   
ipAddress,the| IP address for the interface.   
subnet,the| subnet mask for the interface.   
gateway,the| default gateway for the interface.   
DNS,the| DNS server for the interface.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ deleteProfile()

bool WirelessClientProcess::deleteProfile  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Deletes the wireless profile with the specified name. 

Parameters
     name,the| name of the wireless profile of interest.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ getCurrentApMac()

mac WirelessClientProcess::getCurrentApMac  | ( | | ) |   
---|---|---|---|---  
  
Returns the MAC address of the current access point. 

Returns
    mac, the MAC address of the current access point. 

## ◆ getCurrentNetworkAt()

[WirelessProfile](struct_wireless_profile.html) WirelessClientProcess::getCurrentNetworkAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the current network wireless profile at the specified index. 

Parameters
     index,the| index of the current network wireless profile of interest.  
---|---  
  
Returns
    [WirelessProfile](struct_wireless_profile.html "Data element for WirelessProfile."), the [WirelessProfile](struct_wireless_profile.html "Data element for WirelessProfile.") object at the specified index. 

## ◆ getCurrentNetworkCount()

int WirelessClientProcess::getCurrentNetworkCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of current network wireless profiles. 

Returns
    int, the number of current networks wireless profiles. 

## ◆ getCurrentProfile()

[WirelessProfile](struct_wireless_profile.html) WirelessClientProcess::getCurrentProfile  | ( | | ) |   
---|---|---|---|---  
  
Returns the current wireless profile. 

Returns
    [WirelessProfile](struct_wireless_profile.html "Data element for WirelessProfile."), the [WirelessProfile](struct_wireless_profile.html "Data element for WirelessProfile.") object. 

## ◆ getProfile()

[WirelessProfile](struct_wireless_profile.html) WirelessClientProcess::getProfile  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the wireless profile with the specified name. 

Parameters
     name,the| name of the wireless profile of interest.  
---|---  
  
Returns
    [WirelessProfile](struct_wireless_profile.html "Data element for WirelessProfile."), the [WirelessProfile](struct_wireless_profile.html "Data element for WirelessProfile.") object with the specified name. 

## ◆ getProfileAt()

[WirelessProfile](struct_wireless_profile.html) WirelessClientProcess::getProfileAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the wireless profile at the specified index. 

Parameters
     index,the| index of the wireless profile of interest.  
---|---  
  
Returns
    [WirelessProfile](struct_wireless_profile.html "Data element for WirelessProfile."), the [WirelessProfile](struct_wireless_profile.html "Data element for WirelessProfile.") object at the specified index. 

## ◆ getProfileCount()

int WirelessClientProcess::getProfileCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of wireless profiles. 

Returns
    int, the number of wireless profiles. 

## ◆ setCurrentProfile()

bool WirelessClientProcess::setCurrentProfile  | ( | string  | ,   
---|---|---|---  
|  | string  | ,   
|  | WirelessNetworkType  | ,   
|  | mac  | ,   
|  | WirelessAuthenType  | ,   
|  | WirelessEncryptType  | ,   
|  | string  | ,   
|  | string  | ,   
|  | string  | ,   
|  | bool  | ,   
|  | bool  | ,   
|  | ip  | ,   
|  | ip  | ,   
|  | ip  | ,   
|  | ip  |   
| ) | |   
  
Sets the current wireless profile with the specified settings. 

Parameters
     name,the| name for the wireless profile.   
---|---  
ssid,the| SSID of the access point.   
netType,the| network type. [Network](class_network.html "Network is the entry point for all device configurations in the network. It retrieves devices.") types: eWirelessDisabled = 0x0, eWirelessB = 0x1, eWirelessG = 0x2, eWirelessBGMixed = 0x3, eWirelessN = 0x4, eWirelessA = 0x5, eWirelessMixed = 0x7   
macAddress,the| MAC address of the access point.   
authType,the| authentication type. Authentication types: eAuthenNull = 0, eAuthenWep = 1, eAuthenWPA1_PSK = 2, eAuthenWPA1_EAP = 3, eAuthenWPA2_PSK = 4, eAuthenWPA2_EAP = 5, eAuthenOpen = 6   
encryptType,the| encryption type. Encryption types: eEncryptNull = 0, eEncryptWep_64bit = 1, eEncryptWep_128bit = 2, eEncryptTKIP = 3, eEncryptAES = 4   
wepKey,the| WEP key.   
userid,the| user ID for WPA enterprise.   
password,the| password for WPA enterprise.   
bDHCPOn,true| to enable DHCP, false to disable DHCP.   
bDHCPv6On,true| to enable DHCPv6, false to disable DHCPv6.   
ipAddress,the| IP address for the interface.   
subnet,the| subnet mask for the interface.   
gateway,the| default gateway for the interface.   
DNS,the| DNS server for the interface.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ setCurrentProfileStringIPs()

bool WirelessClientProcess::setCurrentProfileStringIPs  | ( | string  | ,   
---|---|---|---  
|  | string  | ,   
|  | WirelessNetworkType  | ,   
|  | string  | ,   
|  | WirelessAuthenType  | ,   
|  | WirelessEncryptType  | ,   
|  | string  | ,   
|  | string  | ,   
|  | string  | ,   
|  | bool  | ,   
|  | bool  | ,   
|  | string  | ,   
|  | string  | ,   
|  | string  | ,   
|  | string  |   
| ) | |   
  
* * *

The documentation for this class was generated from the following file:

  * [CWirelessClientProcess.pki](_c_wireless_client_process_8pki.html)


