# Cisco Packet Tracer Extensions API: ServicePolicyManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_service_policy_manager.html

---

##  Public Member Functions  
  
---  
void | [deleteServicePolicy](class_service_policy_manager.html#a315ac3a8069ee3748f5cdd4558a2175c) (string, string)  
| Delete the service policy that matches policy-map and interface name. [More...](class_service_policy_manager.html#a315ac3a8069ee3748f5cdd4558a2175c)  
  
[ServicePolicy](class_service_policy.html) | [getServicePolicy](class_service_policy_manager.html#a0613293e72fd4e4c9cf9520ae41ae99d) (string, string, string)  
| Returns the service-policy that matches policy-map name, mode("interface"/"global") and interface nameIf. [More...](class_service_policy_manager.html#a0613293e72fd4e4c9cf9520ae41ae99d)  
  
[ServicePolicy](class_service_policy.html) | [getGlobalServicePolicy](class_service_policy_manager.html#a4d1a3d2c6506ebd7d8ca7818174fc7e8) ()  
| Returns the global service-policy. [More...](class_service_policy_manager.html#a4d1a3d2c6506ebd7d8ca7818174fc7e8)  
  
[ServicePolicy](class_service_policy.html) | [getIntfServicePolicy](class_service_policy_manager.html#a1298242ef34915ddd074a50f7beebf6d) (string)  
| Returns the interface service-policy that matches the interface nameIf. [More...](class_service_policy_manager.html#a1298242ef34915ddd074a50f7beebf6d)  
  
[ServicePolicy](class_service_policy.html) | [getServicePolicyAt](class_service_policy_manager.html#aecc2db8a0d0d72f8c72c690ba5c897e4) (int)  
| Returns the service-policy at a specified index. [More...](class_service_policy_manager.html#aecc2db8a0d0d72f8c72c690ba5c897e4)  
  
int | [getServicePolicyCount](class_service_policy_manager.html#afc55caf098e9b209fedfd80e21e4db22) ()  
| Returns the number of service-policy has been configured. [More...](class_service_policy_manager.html#afc55caf098e9b209fedfd80e21e4db22)  
  
  
## Member Function Documentation

## ◆ deleteServicePolicy()

void ServicePolicyManager::deleteServicePolicy  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Delete the service policy that matches policy-map and interface name. 

## ◆ getGlobalServicePolicy()

[ServicePolicy](class_service_policy.html) ServicePolicyManager::getGlobalServicePolicy  | ( | | ) |   
---|---|---|---|---  
  
Returns the global service-policy. 

## ◆ getIntfServicePolicy()

[ServicePolicy](class_service_policy.html) ServicePolicyManager::getIntfServicePolicy  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the interface service-policy that matches the interface nameIf. 

## ◆ getServicePolicy()

[ServicePolicy](class_service_policy.html) ServicePolicyManager::getServicePolicy  | ( | string  | ,   
---|---|---|---  
|  | string  | ,   
|  | string  |   
| ) | |   
  
Returns the service-policy that matches policy-map name, mode("interface"/"global") and interface nameIf. 

## ◆ getServicePolicyAt()

[ServicePolicy](class_service_policy.html) ServicePolicyManager::getServicePolicyAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the service-policy at a specified index. 

## ◆ getServicePolicyCount()

int ServicePolicyManager::getServicePolicyCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of service-policy has been configured. 

* * *

The documentation for this class was generated from the following file:

  * [CServicePolicyManager.pki](_c_service_policy_manager_8pki.html)


