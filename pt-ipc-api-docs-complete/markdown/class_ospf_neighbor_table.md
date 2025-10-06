# Cisco Packet Tracer Extensions API: OspfNeighborTable Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_ospf_neighbor_table.html

---

[OspfNeighborTable](class_ospf_neighbor_table.html "OspfNeighborTable handles and manipulates OSPF neighbor tables.") handles and manipulates OSPF neighbor tables. [More...](class_ospf_neighbor_table.html#details)

##  Public Member Functions  
  
---  
[OspfNeighbor](struct_ospf_neighbor.html) | [getNeighborAt](class_ospf_neighbor_table.html#a6a1a872c673f84dca378e940953e20df) (int)  
| Returns the neighbor at the specified index. [More...](class_ospf_neighbor_table.html#a6a1a872c673f84dca378e940953e20df)  
  
int | [getNeighborCount](class_ospf_neighbor_table.html#a1d10c762bdb746552faad4356f01c966) ()  
| Returns the number of neighbors. [More...](class_ospf_neighbor_table.html#a1d10c762bdb746552faad4356f01c966)  
  
[RouterPort](class_router_port.html) | [getPort](class_ospf_neighbor_table.html#ab84c6f626e10147e04509ada08f4b3c1) ()  
| Returns the port of this neighbor table. [More...](class_ospf_neighbor_table.html#ab84c6f626e10147e04509ada08f4b3c1)  
  
int | [getAdjNeighborCount](class_ospf_neighbor_table.html#a50538b4de41c5af1deead6f26fbfd2ee) ()  
| Returns the number of adjacent neighbors. [More...](class_ospf_neighbor_table.html#a50538b4de41c5af1deead6f26fbfd2ee)  
  
ip | [getAdjNeighborAt](class_ospf_neighbor_table.html#a60096ec75ae3737db325494cd373143a) (int)  
| Returns the IP address of the adjacent neighbor at the specified index. [More...](class_ospf_neighbor_table.html#a60096ec75ae3737db325494cd373143a)  
  
int | [getFloodLength](class_ospf_neighbor_table.html#a106561973461f81b286e8d1911a48de7) ()  
| Returns the flood length. [More...](class_ospf_neighbor_table.html#a106561973461f81b286e8d1911a48de7)  
  
int | [getLastFloodLength](class_ospf_neighbor_table.html#acc9b925761d48b1cb3361336965e40b4) ()  
| Returns the last flood length. [More...](class_ospf_neighbor_table.html#acc9b925761d48b1cb3361336965e40b4)  
  
int | [getMaxFloodLength](class_ospf_neighbor_table.html#a38e1833a061ba38c3a269328d4113307) ()  
| Returns the maximum flood length. [More...](class_ospf_neighbor_table.html#a38e1833a061ba38c3a269328d4113307)  
  
int | [getLastFloodTime](class_ospf_neighbor_table.html#a807b5294ed1d2a862d9ffac88ddfd64b) ()  
| Returns the last flood time. [More...](class_ospf_neighbor_table.html#a807b5294ed1d2a862d9ffac88ddfd64b)  
  
int | [getMaxFloodTime](class_ospf_neighbor_table.html#ab6ca259f06fa71bf08c0fa6ca7772a7b) ()  
| Returns the maximum flood time. [More...](class_ospf_neighbor_table.html#ab6ca259f06fa71bf08c0fa6ca7772a7b)  
  
  
## Detailed Description

[OspfNeighborTable](class_ospf_neighbor_table.html "OspfNeighborTable handles and manipulates OSPF neighbor tables.") handles and manipulates OSPF neighbor tables. 

## Member Function Documentation

## ◆ getAdjNeighborAt()

ip OspfNeighborTable::getAdjNeighborAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the IP address of the adjacent neighbor at the specified index. 

Parameters
     index,the| index of the adjacent neighbor of interest.  
---|---  
  
Returns
    ip, the IP address of the adjacent neighbor at the specified index. 

## ◆ getAdjNeighborCount()

int OspfNeighborTable::getAdjNeighborCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of adjacent neighbors. 

Returns
    int, the number of adjacent neighbors. 

## ◆ getFloodLength()

int OspfNeighborTable::getFloodLength  | ( | | ) |   
---|---|---|---|---  
  
Returns the flood length. 

Returns
    int, the flood length. 

## ◆ getLastFloodLength()

int OspfNeighborTable::getLastFloodLength  | ( | | ) |   
---|---|---|---|---  
  
Returns the last flood length. 

Returns
    int, the last flood length. 

## ◆ getLastFloodTime()

int OspfNeighborTable::getLastFloodTime  | ( | | ) |   
---|---|---|---|---  
  
Returns the last flood time. 

Returns
    int, the last flood time. 

## ◆ getMaxFloodLength()

int OspfNeighborTable::getMaxFloodLength  | ( | | ) |   
---|---|---|---|---  
  
Returns the maximum flood length. 

Returns
    int, the maximum flood length. 

## ◆ getMaxFloodTime()

int OspfNeighborTable::getMaxFloodTime  | ( | | ) |   
---|---|---|---|---  
  
Returns the maximum flood time. 

Returns
    int, the maximum flood time. 

## ◆ getNeighborAt()

[OspfNeighbor](struct_ospf_neighbor.html) OspfNeighborTable::getNeighborAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the neighbor at the specified index. 

Parameters
     index,the| index of the neighbor of interest.  
---|---  
  
Returns
    [OspfNeighbor](struct_ospf_neighbor.html "Data element of OspfNeighbor."), the [OspfNeighbor](struct_ospf_neighbor.html "Data element of OspfNeighbor.") object at the specified index. 

## ◆ getNeighborCount()

int OspfNeighborTable::getNeighborCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of neighbors. 

Returns
    int, the number of neighbors. 

## ◆ getPort()

[RouterPort](class_router_port.html) OspfNeighborTable::getPort  | ( | | ) |   
---|---|---|---|---  
  
Returns the port of this neighbor table. 

Returns
    [RouterPort](class_router_port.html "RouterPort handles and manipulates the router port."), the [RouterPort](class_router_port.html "RouterPort handles and manipulates the router port.") object of this neighbor table. 

* * *

The documentation for this class was generated from the following file:

  * [COspfNeighborTable.pki](_c_ospf_neighbor_table_8pki.html)


