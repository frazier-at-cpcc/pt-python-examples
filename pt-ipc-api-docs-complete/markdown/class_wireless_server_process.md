# Cisco Packet Tracer Extensions API: WirelessServerProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_wireless_server_process.html

---

##  Public Member Functions  
  
---  
bool | [isMacFilterEnabled](class_wireless_server_process.html#aa31170f90232e6fc1a27e243bb48148f) ()  
| Gets the mac filtering enable or disable state. [More...](class_wireless_server_process.html#aa31170f90232e6fc1a27e243bb48148f)  
  
void | [setMacFilterEnabled](class_wireless_server_process.html#a8fb76ac52e3abd281adddd772a808ab1) (bool)  
| Enables/Disables wireless mac filtering. [More...](class_wireless_server_process.html#a8fb76ac52e3abd281adddd772a808ab1)  
  
void | [setAllowAccess](class_wireless_server_process.html#a1a55e0476c5710a4fa934110b0207246) (bool)  
| Sets the mode to allow access from listed mac addresses, or deny access for listed mac addresses. [More...](class_wireless_server_process.html#a1a55e0476c5710a4fa934110b0207246)  
  
bool | [isAccessAllowed](class_wireless_server_process.html#aca466ded8ea39e66e9409a8f8dc1bc15) ()  
| Gets the mode to allow access from listed mac addresses, or deny access for listed mac addresses. [More...](class_wireless_server_process.html#aca466ded8ea39e66e9409a8f8dc1bc15)  
  
void | [removeAllMacEntries](class_wireless_server_process.html#aac638c6ef2a8cd01ad0aacaf941b760a) ()  
| Clears the mac filtering table. [More...](class_wireless_server_process.html#aac638c6ef2a8cd01ad0aacaf941b760a)  
  
vector< mac > | [getAllMacEntries](class_wireless_server_process.html#a1666699ae16b33a38701d2936cf79a5e) ()  
| Gets all of the mac entries. [More...](class_wireless_server_process.html#a1666699ae16b33a38701d2936cf79a5e)  
  
int | [getMacAddressCount](class_wireless_server_process.html#adf690fe6aed345393b16888394a074fb) ()  
| Gets the count of the mac addresses. [More...](class_wireless_server_process.html#adf690fe6aed345393b16888394a074fb)  
  
mac | [getMacAddressAt](class_wireless_server_process.html#af36a72b72d8d608814b33aac55731851) (int)  
| Gets the mac entry at index. [More...](class_wireless_server_process.html#af36a72b72d8d608814b33aac55731851)  
  
void | [resetAllAssociations](class_wireless_server_process.html#a7ee851f55fd9e1d6165310cd18a38b81) ()  
| Resets wireless client associations so that the new filters will affect existing associations. [More...](class_wireless_server_process.html#a7ee851f55fd9e1d6165310cd18a38b81)  
  
void | [addToMacFilterAddrList](class_wireless_server_process.html#a9d69671aee8fb2ce7e9e401ed5ffaae5) (mac)  
| Add a mac address to the filtering table. [More...](class_wireless_server_process.html#a9d69671aee8fb2ce7e9e401ed5ffaae5)  
  
void | [removeFromMacFilterAddrList](class_wireless_server_process.html#a458cfb0cb95c753c48d4d604fd4e4444) (mac)  
| Removes a mac address from the filtering table. [More...](class_wireless_server_process.html#a458cfb0cb95c753c48d4d604fd4e4444)  
  
bool | [isSsidBrdCastEnabled](class_wireless_server_process.html#a6d331b59a1fe2dea619063f59c779b72) ()  
| Check if ssid broadcast is enabled. [More...](class_wireless_server_process.html#a6d331b59a1fe2dea619063f59c779b72)  
  
void | [setSsidBrdCastEnabled](class_wireless_server_process.html#a9df4d2b919c141c3ba82421d003c4a39) (bool)  
| Set Ssid broadcast enabled. [More...](class_wireless_server_process.html#a9df4d2b919c141c3ba82421d003c4a39)  
  
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
    
    
    \brief WirelessServerProcess handles and manipulates wireless servers.
    
    \example network().getDevice("PC0").getProcess("WirelessServer")
    

## Member Function Documentation

## ◆ addToMacFilterAddrList()

void WirelessServerProcess::addToMacFilterAddrList  | ( | mac  | | ) |   
---|---|---|---|---|---  
  
Add a mac address to the filtering table. 

Parameters
     mac| String of the mac address   
---|---  
  
Returns
    bool whether adding was successful. Adding an existing mac will be considered successful. 

## ◆ getAllMacEntries()

vector< mac > WirelessServerProcess::getAllMacEntries  | ( | | ) |   
---|---|---|---|---  
  
Gets all of the mac entries. 

## ◆ getMacAddressAt()

mac WirelessServerProcess::getMacAddressAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Gets the mac entry at index. 

Parameters
     index| the index of the desired mac address   
---|---  
  
## ◆ getMacAddressCount()

int WirelessServerProcess::getMacAddressCount  | ( | | ) |   
---|---|---|---|---  
  
Gets the count of the mac addresses. 

## ◆ isAccessAllowed()

bool WirelessServerProcess::isAccessAllowed  | ( | | ) |   
---|---|---|---|---  
  
Gets the mode to allow access from listed mac addresses, or deny access for listed mac addresses. 

Returns
    If the current mode is to allow access or deny access. True mean listed macs are allowed. 

## ◆ isMacFilterEnabled()

bool WirelessServerProcess::isMacFilterEnabled  | ( | | ) |   
---|---|---|---|---  
  
Gets the mac filtering enable or disable state. 

Returns
    Whether mac filtering is enabled or disabled. True is enabled. 

## ◆ isSsidBrdCastEnabled()

bool WirelessServerProcess::isSsidBrdCastEnabled  | ( | | ) |   
---|---|---|---|---  
  
Check if ssid broadcast is enabled. 

Returns
    bool, true if ssid broadcast is enabled and false if not 

## ◆ removeAllMacEntries()

void WirelessServerProcess::removeAllMacEntries  | ( | | ) |   
---|---|---|---|---  
  
Clears the mac filtering table. 

## ◆ removeFromMacFilterAddrList()

void WirelessServerProcess::removeFromMacFilterAddrList  | ( | mac  | | ) |   
---|---|---|---|---|---  
  
Removes a mac address from the filtering table. 

Parameters
     mac| The mac addres to remove   
---|---  
  
## ◆ resetAllAssociations()

void WirelessServerProcess::resetAllAssociations  | ( | | ) |   
---|---|---|---|---  
  
Resets wireless client associations so that the new filters will affect existing associations. 

## ◆ setAllowAccess()

void WirelessServerProcess::setAllowAccess  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Sets the mode to allow access from listed mac addresses, or deny access for listed mac addresses. 

Parameters
     enable| true means allow listed mac addresses to use it. false means deny listed mac addresses.   
---|---  
  
## ◆ setMacFilterEnabled()

void WirelessServerProcess::setMacFilterEnabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables/Disables wireless mac filtering. 

Parameters
     enable| Whether to enable or disable it.   
---|---  
  
## ◆ setSsidBrdCastEnabled()

void WirelessServerProcess::setSsidBrdCastEnabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Set Ssid broadcast enabled. 

Parameters
     enabled,true| if ssid broadcast is enabled and false if not   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CWirelessServerProcess.pki](_c_wireless_server_process_8pki.html)


