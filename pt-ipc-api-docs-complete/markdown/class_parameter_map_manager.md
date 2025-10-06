# Cisco Packet Tracer Extensions API: ParameterMapManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_parameter_map_manager.html

---

[ParameterMapManager](class_parameter_map_manager.html "ParameterMapManager holds and manages Zone-Based Policy Firewall parameter maps.") holds and manages Zone-Based Policy Firewall parameter maps. [More...](class_parameter_map_manager.html#details)

##  Public Member Functions  
  
---  
void | [deleteParameterMap](class_parameter_map_manager.html#aef72a811c3ee1c9453efc044cc02fb2c) (string)  
| Deletes the parameter map with the specified name. [More...](class_parameter_map_manager.html#aef72a811c3ee1c9453efc044cc02fb2c)  
  
[ParameterMap](class_parameter_map.html) | [getParameterMap](class_parameter_map_manager.html#ae041427f4cfd1aeea1bd72b3e8cfb525) (string)  
| Returns the parameter map with the specified name. [More...](class_parameter_map_manager.html#ae041427f4cfd1aeea1bd72b3e8cfb525)  
  
[ParameterMap](class_parameter_map.html) | [getParameterMapAt](class_parameter_map_manager.html#aa066774aad3e1d92f7d7cf397636eaa1) (int)  
| Returns the parameter map at the specified index. [More...](class_parameter_map_manager.html#aa066774aad3e1d92f7d7cf397636eaa1)  
  
bool | [isParameterMapExists](class_parameter_map_manager.html#adf9950ee1e54cbdc66baf96f0a14c556) (string)  
| Returns true if the paramter map with the specified name exists, otherwise false. [More...](class_parameter_map_manager.html#adf9950ee1e54cbdc66baf96f0a14c556)  
  
int | [getParameterMapCount](class_parameter_map_manager.html#a92ed257f56690f58b50d2c08c8a42b4a) ()  
| Returns the number of paramter maps. [More...](class_parameter_map_manager.html#a92ed257f56690f58b50d2c08c8a42b4a)  
  
  
## Detailed Description

[ParameterMapManager](class_parameter_map_manager.html "ParameterMapManager holds and manages Zone-Based Policy Firewall parameter maps.") holds and manages Zone-Based Policy Firewall parameter maps. 

## Member Function Documentation

## ◆ deleteParameterMap()

void ParameterMapManager::deleteParameterMap  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Deletes the parameter map with the specified name. 

Parameters
     name,the| name of the paramter map of interest.   
---|---  
  
## ◆ getParameterMap()

[ParameterMap](class_parameter_map.html) ParameterMapManager::getParameterMap  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the parameter map with the specified name. 

Parameters
     name,the| name of the paramter map of interest.  
---|---  
  
Returns
    [ParameterMap](class_parameter_map.html "ParameterMap handles and manipulates Zone-Based Policy Firewall parameter maps."), the [ParameterMap](class_parameter_map.html "ParameterMap handles and manipulates Zone-Based Policy Firewall parameter maps.") object with the specified name. 

## ◆ getParameterMapAt()

[ParameterMap](class_parameter_map.html) ParameterMapManager::getParameterMapAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the parameter map at the specified index. 

Parameters
     index,the| index of the paramter map of interest.  
---|---  
  
Returns
    [ParameterMap](class_parameter_map.html "ParameterMap handles and manipulates Zone-Based Policy Firewall parameter maps."), the [ParameterMap](class_parameter_map.html "ParameterMap handles and manipulates Zone-Based Policy Firewall parameter maps.") object at the specified index. 

## ◆ getParameterMapCount()

int ParameterMapManager::getParameterMapCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of paramter maps. 

Returns
    int, the number of paramter maps. 

## ◆ isParameterMapExists()

bool ParameterMapManager::isParameterMapExists  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns true if the paramter map with the specified name exists, otherwise false. 

Parameters
     name,the| name of the paramter map of interest.  
---|---  
  
Returns
    bool, the true if the paramter map with the specified name exists, otherwise false. 

* * *

The documentation for this class was generated from the following file:

  * [CParameterMapManager.pki](_c_parameter_map_manager_8pki.html)


