# Cisco Packet Tracer Extensions API: CAsaObject Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_c_asa_object.html

---

[CAsaObject](class_c_asa_object.html "CAsaObject is the asa object storage manager class that is used to store and retrieve asa object.") is the asa object storage manager class that is used to store and retrieve asa object. [More...](class_c_asa_object.html#details)

##  Public Member Functions  
  
---  
string | [getObjectName](class_c_asa_object.html#a1449ca408e8b72821e3cab7081aeca06) ()  
| Return the asa object name. [More...](class_c_asa_object.html#a1449ca408e8b72821e3cab7081aeca06)  
  
void | [setObjectName](class_c_asa_object.html#ae2ac2250c0351976417ea33aef8d3a65) (string)  
| Return the asa object name. [More...](class_c_asa_object.html#ae2ac2250c0351976417ea33aef8d3a65)  
  
ObjectType | [getObjectType](class_c_asa_object.html#ac53c3f062062bb0c74f4ee0d81eb81e3) ()  
| Return the asa object type type - asa object type, values: eNetwork = 0, eService = 1, eGroupService = 2, eGroupServiceTcp = 3, eGroupServiceUdp = 4, eGroupServiceTcpUdp = 5, eGroupNetwork = 6, eWebvpn = 7. [More...](class_c_asa_object.html#ac53c3f062062bb0c74f4ee0d81eb81e3)  
  
string | [getDescription](class_c_asa_object.html#ac5d0c07e3d16239fcf23bc4968838bf6) ()  
| Return the asa object description. [More...](class_c_asa_object.html#ac5d0c07e3d16239fcf23bc4968838bf6)  
  
void | [setDescription](class_c_asa_object.html#a49b93b66ce9bda732c740de3144fce62) (string)  
| Set the description of the asa object. [More...](class_c_asa_object.html#a49b93b66ce9bda732c740de3144fce62)  
  
bool | [isReferenced](class_c_asa_object.html#a35dc71225985500c8a6f139d7ed078bf) ()  
| Check to see if the asa object is being used by other classes. [More...](class_c_asa_object.html#a35dc71225985500c8a6f139d7ed078bf)  
  
void | [addReferenceObject](class_c_asa_object.html#afafac9b6b8e11e65581583a9ada2759d) (string)  
| Any class that has reference to the asa object calls this function to confirm its association with the object. [More...](class_c_asa_object.html#afafac9b6b8e11e65581583a9ada2759d)  
  
void | [removeReferenceObject](class_c_asa_object.html#a6b35634293e1cd074992463e823e44bf) (string)  
| Any class that has reference to asa object calls this function to release its association with the object. [More...](class_c_asa_object.html#a6b35634293e1cd074992463e823e44bf)  
  
string | [toString](class_c_asa_object.html#ac99ea23a20a01a8c6dba55d58b8a227d) ()  
| Return the string configuration of the asa object. [More...](class_c_asa_object.html#ac99ea23a20a01a8c6dba55d58b8a227d)  
  
string | [getObjectServiceTypeString](class_c_asa_object.html#aeb5156ea154769701f3d02da0c5e424f) ()  
| Return the string configuration for object-group of service type. [More...](class_c_asa_object.html#aeb5156ea154769701f3d02da0c5e424f)  
  
  
## Detailed Description

[CAsaObject](class_c_asa_object.html "CAsaObject is the asa object storage manager class that is used to store and retrieve asa object.") is the asa object storage manager class that is used to store and retrieve asa object. 

## Member Function Documentation

## ◆ addReferenceObject()

void CAsaObject::addReferenceObject  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Any class that has reference to the asa object calls this function to confirm its association with the object. 

Parameters
     reference,a| unique string to identify which object that has association with the asa object   
---|---  
  
## ◆ getDescription()

string CAsaObject::getDescription  | ( | | ) |   
---|---|---|---|---  
  
Return the asa object description. 

Returns
    string, value is the description. 

## ◆ getObjectName()

string CAsaObject::getObjectName  | ( | | ) |   
---|---|---|---|---  
  
Return the asa object name. 

Returns
    string, value is the asa object name. 

## ◆ getObjectServiceTypeString()

string CAsaObject::getObjectServiceTypeString  | ( | | ) |   
---|---|---|---|---  
  
Return the string configuration for object-group of service type. 

Returns
    string, value is the string configuration for object-group of service type. 

## ◆ getObjectType()

ObjectType CAsaObject::getObjectType  | ( | | ) |   
---|---|---|---|---  
  
Return the asa object type type - asa object type, values: eNetwork = 0, eService = 1, eGroupService = 2, eGroupServiceTcp = 3, eGroupServiceUdp = 4, eGroupServiceTcpUdp = 5, eGroupNetwork = 6, eWebvpn = 7. 

Returns
    ObjectType, value is the asa object type.   


## ◆ isReferenced()

bool CAsaObject::isReferenced  | ( | | ) |   
---|---|---|---|---  
  
Check to see if the asa object is being used by other classes. 

Returns
    bool, Value is true if the asa object is being used by other classes, false if not. 

## ◆ removeReferenceObject()

void CAsaObject::removeReferenceObject  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Any class that has reference to asa object calls this function to release its association with the object. 

Parameters
     reference,a| unique string to identify which object that has association with the asa object   
---|---  
  
## ◆ setDescription()

void CAsaObject::setDescription  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Set the description of the asa object. 

Parameters
     description,value| is the description to use for the object.   
---|---  
  
## ◆ setObjectName()

void CAsaObject::setObjectName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Return the asa object name. 

Parameters
     objectName,value| is the name to give the object.   
---|---  
  
## ◆ toString()

string CAsaObject::toString  | ( | | ) |   
---|---|---|---|---  
  
Return the string configuration of the asa object. 

Returns
    string, value is the string configuration of the asa object. 

* * *

The documentation for this class was generated from the following file:

  * [CAsaObject.pki](_c_asa_object_8pki.html)


