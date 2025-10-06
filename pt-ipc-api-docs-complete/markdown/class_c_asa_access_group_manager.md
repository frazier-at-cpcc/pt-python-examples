# Cisco Packet Tracer Extensions API: CAsaAccessGroupManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_c_asa_access_group_manager.html

---

[CAsaAccessGroupManager](class_c_asa_access_group_manager.html "CAsaAccessGroupManager is the asa object storage manager class that is used to store and retrieve asa...") is the asa object storage manager class that is used to store and retrieve asa object. [More...](class_c_asa_access_group_manager.html#details)

##  Public Member Functions  
  
---  
bool | [deleteAccessGroupWithNameIf](class_c_asa_access_group_manager.html#a81a1f065c206481f6fc22f16ffb1a2cd) (string)  
| delete the access-group that associates with the specified nameIf. [More...](class_c_asa_access_group_manager.html#a81a1f065c206481f6fc22f16ffb1a2cd)  
  
bool | [deleteAccessGroup](class_c_asa_access_group_manager.html#ac1b8fb55ac0bb1ab1ed35272051492fd) (Direction, string, string)  
| delete the access-group that associates with the specified nameIf, aclId and in a certain direction. [More...](class_c_asa_access_group_manager.html#ac1b8fb55ac0bb1ab1ed35272051492fd)  
  
bool | [addAccessGroup](class_c_asa_access_group_manager.html#a85a4182a8fc09a093e96fd42d548327e) (Direction, string, string)  
| add a new access-group. [More...](class_c_asa_access_group_manager.html#a85a4182a8fc09a093e96fd42d548327e)  
  
[AsaAccessGroup](class_asa_access_group.html) | [getAccessGroupAt](class_c_asa_access_group_manager.html#a0167fcdf9a9e468b2c670a7afb6b20ca) (int)  
| Return the access-group at a specified index. [More...](class_c_asa_access_group_manager.html#a0167fcdf9a9e468b2c670a7afb6b20ca)  
  
int | [getAccessGroupCount](class_c_asa_access_group_manager.html#a9ab4d106c1184f100edc6dc3d8f0ae7e) ()  
| Return the number of access-group configured. [More...](class_c_asa_access_group_manager.html#a9ab4d106c1184f100edc6dc3d8f0ae7e)  
  
  
## Detailed Description

[CAsaAccessGroupManager](class_c_asa_access_group_manager.html "CAsaAccessGroupManager is the asa object storage manager class that is used to store and retrieve asa...") is the asa object storage manager class that is used to store and retrieve asa object. 

## Member Function Documentation

## ◆ addAccessGroup()

bool CAsaAccessGroupManager::addAccessGroup  | ( | Direction  | ,   
---|---|---|---  
|  | string  | ,   
|  | string  |   
| ) | |   
  
add a new access-group. 

Parameters
     direction,the| traffic direction eIn =0, eOut, eGlobal   
---|---  
nameIf,nameIf| of the interface that has the acl applied on   
aclId,acl| id of the acl.  
  
Returns
    bool, value is true if the add was successful, false if not. 

## ◆ deleteAccessGroup()

bool CAsaAccessGroupManager::deleteAccessGroup  | ( | Direction  | ,   
---|---|---|---  
|  | string  | ,   
|  | string  |   
| ) | |   
  
delete the access-group that associates with the specified nameIf, aclId and in a certain direction. 

Parameters
     direction,the| traffic direction   
---|---  
nameIf,nameIf| of the interface that has the acl applied on   
aclId,acl| id of the acl   
  
## ◆ deleteAccessGroupWithNameIf()

bool CAsaAccessGroupManager::deleteAccessGroupWithNameIf  | ( | string  | | ) |   
---|---|---|---|---|---  
  
delete the access-group that associates with the specified nameIf. 

Parameters
     nameIf,the| nameIf of the interface that has access-list applied on.   
---|---  
  
## ◆ getAccessGroupAt()

[AsaAccessGroup](class_asa_access_group.html) CAsaAccessGroupManager::getAccessGroupAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Return the access-group at a specified index. 

Parameters
     index,index| of the access group to get. Range (0, [getAccessGroupCount()](class_c_asa_access_group_manager.html#a9ab4d106c1184f100edc6dc3d8f0ae7e "Return the number of access-group configured.")).   
---|---  
  
## ◆ getAccessGroupCount()

int CAsaAccessGroupManager::getAccessGroupCount  | ( | | ) |   
---|---|---|---|---  
  
Return the number of access-group configured. 

Returns
    int, value is how many access groups there are total. 

* * *

The documentation for this class was generated from the following file:

  * [CAsaAccessGrpManager.pki](_c_asa_access_grp_manager_8pki.html)


