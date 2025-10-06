# Cisco Packet Tracer Extensions API: BbaGroup Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_bba_group.html

---

[BbaGroup](class_bba_group.html "BbaGroup handles and manipulates Bba groups.") handles and manipulates Bba groups. [More...](class_bba_group.html#details)

##  Public Member Functions  
  
---  
void | [setGroupName](class_bba_group.html#a87afd879e852651fdf8b9e89a5ad6687) (string)  
| Sets the Bba group name. [More...](class_bba_group.html#a87afd879e852651fdf8b9e89a5ad6687)  
  
string | [getGroupName](class_bba_group.html#ab89244b67127980e0ab6d33115725c2f) ()  
| Returns the Bba group name. [More...](class_bba_group.html#ab89244b67127980e0ab6d33115725c2f)  
  
void | [setVirtualTempInt](class_bba_group.html#a0be28ca45e0a61910a61989cadde8923) ([VirtualTemplateInterface](class_virtual_template_interface.html))  
| Sets the specified [VirtualTemplateInterface](class_virtual_template_interface.html "VirtualTemplateInterface handles and manipulates individual virtual template interfaces for PPPoE.") as the virtual template interface. [More...](class_bba_group.html#a0be28ca45e0a61910a61989cadde8923)  
  
[VirtualTemplateInterface](class_virtual_template_interface.html) | [getVirtualTempInt](class_bba_group.html#af7b31bd2c732ea78a7a456abf44a083b) ()  
| Returns the virtual template interface. [More...](class_bba_group.html#af7b31bd2c732ea78a7a456abf44a083b)  
  
  
## Detailed Description

[BbaGroup](class_bba_group.html "BbaGroup handles and manipulates Bba groups.") handles and manipulates Bba groups. 

## Member Function Documentation

## ◆ getGroupName()

string BbaGroup::getGroupName  | ( | | ) |   
---|---|---|---|---  
  
Returns the Bba group name. 

Returns
    string, the name of the Bba group. 

## ◆ getVirtualTempInt()

[VirtualTemplateInterface](class_virtual_template_interface.html) BbaGroup::getVirtualTempInt  | ( | | ) |   
---|---|---|---|---  
  
Returns the virtual template interface. 

Returns
    vInterface, the [VirtualTemplateInterface](class_virtual_template_interface.html "VirtualTemplateInterface handles and manipulates individual virtual template interfaces for PPPoE.") object. 

## ◆ setGroupName()

void BbaGroup::setGroupName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the Bba group name. 

Parameters
     name,the| name for the Bba group.   
---|---  
  
## ◆ setVirtualTempInt()

void BbaGroup::setVirtualTempInt  | ( | [VirtualTemplateInterface](class_virtual_template_interface.html) | | ) |   
---|---|---|---|---|---  
  
Sets the specified [VirtualTemplateInterface](class_virtual_template_interface.html "VirtualTemplateInterface handles and manipulates individual virtual template interfaces for PPPoE.") as the virtual template interface. 

Parameters
     vInterface,the| [VirtualTemplateInterface](class_virtual_template_interface.html "VirtualTemplateInterface handles and manipulates individual virtual template interfaces for PPPoE.") object of interest.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CBbaGroup.pki](_c_bba_group_8pki.html)


