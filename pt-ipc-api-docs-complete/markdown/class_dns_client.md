# Cisco Packet Tracer Extensions API: DnsClient Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_dns_client.html

---

[DnsClient](class_dns_client.html "DnsClient is the process that handles retrieving DNS lookups.") is the process that handles retrieving DNS lookups. [More...](class_dns_client.html#details)

##  Public Member Functions  
  
---  
bool | [addIpAddress](class_dns_client.html#a41cd2bac50206d5cd3ece4d38c989097) (string, ip)  
| Adds a DNS entry with the specified hostname and IP address to the DNS table. [More...](class_dns_client.html#a41cd2bac50206d5cd3ece4d38c989097)  
  
void | [removeIpAddress](class_dns_client.html#a7d978f7def0e4c0798440299c11b8edb) (string)  
| Removes the DNS entry from the table based on the hostname. [More...](class_dns_client.html#a7d978f7def0e4c0798440299c11b8edb)  
  
void | [removeIp](class_dns_client.html#afc0572ddd8683cba451e4428c96a5187) (string, ip)  
| Removes the DNS entry from the table based on the hostname and the IP address. [More...](class_dns_client.html#afc0572ddd8683cba451e4428c96a5187)  
  
bool | [isValidName](class_dns_client.html#a6fddf9cf84a07b0e3f950b6726e59fd8) (string)  
void | [setServerIp](class_dns_client.html#ae9352af7f8b1da018a66a6c8f4100a6b) (ip)  
| Sets the IP address of the DNS server. [More...](class_dns_client.html#ae9352af7f8b1da018a66a6c8f4100a6b)  
  
ip | [getServerIp](class_dns_client.html#a53fe80037c50e3436f6d657e3a4efc57) ()  
| Returns the IP address of the DNS server. [More...](class_dns_client.html#a53fe80037c50e3436f6d657e3a4efc57)  
  
ipv6 | [getServerIpv6](class_dns_client.html#ae1b270065c2fdffbf7e2f8cec6b8c47e) () const  
| Returns the IPv6 address of the DNS server. [More...](class_dns_client.html#ae1b270065c2fdffbf7e2f8cec6b8c47e)  
  
void | [setServerIpv6](class_dns_client.html#aefbf56af88f88861c037f33bfb4c306b) (ipv6)  
| Sets the IPv6 address of the DNS server. [More...](class_dns_client.html#aefbf56af88f88861c037f33bfb4c306b)  
  
void | [setEnabled](class_dns_client.html#adb126c6112b700d352f31a9a673e2fed) (bool)  
| Enable or disable Dns Client [Process](class_process.html "Process is the base class for all device processes."). [More...](class_dns_client.html#adb126c6112b700d352f31a9a673e2fed)  
  
bool | [isEnabled](class_dns_client.html#aac02ad21070b1017655e5d624ff1aa56) ()  
| Returns true if this DNS client process is enabled, otherwise false. [More...](class_dns_client.html#aac02ad21070b1017655e5d624ff1aa56)  
  
int | [getStrToIpCount](class_dns_client.html#adfa28577058b29af24feca366fead509) ()  
| Returns the number of DNS entries in the DNS table. [More...](class_dns_client.html#adfa28577058b29af24feca366fead509)  
  
string | [getHostAt](class_dns_client.html#ac0a089644514fe62a2ea7adc66b1b992) (int)  
| Returns the hostname at the specified index. [More...](class_dns_client.html#ac0a089644514fe62a2ea7adc66b1b992)  
  
bool | [isHostNameExisted](class_dns_client.html#a9afaf767f90efab8d974a3671b14435e) (string)  
| Returns true if the hostname exists in the DNS table, otherwise false. [More...](class_dns_client.html#a9afaf767f90efab8d974a3671b14435e)  
  
bool | [isIpExisted](class_dns_client.html#a041d3f24cf8b5ea17458f9e601350367) (string, ip)  
| Returns true if the hostname and IP address DNS entry exists, otherwise false. [More...](class_dns_client.html#a041d3f24cf8b5ea17458f9e601350367)  
  
vector< ip > | [getIpOfHost](class_dns_client.html#a63d6447f16af4da9b768bd86427b5ca7) (string)  
| Returns a list of IP addresses associated with the specified hostname. [More...](class_dns_client.html#a63d6447f16af4da9b768bd86427b5ca7)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[DnsClient](class_dns_client.html "DnsClient is the process that handles retrieving DNS lookups.") is the process that handles retrieving DNS lookups. 

## Member Function Documentation

## ◆ addIpAddress()

bool DnsClient::addIpAddress  | ( | string  | ,   
---|---|---|---  
|  | ip  |   
| ) | |   
  
Adds a DNS entry with the specified hostname and IP address to the DNS table. 

Parameters
     hostname,the| hostname of the node.   
---|---  
ipAddress,the| IP address of the node.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ getHostAt()

string DnsClient::getHostAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the hostname at the specified index. 

Parameters
     index,the| index of the hostname of interest.  
---|---  
  
Returns
    string, the hostname at the specified index. 

## ◆ getIpOfHost()

vector< ip > DnsClient::getIpOfHost  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns a list of IP addresses associated with the specified hostname. 

Parameters
     hostname,the| hostname of interest.  
---|---  
  
Returns
    vector<ip>, the list of IP addresses associated with the specified hostname. 

## ◆ getServerIp()

ip DnsClient::getServerIp  | ( | | ) |   
---|---|---|---|---  
  
Returns the IP address of the DNS server. 

Returns
    ip, the DNS server ip address. 

## ◆ getServerIpv6()

ipv6 DnsClient::getServerIpv6  | ( | | ) |  const  
---|---|---|---|---  
  
Returns the IPv6 address of the DNS server. 

Returns
    ipv6, the DNS server ipv6 address. 

## ◆ getStrToIpCount()

int DnsClient::getStrToIpCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of DNS entries in the DNS table. 

Returns
    int, the number of DNS entries in the DNS table. 

## ◆ isEnabled()

bool DnsClient::isEnabled  | ( | | ) |   
---|---|---|---|---  
  
Returns true if this DNS client process is enabled, otherwise false. 

Returns
    bool, true if this DNS client process is enabled, otherwise false. 

## ◆ isHostNameExisted()

bool DnsClient::isHostNameExisted  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns true if the hostname exists in the DNS table, otherwise false. 

Parameters
     hostname,the| hostname of interest.  
---|---  
  
Returns
    bool, true if the hostname exists in the DNS table, otherwise false. 

## ◆ isIpExisted()

bool DnsClient::isIpExisted  | ( | string  | ,   
---|---|---|---  
|  | ip  |   
| ) | |   
  
Returns true if the hostname and IP address DNS entry exists, otherwise false. 

Parameters
     hostname,the| hostname to lookup.   
---|---  
ipAddress,the| IP address to lookup.  
  
Returns
    bool, true if the hostname and IP address entry exists, otherwise false. 

## ◆ isValidName()

bool DnsClient::isValidName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns true if the hostname is a valid name (non-special characters), otherwise false.

Parameters
     hostname,the| hostname of interest.  
---|---  
  
Returns
    bool, true if the hostname is a valid name (non-special characters), otherwise false. 

## ◆ removeIp()

void DnsClient::removeIp  | ( | string  | ,   
---|---|---|---  
|  | ip  |   
| ) | |   
  
Removes the DNS entry from the table based on the hostname and the IP address. 

Parameters
     hostname,the| hostname of the node.   
---|---  
ipAddress,the| IP address of the node.   
  
## ◆ removeIpAddress()

void DnsClient::removeIpAddress  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes the DNS entry from the table based on the hostname. 

Parameters
     hostname,the| hostname associated with the IP address to remove.   
---|---  
  
## ◆ setEnabled()

void DnsClient::setEnabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enable or disable Dns Client [Process](class_process.html "Process is the base class for all device processes."). 

Parameters
     bEnable,true| to enable, otherwise false.   
---|---  
  
## ◆ setServerIp()

void DnsClient::setServerIp  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Sets the IP address of the DNS server. 

Parameters
     ipAddress,the| DNS server IP address.   
---|---  
  
## ◆ setServerIpv6()

void DnsClient::setServerIpv6  | ( | ipv6  | | ) |   
---|---|---|---|---|---  
  
Sets the IPv6 address of the DNS server. 

Parameters
     ipAddress,the| DNS server IPv6 address.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CDnsClient.pki](_c_dns_client_8pki.html)


