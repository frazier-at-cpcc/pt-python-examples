# Cisco Packet Tracer Extensions API: PolicyMap Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_policy_map.html

---

[PolicyMap](class_policy_map.html "PolicyMap handles and manipulates policy maps.") handles and manipulates policy maps. [More...](class_policy_map.html#details)

##  Public Member Functions  
  
---  
int | [getClassCnt](class_policy_map.html#a43ae99514f427020b08a903b78403003) ()  
| Returns the number of policies. [More...](class_policy_map.html#a43ae99514f427020b08a903b78403003)  
  
[PolicyMapQosClass](class_policy_map_qos_class.html) | [getClassAt](class_policy_map.html#a132b15934bcba3ebbba63ad1e336847a) (int)  
| Returns QoS class at the specified index. [More...](class_policy_map.html#a132b15934bcba3ebbba63ad1e336847a)  
  
int | [getTotalBandwidth](class_policy_map.html#a69ad988cc3a42e26c53c85d4c410b18e) ()  
| Returns the total bandwidth value. [More...](class_policy_map.html#a69ad988cc3a42e26c53c85d4c410b18e)  
  
int | [getTotalBandwidthPercent](class_policy_map.html#a3a5a8bae15e30b2e53247363cc076490) ()  
| Returns the total bandwidth percentage. [More...](class_policy_map.html#a3a5a8bae15e30b2e53247363cc076490)  
  
int | [getTotalBandwidthRemainPercent](class_policy_map.html#a42fa6754aef73fdde14b51afe6f7fdfd) ()  
| Returns the total bandwidth remaining percentage. [More...](class_policy_map.html#a42fa6754aef73fdde14b51afe6f7fdfd)  
  
bool | [isBandwidthConfigured](class_policy_map.html#af5c92e99c0d28ca237e303bed77b647b) ()  
| Returns true if the bandwidth value is configured, otherwise false. [More...](class_policy_map.html#af5c92e99c0d28ca237e303bed77b647b)  
  
bool | [isPriorityConfigured](class_policy_map.html#a4f3c0b30c4025666c34ae1e903c2b20c) ()  
| Returns true if the priority is configured, otherwise false. [More...](class_policy_map.html#a4f3c0b30c4025666c34ae1e903c2b20c)  
  
bool | [isFairQueueConfigured](class_policy_map.html#a49b8723f803feef874348dc19ef35f2b) ()  
| Returns true if fair queue is configured, otherwise false. [More...](class_policy_map.html#a49b8723f803feef874348dc19ef35f2b)  
  
bool | [isShapeConfigured](class_policy_map.html#a9b53a335b655715c7f0737bf85858599) ()  
| Returns true if traffic shaping is configured, otherwise false. [More...](class_policy_map.html#a9b53a335b655715c7f0737bf85858599)  
  
bool | [hasOutputFeature](class_policy_map.html#a4a35f2550ab8250ce39a37eaae5dddba) ()  
| Returns true if the policy map has output feature, otherwise false. [More...](class_policy_map.html#a4a35f2550ab8250ce39a37eaae5dddba)  
  
bool | [hasGtsFeature](class_policy_map.html#a53c3a2b8b5ab8ce884033f21fa2960d2) ()  
| Returns true if the policy map has GTS feature, otherwise false. [More...](class_policy_map.html#a53c3a2b8b5ab8ce884033f21fa2960d2)  
  
void | [updateOutputPort](class_policy_map.html#a3056de592e2ce0ca1fe4136e1a657a14) ()  
| Updates the output port. [More...](class_policy_map.html#a3056de592e2ce0ca1fe4136e1a657a14)  
  
string | [getMapName](class_policy_map.html#ae6e5afe7e4fa061c4cf4f84e8b1824b2) ()  
| Returns the name of the policy map. [More...](class_policy_map.html#ae6e5afe7e4fa061c4cf4f84e8b1824b2)  
  
QoS::eMapType | [getMapType](class_policy_map.html#ac032e923d92a409be7e869df2dfbc74d) ()  
| Returns the type of the policy map. [More...](class_policy_map.html#ac032e923d92a409be7e869df2dfbc74d)  
  
void | [setMapType](class_policy_map.html#a024840ed16a88f69f65c4fc04cc86916) (QoS::eMapType)  
| Sets the type of the policy map. [More...](class_policy_map.html#a024840ed16a88f69f65c4fc04cc86916)  
  
string | [toString](class_policy_map.html#ad53b4f6439b1fe9fdfdd965f241cdbbe) (bool)  
| Returns the name of the policy map. [More...](class_policy_map.html#ad53b4f6439b1fe9fdfdd965f241cdbbe)  
  
  
## Detailed Description

[PolicyMap](class_policy_map.html "PolicyMap handles and manipulates policy maps.") handles and manipulates policy maps. 

## Member Function Documentation

## ◆ getClassAt()

[PolicyMapQosClass](class_policy_map_qos_class.html) PolicyMap::getClassAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns QoS class at the specified index. 

Parameters
     index,the| index of the QoS class of interest.  
---|---  
  
Returns
    [PolicyMapQosClass](class_policy_map_qos_class.html "PolicyMapQosClass handles and manipulates QoS classes."), the [PolicyMapQosClass](class_policy_map_qos_class.html "PolicyMapQosClass handles and manipulates QoS classes.") object. 

## ◆ getClassCnt()

int PolicyMap::getClassCnt  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of policies. 

Returns
    int, the number of policies. 

## ◆ getMapName()

string PolicyMap::getMapName  | ( | | ) |   
---|---|---|---|---  
  
Returns the name of the policy map. 

Returns
    string, the name of the policy map. 

## ◆ getMapType()

QoS::eMapType PolicyMap::getMapType  | ( | | ) |   
---|---|---|---|---  
  
Returns the type of the policy map. 

Returns
    enum<QoS::eMapType>, the type of the policy map. Map types: type_default = 0, type_control = 1, type_inspect = 2, type_asaInspect = 3, type_logging = 4 

## ◆ getTotalBandwidth()

int PolicyMap::getTotalBandwidth  | ( | | ) |   
---|---|---|---|---  
  
Returns the total bandwidth value. 

Returns
    int, the total bandwidth value. 

## ◆ getTotalBandwidthPercent()

int PolicyMap::getTotalBandwidthPercent  | ( | | ) |   
---|---|---|---|---  
  
Returns the total bandwidth percentage. 

Returns
    int, the total bandwidth percentage. 

## ◆ getTotalBandwidthRemainPercent()

int PolicyMap::getTotalBandwidthRemainPercent  | ( | | ) |   
---|---|---|---|---  
  
Returns the total bandwidth remaining percentage. 

Returns
    int, the total bandwidth remaining percentage. 

## ◆ hasGtsFeature()

bool PolicyMap::hasGtsFeature  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the policy map has GTS feature, otherwise false. 

Returns
    bool, true if the policy map has GTS feature, otherwise false. 

## ◆ hasOutputFeature()

bool PolicyMap::hasOutputFeature  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the policy map has output feature, otherwise false. 

Returns
    bool, true if the policy map has output feature, otherwise false. 

## ◆ isBandwidthConfigured()

bool PolicyMap::isBandwidthConfigured  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the bandwidth value is configured, otherwise false. 

Returns
    bool, true if the bandwidth value is configured, otherwise false. 

## ◆ isFairQueueConfigured()

bool PolicyMap::isFairQueueConfigured  | ( | | ) |   
---|---|---|---|---  
  
Returns true if fair queue is configured, otherwise false. 

Returns
    bool, true if fair queue is configured, otherwise false. 

## ◆ isPriorityConfigured()

bool PolicyMap::isPriorityConfigured  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the priority is configured, otherwise false. 

Returns
    bool, true if the priority is configured, otherwise false. 

## ◆ isShapeConfigured()

bool PolicyMap::isShapeConfigured  | ( | | ) |   
---|---|---|---|---  
  
Returns true if traffic shaping is configured, otherwise false. 

Returns
    bool, true if traffic shaping is configured, otherwise false. 

## ◆ setMapType()

void PolicyMap::setMapType  | ( | QoS::eMapType  | | ) |   
---|---|---|---|---|---  
  
Sets the type of the policy map. 

Parameters
     mapType,the| type of the policy map. Map types: type_default = 0, type_control = 1, type_inspect = 2, type_asaInspect = 3 type_logging = 4   
---|---  
  
## ◆ toString()

string PolicyMap::toString  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Returns the name of the policy map. 

Returns
    string, the name of the policy map. 

## ◆ updateOutputPort()

void PolicyMap::updateOutputPort  | ( | | ) |   
---|---|---|---|---  
  
Updates the output port. 

* * *

The documentation for this class was generated from the following file:

  * [CPolicyMap.pki](_c_policy_map_8pki.html)


