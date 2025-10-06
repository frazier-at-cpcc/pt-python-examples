# Cisco Packet Tracer Extensions API: EigrpNeighborTable Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_eigrp_neighbor_table.html

---

[EigrpNeighborTable](class_eigrp_neighbor_table.html "EigrpNeighborTable holds the EIGRP neighbor table.") holds the EIGRP neighbor table. [More...](class_eigrp_neighbor_table.html#details)

##  Public Member Functions  
  
---  
int | [getNeighborCount](class_eigrp_neighbor_table.html#ac5c92c056bda735ba0ae9c8b1d3cbaa3) ()  
| Returns the number of neighbors in the table. [More...](class_eigrp_neighbor_table.html#ac5c92c056bda735ba0ae9c8b1d3cbaa3)  
  
[EigrpNeighbor](struct_eigrp_neighbor.html) | [getNeighborAt](class_eigrp_neighbor_table.html#a600d785b22b1fb0d0dd7f8aef2154b51) (int)  
| Returns the neighbor at the specified index. [More...](class_eigrp_neighbor_table.html#a600d785b22b1fb0d0dd7f8aef2154b51)  
  
[EigrpNeighbor](struct_eigrp_neighbor.html) | [getNeighborByIp](class_eigrp_neighbor_table.html#a49c99f0e32b39626edad00eefa1aaf19) (ip)  
| Returns the neighbor with the specified IP address. [More...](class_eigrp_neighbor_table.html#a49c99f0e32b39626edad00eefa1aaf19)  
  
  
## Detailed Description

[EigrpNeighborTable](class_eigrp_neighbor_table.html "EigrpNeighborTable holds the EIGRP neighbor table.") holds the EIGRP neighbor table. 

## Member Function Documentation

## ◆ getNeighborAt()

[EigrpNeighbor](struct_eigrp_neighbor.html) EigrpNeighborTable::getNeighborAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the neighbor at the specified index. 

Parameters
     index,the| index of the neighbor of interest.  
---|---  
  
Returns
    [EigrpNeighbor](struct_eigrp_neighbor.html "Data element for EIGRP neighbors."), the [EigrpNeighbor](struct_eigrp_neighbor.html "Data element for EIGRP neighbors.") at the specified index. 

## ◆ getNeighborByIp()

[EigrpNeighbor](struct_eigrp_neighbor.html) EigrpNeighborTable::getNeighborByIp  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Returns the neighbor with the specified IP address. 

Parameters
     ipAddress,the| IP address of the neighbor of interest.  
---|---  
  
Returns
    [EigrpNeighbor](struct_eigrp_neighbor.html "Data element for EIGRP neighbors."), the [EigrpNeighbor](struct_eigrp_neighbor.html "Data element for EIGRP neighbors.") with the specified IP address. 

## ◆ getNeighborCount()

int EigrpNeighborTable::getNeighborCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of neighbors in the table. 

Returns
    int, the number of neighbors in the table. 

* * *

The documentation for this class was generated from the following file:

  * [CEigrpNeighborTable.pki](_c_eigrp_neighbor_table_8pki.html)


