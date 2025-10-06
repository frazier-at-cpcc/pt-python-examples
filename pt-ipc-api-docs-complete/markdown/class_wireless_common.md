# Cisco Packet Tracer Extensions API: WirelessCommon Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_wireless_common.html

---

[WirelessCommon](class_wireless_common.html "WirelessCommon handles and manipulates common wireless settings.") handles and manipulates common wireless settings. [More...](class_wireless_common.html#details)

##  Public Member Functions  
  
---  
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

[WirelessCommon](class_wireless_common.html "WirelessCommon handles and manipulates common wireless settings.") handles and manipulates common wireless settings. 

## Member Function Documentation

## ◆ getAuthenType()

WirelessAuthenType WirelessCommon::getAuthenType  | ( | | ) |   
---|---|---|---|---  
  
Returns the authentication type. 

Returns
    enum<WirelessAuthenType>, the authentication type. Authentication types: eAuthenNull = 0, eAuthenWep = 1, eAuthenWPA1_PSK = 2, eAuthenWPA1_EAP = 3, eAuthenWPA2_PSK = 4, eAuthenWPA2_EAP = 5, eAuthenOpen = 6 

## ◆ getEncryptType()

WirelessEncryptType WirelessCommon::getEncryptType  | ( | | ) |   
---|---|---|---|---  
  
Get encryption type. 

Returns
    enum<WirelessEncryptType>, eEncryptNull = 0, eEncryptWep_64bit = 1, eEncryptWep_128bit = 2, eEncryptTKIP = 3, //Arun wpa eEncryptAES = 4 

## ◆ getNetworkType()

WirelessNetworkType WirelessCommon::getNetworkType  | ( | | ) |   
---|---|---|---|---  
  
Returns the network type. 

Returns
    enum<WirelessNetworkType>, the network type. [Network](class_network.html "Network is the entry point for all device configurations in the network. It retrieves devices.") types: eWirelessDisabled = 0x0, eWirelessB = 0x1, eWirelessG = 0x2, eWirelessBGMixed = 0x3, eWirelessN = 0x4, eWirelessA = 0x5, eWirelessMixed = 0x7 

## ◆ getPort()

[Port](class_port.html) WirelessCommon::getPort  | ( | | ) |   
---|---|---|---|---  
  
Returns the wireless port. 

Returns
    [Port](class_port.html "Port holds and manipulates the ports on devices."), the [Port](class_port.html "Port holds and manipulates the ports on devices.") object. 

## ◆ getRadioBand()

WirelessRadioBand WirelessCommon::getRadioBand  | ( | | ) |   
---|---|---|---|---  
  
Get radio band. 

Returns
    enum<WirelessRadioBand>   
eRadioAuto = 0, eRadioStandard = 1, // 20 MHz Channel - on linksys eRadioWide = 2 // 40 MHz Channel - on linksys   


## ◆ getSsid()

string WirelessCommon::getSsid  | ( | | ) |   
---|---|---|---|---  
  
Returns the SSID. 

Returns
    string, the SSID. 

## ◆ getStandardChannel()

StandardChannel WirelessCommon::getStandardChannel  | ( | | ) |   
---|---|---|---|---  
  
Get standard channel. 

Returns
    enum<StandardChannel>   
eStandardChannel_1 = 0, // channel: 1 - 2.412GHz eStandardChannel_2 = 1, // channel: 2 - 2.417GHz eStandardChannel_3 = 2, // channel: 3 - 2.422GHz eStandardChannel_4 = 3, // channel: 4 - 2.427GHz eStandardChannel_5 = 4, // channel: 5 - 2.432GHz eStandardChannel_6 = 5, // channel: 6 - 2.437GHz eStandardChannel_7 = 6, // channel: 7 - 2.442GHz eStandardChannel_8 = 7, // channel: 8 - 2.447GHz eStandardChannel_9 = 8, // channel: 9 - 2.452GHz eStandardChannel_10 = 9, // channel: 10 - 2.457GHz eStandardChannel_11 = 10 // channel: 11 - 2.462GHz   


## ◆ getWepProcess()

[WEPProcess](class_w_e_p_process.html) WirelessCommon::getWepProcess  | ( | | ) |   
---|---|---|---|---  
  
Returns the WEP process. 

Returns
    [WEPProcess](class_w_e_p_process.html "WEPProcess handles and manipulates the WEP encryption process on wireless clients."), the [WEPProcess](class_w_e_p_process.html "WEPProcess handles and manipulates the WEP encryption process on wireless clients.") object. 

## ◆ getWideChannel()

WideChannel WirelessCommon::getWideChannel  | ( | | ) |   
---|---|---|---|---  
  
Get wide channel. 

Returns
    enum<StandardChannel>   
eWideChannel_Auto = 0, eWideChannel_3 = 1, eWideChannel_4 = 2, eWideChannel_5 = 3, eWideChannel_6 = 4, eWideChannel_7 = 5, eWideChannel_8 = 6, eWideChannel_9 = 7,   


## ◆ getWpaProcess()

[WPAProcess](class_w_p_a_process.html) WirelessCommon::getWpaProcess  | ( | | ) |   
---|---|---|---|---  
  
Get Wpa [Process](class_process.html "Process is the base class for all device processes."). 

Returns
    [WPAProcess](class_w_p_a_process.html "WPAProcess handles and manipulates the WPA encryption process on wireless clients."), the process that handles and manipulates the WPA encryption process on wireless clients.   


## ◆ resetAllAssociations()

void WirelessCommon::resetAllAssociations  | ( | | ) |   
---|---|---|---|---  
  
Resets all wireless associations. 

## ◆ setAuthenType()

void WirelessCommon::setAuthenType  | ( | WirelessAuthenType  | | ) |   
---|---|---|---|---|---  
  
## ◆ setEncryptType()

void WirelessCommon::setEncryptType  | ( | WirelessEncryptType  | | ) |   
---|---|---|---|---|---  
  
Set encryption type \para type, enum<WirelessEncryptType> eEncryptNull = 0, eEncryptWep_64bit = 1, eEncryptWep_128bit = 2, eEncryptTKIP = 3, //Arun wpa eEncryptAES = 4. 

Returns
    none   


## ◆ setNetworkType()

void WirelessCommon::setNetworkType  | ( | WirelessNetworkType  | | ) |   
---|---|---|---|---|---  
  
## ◆ setPort()

bool WirelessCommon::setPort  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the wireless port with the specified port. 

Parameters
     portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0   
---|---  
  
## ◆ setRadioBand()

void WirelessCommon::setRadioBand  | ( | WirelessRadioBand  | | ) |   
---|---|---|---|---|---  
  
Set radio band. 

Parameters
     radioBand,enum<WirelessRadioBand>|   
eRadioAuto = 0, eRadioStandard = 1, // 20 MHz Channel - on linksys eRadioWide = 2 // 40 MHz Channel - on linksys   
  
---|---  
  
## ◆ setSsid()

void WirelessCommon::setSsid  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the SSID. 

Parameters
     ssid,the| SSID.   
---|---  
  
## ◆ setStandardChannel()

void WirelessCommon::setStandardChannel  | ( | StandardChannel  | | ) |   
---|---|---|---|---|---  
  
Set standard channel \para type, enum<StandardChannel>   
eStandardChannel_1 = 0, // channel: 1 - 2.412GHz eStandardChannel_2 = 1, // channel: 2 - 2.417GHz eStandardChannel_3 = 2, // channel: 3 - 2.422GHz eStandardChannel_4 = 3, // channel: 4 - 2.427GHz eStandardChannel_5 = 4, // channel: 5 - 2.432GHz eStandardChannel_6 = 5, // channel: 6 - 2.437GHz eStandardChannel_7 = 6, // channel: 7 - 2.442GHz eStandardChannel_8 = 7, // channel: 8 - 2.447GHz eStandardChannel_9 = 8, // channel: 9 - 2.452GHz eStandardChannel_10 = 9, // channel: 10 - 2.457GHz eStandardChannel_11 = 10 // channel: 11 - 2.462GHz. 

Returns
    none   


## ◆ setWideChannel()

void WirelessCommon::setWideChannel  | ( | WideChannel  | | ) |   
---|---|---|---|---|---  
  
Set wide channel. 

Parameters
     channel,enum<StandardChannel>|   
eWideChannel_Auto = 0, eWideChannel_3 = 1, eWideChannel_4 = 2, eWideChannel_5 = 3, eWideChannel_6 = 4, eWideChannel_7 = 5, eWideChannel_8 = 6, eWideChannel_9 = 7,   
---|---  
  
Returns
    none   


* * *

The documentation for this class was generated from the following file:

  * [CWirelessCommon.pki](_c_wireless_common_8pki.html)


