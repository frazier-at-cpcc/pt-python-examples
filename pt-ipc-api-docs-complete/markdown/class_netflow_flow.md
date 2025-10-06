# Cisco Packet Tracer Extensions API: NetflowFlow Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_netflow_flow.html

---

[NetflowFlow](class_netflow_flow.html "NetflowFlow holds and manipulates NetFlow flows.") holds and manipulates NetFlow flows. [More...](class_netflow_flow.html#details)

##  Public Member Functions  
  
---  
int | [getMatchStatementCount](class_netflow_flow.html#aebba48e87dec7e6cbc1eac7cc0f6e498) ()  
| Returns the number of match statements. [More...](class_netflow_flow.html#aebba48e87dec7e6cbc1eac7cc0f6e498)  
  
[FlowMatchStatement](struct_flow_match_statement.html) | [getMatchStatementAt](class_netflow_flow.html#a6b7319d9bc2bb576d0755d8ba9ea1664) (int)  
| Returns the match statement at the specified index. [More...](class_netflow_flow.html#a6b7319d9bc2bb576d0755d8ba9ea1664)  
  
int | [getCollectStatementCount](class_netflow_flow.html#a4c0fe5e711f168325e6de14fc160913d) ()  
| Returns the number of collect statements. [More...](class_netflow_flow.html#a4c0fe5e711f168325e6de14fc160913d)  
  
[FlowCollectStatement](struct_flow_collect_statement.html) | [getCollectStatementAt](class_netflow_flow.html#a0a1f0ea6c25240fc3447b208af6a91bd) (int)  
| Returns the collect statement at the specified index. [More...](class_netflow_flow.html#a0a1f0ea6c25240fc3447b208af6a91bd)  
  
string | [getAssociatedRecordName](class_netflow_flow.html#ab8024815be8d6c5be1f4a5b82395c508) ()  
| Returns the name of the associated record. [More...](class_netflow_flow.html#ab8024815be8d6c5be1f4a5b82395c508)  
  
void | [setAssociatedRecordName](class_netflow_flow.html#a785b872624a48f75dd787de6b652e388) (string)  
| Sets the name for the associated record. [More...](class_netflow_flow.html#a785b872624a48f75dd787de6b652e388)  
  
string | [getIpFlowCacheString](class_netflow_flow.html#a742ff913d34c6158a75f9327ac7c791f) ()  
| Returns the IP cache flow output. [More...](class_netflow_flow.html#a742ff913d34c6158a75f9327ac7c791f)  
  
  
## Detailed Description

[NetflowFlow](class_netflow_flow.html "NetflowFlow holds and manipulates NetFlow flows.") holds and manipulates NetFlow flows. 

## Member Function Documentation

## ◆ getAssociatedRecordName()

string NetflowFlow::getAssociatedRecordName  | ( | | ) |   
---|---|---|---|---  
  
Returns the name of the associated record. 

Returns
    string, the name of the associated record. 

## ◆ getCollectStatementAt()

[FlowCollectStatement](struct_flow_collect_statement.html) NetflowFlow::getCollectStatementAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the collect statement at the specified index. 

Parameters
     index,the| index of the collect statement of interest.  
---|---  
  
Returns
    [FlowCollectStatement](struct_flow_collect_statement.html "FlowCollectStatement structure."), the [FlowCollectStatement](struct_flow_collect_statement.html "FlowCollectStatement structure.") at the specified index. 

## ◆ getCollectStatementCount()

int NetflowFlow::getCollectStatementCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of collect statements. 

Returns
    int, the number of collect statements. 

## ◆ getIpFlowCacheString()

string NetflowFlow::getIpFlowCacheString  | ( | | ) |   
---|---|---|---|---  
  
Returns the IP cache flow output. 

Returns
    string, the IP cache flow output. 

## ◆ getMatchStatementAt()

[FlowMatchStatement](struct_flow_match_statement.html) NetflowFlow::getMatchStatementAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the match statement at the specified index. 

Parameters
     index,the| index of the match statement of interest.  
---|---  
  
Returns
    [FlowMatchStatement](struct_flow_match_statement.html "FlowMatchStatement structure."), the [FlowMatchStatement](struct_flow_match_statement.html "FlowMatchStatement structure.") at the specified index. 

## ◆ getMatchStatementCount()

int NetflowFlow::getMatchStatementCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of match statements. 

Returns
    int, the number of match statements. 

## ◆ setAssociatedRecordName()

void NetflowFlow::setAssociatedRecordName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the name for the associated record. 

Parameters
     record,the| name for the associated record.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CNetflowFlow.pki](_c_netflow_flow_8pki.html)


