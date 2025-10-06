# Cisco Packet Tracer Extensions API: VpdnGroup Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_vpdn_group.html

---

[VpdnGroup](class_vpdn_group.html "VpdnGroup handles and manipulates VPDN groups.") handles and manipulates VPDN groups. [More...](class_vpdn_group.html#details)

##  Public Member Functions  
  
---  
void | [setDialIn](class_vpdn_group.html#abeecacd827fe160f52c0e04c9d4af7c4) (bool)  
| Enables or disables dial in. [More...](class_vpdn_group.html#abeecacd827fe160f52c0e04c9d4af7c4)  
  
bool | [isDialIn](class_vpdn_group.html#a1acd3c9c778f40a419cc5685b4b4ba11) ()  
| Returns true if dial in is enabled, otherwise false. [More...](class_vpdn_group.html#a1acd3c9c778f40a419cc5685b4b4ba11)  
  
void | [setProtocolPppoe](class_vpdn_group.html#a03fbd41d432a75ab8f7cfd0e7bfea388) (bool)  
| Enables or disables the PPPoE protocol. [More...](class_vpdn_group.html#a03fbd41d432a75ab8f7cfd0e7bfea388)  
  
bool | [isProtocolPppoe](class_vpdn_group.html#a9946e4dd7dbfee34a92527750ff73b03) ()  
| Returns true if the PPPoE protocol is enabled, otherwise false. [More...](class_vpdn_group.html#a9946e4dd7dbfee34a92527750ff73b03)  
  
void | [setGroupName](class_vpdn_group.html#ad71eb3681eb5ced76e760b9c425f953c) (string)  
| Sets the VPDN group name. [More...](class_vpdn_group.html#ad71eb3681eb5ced76e760b9c425f953c)  
  
string | [getGroupName](class_vpdn_group.html#a723692ea9b7825fd0c54b150fa3210fa) ()  
| Returns the VPDN group name. [More...](class_vpdn_group.html#a723692ea9b7825fd0c54b150fa3210fa)  
  
void | [setVirtualTempInt](class_vpdn_group.html#acd288af474f6950ac93bc911ad4d7975) ([VirtualTemplateInterface](class_virtual_template_interface.html))  
| Sets the specified [VirtualTemplateInterface](class_virtual_template_interface.html "VirtualTemplateInterface handles and manipulates individual virtual template interfaces for PPPoE.") as the virtual template interface. [More...](class_vpdn_group.html#acd288af474f6950ac93bc911ad4d7975)  
  
[VirtualTemplateInterface](class_virtual_template_interface.html) | [getVirtualTempInt](class_vpdn_group.html#afbb09bc08741624c81752cd59ea2f39a) ()  
| Returns the virtual template interface. [More...](class_vpdn_group.html#afbb09bc08741624c81752cd59ea2f39a)  
  
  
## Detailed Description

[VpdnGroup](class_vpdn_group.html "VpdnGroup handles and manipulates VPDN groups.") handles and manipulates VPDN groups. 

## Member Function Documentation

## ◆ getGroupName()

string VpdnGroup::getGroupName  | ( | | ) |   
---|---|---|---|---  
  
Returns the VPDN group name. 

Returns
    string, the name of the VPDN group. 

## ◆ getVirtualTempInt()

[VirtualTemplateInterface](class_virtual_template_interface.html) VpdnGroup::getVirtualTempInt  | ( | | ) |   
---|---|---|---|---  
  
Returns the virtual template interface. 

Returns
    vInterface, the [VirtualTemplateInterface](class_virtual_template_interface.html "VirtualTemplateInterface handles and manipulates individual virtual template interfaces for PPPoE.") object. 

## ◆ isDialIn()

bool VpdnGroup::isDialIn  | ( | | ) |   
---|---|---|---|---  
  
Returns true if dial in is enabled, otherwise false. 

Returns
    bool, true if dial in is enabled, otherwise false. 

## ◆ isProtocolPppoe()

bool VpdnGroup::isProtocolPppoe  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the PPPoE protocol is enabled, otherwise false. 

Returns
    bool, true if the PPPoE protocol is enabled, otherwise false. 

## ◆ setDialIn()

void VpdnGroup::setDialIn  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables dial in. 

Parameters
     flag,true| to enable dial in, false to disable it.   
---|---  
  
## ◆ setGroupName()

void VpdnGroup::setGroupName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the VPDN group name. 

Parameters
     name,the| name for the VPDN group.   
---|---  
  
## ◆ setProtocolPppoe()

void VpdnGroup::setProtocolPppoe  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables the PPPoE protocol. 

Parameters
     bIsPppoe,true| to enable the PPPoE protocol, false to disable it.   
---|---  
  
## ◆ setVirtualTempInt()

void VpdnGroup::setVirtualTempInt  | ( | [VirtualTemplateInterface](class_virtual_template_interface.html) | | ) |   
---|---|---|---|---|---  
  
Sets the specified [VirtualTemplateInterface](class_virtual_template_interface.html "VirtualTemplateInterface handles and manipulates individual virtual template interfaces for PPPoE.") as the virtual template interface. 

Parameters
     vInterface,the| [VirtualTemplateInterface](class_virtual_template_interface.html "VirtualTemplateInterface handles and manipulates individual virtual template interfaces for PPPoE.") object of interest.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CVpdnGroup.pki](_c_vpdn_group_8pki.html)


