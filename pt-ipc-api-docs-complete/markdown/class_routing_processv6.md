# Cisco Packet Tracer Extensions API: RoutingProcessv6 Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_routing_processv6.html

---

##  Public Member Functions  
  
---  
void | [routeAdded](class_routing_processv6.html#a1b5b6e6bcd05d456d0154877c11f22b0) (ipv6, ipv6, int, int, ipv6, string, string)  
| This event is emitted when a route is added. [More...](class_routing_processv6.html#a1b5b6e6bcd05d456d0154877c11f22b0)  
  
void | [routeRemoved](class_routing_processv6.html#a1b8a013b49f01efb7f4a442ade5b6a01) (ipv6, ipv6, int, int, ipv6, string, string)  
| This event is emitted when a route is removed. [More...](class_routing_processv6.html#a1b8a013b49f01efb7f4a442ade5b6a01)  
  
void | [networkAdded](class_routing_processv6.html#a803e59f3d4363cfe8b57199b377c7c27) (ipv6, ipv6)  
| This event is emitted when a network is added. [More...](class_routing_processv6.html#a803e59f3d4363cfe8b57199b377c7c27)  
  
void | [networkRemoved](class_routing_processv6.html#a386a5c474df05c3d03dbdf9c5ec8c61b) (ipv6, ipv6)  
| This event is emitted when a network is removed. [More...](class_routing_processv6.html#a386a5c474df05c3d03dbdf9c5ec8c61b)  
  
Public Member Functions inherited from [RoutingProcess](class_routing_process.html)  
void | [clearAllRoutes](class_routing_process.html#a30e406229488fc94eb2e3851bf2678a4) ()  
| Clears all routes. [More...](class_routing_process.html#a30e406229488fc94eb2e3851bf2678a4)  
  
void | [clearRoute](class_routing_process.html#a83235b67695fa7463fdc6cf486555d5b) (ip, ip)  
| Clears the specified route. [More...](class_routing_process.html#a83235b67695fa7463fdc6cf486555d5b)  
  
bool | [addStaticRoute](class_routing_process.html#aa473b97b85170004e39b6f187ae60e8e) (ip, ip, ip, string, int)  
| Adds a static route. [More...](class_routing_process.html#aa473b97b85170004e39b6f187ae60e8e)  
  
bool | [removeStaticRoute](class_routing_process.html#ae17559163355d09738e5ab853112fdda) (ip, ip, ip, string, int)  
| Removes the specified static route. [More...](class_routing_process.html#ae17559163355d09738e5ab853112fdda)  
  
int | [getStaticRouteCount](class_routing_process.html#a7ee0a048fa13d0be23c6168ee8c96455) ()  
| Returns the number of static routes. [More...](class_routing_process.html#a7ee0a048fa13d0be23c6168ee8c96455)  
  
[StaticRoute](struct_static_route.html) | [getStaticRouteAt](class_routing_process.html#aab20c26d421e7a4e4967182a4ad1ed71) (int)  
| Returns the static route at the specified index. [More...](class_routing_process.html#aab20c26d421e7a4e4967182a4ad1ed71)  
  
[RoutingTable](struct_routing_table.html) | [getRoutingTable](class_routing_process.html#a3097d4a69b40d305173ea4751b397b20) ()  
| Returns the routing table. [More...](class_routing_process.html#a3097d4a69b40d305173ea4751b397b20)  
  
void | [routeAdded](class_routing_process.html#aae94f04ef3a109cb2eb63ec16fcf2c20) (ip, ip, int, int, ip, string, string)  
| This event is emitted when a route is added. [More...](class_routing_process.html#aae94f04ef3a109cb2eb63ec16fcf2c20)  
  
void | [routeRemoved](class_routing_process.html#a9c7c8bc058c923f60338a8d26e3d3f4e) (ip, ip, int, int, ip, string, string)  
| This event is emitted when a route is removed. [More...](class_routing_process.html#a9c7c8bc058c923f60338a8d26e3d3f4e)  
  
void | [networkAdded](class_routing_process.html#acd75160017b98afacd1d0a45e7ba8037) (ip, ip)  
| This event is emitted when a network is added. [More...](class_routing_process.html#acd75160017b98afacd1d0a45e7ba8037)  
  
void | [networkRemoved](class_routing_process.html#a4b53f5c8422444db3480cfac2500111e) (ip, ip)  
| This event is emitted when a network is removed. [More...](class_routing_process.html#a4b53f5c8422444db3480cfac2500111e)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Member Function Documentation

## ◆ networkAdded()

void RoutingProcessv6::networkAdded  | ( | ipv6  | ,   
---|---|---|---  
|  | ipv6  |   
| ) | |   
  
This event is emitted when a network is added. 

  * network, the network address. 
  * mask, the network mask.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ networkRemoved()

void RoutingProcessv6::networkRemoved  | ( | ipv6  | ,   
---|---|---|---  
|  | ipv6  |   
| ) | |   
  
This event is emitted when a network is removed. 

  * network, the network address. 
  * mask, the network mask.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ routeAdded()

void RoutingProcessv6::routeAdded  | ( | ipv6  | ,   
---|---|---|---  
|  | ipv6  | ,   
|  | int  | ,   
|  | int  | ,   
|  | ipv6  | ,   
|  | string  | ,   
|  | string  |   
| ) | |   
  
This event is emitted when a route is added. 

  * network, the network address. 
  * mask, the network mask. 
  * metric, the metric value. 
  * distance, the administrative distance value. 
  * nexthop, the next hop address. 
  * portName, portName can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0 
  * protocolCode, the protocol code.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ routeRemoved()

void RoutingProcessv6::routeRemoved  | ( | ipv6  | ,   
---|---|---|---  
|  | ipv6  | ,   
|  | int  | ,   
|  | int  | ,   
|  | ipv6  | ,   
|  | string  | ,   
|  | string  |   
| ) | |   
  
This event is emitted when a route is removed. 

  * network, the network address. 
  * mask, the network mask. 
  * metric, the metric value. 
  * distance, the administrative distance value. 
  * nexthop, the next hop address. 
  * portName, portName can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0 
  * protocolCode, the protocol code.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

* * *

The documentation for this class was generated from the following file:

  * [CRoutingProcessv6.pki](_c_routing_processv6_8pki.html)


