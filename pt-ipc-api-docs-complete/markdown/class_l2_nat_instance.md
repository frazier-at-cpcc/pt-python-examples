# Cisco Packet Tracer Extensions API: L2NatInstance Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_l2_nat_instance.html

---

##  Public Member Functions  
  
---  
string | [getInstanceName](class_l2_nat_instance.html#a345033656a80b92b0810523ef73a3c38) ()  
| Returns the instance name. [More...](class_l2_nat_instance.html#a345033656a80b92b0810523ef73a3c38)  
  
void | [setInstanceName](class_l2_nat_instance.html#acc6f94df4e1c0842ffee3fb8d78ac50f) (string)  
| Sets the instance name to the given name. [More...](class_l2_nat_instance.html#acc6f94df4e1c0842ffee3fb8d78ac50f)  
  
int | [getInstanceId](class_l2_nat_instance.html#ad5931a9662ca09fe3cabd2e4a8cf3aef) ()  
| Returns the instance ID. [More...](class_l2_nat_instance.html#ad5931a9662ca09fe3cabd2e4a8cf3aef)  
  
[L2NatTable](struct_l2_nat_table.html) | [getNatTable](class_l2_nat_instance.html#a11f3a028c5d4e3c3b91bfd6ed3285426) ()  
| Returns the nat table. [More...](class_l2_nat_instance.html#a11f3a028c5d4e3c3b91bfd6ed3285426)  
  
int | [getStatementsCount](class_l2_nat_instance.html#af9ad416bfbdd2d066871ced02dc64544) ()  
| Returns the statement count. [More...](class_l2_nat_instance.html#af9ad416bfbdd2d066871ced02dc64544)  
  
  
## Member Function Documentation

## ◆ getInstanceId()

int L2NatInstance::getInstanceId  | ( | | ) |   
---|---|---|---|---  
  
Returns the instance ID. 

Returns
    int, value is the instance ID. 

## ◆ getInstanceName()

string L2NatInstance::getInstanceName  | ( | | ) |   
---|---|---|---|---  
  
Returns the instance name. 

Returns
    string, value is the instance name. 

## ◆ getNatTable()

[L2NatTable](struct_l2_nat_table.html) L2NatInstance::getNatTable  | ( | | ) |   
---|---|---|---|---  
  
Returns the nat table. 

Returns
    [L2NatTable](struct_l2_nat_table.html "Data element for L2NatTable."), value is the nat table. 

## ◆ getStatementsCount()

int L2NatInstance::getStatementsCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the statement count. 

Returns
    int, value is the statement count. 

## ◆ setInstanceName()

void L2NatInstance::setInstanceName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the instance name to the given name. 

Parameters
     instanceName,the| name to use for the instance.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CL2NatInstance.pki](_c_l2_nat_instance_8pki.html)


