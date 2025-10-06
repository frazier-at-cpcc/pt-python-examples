# Cisco Packet Tracer Extensions API: CdpNeighborTable Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_cdp_neighbor_table.html

---

[CdpNeighborTable](class_cdp_neighbor_table.html "CdpNeighborTable holds the CDP neighbor tables.") holds the CDP neighbor tables. [More...](class_cdp_neighbor_table.html#details)

##  Public Member Functions  
  
---  
int | [getNeighborTableCount](class_cdp_neighbor_table.html#a1df3e1f1b1b193a70c481158ea820c77) ()  
| Returns the number of neighbor tables. [More...](class_cdp_neighbor_table.html#a1df3e1f1b1b193a70c481158ea820c77)  
  
[CdpNeighbor](struct_cdp_neighbor.html) | [getCdpNeighborAt](class_cdp_neighbor_table.html#ac3fa004da18fbcadc63434d8c3e7d1e3) (int)  
| Returns a CDP neighbor at the specified index. [More...](class_cdp_neighbor_table.html#ac3fa004da18fbcadc63434d8c3e7d1e3)  
  
  
## Detailed Description

[CdpNeighborTable](class_cdp_neighbor_table.html "CdpNeighborTable holds the CDP neighbor tables.") holds the CDP neighbor tables. 

## Member Function Documentation

## ◆ getCdpNeighborAt()

[CdpNeighbor](struct_cdp_neighbor.html) CdpNeighborTable::getCdpNeighborAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns a CDP neighbor at the specified index. 

Parameters
     index,the| index of the CDP neighbor.  
---|---  
  
Returns
    [CdpNeighbor](struct_cdp_neighbor.html "Data elements of CDP neighbor."), the CDP neighbor at the specified index. 

## ◆ getNeighborTableCount()

int CdpNeighborTable::getNeighborTableCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of neighbor tables. 

Returns
    int, the number of neighbor tables. 

* * *

The documentation for this class was generated from the following file:

  * [CCdpNeighborTable.pki](_c_cdp_neighbor_table_8pki.html)


