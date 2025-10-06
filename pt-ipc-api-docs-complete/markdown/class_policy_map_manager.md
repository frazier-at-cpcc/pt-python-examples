# Cisco Packet Tracer Extensions API: PolicyMapManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_policy_map_manager.html

---

[PolicyMapManager](class_policy_map_manager.html "PolicyMapManager holds and manages policy maps.") holds and manages policy maps. [More...](class_policy_map_manager.html#details)

##  Public Member Functions  
  
---  
int | [getPolicyMapCount](class_policy_map_manager.html#a0f4c22952438c79dadfbcdd86457135c) ()  
| Returns the number of policy maps. [More...](class_policy_map_manager.html#a0f4c22952438c79dadfbcdd86457135c)  
  
[PolicyMap](class_policy_map.html) | [getPolicyMapAt](class_policy_map_manager.html#a5940b0ac82938e0567705fd9d0a4899e) (int)  
| Returns the policy map at the specified index. [More...](class_policy_map_manager.html#a5940b0ac82938e0567705fd9d0a4899e)  
  
[PolicyMap](class_policy_map.html) | [getPolicyMap](class_policy_map_manager.html#a26e98a3535fc957a1c9da831d27379ef) (string)  
| Returns the policy map with the specified name. [More...](class_policy_map_manager.html#a26e98a3535fc957a1c9da831d27379ef)  
  
  
## Detailed Description

[PolicyMapManager](class_policy_map_manager.html "PolicyMapManager holds and manages policy maps.") holds and manages policy maps. 

## Member Function Documentation

## ◆ getPolicyMap()

[PolicyMap](class_policy_map.html) PolicyMapManager::getPolicyMap  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the policy map with the specified name. 

Parameters
     name,the| name of the policy map of interest.  
---|---  
  
Returns
    [PolicyMap](class_policy_map.html "PolicyMap handles and manipulates policy maps."), the [PolicyMap](class_policy_map.html "PolicyMap handles and manipulates policy maps.") object with the specified name. 

## ◆ getPolicyMapAt()

[PolicyMap](class_policy_map.html) PolicyMapManager::getPolicyMapAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the policy map at the specified index. 

Parameters
     index,the| index of the policy map of interest.  
---|---  
  
Returns
    [PolicyMap](class_policy_map.html "PolicyMap handles and manipulates policy maps."), the [PolicyMap](class_policy_map.html "PolicyMap handles and manipulates policy maps.") object at the specified index. 

## ◆ getPolicyMapCount()

int PolicyMapManager::getPolicyMapCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of policy maps. 

Returns
    int, the number of policy maps. 

* * *

The documentation for this class was generated from the following file:

  * [CPolicyMapManager.pki](_c_policy_map_manager_8pki.html)


