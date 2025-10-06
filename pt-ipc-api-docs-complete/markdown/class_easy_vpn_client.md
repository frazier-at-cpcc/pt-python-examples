# Cisco Packet Tracer Extensions API: EasyVpnClient Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_easy_vpn_client.html

---

[EasyVpnClient](class_easy_vpn_client.html "EasyVpnClient is the process that handles the Easy VPN client.") is the process that handles the Easy VPN client. [More...](class_easy_vpn_client.html#details)

##  Public Member Functions  
  
---  
void | [setServerIp](class_easy_vpn_client.html#a71c56f09d3ce445aba54005fc4f6673e) (ip)  
| Sets the server IP address for the Easy VPN client. [More...](class_easy_vpn_client.html#a71c56f09d3ce445aba54005fc4f6673e)  
  
ip | [getServerIp](class_easy_vpn_client.html#a988a4a5fae3c513ca3a28b747ba95594) ()  
| Returns the server IP address for the Easy VPN client. [More...](class_easy_vpn_client.html#a988a4a5fae3c513ca3a28b747ba95594)  
  
void | [setUsername](class_easy_vpn_client.html#a4d59f4f6d2461653d67c916be0c40d9c) (string)  
| Sets the username for the Easy VPN client. [More...](class_easy_vpn_client.html#a4d59f4f6d2461653d67c916be0c40d9c)  
  
string | [getUsername](class_easy_vpn_client.html#a693bf96f8380c5e5a6ebbfa2fae1dcee) ()  
| Returns the username for the Easy VPN client. [More...](class_easy_vpn_client.html#a693bf96f8380c5e5a6ebbfa2fae1dcee)  
  
void | [setPassword](class_easy_vpn_client.html#ad691a2d0afb6945f7a0486e0e7042c98) (string)  
| Sets the password for the Easy VPN client. [More...](class_easy_vpn_client.html#ad691a2d0afb6945f7a0486e0e7042c98)  
  
string | [getPassword](class_easy_vpn_client.html#a1e79968dd9f16d566639f68c47d64e63) ()  
| Returns the password for the Easy VPN client. [More...](class_easy_vpn_client.html#a1e79968dd9f16d566639f68c47d64e63)  
  
void | [setGroupName](class_easy_vpn_client.html#a18325c3ca7b3890ffcbc6fb70c5a6673) (string)  
| Sets the group name for the Easy VPN client. [More...](class_easy_vpn_client.html#a18325c3ca7b3890ffcbc6fb70c5a6673)  
  
string | [getGroupName](class_easy_vpn_client.html#a04dbf8ef6041c423db43af076a17571b) ()  
| Returns the group name for the Easy VPN client. [More...](class_easy_vpn_client.html#a04dbf8ef6041c423db43af076a17571b)  
  
void | [setGroupKey](class_easy_vpn_client.html#aa5f50a81a14db86b59e054133d7b3867) (string)  
| Sets the group key for the Easy VPN client. [More...](class_easy_vpn_client.html#aa5f50a81a14db86b59e054133d7b3867)  
  
string | [getGroupKey](class_easy_vpn_client.html#a0263429552b2fc21e71ea7619a397338) ()  
| Returns the group key for the Easy VPN client. [More...](class_easy_vpn_client.html#a0263429552b2fc21e71ea7619a397338)  
  
void | [setTunnelIp](class_easy_vpn_client.html#a74b37f8e65a954f44901ef994047bdf3) (ip)  
| Sets the tunnel IP address for the Easy VPN client. [More...](class_easy_vpn_client.html#a74b37f8e65a954f44901ef994047bdf3)  
  
ip | [getTunnelIp](class_easy_vpn_client.html#a7c5f1e2be3000026f0409e874b653abe) ()  
| Returns the tunnel IP address for the Easy VPN client. [More...](class_easy_vpn_client.html#a7c5f1e2be3000026f0409e874b653abe)  
  
void | [setTunnelMask](class_easy_vpn_client.html#aa919fb35511a97e56cb18878ce258351) (ip)  
| Sets the tunnel mask for the Easy VPN client. [More...](class_easy_vpn_client.html#aa919fb35511a97e56cb18878ce258351)  
  
ip | [getTunnelMask](class_easy_vpn_client.html#a11e4f81422ce2f4e6be3395bc4e80da6) ()  
| Returns the tunnel mask for the Easy VPN client. [More...](class_easy_vpn_client.html#a11e4f81422ce2f4e6be3395bc4e80da6)  
  
void | [connect](class_easy_vpn_client.html#a436912b9004ecd0279d3f62ebae7ff2e) ()  
| Connects the Easy VPN client. [More...](class_easy_vpn_client.html#a436912b9004ecd0279d3f62ebae7ff2e)  
  
void | [disconnect](class_easy_vpn_client.html#a8bc985c46bb7fde0d4b8d075185ae3be) ()  
| Disconnects the Easy VPN client. [More...](class_easy_vpn_client.html#a8bc985c46bb7fde0d4b8d075185ae3be)  
  
bool | [isConnected](class_easy_vpn_client.html#a31fdde7870741dfd67f1d06d21d4724c) ()  
| Returns true if the Easy VPN client is connected, false otherwise. [More...](class_easy_vpn_client.html#a31fdde7870741dfd67f1d06d21d4724c)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[EasyVpnClient](class_easy_vpn_client.html "EasyVpnClient is the process that handles the Easy VPN client.") is the process that handles the Easy VPN client. 

## Member Function Documentation

## ◆ connect()

void EasyVpnClient::connect  | ( | | ) |   
---|---|---|---|---  
  
Connects the Easy VPN client. 

## ◆ disconnect()

void EasyVpnClient::disconnect  | ( | | ) |   
---|---|---|---|---  
  
Disconnects the Easy VPN client. 

## ◆ getGroupKey()

string EasyVpnClient::getGroupKey  | ( | | ) |   
---|---|---|---|---  
  
Returns the group key for the Easy VPN client. 

Returns
    string, the group key for the Easy VPN client. 

## ◆ getGroupName()

string EasyVpnClient::getGroupName  | ( | | ) |   
---|---|---|---|---  
  
Returns the group name for the Easy VPN client. 

Returns
    string, the group name for the Easy VPN client. 

## ◆ getPassword()

string EasyVpnClient::getPassword  | ( | | ) |   
---|---|---|---|---  
  
Returns the password for the Easy VPN client. 

Returns
    string, the password for the Easy VPN client. 

## ◆ getServerIp()

ip EasyVpnClient::getServerIp  | ( | | ) |   
---|---|---|---|---  
  
Returns the server IP address for the Easy VPN client. 

Returns
    ip, the server IP address for the Easy VPN client. 

## ◆ getTunnelIp()

ip EasyVpnClient::getTunnelIp  | ( | | ) |   
---|---|---|---|---  
  
Returns the tunnel IP address for the Easy VPN client. 

Returns
    ip, the tunnel IP address for the Easy VPN client. 

## ◆ getTunnelMask()

ip EasyVpnClient::getTunnelMask  | ( | | ) |   
---|---|---|---|---  
  
Returns the tunnel mask for the Easy VPN client. 

Returns
    ip, the tunnel mask for the Easy VPN client. 

## ◆ getUsername()

string EasyVpnClient::getUsername  | ( | | ) |   
---|---|---|---|---  
  
Returns the username for the Easy VPN client. 

Returns
    string, the sername for the Easy VPN client. 

## ◆ isConnected()

bool EasyVpnClient::isConnected  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the Easy VPN client is connected, false otherwise. 

Returns
    bool, true if the Easy VPN client is connected, false otherwise. 

## ◆ setGroupKey()

void EasyVpnClient::setGroupKey  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the group key for the Easy VPN client. 

Parameters
     groupKey,the| group key for the Easy VPN client.   
---|---  
  
## ◆ setGroupName()

void EasyVpnClient::setGroupName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the group name for the Easy VPN client. 

Parameters
     groupName,the| group name for the Easy VPN client.   
---|---  
  
## ◆ setPassword()

void EasyVpnClient::setPassword  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the password for the Easy VPN client. 

Parameters
     password,the| password for the Easy VPN client.   
---|---  
  
## ◆ setServerIp()

void EasyVpnClient::setServerIp  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Sets the server IP address for the Easy VPN client. 

Parameters
     serverIp,the| server IP address for the Easy VPN client.   
---|---  
  
## ◆ setTunnelIp()

void EasyVpnClient::setTunnelIp  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Sets the tunnel IP address for the Easy VPN client. 

Parameters
     tunnelIp,the| tunnel IP address for the Easy VPN client.   
---|---  
  
## ◆ setTunnelMask()

void EasyVpnClient::setTunnelMask  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Sets the tunnel mask for the Easy VPN client. 

Parameters
     tunnelIp,the| tunnel mask for the Easy VPN client.   
---|---  
  
## ◆ setUsername()

void EasyVpnClient::setUsername  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the username for the Easy VPN client. 

Parameters
     username,the| username for the Easy VPN client.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CEasyVpnClient.pki](_c_easy_vpn_client_8pki.html)


