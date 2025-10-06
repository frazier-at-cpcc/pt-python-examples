# Cisco Packet Tracer Extensions API: VirtualTemplateManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_virtual_template_manager.html

---

[VirtualTemplateManager](class_virtual_template_manager.html "VirtualTemplateManager manages and manipulates virtual template interfaces for PPPoE.") manages and manipulates virtual template interfaces for PPPoE. [More...](class_virtual_template_manager.html#details)

##  Public Member Functions  
  
---  
[VirtualTemplateInterface](class_virtual_template_interface.html) | [addVirtualTempIntByNum](class_virtual_template_manager.html#a1b1036df82304219654e5d45d4040329) (int)  
| Adds a virtual template interface. [More...](class_virtual_template_manager.html#a1b1036df82304219654e5d45d4040329)  
  
void | [removeVirtualTempByNum](class_virtual_template_manager.html#ac620da72161d70ffca22f1290df32277) (int)  
| Removes the virtual template interface with the specified interface number. [More...](class_virtual_template_manager.html#ac620da72161d70ffca22f1290df32277)  
  
[VirtualTemplateInterface](class_virtual_template_interface.html) | [getVirtualTempIntByNum](class_virtual_template_manager.html#ac612e4c24f12edc26be032bd7e887020) (int)  
| Returns the virtual template interface with the specified interface number. [More...](class_virtual_template_manager.html#ac612e4c24f12edc26be032bd7e887020)  
  
int | [getIntCount](class_virtual_template_manager.html#aa2c5483f9ad12a24c27f5b27120ebfb5) ()  
| Returns the number of virtual template interfaces. [More...](class_virtual_template_manager.html#aa2c5483f9ad12a24c27f5b27120ebfb5)  
  
[VirtualTemplateInterface](class_virtual_template_interface.html) | [getIntAt](class_virtual_template_manager.html#a5e8cf954af34f83539dee178695320b2) (int)  
| Returns the virtual template interface at the specified index. [More...](class_virtual_template_manager.html#a5e8cf954af34f83539dee178695320b2)  
  
void | [addVpdnGroupByName](class_virtual_template_manager.html#a08c95aecd6e064525a5a7472a95a29c9) (string)  
| Adds a VPDN group. [More...](class_virtual_template_manager.html#a08c95aecd6e064525a5a7472a95a29c9)  
  
void | [removeVpdnGroupByName](class_virtual_template_manager.html#af4f28c45835511daa8614ff98e79b5d5) (string)  
| Removes the VPDN group with the specified name. [More...](class_virtual_template_manager.html#af4f28c45835511daa8614ff98e79b5d5)  
  
[VpdnGroup](class_vpdn_group.html) | [getVpdnGroupByName](class_virtual_template_manager.html#a24d434723c9409fa681173254909f066) (string)  
| Returns the VPDN group with the specified name. [More...](class_virtual_template_manager.html#a24d434723c9409fa681173254909f066)  
  
int | [getVpdnGroupCount](class_virtual_template_manager.html#a42ff360a014bb06495d4a3d0ea3f340e) ()  
| Returns the number of VPDN groups. [More...](class_virtual_template_manager.html#a42ff360a014bb06495d4a3d0ea3f340e)  
  
[VpdnGroup](class_vpdn_group.html) | [getVpdnGroupAt](class_virtual_template_manager.html#aa70fa6087a545eb00610aa6b462d5c1e) (int)  
| Returns the VPDN group at the specified name. [More...](class_virtual_template_manager.html#aa70fa6087a545eb00610aa6b462d5c1e)  
  
void | [setVpdnEnable](class_virtual_template_manager.html#a4e7fc5e5ac4fda99d71b688b7ee04e95) (bool)  
| Enables or disables VPDN. [More...](class_virtual_template_manager.html#a4e7fc5e5ac4fda99d71b688b7ee04e95)  
  
bool | [isVpdnEnable](class_virtual_template_manager.html#ad8bb83f644f7242c257386a435eb46a7) ()  
| Returns true if VPDN is enabled, otherwise false. [More...](class_virtual_template_manager.html#ad8bb83f644f7242c257386a435eb46a7)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[VirtualTemplateManager](class_virtual_template_manager.html "VirtualTemplateManager manages and manipulates virtual template interfaces for PPPoE.") manages and manipulates virtual template interfaces for PPPoE. 

## Member Function Documentation

## ◆ addVirtualTempIntByNum()

[VirtualTemplateInterface](class_virtual_template_interface.html) VirtualTemplateManager::addVirtualTempIntByNum  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Adds a virtual template interface. 

Parameters
     number,the| interface number for the virtual template interface.   
---|---  
  
## ◆ addVpdnGroupByName()

void VirtualTemplateManager::addVpdnGroupByName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Adds a VPDN group. 

Parameters
     name,the| name for the VPDN group.   
---|---  
  
## ◆ getIntAt()

[VirtualTemplateInterface](class_virtual_template_interface.html) VirtualTemplateManager::getIntAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the virtual template interface at the specified index. 

Parameters
     number,the| index of the virtual template interface of interest.  
---|---  
  
Returns
    [VirtualTemplateInterface](class_virtual_template_interface.html "VirtualTemplateInterface handles and manipulates individual virtual template interfaces for PPPoE."), the [VirtualTemplateInterface](class_virtual_template_interface.html "VirtualTemplateInterface handles and manipulates individual virtual template interfaces for PPPoE.") object at the specified index. 

## ◆ getIntCount()

int VirtualTemplateManager::getIntCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of virtual template interfaces. 

Returns
    int, the number of virtual template interfaces. 

## ◆ getVirtualTempIntByNum()

[VirtualTemplateInterface](class_virtual_template_interface.html) VirtualTemplateManager::getVirtualTempIntByNum  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the virtual template interface with the specified interface number. 

Parameters
     number,the| interface number of the virtual template interface of interest.  
---|---  
  
Returns
    [VirtualTemplateInterface](class_virtual_template_interface.html "VirtualTemplateInterface handles and manipulates individual virtual template interfaces for PPPoE."), the [VirtualTemplateInterface](class_virtual_template_interface.html "VirtualTemplateInterface handles and manipulates individual virtual template interfaces for PPPoE.") object with the specified interface number. 

## ◆ getVpdnGroupAt()

[VpdnGroup](class_vpdn_group.html) VirtualTemplateManager::getVpdnGroupAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the VPDN group at the specified name. 

Parameters
     index,the| index of the VPDN group of interest.  
---|---  
  
Returns
    [VpdnGroup](class_vpdn_group.html "VpdnGroup handles and manipulates VPDN groups."), the [VpdnGroup](class_vpdn_group.html "VpdnGroup handles and manipulates VPDN groups.") object at the specified name. 

## ◆ getVpdnGroupByName()

[VpdnGroup](class_vpdn_group.html) VirtualTemplateManager::getVpdnGroupByName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the VPDN group with the specified name. 

Parameters
     name,the| name of the VPDN group of interest.  
---|---  
  
Returns
    [VpdnGroup](class_vpdn_group.html "VpdnGroup handles and manipulates VPDN groups."), the [VpdnGroup](class_vpdn_group.html "VpdnGroup handles and manipulates VPDN groups.") object with the specified name. 

## ◆ getVpdnGroupCount()

int VirtualTemplateManager::getVpdnGroupCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of VPDN groups. 

Parameters
     int,the| number of VPDN groups.   
---|---  
  
## ◆ isVpdnEnable()

bool VirtualTemplateManager::isVpdnEnable  | ( | | ) |   
---|---|---|---|---  
  
Returns true if VPDN is enabled, otherwise false. 

Returns
    bool, true if VPDN is enabled, otherwise false. 

## ◆ removeVirtualTempByNum()

void VirtualTemplateManager::removeVirtualTempByNum  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Removes the virtual template interface with the specified interface number. 

Parameters
     number,the| interface number of the virtual template interface of interest.   
---|---  
  
## ◆ removeVpdnGroupByName()

void VirtualTemplateManager::removeVpdnGroupByName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes the VPDN group with the specified name. 

Parameters
     name,the| name of the VPDN group of interest.   
---|---  
  
## ◆ setVpdnEnable()

void VirtualTemplateManager::setVpdnEnable  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables VPDN. 

Parameters
     flag,true| to enable VPDN, false to disable it.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CVirtualTemplateManager.pki](_c_virtual_template_manager_8pki.html)


