# Cisco Packet Tracer Extensions API: CAsaObjectManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_c_asa_object_manager.html

---

[CAsaObjectManager](class_c_asa_object_manager.html "CAsaObjectManager is the asa object storage manager class that is used to store and retrieve asa obje...") is the asa object storage manager class that is used to store and retrieve asa object. [More...](class_c_asa_object_manager.html#details)

##  Public Member Functions  
  
---  
[CAsaObject](class_c_asa_object.html) | [getObjectByName](class_c_asa_object_manager.html#a4acd4ac62f39d927c658e64191ab56dd) (string)  
| Returns the asa object based on name. [More...](class_c_asa_object_manager.html#a4acd4ac62f39d927c658e64191ab56dd)  
  
[CAsaObject](class_c_asa_object.html) | [createObject](class_c_asa_object_manager.html#a87ec7f71f5a6de45060773bc7eed8cda) (ObjectType, string)  
| Creates an asa object. [More...](class_c_asa_object_manager.html#a87ec7f71f5a6de45060773bc7eed8cda)  
  
void | [removeObjectByName](class_c_asa_object_manager.html#a10d8c22b0b529b2c19d993eb27ca6ef5) (string)  
| Remove the asa object based on name. [More...](class_c_asa_object_manager.html#a10d8c22b0b529b2c19d993eb27ca6ef5)  
  
int | [getNatObjectCount](class_c_asa_object_manager.html#aa48387fe5fcf94a64f28dd34135e4ac9) ()  
| Get Number of Nat Objects. [More...](class_c_asa_object_manager.html#aa48387fe5fcf94a64f28dd34135e4ac9)  
  
int | [getMostUse](class_c_asa_object_manager.html#a73af8d107d57196ddde20c7b70a12e43) ()  
| Get the number of static and dynamic nat entries have been used. [More...](class_c_asa_object_manager.html#a73af8d107d57196ddde20c7b70a12e43)  
  
void | [setMostUse](class_c_asa_object_manager.html#a110fdf7b6f731fe19f2837e2c98c6452) (int)  
| Set the number of static and dynamic nat entries have been used. [More...](class_c_asa_object_manager.html#a110fdf7b6f731fe19f2837e2c98c6452)  
  
int | [getObjectCount](class_c_asa_object_manager.html#ae1c8bf30359d236fa92555449d1767b6) ()  
| Get the number of asa objects. [More...](class_c_asa_object_manager.html#ae1c8bf30359d236fa92555449d1767b6)  
  
[CAsaObject](class_c_asa_object.html) | [getObjectAt](class_c_asa_object_manager.html#a5712020aa0d37be44296456a43c7f9a3) (int)  
| Get the Asa object at a specified index. [More...](class_c_asa_object_manager.html#a5712020aa0d37be44296456a43c7f9a3)  
  
void | [nameifChanged](class_c_asa_object_manager.html#ab23f970a7e7e5b4b6748efa7a66bd7a3) (string, string)  
| This function updates the asa object that has reference to interface nameIf. [More...](class_c_asa_object_manager.html#ab23f970a7e7e5b4b6748efa7a66bd7a3)  
  
  
## Detailed Description

[CAsaObjectManager](class_c_asa_object_manager.html "CAsaObjectManager is the asa object storage manager class that is used to store and retrieve asa obje...") is the asa object storage manager class that is used to store and retrieve asa object. 

## Member Function Documentation

## ◆ createObject()

[CAsaObject](class_c_asa_object.html) CAsaObjectManager::createObject  | ( | ObjectType  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Creates an asa object. 

Parameters
     objName,object| name   
---|---  
type,asa| object type, values: eNetwork = 0, eService = 1, eGroupService = 2, eGroupServiceTcp = 3, eGroupServiceUdp = 4, eGroupServiceTcpUdp = 5, eGroupNetwork = 6, eWebvpn = 7  
  
Returns
    [CAsaObject](class_c_asa_object.html "CAsaObject is the asa object storage manager class that is used to store and retrieve asa object."), value is the asa object that is newly created. 

## ◆ getMostUse()

int CAsaObjectManager::getMostUse  | ( | | ) |   
---|---|---|---|---  
  
Get the number of static and dynamic nat entries have been used. 

Returns
    int, value is the number of static and dynamic nat entries have been used 

## ◆ getNatObjectCount()

int CAsaObjectManager::getNatObjectCount  | ( | | ) |   
---|---|---|---|---  
  
Get Number of Nat Objects. 

Returns
    int, value is the number of nat objects that are stored. 

## ◆ getObjectAt()

[CAsaObject](class_c_asa_object.html) CAsaObjectManager::getObjectAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Get the Asa object at a specified index. 

Parameters
     index,index| of the asa object to get. Range is (0, [getObjectCount()](class_c_asa_object_manager.html#ae1c8bf30359d236fa92555449d1767b6 "Get the number of asa objects.")).  
---|---  
  
Returns
    value is the Asa object at the specified index. 

## ◆ getObjectByName()

[CAsaObject](class_c_asa_object.html) CAsaObjectManager::getObjectByName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the asa object based on name. 

Parameters
     objName,object| name.  
---|---  
  
Returns
    [CAsaObject](class_c_asa_object.html "CAsaObject is the asa object storage manager class that is used to store and retrieve asa object."), value is the asa object based on name. 

## ◆ getObjectCount()

int CAsaObjectManager::getObjectCount  | ( | | ) |   
---|---|---|---|---  
  
Get the number of asa objects. 

Returns
    int, value is the number of asa objects. 

## ◆ nameifChanged()

void CAsaObjectManager::nameifChanged  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
This function updates the asa object that has reference to interface nameIf. 

Parameters
     newName,the| interface new nameIf   
---|---  
oldName,the| interface old nameIf   
  
## ◆ removeObjectByName()

void CAsaObjectManager::removeObjectByName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Remove the asa object based on name. 

Parameters
     objName,object| name to search with.   
---|---  
  
## ◆ setMostUse()

void CAsaObjectManager::setMostUse  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Set the number of static and dynamic nat entries have been used. 

Parameters
     mostUse,the| number of static and dynamic nat entries have been used   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CAsaObjectManager.pki](_c_asa_object_manager_8pki.html)


