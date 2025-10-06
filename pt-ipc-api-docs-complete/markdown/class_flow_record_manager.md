# Cisco Packet Tracer Extensions API: FlowRecordManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_flow_record_manager.html

---

[FlowRecordManager](class_flow_record_manager.html "FlowRecordManager manages all the flow records defined on a device.") manages all the flow records defined on a device. [More...](class_flow_record_manager.html#details)

##  Public Member Functions  
  
---  
int | [getRecordCount](class_flow_record_manager.html#ad24035b9e590e1a1a0fe728f5e2104d6) ()  
| Returns the number of flow records. [More...](class_flow_record_manager.html#ad24035b9e590e1a1a0fe728f5e2104d6)  
  
[FlowRecord](struct_flow_record.html) | [getRecordAt](class_flow_record_manager.html#a30585a17bfe150f9145b567b3e27479e) (int)  
| Returns the flow record at the specified index. [More...](class_flow_record_manager.html#a30585a17bfe150f9145b567b3e27479e)  
  
[FlowRecord](struct_flow_record.html) | [getRecord](class_flow_record_manager.html#a7e0307fefa8ba9f49472272e34553f4e) (string)  
| Returns the flow record with the specified name. [More...](class_flow_record_manager.html#a7e0307fefa8ba9f49472272e34553f4e)  
  
[FlowRecord](struct_flow_record.html) | [createRecord](class_flow_record_manager.html#a2a807b186a365aed2aae4d3600f5bf4d) (string)  
| Creates a flow record with the specified name. [More...](class_flow_record_manager.html#a2a807b186a365aed2aae4d3600f5bf4d)  
  
void | [removeRecord](class_flow_record_manager.html#a67544de7646d15ac4fb45e70a3c5c3b5) (string)  
| Removes the flow record with the specified name. [More...](class_flow_record_manager.html#a67544de7646d15ac4fb45e70a3c5c3b5)  
  
  
## Detailed Description

[FlowRecordManager](class_flow_record_manager.html "FlowRecordManager manages all the flow records defined on a device.") manages all the flow records defined on a device. 

## Member Function Documentation

## ◆ createRecord()

[FlowRecord](struct_flow_record.html) FlowRecordManager::createRecord  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Creates a flow record with the specified name. 

Parameters
     recordName,the| name of the flow record.  
---|---  
  
Returns
    [FlowRecord](struct_flow_record.html "FlowRecord structure."), the [FlowRecord](struct_flow_record.html "FlowRecord structure.") object with the specified name. 

## ◆ getRecord()

[FlowRecord](struct_flow_record.html) FlowRecordManager::getRecord  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the flow record with the specified name. 

Parameters
     recordName,the| name of the flow record of interest.  
---|---  
  
Returns
    [FlowRecord](struct_flow_record.html "FlowRecord structure."), the [FlowRecord](struct_flow_record.html "FlowRecord structure.") object with the specified name. 

## ◆ getRecordAt()

[FlowRecord](struct_flow_record.html) FlowRecordManager::getRecordAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the flow record at the specified index. 

Parameters
     index,the| index of the flow record of interest.  
---|---  
  
Returns
    [FlowRecord](struct_flow_record.html "FlowRecord structure."), the [FlowRecord](struct_flow_record.html "FlowRecord structure.") object at the specified index. 

## ◆ getRecordCount()

int FlowRecordManager::getRecordCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of flow records. 

Returns
    string, the number of flow records. 

## ◆ removeRecord()

void FlowRecordManager::removeRecord  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes the flow record with the specified name. 

Parameters
     recordName,the| name of the flow record of interest.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CFlowRecordManager.pki](_c_flow_record_manager_8pki.html)


