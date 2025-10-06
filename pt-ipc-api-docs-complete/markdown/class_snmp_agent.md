# Cisco Packet Tracer Extensions API: SnmpAgent Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_snmp_agent.html

---

[SnmpAgent](class_snmp_agent.html "SnmpAgent holds and manipulates the SNMP agent.") holds and manipulates the SNMP agent. [More...](class_snmp_agent.html#details)

##  Public Member Functions  
  
---  
pair< string, Access > | [getCommunity](class_snmp_agent.html#a0ad1a1ef3383caafdafae8452bda7936) (string)  
| Returns the community with the specified name. [More...](class_snmp_agent.html#a0ad1a1ef3383caafdafae8452bda7936)  
  
pair< string, Access > | [getCommunityAt](class_snmp_agent.html#a839d48d51231d763b7e2b5c97213ff8c) (int)  
| Returns the community at the specified name. [More...](class_snmp_agent.html#a839d48d51231d763b7e2b5c97213ff8c)  
  
bool | [removeCommunity](class_snmp_agent.html#ac7bc58ac213e8729db6c47e7ce0c938f) (string)  
| Removes the specified community. [More...](class_snmp_agent.html#ac7bc58ac213e8729db6c47e7ce0c938f)  
  
void | [addCommunity](class_snmp_agent.html#ac960023f4a67eb734d02b4899924bff8) (string, Access)  
| Adds a community. [More...](class_snmp_agent.html#ac960023f4a67eb734d02b4899924bff8)  
  
int | [getCommunityCount](class_snmp_agent.html#a9ff3537e19a6a3a82b89e8c6c8909ca2) ()  
| Returns the number of communities. [More...](class_snmp_agent.html#a9ff3537e19a6a3a82b89e8c6c8909ca2)  
  
bool | [isEnabled](class_snmp_agent.html#a9379c257714545b84f860dbf91771c97) ()  
| Returns true if the SNMP agent is enabled, otherwise false. [More...](class_snmp_agent.html#a9379c257714545b84f860dbf91771c97)  
  
void | [setEnabled](class_snmp_agent.html#afadc8ae04b712aab88aca8b508af3c62) (bool)  
| Enables or disables the SNMP agent. [More...](class_snmp_agent.html#afadc8ae04b712aab88aca8b508af3c62)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[SnmpAgent](class_snmp_agent.html "SnmpAgent holds and manipulates the SNMP agent.") holds and manipulates the SNMP agent. 

## Member Function Documentation

## ◆ addCommunity()

void SnmpAgent::addCommunity  | ( | string  | ,   
---|---|---|---  
|  | Access  |   
| ) | |   
  
Adds a community. 

Parameters
     communityStr,the| name of the community.   
---|---  
access,the| community name and access privileges. Access privileges: eAccess_ReadOnly = 0, eAccess_ReadWrite = 1, eAccess_ReadCreate = 2, eAccess_NotAccessible = 3  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ getCommunity()

pair< string, Access > SnmpAgent::getCommunity  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the community with the specified name. 

Parameters
     community,the| name of the community of interest.  
---|---  
  
Returns
    pair<string, enum<Access>, the community name and access privileges. Access privileges: eAccess_ReadOnly = 0, eAccess_ReadWrite = 1, eAccess_ReadCreate = 2, eAccess_NotAccessible = 3 

## ◆ getCommunityAt()

pair< string, Access > SnmpAgent::getCommunityAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the community at the specified name. 

Parameters
     index,the| index of the community of interest.  
---|---  
  
Returns
    pair<string, enum<Access>, the community name and access privileges. Access privileges: eAccess_ReadOnly = 0, eAccess_ReadWrite = 1, eAccess_ReadCreate = 2, eAccess_NotAccessible = 3 

## ◆ getCommunityCount()

int SnmpAgent::getCommunityCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of communities. 

Returns
    int, the number of communities. 

## ◆ isEnabled()

bool SnmpAgent::isEnabled  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the SNMP agent is enabled, otherwise false. 

Returns
    bool, true if the SNMP agent is enabled, otherwise false. 

## ◆ removeCommunity()

bool SnmpAgent::removeCommunity  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes the specified community. 

Parameters
     communityStr,the| name of the community of interest.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ setEnabled()

void SnmpAgent::setEnabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables the SNMP agent. 

Returns
    enabled, true to enable the SNMP agent, false to disable it. 

* * *

The documentation for this class was generated from the following file:

  * [CSnmpAgent.pki](_c_snmp_agent_8pki.html)


