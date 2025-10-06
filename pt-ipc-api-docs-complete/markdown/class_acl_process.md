# Cisco Packet Tracer Extensions API: AclProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_acl_process.html

---

[AclProcess](class_acl_process.html "AclProcess is the process that handles ACLs.") is the process that handles ACLs. [More...](class_acl_process.html#details)

##  Public Member Functions  
  
---  
void | [addAcl](class_acl_process.html#aac8cb9ef19858b92145dcaf87db9a0dc) (string)  
| Adds the [Acl](class_acl.html "Acl holds and manipulates AclStatements.") object with the specified ID to this process. [More...](class_acl_process.html#aac8cb9ef19858b92145dcaf87db9a0dc)  
  
void | [removeAcl](class_acl_process.html#ad02eeb3ab89f89dc21eb50f8d65b0184) (string)  
| Removes the [Acl](class_acl.html "Acl holds and manipulates AclStatements.") object with the specified ID from this process. [More...](class_acl_process.html#ad02eeb3ab89f89dc21eb50f8d65b0184)  
  
[Acl](class_acl.html) | [getAcl](class_acl_process.html#a7fd128030591057648c6c0846c172678) (string)  
| Returns the [Acl](class_acl.html "Acl holds and manipulates AclStatements.") object from the specified ID. [More...](class_acl_process.html#a7fd128030591057648c6c0846c172678)  
  
[Acl](class_acl.html) | [getAclAt](class_acl_process.html#af432b6cec55535352559f2714ef0da3e) (int)  
| Returns the [Acl](class_acl.html "Acl holds and manipulates AclStatements.") object at the specified index. [More...](class_acl_process.html#af432b6cec55535352559f2714ef0da3e)  
  
int | [getAclCount](class_acl_process.html#ac037dfdef6b10032718b0d57eb6a766b) ()  
| Returns the number of [Acl](class_acl.html "Acl holds and manipulates AclStatements.") objects in this process. [More...](class_acl_process.html#ac037dfdef6b10032718b0d57eb6a766b)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[AclProcess](class_acl_process.html "AclProcess is the process that handles ACLs.") is the process that handles ACLs. 

## Member Function Documentation

## ◆ addAcl()

void AclProcess::addAcl  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Adds the [Acl](class_acl.html "Acl holds and manipulates AclStatements.") object with the specified ID to this process. 

Parameters
     aclID,the| ID of the [Acl](class_acl.html "Acl holds and manipulates AclStatements.") object to add.   
---|---  
  
## ◆ getAcl()

[Acl](class_acl.html) AclProcess::getAcl  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the [Acl](class_acl.html "Acl holds and manipulates AclStatements.") object from the specified ID. 

Parameters
     aclID,the| ID of the [Acl](class_acl.html "Acl holds and manipulates AclStatements.") object.  
---|---  
  
Returns
    [Acl](class_acl.html "Acl holds and manipulates AclStatements."), the [Acl](class_acl.html "Acl holds and manipulates AclStatements.") object associated with the specified ID. 

## ◆ getAclAt()

[Acl](class_acl.html) AclProcess::getAclAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the [Acl](class_acl.html "Acl holds and manipulates AclStatements.") object at the specified index. 

Parameters
     index,the| index of [Acl](class_acl.html "Acl holds and manipulates AclStatements.") object.  
---|---  
  
Returns
    [Acl](class_acl.html "Acl holds and manipulates AclStatements."), the [Acl](class_acl.html "Acl holds and manipulates AclStatements.") object associated with the specified index. 

## ◆ getAclCount()

int AclProcess::getAclCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of [Acl](class_acl.html "Acl holds and manipulates AclStatements.") objects in this process. 

Returns
    int, the number of [Acl](class_acl.html "Acl holds and manipulates AclStatements.") objects in this process. 

## ◆ removeAcl()

void AclProcess::removeAcl  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes the [Acl](class_acl.html "Acl holds and manipulates AclStatements.") object with the specified ID from this process. 

Parameters
     aclID,the| ID of the [Acl](class_acl.html "Acl holds and manipulates AclStatements.") object to remove.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CAclProcess.pki](_c_acl_process_8pki.html)


