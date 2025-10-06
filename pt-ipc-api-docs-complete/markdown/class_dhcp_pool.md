# Cisco Packet Tracer Extensions API: DhcpPool Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_dhcp_pool.html

---

[DhcpPool](class_dhcp_pool.html "DhcpPool holds and manipulates the DHCP pool on the DHCP server.") holds and manipulates the DHCP pool on the DHCP server. [More...](class_dhcp_pool.html#details)

##  Public Member Functions  
  
---  
string | [getDhcpPoolName](class_dhcp_pool.html#a93e22f0ea10ab4cf4492326c20c61922) ()  
| Returns the name of this pool. [More...](class_dhcp_pool.html#a93e22f0ea10ab4cf4492326c20c61922)  
  
ip | [getNetworkAddress](class_dhcp_pool.html#a017c029f578acd42ec39d21737a8226a) ()  
| Returns the network address of this pool. [More...](class_dhcp_pool.html#a017c029f578acd42ec39d21737a8226a)  
  
void | [setNetworkMask](class_dhcp_pool.html#a3b4599fab1a9a12f54a49d9e084097b5) (ip, ip)  
| Sets the network address for this pool. [More...](class_dhcp_pool.html#a3b4599fab1a9a12f54a49d9e084097b5)  
  
ip | [getSubnetMask](class_dhcp_pool.html#a3d401a7d5bdfb0540cedd3bd27ec43b6) ()  
| Returns the subnet mask of this pool. [More...](class_dhcp_pool.html#a3d401a7d5bdfb0540cedd3bd27ec43b6)  
  
void | [setDefaultRouter](class_dhcp_pool.html#ad10e4e04f1975f2f841ce073adf870b4) (ip)  
| Sets the default router address. [More...](class_dhcp_pool.html#ad10e4e04f1975f2f841ce073adf870b4)  
  
ip | [getDefaultRouter](class_dhcp_pool.html#ac259aa6717f88982930f2788f30bc780) ()  
| Returns the default router IP address. [More...](class_dhcp_pool.html#ac259aa6717f88982930f2788f30bc780)  
  
[DhcpPoolLease](struct_dhcp_pool_lease.html) | [getLeaseAt](class_dhcp_pool.html#a357e6707f5d5fa8e636120c34fb6f58a) (int)  
| Returns the DHCP lease at the specified index. [More...](class_dhcp_pool.html#a357e6707f5d5fa8e636120c34fb6f58a)  
  
void | [setStartIp](class_dhcp_pool.html#a1e2d2caeea79affc45da3bf7fc1e7cfc) (ip)  
| Sets the start IP address for this pool. [More...](class_dhcp_pool.html#a1e2d2caeea79affc45da3bf7fc1e7cfc)  
  
void | [setNextAvailableIpAddress](class_dhcp_pool.html#a02cda9e36ed87f7a3b5b623767aa2a1a) (ip)  
void | [setEndIp](class_dhcp_pool.html#a1869e39780d46faaad2b953e749d83d3) (ip)  
| Sets the end IP address for this pool. [More...](class_dhcp_pool.html#a1869e39780d46faaad2b953e749d83d3)  
  
void | [setNetworkAddress](class_dhcp_pool.html#a531c4ca2169096fd97a663a06f690b43) (ip)  
ip | [getStartIp](class_dhcp_pool.html#ab8507672c5c4d790b3281a605d5beb22) ()  
| Returns the start IP address of this pool. [More...](class_dhcp_pool.html#ab8507672c5c4d790b3281a605d5beb22)  
  
ip | [getEndIp](class_dhcp_pool.html#a7b2d72894c46fffa82606f3dfea0c7f3) ()  
| Returns the end IP address of this pool. [More...](class_dhcp_pool.html#a7b2d72894c46fffa82606f3dfea0c7f3)  
  
void | [setDnsServerIp](class_dhcp_pool.html#a1b57c9874f408054e10334e86a14868c) (ip)  
| Sets the DNS server IP address. [More...](class_dhcp_pool.html#a1b57c9874f408054e10334e86a14868c)  
  
ip | [getDnsServerIp](class_dhcp_pool.html#a1426c194f26687d288b1b14e19f7d4a8) ()  
| Returns the DNS server IP address. [More...](class_dhcp_pool.html#a1426c194f26687d288b1b14e19f7d4a8)  
  
string | [getDomainName](class_dhcp_pool.html#a3831b609e44d9d43c5fa9cb3b48db6b1) ()  
| Returns the domain name. [More...](class_dhcp_pool.html#a3831b609e44d9d43c5fa9cb3b48db6b1)  
  
int | [getMaxUsers](class_dhcp_pool.html#afc0edd8d23dfdd7c2edfca5c97806c5d) ()  
| Returns the maximum number of users. [More...](class_dhcp_pool.html#afc0edd8d23dfdd7c2edfca5c97806c5d)  
  
void | [setMaxUsers](class_dhcp_pool.html#a68887b7768e6e9a5749e373a4f86f220) (int)  
| Set max users. [More...](class_dhcp_pool.html#a68887b7768e6e9a5749e373a4f86f220)  
  
ip | [getTftpAddress](class_dhcp_pool.html#ab611fa6e83240f10b55c89189d9e38b0) ()  
| Returns the IP address of the TFTP server. [More...](class_dhcp_pool.html#ab611fa6e83240f10b55c89189d9e38b0)  
  
ip | [getWlcAddress](class_dhcp_pool.html#ac45650b0e6184205f30ee3f820dfc701) ()  
  
## Detailed Description

[DhcpPool](class_dhcp_pool.html "DhcpPool holds and manipulates the DHCP pool on the DHCP server.") holds and manipulates the DHCP pool on the DHCP server. 

## Member Function Documentation

## ◆ getDefaultRouter()

ip DhcpPool::getDefaultRouter  | ( | | ) |   
---|---|---|---|---  
  
Returns the default router IP address. 

Returns
    ip, the default router IP address. 

## ◆ getDhcpPoolName()

string DhcpPool::getDhcpPoolName  | ( | | ) |   
---|---|---|---|---  
  
Returns the name of this pool. 

Returns
    string, the name of this pool. 

## ◆ getDnsServerIp()

ip DhcpPool::getDnsServerIp  | ( | | ) |   
---|---|---|---|---  
  
Returns the DNS server IP address. 

Returns
    ip, the DNS server IP address. 

## ◆ getDomainName()

string DhcpPool::getDomainName  | ( | | ) |   
---|---|---|---|---  
  
Returns the domain name. 

Returns
    string, the domain name. 

## ◆ getEndIp()

ip DhcpPool::getEndIp  | ( | | ) |   
---|---|---|---|---  
  
Returns the end IP address of this pool. 

Returns
    ip, the end IP address of this pool. 

## ◆ getLeaseAt()

[DhcpPoolLease](struct_dhcp_pool_lease.html) DhcpPool::getLeaseAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the DHCP lease at the specified index. 

Parameters
     index,the| index of the DHCP lease of interest.  
---|---  
  
Returns
    [DhcpPoolLease](struct_dhcp_pool_lease.html "DHCP pool lease structure."), the [DhcpPoolLease](struct_dhcp_pool_lease.html "DHCP pool lease structure.") object at the specified index. 

## ◆ getMaxUsers()

int DhcpPool::getMaxUsers  | ( | | ) |   
---|---|---|---|---  
  
Returns the maximum number of users. 

Returns
    int, the maximum number of users. 

## ◆ getNetworkAddress()

ip DhcpPool::getNetworkAddress  | ( | | ) |   
---|---|---|---|---  
  
Returns the network address of this pool. 

Returns
    ip, the network address of this pool. 

## ◆ getStartIp()

ip DhcpPool::getStartIp  | ( | | ) |   
---|---|---|---|---  
  
Returns the start IP address of this pool. 

Returns
    ip, the start IP address of this pool. 

## ◆ getSubnetMask()

ip DhcpPool::getSubnetMask  | ( | | ) |   
---|---|---|---|---  
  
Returns the subnet mask of this pool. 

Returns
    ip, the subnet mask of this pool. 

## ◆ getTftpAddress()

ip DhcpPool::getTftpAddress  | ( | | ) |   
---|---|---|---|---  
  
Returns the IP address of the TFTP server. 

Returns
    ip, the IP address of the TFTP server. 

## ◆ getWlcAddress()

ip DhcpPool::getWlcAddress  | ( | | ) |   
---|---|---|---|---  
  
## ◆ setDefaultRouter()

void DhcpPool::setDefaultRouter  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Sets the default router address. 

Parameters
     ipAddress,the| IP address of the default router.   
---|---  
  
## ◆ setDnsServerIp()

void DhcpPool::setDnsServerIp  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Sets the DNS server IP address. 

Parameters
     ipAddress,the| DNS server IP address.   
---|---  
  
## ◆ setEndIp()

void DhcpPool::setEndIp  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Sets the end IP address for this pool. 

Parameters
     ipAddress,the| end IP address for this pool.   
---|---  
  
## ◆ setMaxUsers()

void DhcpPool::setMaxUsers  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Set max users. 

Parameters
     max,the| maximum number of users.   
---|---  
  
## ◆ setNetworkAddress()

void DhcpPool::setNetworkAddress  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
## ◆ setNetworkMask()

void DhcpPool::setNetworkMask  | ( | ip  | ,   
---|---|---|---  
|  | ip  |   
| ) | |   
  
Sets the network address for this pool. 

Parameters
     network,the| network address for this pool.   
---|---  
mask,the| subnet mask for this pool.   
  
## ◆ setNextAvailableIpAddress()

void DhcpPool::setNextAvailableIpAddress  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
## ◆ setStartIp()

void DhcpPool::setStartIp  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Sets the start IP address for this pool. 

Parameters
     ipAddress,the| start IP address for this pool.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CDhcpPool.pki](_c_dhcp_pool_8pki.html)


