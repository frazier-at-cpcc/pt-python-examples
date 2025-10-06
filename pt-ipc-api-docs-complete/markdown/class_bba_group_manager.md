# Cisco Packet Tracer Extensions API: BbaGroupManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_bba_group_manager.html

---

[BbaGroupManager](class_bba_group_manager.html "BbaGroupManager manages and manipulates virtual template interfaces for PPPoE.") manages and manipulates virtual template interfaces for PPPoE. [More...](class_bba_group_manager.html#details)

##  Public Member Functions  
  
---  
void | [addBbaGroupByName](class_bba_group_manager.html#ab61c96b0aa35138f450a32f32a721aa9) (string)  
| Adds a BBA group. [More...](class_bba_group_manager.html#ab61c96b0aa35138f450a32f32a721aa9)  
  
void | [removeBbaGroupByName](class_bba_group_manager.html#a804c4aaa449758155e05e896d268df8b) (string)  
| Removes the BBA group with the specified name. [More...](class_bba_group_manager.html#a804c4aaa449758155e05e896d268df8b)  
  
[BbaGroup](class_bba_group.html) | [getBbaGroupByName](class_bba_group_manager.html#a4271f8e5a20274c2e40a83823109eded) (string)  
| Returns the BBA group with the specified name. [More...](class_bba_group_manager.html#a4271f8e5a20274c2e40a83823109eded)  
  
int | [getBbaGroupCount](class_bba_group_manager.html#a009de24ed36cf035ab2f1c394be42e7f) ()  
| Returns the number of BBA groups. [More...](class_bba_group_manager.html#a009de24ed36cf035ab2f1c394be42e7f)  
  
[BbaGroup](class_bba_group.html) | [getBbaGroupAt](class_bba_group_manager.html#aa1a3253154e7f88dcc5d08e7cefe0d0c) (int)  
| Returns the BBA group at the specified name. [More...](class_bba_group_manager.html#aa1a3253154e7f88dcc5d08e7cefe0d0c)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[BbaGroupManager](class_bba_group_manager.html "BbaGroupManager manages and manipulates virtual template interfaces for PPPoE.") manages and manipulates virtual template interfaces for PPPoE. 

## Member Function Documentation

## ◆ addBbaGroupByName()

void BbaGroupManager::addBbaGroupByName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Adds a BBA group. 

Parameters
     name,the| name for the BBA group.   
---|---  
  
## ◆ getBbaGroupAt()

[BbaGroup](class_bba_group.html) BbaGroupManager::getBbaGroupAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the BBA group at the specified name. 

Parameters
     index,the| index of the BBA group of interest.  
---|---  
  
Returns
    [BbaGroup](class_bba_group.html "BbaGroup handles and manipulates Bba groups."), the [BbaGroup](class_bba_group.html "BbaGroup handles and manipulates Bba groups.") object at the specified name. 

## ◆ getBbaGroupByName()

[BbaGroup](class_bba_group.html) BbaGroupManager::getBbaGroupByName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the BBA group with the specified name. 

Parameters
     name,the| name of the BBA group of interest.  
---|---  
  
Returns
    [BbaGroup](class_bba_group.html "BbaGroup handles and manipulates Bba groups."), the [BbaGroup](class_bba_group.html "BbaGroup handles and manipulates Bba groups.") object with the specified name. 

## ◆ getBbaGroupCount()

int BbaGroupManager::getBbaGroupCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of BBA groups. 

Parameters
     int,the| number of BBA groups.   
---|---  
  
## ◆ removeBbaGroupByName()

void BbaGroupManager::removeBbaGroupByName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes the BBA group with the specified name. 

Parameters
     name,the| name of the BBA group of interest.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CBbaGroupManager.pki](_c_bba_group_manager_8pki.html)


