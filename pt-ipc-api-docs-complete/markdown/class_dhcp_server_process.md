# Cisco Packet Tracer Extensions API: DhcpServerProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_dhcp_server_process.html

---

[DhcpServerProcess](class_dhcp_server_process.html "DhcpServerProcess is the process that handles DHCP pools and leases.") is the process that handles DHCP pools and leases. [More...](class_dhcp_server_process.html#details)

##  Public Member Functions  
  
---  
void | [addExcludedAddress](class_dhcp_server_process.html#a6f35cc338ac810aeb262f6312867c2d1) (ip, ip)  
| Adds a range of IP addresses to exclude. [More...](class_dhcp_server_process.html#a6f35cc338ac810aeb262f6312867c2d1)  
  
void | [removeExcludedAddress](class_dhcp_server_process.html#a045d630f93bc2dbffaefec059b7b6935) (ip, ip)  
| Removes the range of IP addresses to exclude. [More...](class_dhcp_server_process.html#a045d630f93bc2dbffaefec059b7b6935)  
  
void | [updateNetworkReservation](class_dhcp_server_process.html#a41d0e6db0dbadd7ab2311a533b5e14b4) (ip)  
int | [getExcludedAddressCount](class_dhcp_server_process.html#a217df117946ced3da64a83de9efca4a9) ()  
| Returns the number of address ranges that is excluded. [More...](class_dhcp_server_process.html#a217df117946ced3da64a83de9efca4a9)  
  
pair< ip, ip > | [getExcludedAddressAt](class_dhcp_server_process.html#aab7c50f559a2b09538957203f71e95a2) (int)  
| Returns the excluded address range at the specified index. [More...](class_dhcp_server_process.html#aab7c50f559a2b09538957203f71e95a2)  
  
void | [addPool](class_dhcp_server_process.html#ae9274bed8a68a3721675df62034fba0d) (string)  
| Adds a DHCP pool to this process. [More...](class_dhcp_server_process.html#ae9274bed8a68a3721675df62034fba0d)  
  
void | [addNewPool](class_dhcp_server_process.html#ae32ccfa20b5570690d20a06ecc42b680) (string, string, string, string, string, int, string, string)  
| Adds a new DHCP pool with the specified arguments. [More...](class_dhcp_server_process.html#ae32ccfa20b5570690d20a06ecc42b680)  
  
[DhcpPool](class_dhcp_pool.html) | [getPool](class_dhcp_server_process.html#ae2f28f1bfb6faa8d4c3ef1a0e92a77bc) (string)  
| Returns a [DhcpPool](class_dhcp_pool.html "DhcpPool holds and manipulates the DHCP pool on the DHCP server.") object with the specified pool name. [More...](class_dhcp_server_process.html#ae2f28f1bfb6faa8d4c3ef1a0e92a77bc)  
  
void | [removePool](class_dhcp_server_process.html#a42b665a6f2c20e4ac641210ecfeb2503) (string)  
| Removes the DHCP pool from this process. [More...](class_dhcp_server_process.html#a42b665a6f2c20e4ac641210ecfeb2503)  
  
int | [getPoolCount](class_dhcp_server_process.html#a6b4026955c69878a27ee8e8455d8db0a) ()  
| Returns the number of DHCP pools in this process. [More...](class_dhcp_server_process.html#a6b4026955c69878a27ee8e8455d8db0a)  
  
[DhcpPool](class_dhcp_pool.html) | [getPoolAt](class_dhcp_server_process.html#af8344544523c35f3e995e705935323a1) (int)  
| Returns the DHCP pool at the specified index. [More...](class_dhcp_server_process.html#af8344544523c35f3e995e705935323a1)  
  
bool | [isEnable](class_dhcp_server_process.html#ac5da8f361abd4ad8f3c25d85b6449ebe) ()  
| Returns true if this DHCP server process is enabled, otherwise false. [More...](class_dhcp_server_process.html#ac5da8f361abd4ad8f3c25d85b6449ebe)  
  
void | [setEnable](class_dhcp_server_process.html#a7a1fcdc45669b4300fb98d2589c02f59) (bool)  
| Enables or disables this DHCP server process. [More...](class_dhcp_server_process.html#a7a1fcdc45669b4300fb98d2589c02f59)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[DhcpServerProcess](class_dhcp_server_process.html "DhcpServerProcess is the process that handles DHCP pools and leases.") is the process that handles DHCP pools and leases. 

## Member Function Documentation

## ◆ addExcludedAddress()

void DhcpServerProcess::addExcludedAddress  | ( | ip  | ,   
---|---|---|---  
|  | ip  |   
| ) | |   
  
Adds a range of IP addresses to exclude. 

Parameters
     startIp,the| starting IP address.   
---|---  
endIp,the| ending IP address.   
  
## ◆ addNewPool()

void DhcpServerProcess::addNewPool  | ( | string  | ,   
---|---|---|---  
|  | string  | ,   
|  | string  | ,   
|  | string  | ,   
|  | string  | ,   
|  | int  | ,   
|  | string  | ,   
|  | string  |   
| ) | |   
  
Adds a new DHCP pool with the specified arguments. 

Parameters
     poolName,the| name for the DHCP pool.   
---|---  
gateway,the| IP address of the default gateway.   
dnsServer,the| IP address of the DNS server.   
startIp,the| start IP address of the DHCP pool.   
subnetMask,the| subnet mask of the DHCP pool.   
maxUsers,the| maximum number of users for the DHCP pool.   
tftpServerIp,the| IP address of the TFTP server.   
wlcIp,the| IP address of the WLC.   
  
## ◆ addPool()

void DhcpServerProcess::addPool  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Adds a DHCP pool to this process. 

Parameters
     poolName,the| name of the DHCP pool to add.   
---|---  
  
## ◆ getExcludedAddressAt()

pair< ip, ip > DhcpServerProcess::getExcludedAddressAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the excluded address range at the specified index. 

Parameters
     index,the| index of excluded address range of interest.  
---|---  
  
Returns
    pair<ip,ip>, a pair of IP addresses, the first is the start IP address, the second is the end IP address. 

## ◆ getExcludedAddressCount()

int DhcpServerProcess::getExcludedAddressCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of address ranges that is excluded. 

Returns
    int, the number of address ranges that is excluded. 

## ◆ getPool()

[DhcpPool](class_dhcp_pool.html) DhcpServerProcess::getPool  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns a [DhcpPool](class_dhcp_pool.html "DhcpPool holds and manipulates the DHCP pool on the DHCP server.") object with the specified pool name. 

Parameters
     poolName,the| name of the DHCP pool of interest.  
---|---  
  
Returns
    [DhcpPool](class_dhcp_pool.html "DhcpPool holds and manipulates the DHCP pool on the DHCP server."), the [DhcpPool](class_dhcp_pool.html "DhcpPool holds and manipulates the DHCP pool on the DHCP server.") object associated with the pool name. 

## ◆ getPoolAt()

[DhcpPool](class_dhcp_pool.html) DhcpServerProcess::getPoolAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the DHCP pool at the specified index. 

Parameters
     index,the| index of the DHCP pool of interest.  
---|---  
  
Returns
    [DhcpPool](class_dhcp_pool.html "DhcpPool holds and manipulates the DHCP pool on the DHCP server."), the [DhcpPool](class_dhcp_pool.html "DhcpPool holds and manipulates the DHCP pool on the DHCP server.") object at the specified index. 

## ◆ getPoolCount()

int DhcpServerProcess::getPoolCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of DHCP pools in this process. 

Returns
    int, the number of DHCP pools in this process. 

## ◆ isEnable()

bool DhcpServerProcess::isEnable  | ( | | ) |   
---|---|---|---|---  
  
Returns true if this DHCP server process is enabled, otherwise false. 

Returns
    bool, true if this DHCP server process is enabled, otherwise false. 

## ◆ removeExcludedAddress()

void DhcpServerProcess::removeExcludedAddress  | ( | ip  | ,   
---|---|---|---  
|  | ip  |   
| ) | |   
  
Removes the range of IP addresses to exclude. 

Parameters
     startIp,the| starting IP address.   
---|---  
endIp,the| ending IP address.   
  
## ◆ removePool()

void DhcpServerProcess::removePool  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes the DHCP pool from this process. 

Parameters
     poolName,the| name of the pool to remove.   
---|---  
  
## ◆ setEnable()

void DhcpServerProcess::setEnable  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables this DHCP server process. 

Parameters
     bEnable,true| to enable this DHCP server process, false to disable it.   
---|---  
  
## ◆ updateNetworkReservation()

void DhcpServerProcess::updateNetworkReservation  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CDhcpServerProcess.pki](_c_dhcp_server_process_8pki.html)


