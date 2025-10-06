# Cisco Packet Tracer Extensions API: FlowTable Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_flow_table.html

---

[FlowTable](class_flow_table.html "FlowTable holds and manipulates the flow table.") holds and manipulates the flow table. [More...](class_flow_table.html#details)

##  Public Member Functions  
  
---  
int | [getFlowCount](class_flow_table.html#a67daa03f7322336053400f9943b2b557) ()  
| Returns the number of flows in the flow table. [More...](class_flow_table.html#a67daa03f7322336053400f9943b2b557)  
  
[Flow](class_flow.html) | [getFlowAt](class_flow_table.html#ae23175e3043437b0d40d451a69740076) (int)  
| Returns the flow at the specified index. [More...](class_flow_table.html#ae23175e3043437b0d40d451a69740076)  
  
  
## Detailed Description

[FlowTable](class_flow_table.html "FlowTable holds and manipulates the flow table.") holds and manipulates the flow table. 

## Member Function Documentation

## ◆ getFlowAt()

[Flow](class_flow.html) FlowTable::getFlowAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the flow at the specified index. 

Parameters
     index,the| index of the flow of interest.  
---|---  
  
Returns
    index, the [Flow](class_flow.html "Flow holds and manipulates the flow routes in FlowTable objects.") object at the specified index. 

## ◆ getFlowCount()

int FlowTable::getFlowCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of flows in the flow table. 

Returns
    int, the number of flows in the flow table. 

* * *

The documentation for this class was generated from the following file:

  * [CFlowTable.pki](_c_flow_table_8pki.html)


