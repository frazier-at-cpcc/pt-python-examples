# Cisco Packet Tracer Extensions API: OspfProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_ospf_process.html

---

[OspfProcess](class_ospf_process.html "OspfProcess is the process that handles the individual OSPF process.") is the process that handles the individual OSPF process. [More...](class_ospf_process.html#details)

##  Public Member Functions  
  
---  
int | [getProcessId](class_ospf_process.html#a830a5aec9104f855d83145053743005d) ()  
| Returns the OSPF process ID. [More...](class_ospf_process.html#a830a5aec9104f855d83145053743005d)  
  
ip | [getRouterId](class_ospf_process.html#a266fe549ee70c3bc6251797aecab2de3) ()  
| Returns the router-ID for this OSPF process. [More...](class_ospf_process.html#a266fe549ee70c3bc6251797aecab2de3)  
  
int | [getAreaCount](class_ospf_process.html#ab2479c1fb1f4de16165b154340bf167f) ()  
| Returns the number of OSPF areas. [More...](class_ospf_process.html#ab2479c1fb1f4de16165b154340bf167f)  
  
[OspfArea](class_ospf_area.html) | [getAreaAt](class_ospf_process.html#ae10cfa636b392959660457fdd9a32a25) (int)  
| Returns the OSPF area at the specified index. [More...](class_ospf_process.html#ae10cfa636b392959660457fdd9a32a25)  
  
[OspfArea](class_ospf_area.html) | [getArea](class_ospf_process.html#acddb1b84434dde6437e3c659105c79ec) (ip)  
| Returns the OSPF area with the specified ID in IP address format. [More...](class_ospf_process.html#acddb1b84434dde6437e3c659105c79ec)  
  
void | [removeArea](class_ospf_process.html#a64b482729adaf85f85a7aa051ab25898) (ip)  
| Removes the OSPF area with the specified ID in IP address format. [More...](class_ospf_process.html#a64b482729adaf85f85a7aa051ab25898)  
  
bool | [setAreaAuthentication](class_ospf_process.html#a6d5e0796d6e3fd8822c61c19969f7ef8) (ip, OspfAuthType)  
int | [getAreaAuthenticationCount](class_ospf_process.html#a395669fd5429bb82b32283f006bce854) ()  
| Returns the number of authenticated areas. [More...](class_ospf_process.html#a395669fd5429bb82b32283f006bce854)  
  
pair< ip, int > | [getAreaAuthenticationAt](class_ospf_process.html#ab0c4092ae8e621a1681ff8c619af8d03) (int)  
| Returns the ID in IP address format and authentication type of the authenticated area at the specifed index. [More...](class_ospf_process.html#ab0c4092ae8e621a1681ff8c619af8d03)  
  
OspfAuthType | [getAreaAuthentication](class_ospf_process.html#ac73e89d626a4533c6b38cf988e500469) (ip)  
| Returns the authentication type of the area with the specified ID in IP address format. [More...](class_ospf_process.html#ac73e89d626a4533c6b38cf988e500469)  
  
void | [setDefaultInfoOrig](class_ospf_process.html#a69d8a697e7a16d86e14c5b266923d36f) (OspfDefaultInfoOrig)  
| Sets the default information originate setting. [More...](class_ospf_process.html#a69d8a697e7a16d86e14c5b266923d36f)  
  
OspfDefaultInfoOrig | [getDefaultInfoOrig](class_ospf_process.html#a360dcf3536b0932733c8f6e3cb2ae25b) ()  
| Returns the default information originate setting. [More...](class_ospf_process.html#a360dcf3536b0932733c8f6e3cb2ae25b)  
  
void | [setLogAdjacencyChanges](class_ospf_process.html#a0c628691e58fb3ddd027b5ee3041939d) (OspfLogChanges)  
| Sets the log adjacadeny changes setting. [More...](class_ospf_process.html#a0c628691e58fb3ddd027b5ee3041939d)  
  
OspfLogChanges | [getLogAdjacencyChanges](class_ospf_process.html#a283134fbd3c0f7203027841b086651ca) ()  
| Returns the log adjacadeny changes setting. [More...](class_ospf_process.html#a283134fbd3c0f7203027841b086651ca)  
  
void | [addConfiguredNetwork](class_ospf_process.html#ab5488b8dee0f2f0cc227561042e60cea) (ip, ip, ip)  
| Enables OSPF routing in the specified OSPF area for the specified network. [More...](class_ospf_process.html#ab5488b8dee0f2f0cc227561042e60cea)  
  
void | [removeConfigureNetwork](class_ospf_process.html#a35fb542f083857ffa78142a60092d2df) (ip, ip, ip)  
| Disables OSPF routing in the specified OSPF area for the specified network. [More...](class_ospf_process.html#a35fb542f083857ffa78142a60092d2df)  
  
int | [getConfNetworkCount](class_ospf_process.html#a475d55c0dfca00e12f372edd6ab7d0f0) ()  
| Returns the number of configured networks. [More...](class_ospf_process.html#a475d55c0dfca00e12f372edd6ab7d0f0)  
  
[OspfAreaNetwork](struct_ospf_area_network.html) | [getConfNetworkAt](class_ospf_process.html#ad78f1c2c0fdb39d07ab617fb969c8429) (int)  
| Returns the configured network at the specified index. [More...](class_ospf_process.html#ad78f1c2c0fdb39d07ab617fb969c8429)  
  
ip | [getAreaId](class_ospf_process.html#a52c4ad7ca2ec6909f12dc05dd4e4ea31) (ip, ip)  
| Returns the area ID in IP address format of the specified network. [More...](class_ospf_process.html#a52c4ad7ca2ec6909f12dc05dd4e4ea31)  
  
void | [setDefaultPassiveInt](class_ospf_process.html#aa6f9440e51e96e9944950e36f308fe66) (bool)  
| Enables or disables default passive interface. [More...](class_ospf_process.html#aa6f9440e51e96e9944950e36f308fe66)  
  
bool | [getDefaultPassiveInt](class_ospf_process.html#aa759df5bdcf9e979f0caa819c9e2ce3c) ()  
| Returns true if default passive interface is enabled, otherwise false. [More...](class_ospf_process.html#aa759df5bdcf9e979f0caa819c9e2ce3c)  
  
void | [setPassiveInt](class_ospf_process.html#a6dfcd2748e4d045664027128be8d0ded) (string, bool)  
| Enables or disables passive interface for the specified port. [More...](class_ospf_process.html#a6dfcd2748e4d045664027128be8d0ded)  
  
void | [generateOspfRoutes](class_ospf_process.html#af66f3b3a849a09792c0ca2462e529760) (ip)  
| Generates the OSPF routes for the OSPF area with the specified ID in IP address format. [More...](class_ospf_process.html#af66f3b3a849a09792c0ca2462e529760)  
  
Public Member Functions inherited from [RoutingProtocol](class_routing_protocol.html)  
void | [setAdminDistance](class_routing_protocol.html#a1f39516098814724cf82c520c510de71) (int)  
| Sets the administrative distance. [More...](class_routing_protocol.html#a1f39516098814724cf82c520c510de71)  
  
int | [getAdminDistance](class_routing_protocol.html#a297c8e3af679475657e71c9363970289) ()  
| Returns the administrative distance. [More...](class_routing_protocol.html#a297c8e3af679475657e71c9363970289)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[OspfProcess](class_ospf_process.html "OspfProcess is the process that handles the individual OSPF process.") is the process that handles the individual OSPF process. 

## Member Function Documentation

## ◆ addConfiguredNetwork()

void OspfProcess::addConfiguredNetwork  | ( | ip  | ,   
---|---|---|---  
|  | ip  | ,   
|  | ip  |   
| ) | |   
  
Enables OSPF routing in the specified OSPF area for the specified network. 

Parameters
     ipAddressArea,the| ID in IP address format of the OSPF area.   
---|---  
ipAddress,the| network address.   
mask,the| OSPF wild card bits.   
  
## ◆ generateOspfRoutes()

void OspfProcess::generateOspfRoutes  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Generates the OSPF routes for the OSPF area with the specified ID in IP address format. 

Parameters
     ipAddressAreaID,the| ID in IP address format of the OSPF area of interest.   
---|---  
  
## ◆ getArea()

[OspfArea](class_ospf_area.html) OspfProcess::getArea  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Returns the OSPF area with the specified ID in IP address format. 

Parameters
     ipAddressArea,the| ID in IP address format of the OSPF area of interest.  
---|---  
  
Returns
    [OspfArea](class_ospf_area.html "OspfArea handles and manipulates OSPF areas."), the [OspfArea](class_ospf_area.html "OspfArea handles and manipulates OSPF areas.") object with the specified IP address. 

## ◆ getAreaAt()

[OspfArea](class_ospf_area.html) OspfProcess::getAreaAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the OSPF area at the specified index. 

Parameters
     index,the| index of the OSPF area of interest.  
---|---  
  
Returns
    [OspfArea](class_ospf_area.html "OspfArea handles and manipulates OSPF areas."), the [OspfArea](class_ospf_area.html "OspfArea handles and manipulates OSPF areas.") object at the specified index. 

## ◆ getAreaAuthentication()

OspfAuthType OspfProcess::getAreaAuthentication  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Returns the authentication type of the area with the specified ID in IP address format. 

Parameters
     ipAddressArea,the| ID in IP address format of the area of interest.  
---|---  
  
Returns
    enum<OspfAuthType>, the authentication type. Authentication types: eNoAuth = 0, eAuth = 1, eMD5Auth = 2 

## ◆ getAreaAuthenticationAt()

pair< ip, int > OspfProcess::getAreaAuthenticationAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the ID in IP address format and authentication type of the authenticated area at the specifed index. 

Parameters
     index,the| index of the authenticated area of interest.  
---|---  
  
Returns
    pair<ip, int>, the ID in IP address format and authentication type of the authenticated area at the specifed index. 

## ◆ getAreaAuthenticationCount()

int OspfProcess::getAreaAuthenticationCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of authenticated areas. 

Returns
    int, the number of authenticated areas. 

## ◆ getAreaCount()

int OspfProcess::getAreaCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of OSPF areas. 

Returns
    int, the number of OSPF areas. 

## ◆ getAreaId()

ip OspfProcess::getAreaId  | ( | ip  | ,   
---|---|---|---  
|  | ip  |   
| ) | |   
  
Returns the area ID in IP address format of the specified network. 

Parameters
     ipAddress,the| network address.   
---|---  
mask,the| OSPF wild card bits.  
  
Returns
    ip, the ID in IP address format of the specified network. 

## ◆ getConfNetworkAt()

[OspfAreaNetwork](struct_ospf_area_network.html) OspfProcess::getConfNetworkAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the configured network at the specified index. 

Parameters
     index,the| index of the network of interest.  
---|---  
  
Returns
    [OspfAreaNetwork](struct_ospf_area_network.html "Data element for OspfAreaNetwork."), the [OspfAreaNetwork](struct_ospf_area_network.html "Data element for OspfAreaNetwork.") object. 

## ◆ getConfNetworkCount()

int OspfProcess::getConfNetworkCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of configured networks. 

Returns
    int, the number of configured networks. 

## ◆ getDefaultInfoOrig()

OspfDefaultInfoOrig OspfProcess::getDefaultInfoOrig  | ( | | ) |   
---|---|---|---|---  
  
Returns the default information originate setting. 

Returns
    enum<OspfDefaultInfoOrig>, the default information originate setting. Default information originate settings: eNoDefaultInfoOrig = 0, eDefaultInfoOrig = 1, eDefaultInfoOrigAlways = 2 

## ◆ getDefaultPassiveInt()

bool OspfProcess::getDefaultPassiveInt  | ( | | ) |   
---|---|---|---|---  
  
Returns true if default passive interface is enabled, otherwise false. 

Returns
    bool, true if default passive interface is enabled, otherwise false. 

## ◆ getLogAdjacencyChanges()

OspfLogChanges OspfProcess::getLogAdjacencyChanges  | ( | | ) |   
---|---|---|---|---  
  
Returns the log adjacadeny changes setting. 

Returns
    enum<OspfLogChanges>, the log adjacadeny changes setting. Log adjacadeny changes settings: eNoLogChange = 0, eLogChange = 1, eLogChangeDetail = 2 

## ◆ getProcessId()

int OspfProcess::getProcessId  | ( | | ) |   
---|---|---|---|---  
  
Returns the OSPF process ID. 

Returns
    int, the OSPF process ID. 

## ◆ getRouterId()

ip OspfProcess::getRouterId  | ( | | ) |   
---|---|---|---|---  
  
Returns the router-ID for this OSPF process. 

Returns
    ip, the router-ID for this OSPF process. 

## ◆ removeArea()

void OspfProcess::removeArea  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Removes the OSPF area with the specified ID in IP address format. 

Parameters
     ipAddressArea,the| ID in IP address format of the OSPF area of interest.   
---|---  
  
## ◆ removeConfigureNetwork()

void OspfProcess::removeConfigureNetwork  | ( | ip  | ,   
---|---|---|---  
|  | ip  | ,   
|  | ip  |   
| ) | |   
  
Disables OSPF routing in the specified OSPF area for the specified network. 

Parameters
     ipAddressArea,the| ID in IP address format of the OSPF area.   
---|---  
ipAddress,the| network address.   
mask,the| OSPF wild card bits.   
  
## ◆ setAreaAuthentication()

bool OspfProcess::setAreaAuthentication  | ( | ip  | ,   
---|---|---|---  
|  | OspfAuthType  |   
| ) | |   
  
\Sets the authentication type for the OSPF area with the specified ID in IP address format.

Parameters
     ipAddressArea,the| ID in IP address format of the OSPF area of interest.   
---|---  
type,the| authentication type. Authentication types: eNoAuth = 0, eAuth = 1, eMD5Auth = 2  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ setDefaultInfoOrig()

void OspfProcess::setDefaultInfoOrig  | ( | OspfDefaultInfoOrig  | | ) |   
---|---|---|---|---|---  
  
Sets the default information originate setting. 

Parameters
     type,the| default information originate setting. Default information originate settings: eNoDefaultInfoOrig = 0, eDefaultInfoOrig = 1, eDefaultInfoOrigAlways = 2   
---|---  
  
## ◆ setDefaultPassiveInt()

void OspfProcess::setDefaultPassiveInt  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables default passive interface. 

Parameters
     b,true| to enable default passive interface, false to disable it.   
---|---  
  
## ◆ setLogAdjacencyChanges()

void OspfProcess::setLogAdjacencyChanges  | ( | OspfLogChanges  | | ) |   
---|---|---|---|---|---  
  
Sets the log adjacadeny changes setting. 

Parameters
     type,the| log adjacadeny changes setting. Log adjacadeny changes settings: eNoLogChange = 0, eLogChange = 1, eLogChangeDetail = 2   
---|---  
  
## ◆ setPassiveInt()

void OspfProcess::setPassiveInt  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Enables or disables passive interface for the specified port. 

Parameters
     portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0   
---|---  
bPassive,true| to enable passive interface, false to disable it.   
  
* * *

The documentation for this class was generated from the following file:

  * [COspfProcess.pki](_c_ospf_process_8pki.html)


