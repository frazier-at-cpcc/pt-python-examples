# Cisco Packet Tracer Extensions API: DnsServerProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_dns_server_process.html

---

[DnsServerProcess](class_dns_server_process.html "DnsServerProcess is the process that stores DNS records and resolves domain names and hostnames into ...") is the process that stores DNS records and resolves domain names and hostnames into IP addresses. [More...](class_dns_server_process.html#details)

##  Public Member Functions  
  
---  
bool | [addIpAddress](class_dns_server_process.html#a05cd8dbb2ee61c6988b7f983c0ede320) (string, ip)  
| Adds a DNS record with the specified hostname and IP address. [More...](class_dns_server_process.html#a05cd8dbb2ee61c6988b7f983c0ede320)  
  
void | [removeIpAddress](class_dns_server_process.html#a5fd922e46cf1dc099eeb692688ffa83f) (string)  
| Removes the DNS record with the associated hostname. [More...](class_dns_server_process.html#a5fd922e46cf1dc099eeb692688ffa83f)  
  
pair< string, ip > | [getEntryAt](class_dns_server_process.html#acc4cd718296529de272093ba68d8e990) (int)  
int | [getEntryCount](class_dns_server_process.html#a8c7b53dca7a4effbc6ec09ba7585957e) ()  
| Returns the number of DNS records. [More...](class_dns_server_process.html#a8c7b53dca7a4effbc6ec09ba7585957e)  
  
bool | [isValidName](class_dns_server_process.html#a22334987af9212c8baafc56d0900a423) (string)  
| Returns true if the specified hostname is a valid name (non-special characters), otherwise false. [More...](class_dns_server_process.html#a22334987af9212c8baafc56d0900a423)  
  
void | [setEnable](class_dns_server_process.html#ae02e08e4063e4ccb88ace23b268e3330) (bool)  
| Enables or disables the DNS server process. [More...](class_dns_server_process.html#ae02e08e4063e4ccb88ace23b268e3330)  
  
bool | [isEnabled](class_dns_server_process.html#a1b69019c0f0a6f6974047c4194a24d4e) ()  
| Returns true if the DNS server process is enabled, otherwise false. [More...](class_dns_server_process.html#a1b69019c0f0a6f6974047c4194a24d4e)  
  
void | [setPortNumber](class_dns_server_process.html#a91f037c2ac274fe584e7fc3aa1a38482) (int)  
| Sets the port number of the DNS service. [More...](class_dns_server_process.html#a91f037c2ac274fe584e7fc3aa1a38482)  
  
int | [getPortNumber](class_dns_server_process.html#ac0a3b5ea7a91bf6a50aebaf36e57afab) ()  
| Returns the port number of the DNS service. [More...](class_dns_server_process.html#ac0a3b5ea7a91bf6a50aebaf36e57afab)  
  
bool | [isDomainNameExisted](class_dns_server_process.html#a6ccf5a2ac18b7be55a89ad3103965bcf) (string)  
| Returns true if the specified domain name exists, otherwise false. [More...](class_dns_server_process.html#a6ccf5a2ac18b7be55a89ad3103965bcf)  
  
ip | [getIpAddOfDomain](class_dns_server_process.html#a3bd9942f3c63b9dd4b63145ed3906f79) (string)  
| Returns the IP address of the specified domain name. [More...](class_dns_server_process.html#a3bd9942f3c63b9dd4b63145ed3906f79)  
  
[DnsRrA](struct_dns_rr_a.html) | [getARecordWithAddress](class_dns_server_process.html#a3fbdd2292860192123562d7e2194bade) (string, ip)  
| Returns the A resource record with the specified parameters. [More...](class_dns_server_process.html#a3fbdd2292860192123562d7e2194bade)  
  
[DnsRrCname](struct_dns_rr_cname.html) | [getCNameRecordWithHostname](class_dns_server_process.html#add131ae32645af85919d9c4cd5880ba9) (string, string)  
| Returns the CNAME resource record with the specified parameters. [More...](class_dns_server_process.html#add131ae32645af85919d9c4cd5880ba9)  
  
[DnsRrSoa](struct_dns_rr_soa.html) | [getSOARecordWithMailbox](class_dns_server_process.html#ac33dbe35589d43e7244992b5a0cc0cf1) (string, string)  
| Returns the SOA resource record with the specified parameters. [More...](class_dns_server_process.html#ac33dbe35589d43e7244992b5a0cc0cf1)  
  
[DnsRrNs](struct_dns_rr_ns.html) | [getNSRecordWithServerName](class_dns_server_process.html#afb4750483fd0c5abc1ba008f7cf6bdac) (string, string)  
| Returns the NS resource record with the specified parameters. [More...](class_dns_server_process.html#afb4750483fd0c5abc1ba008f7cf6bdac)  
  
bool | [addARecordToNameServerDb](class_dns_server_process.html#ad345c0cf9a3d29c0380b1341e4c10001) (string, string)  
| Returns true if the A resource record was added successfully, otherwise false. [More...](class_dns_server_process.html#ad345c0cf9a3d29c0380b1341e4c10001)  
  
bool | [addCNAMEToNameServerDb](class_dns_server_process.html#a4def3a69c984444d4be46548fde69d7e) (string, string)  
| Returns true if the CNAME resource record was added successfully, otherwise false. [More...](class_dns_server_process.html#a4def3a69c984444d4be46548fde69d7e)  
  
bool | [addSOAToNameServerDb](class_dns_server_process.html#a596b45cc359b1b45d3683b0fc2271f7d) (string, string, string, string, string, string, string)  
| Returns true if the SOA resource record was added successfully, otherwise false. [More...](class_dns_server_process.html#a596b45cc359b1b45d3683b0fc2271f7d)  
  
bool | [addNSRecordToNameServerDb](class_dns_server_process.html#a4c6c10069130b6422785a9f39d2bedd9) (string, string)  
| Returns true if the NS resource record was added successfully, otherwise false. [More...](class_dns_server_process.html#a4c6c10069130b6422785a9f39d2bedd9)  
  
bool | [removeARecordFromNameServerDb](class_dns_server_process.html#a1f6d74bb60383a950d81bbc956afab31) (string, string)  
| Returns true if the specified A resource record was removed successfully, otherwise false. [More...](class_dns_server_process.html#a1f6d74bb60383a950d81bbc956afab31)  
  
bool | [removeCNAMEFromNameServerDb](class_dns_server_process.html#a926d54a02ad3c0ada90ddd9e4711e3ee) (string, string)  
| Returns true if the specified CNAME resource record was removed successfully, otherwise false. [More...](class_dns_server_process.html#a926d54a02ad3c0ada90ddd9e4711e3ee)  
  
bool | [removeSOAFromNameServerDb](class_dns_server_process.html#a8613cb3b52a1902d29595ff78885a7c1) (string, string)  
| Returns true if the specified SOA resource record was removed successfully, otherwise false. [More...](class_dns_server_process.html#a8613cb3b52a1902d29595ff78885a7c1)  
  
bool | [removeNSRecordFromNameServerDb](class_dns_server_process.html#a9ae04b6801151fea53d60f0f2114caba) (string, string)  
| Returns true if the specified NS resource record was removed successfully, otherwise false. [More...](class_dns_server_process.html#a9ae04b6801151fea53d60f0f2114caba)  
  
int | [getSizeOfNameServerDb](class_dns_server_process.html#a9be6e86596386f580d7c4c0b094765ec) ()  
| Returns the size of the name server database. [More...](class_dns_server_process.html#a9be6e86596386f580d7c4c0b094765ec)  
  
[DnsResourceRecord](struct_dns_resource_record.html) | [getRrFromNameServerDbAt](class_dns_server_process.html#af09a5e45d8bf81ee116b2134af58202b) (int)  
| Returns the resource record at the specified index. [More...](class_dns_server_process.html#af09a5e45d8bf81ee116b2134af58202b)  
  
vector< [DnsResourceRecord](struct_dns_resource_record.html) > | [getMatchingRRsFromCache](class_dns_server_process.html#acef13371f59b46d48c8b88da611114bc) (string)  
| Returns the resource record associated with the resource record name. [More...](class_dns_server_process.html#acef13371f59b46d48c8b88da611114bc)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[DnsServerProcess](class_dns_server_process.html "DnsServerProcess is the process that stores DNS records and resolves domain names and hostnames into ...") is the process that stores DNS records and resolves domain names and hostnames into IP addresses. 

## Member Function Documentation

## ◆ addARecordToNameServerDb()

bool DnsServerProcess::addARecordToNameServerDb  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Returns true if the A resource record was added successfully, otherwise false. 

Parameters
     domainName,the| domain name for the A resource record.   
---|---  
address,the| address for the A resource record.  
  
Returns
    bool, true if the A resource record was added successfully, otherwise false. 

## ◆ addCNAMEToNameServerDb()

bool DnsServerProcess::addCNAMEToNameServerDb  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Returns true if the CNAME resource record was added successfully, otherwise false. 

Parameters
     domainName,the| domain name for the CNAME resource record.   
---|---  
hostName,the| hostname for the CNAME resource record.  
  
Returns
    bool, true if the CNAME resource record was added successfully, otherwise false. 

## ◆ addIpAddress()

bool DnsServerProcess::addIpAddress  | ( | string  | ,   
---|---|---|---  
|  | ip  |   
| ) | |   
  
Adds a DNS record with the specified hostname and IP address. 

Parameters
     hostname,the| hostname of the DNS record.   
---|---  
ipAddress,the| IP address of the DNS record.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ addNSRecordToNameServerDb()

bool DnsServerProcess::addNSRecordToNameServerDb  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Returns true if the NS resource record was added successfully, otherwise false. 

Parameters
     domainName,the| domain name for the NS resource record.   
---|---  
serverName,the| server name for the NS resource record.  
  
Returns
    bool, true if the NS record was added successfully, otherwise false. 

## ◆ addSOAToNameServerDb()

bool DnsServerProcess::addSOAToNameServerDb  | ( | string  | ,   
---|---|---|---  
|  | string  | ,   
|  | string  | ,   
|  | string  | ,   
|  | string  | ,   
|  | string  | ,   
|  | string  |   
| ) | |   
  
Returns true if the SOA resource record was added successfully, otherwise false. 

Parameters
     domainName,the| domain name for the SOA resource record.   
---|---  
serverName,the| primary server name for the SOA resource record.   
mailbox,the| mailbox for the SOA resource record.   
minTtl,the| minimum TTL for the SOA resource record.   
refresh,the| refresh time for the SOA resource record.   
retry,the| retry time for the SOA resource record.   
expiry,the| expiry time for the SOA resource record.  
  
Returns
    bool, true if the CNAME resource record was added successfully, otherwise false. 

## ◆ getARecordWithAddress()

[DnsRrA](struct_dns_rr_a.html) DnsServerProcess::getARecordWithAddress  | ( | string  | ,   
---|---|---|---  
|  | ip  |   
| ) | |   
  
Returns the A resource record with the specified parameters. 

Parameters
     domainName,the| domain name of the A resource record of interest.   
---|---  
address,the| address of the A resource record of interest.  
  
Returns
    [DnsRrA](struct_dns_rr_a.html "IPv4 DNS A record structure."), the A resource record object with the specified parameters. 

## ◆ getCNameRecordWithHostname()

[DnsRrCname](struct_dns_rr_cname.html) DnsServerProcess::getCNameRecordWithHostname  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Returns the CNAME resource record with the specified parameters. 

Parameters
     domainName,the| domain name of the CNAME resource record of interest.   
---|---  
hostName,the| hostname of the CNAME resource record of interest.  
  
Returns
    [DnsRrCname](struct_dns_rr_cname.html "DNS CNAME record structure."), the CNAME resource record object with the specified parameters. 

## ◆ getEntryAt()

pair< string, ip > DnsServerProcess::getEntryAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
\Returns the hostname and IP address of the DNS record at the specified index.

Parameters
     index,the| DNS record index of interest.  
---|---  
  
Returns
    pair<string, ip>, the hostname and IP address of the DNS record at the specified index. 

## ◆ getEntryCount()

int DnsServerProcess::getEntryCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of DNS records. 

Returns
    int, the number of DNS records. 

## ◆ getIpAddOfDomain()

ip DnsServerProcess::getIpAddOfDomain  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the IP address of the specified domain name. 

Parameters
     domainName,the| domain name of interest.  
---|---  
  
Returns
    ip, the IP address of the specified domain name. 

## ◆ getMatchingRRsFromCache()

vector< [DnsResourceRecord](struct_dns_resource_record.html) > DnsServerProcess::getMatchingRRsFromCache  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the resource record associated with the resource record name. 

Parameters
     name,the| name of the resource record of interest.  
---|---  
  
Returns
    [DnsResourceRecord](struct_dns_resource_record.html "DNS resource record structure."), the resource record [DnsResourceRecord](struct_dns_resource_record.html "DNS resource record structure.") object associated with the resource record name. 

## ◆ getNSRecordWithServerName()

[DnsRrNs](struct_dns_rr_ns.html) DnsServerProcess::getNSRecordWithServerName  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Returns the NS resource record with the specified parameters. 

Parameters
     domainName,the| domain name of the NS resource record of interest.   
---|---  
serverName,the| server name of the NS resource record of interest.  
  
Returns
    [DnsRrNs](struct_dns_rr_ns.html "DNS NS record structure."), the NS resource record object with the specified parameters. 

## ◆ getPortNumber()

int DnsServerProcess::getPortNumber  | ( | | ) |   
---|---|---|---|---  
  
Returns the port number of the DNS service. 

Returns
    int, the port number of the DNS service. 

## ◆ getRrFromNameServerDbAt()

[DnsResourceRecord](struct_dns_resource_record.html) DnsServerProcess::getRrFromNameServerDbAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the resource record at the specified index. 

Parameters
     index,the| index of the resource record of interest.  
---|---  
  
Returns
    [DnsResourceRecord](struct_dns_resource_record.html "DNS resource record structure."), the resource record [DnsResourceRecord](struct_dns_resource_record.html "DNS resource record structure.") object at the specified index. 

## ◆ getSizeOfNameServerDb()

int DnsServerProcess::getSizeOfNameServerDb  | ( | | ) |   
---|---|---|---|---  
  
Returns the size of the name server database. 

Returns
    int, the size of the name server database. 

## ◆ getSOARecordWithMailbox()

[DnsRrSoa](struct_dns_rr_soa.html) DnsServerProcess::getSOARecordWithMailbox  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Returns the SOA resource record with the specified parameters. 

Parameters
     domainName,the| domain name of the SOA resource record of interest.   
---|---  
mailbox,the| mailbox of the SOA resource record of interest.  
  
Returns
    [DnsRrSoa](struct_dns_rr_soa.html "DNS SOA record structure."), the SOA resource record object with the specified parameters. 

## ◆ isDomainNameExisted()

bool DnsServerProcess::isDomainNameExisted  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns true if the specified domain name exists, otherwise false. 

Parameters
     domainName,the| domain name of interest.  
---|---  
  
Returns
    bool, true if the specified domain name exists, otherwise false. 

## ◆ isEnabled()

bool DnsServerProcess::isEnabled  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the DNS server process is enabled, otherwise false. 

Returns
    bool, true if the DNS server process is enabled, otherwise false. 

## ◆ isValidName()

bool DnsServerProcess::isValidName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns true if the specified hostname is a valid name (non-special characters), otherwise false. 

Parameters
     hostname,the| hostname of interest.  
---|---  
  
Returns
    bool, true if the specified hostname is a valid name (non-special characters), otherwise false. 

## ◆ removeARecordFromNameServerDb()

bool DnsServerProcess::removeARecordFromNameServerDb  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Returns true if the specified A resource record was removed successfully, otherwise false. 

Parameters
     domainName,the| domain name of the A resource record of interest.   
---|---  
address,the| address of the A resource record of interest.  
  
Returns
    bool, true if the specified A resource record was removed successfully, otherwise false. 

## ◆ removeCNAMEFromNameServerDb()

bool DnsServerProcess::removeCNAMEFromNameServerDb  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Returns true if the specified CNAME resource record was removed successfully, otherwise false. 

Parameters
     domainName,the| domain name of the CNAME resource record of interest.   
---|---  
hostName,the| hostname of the CNAME resource record of interest.  
  
Returns
    bool, true if the specified CNAME resource record was removed successfully, otherwise false. 

## ◆ removeIpAddress()

void DnsServerProcess::removeIpAddress  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes the DNS record with the associated hostname. 

Parameters
     hostname,the| hostname of the DNS record of interest.   
---|---  
  
## ◆ removeNSRecordFromNameServerDb()

bool DnsServerProcess::removeNSRecordFromNameServerDb  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Returns true if the specified NS resource record was removed successfully, otherwise false. 

Parameters
     domainName,the| domain name of the NS resource record of interest.   
---|---  
serverName,the| server name of the NS resource record of interest.  
  
Returns
    bool, true if the specified NS resource record was removed successfully, otherwise false. 

## ◆ removeSOAFromNameServerDb()

bool DnsServerProcess::removeSOAFromNameServerDb  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Returns true if the specified SOA resource record was removed successfully, otherwise false. 

Parameters
     domainName,the| domain name of the SOA resource record of interest.   
---|---  
mailbox,the| mailbox of the SOA resource record of interest.  
  
Returns
    bool, true if the specified SOA resource record was removed successfully, otherwise false. 

## ◆ setEnable()

void DnsServerProcess::setEnable  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables the DNS server process. 

Parameters
     bEnable,true| to enable the DNS server process, false to disable it.   
---|---  
  
## ◆ setPortNumber()

void DnsServerProcess::setPortNumber  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the port number of the DNS service. 

Parameters
     num,the| port number to set the DNS service to.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CDnsServerProcess.pki](_c_dns_server_process_8pki.html)


