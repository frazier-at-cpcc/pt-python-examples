# Cisco Packet Tracer Extensions API: AsaAccessGroup Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_asa_access_group.html

---

##  Public Member Functions  
  
---  
Direction | [getDirection](class_asa_access_group.html#aa757c6bbb3a3b51f336abd8380f675d0) ()  
| Return the direction in which the acl is applied on the interface. [More...](class_asa_access_group.html#aa757c6bbb3a3b51f336abd8380f675d0)  
  
string | [getNameIf](class_asa_access_group.html#a05fc83ade9974bde09e3bdda0126da7f) ()  
| Return the nameIf of the interface the acl is applied on. [More...](class_asa_access_group.html#a05fc83ade9974bde09e3bdda0126da7f)  
  
string | [getAclId](class_asa_access_group.html#a4146f4e3be2f779439517999a8179c20) ()  
| Return the acl id that the access-group is associated with. [More...](class_asa_access_group.html#a4146f4e3be2f779439517999a8179c20)  
  
void | [setDirection](class_asa_access_group.html#a9c0270f39a259f64d94253eb824c442c) (Direction)  
| Set the direction of the acl. [More...](class_asa_access_group.html#a9c0270f39a259f64d94253eb824c442c)  
  
void | [setNameIf](class_asa_access_group.html#a42677531006ffae24c62ff407965ae57) (string)  
| Set the nameIf that the access-list will be applied on. [More...](class_asa_access_group.html#a42677531006ffae24c62ff407965ae57)  
  
void | [setAclId](class_asa_access_group.html#a655be6aa99de6b20fd7f395594d35001) (string)  
| Set the access-list id to be used to apply on the interface. [More...](class_asa_access_group.html#a655be6aa99de6b20fd7f395594d35001)  
  
string | [toString](class_asa_access_group.html#a1907728292a65db08f377a2767c2d92b) ()  
| Return the string configuration of the access-group. [More...](class_asa_access_group.html#a1907728292a65db08f377a2767c2d92b)  
  
  
## Member Function Documentation

## ◆ getAclId()

string AsaAccessGroup::getAclId  | ( | | ) |   
---|---|---|---|---  
  
Return the acl id that the access-group is associated with. 

## ◆ getDirection()

Direction AsaAccessGroup::getDirection  | ( | | ) |   
---|---|---|---|---  
  
Return the direction in which the acl is applied on the interface. 

## ◆ getNameIf()

string AsaAccessGroup::getNameIf  | ( | | ) |   
---|---|---|---|---  
  
Return the nameIf of the interface the acl is applied on. 

## ◆ setAclId()

void AsaAccessGroup::setAclId  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Set the access-list id to be used to apply on the interface. 

## ◆ setDirection()

void AsaAccessGroup::setDirection  | ( | Direction  | | ) |   
---|---|---|---|---|---  
  
Set the direction of the acl. 

Parameters
     direction| eIn =0, eOut, eGlobal   
---|---  
  
## ◆ setNameIf()

void AsaAccessGroup::setNameIf  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Set the nameIf that the access-list will be applied on. 

## ◆ toString()

string AsaAccessGroup::toString  | ( | | ) |   
---|---|---|---|---  
  
Return the string configuration of the access-group. 

* * *

The documentation for this class was generated from the following file:

  * [CAsaAccessGrp.pki](_c_asa_access_grp_8pki.html)


