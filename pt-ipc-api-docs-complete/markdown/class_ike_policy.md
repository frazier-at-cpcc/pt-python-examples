# Cisco Packet Tracer Extensions API: IkePolicy Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_ike_policy.html

---

[IkePolicy](class_ike_policy.html "IkePolicy handles and manipulates IKE policies.") handles and manipulates IKE policies. [More...](class_ike_policy.html#details)

##  Public Member Functions  
  
---  
void | [setPriorityNum](class_ike_policy.html#a0523fc004ab62c8f8814a7dfb2ad6305) (int)  
| Sets the priority value. [More...](class_ike_policy.html#a0523fc004ab62c8f8814a7dfb2ad6305)  
  
int | [getPriorityNum](class_ike_policy.html#a960b86a8fcfb35031504f4198a28e4a3) ()  
| Returns the priority value. [More...](class_ike_policy.html#a960b86a8fcfb35031504f4198a28e4a3)  
  
int | [getEncryKeyBits](class_ike_policy.html#a35eab5461d546e179268f24280a2f914) ()  
| Returns the number of bits in the encryption key. [More...](class_ike_policy.html#a35eab5461d546e179268f24280a2f914)  
  
void | [setLifetime](class_ike_policy.html#a7556374cdc494a09d30e7d66a20be5f8) (int)  
| Sets the lifetime for the IKE policy. [More...](class_ike_policy.html#a7556374cdc494a09d30e7d66a20be5f8)  
  
int | [getLifetime](class_ike_policy.html#a0fb60473b8eb63ad0e673721ac88730b) ()  
| Returns the lifetime value for the IKE policy. [More...](class_ike_policy.html#a0fb60473b8eb63ad0e673721ac88730b)  
  
  
## Detailed Description

[IkePolicy](class_ike_policy.html "IkePolicy handles and manipulates IKE policies.") handles and manipulates IKE policies. 

## Member Function Documentation

## ◆ getEncryKeyBits()

int IkePolicy::getEncryKeyBits  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of bits in the encryption key. 

Returns
    int, the number of bits in the encryption key. 

## ◆ getLifetime()

int IkePolicy::getLifetime  | ( | | ) |   
---|---|---|---|---  
  
Returns the lifetime value for the IKE policy. 

Returns
    int, the lifetime value for the IKE policy. 

## ◆ getPriorityNum()

int IkePolicy::getPriorityNum  | ( | | ) |   
---|---|---|---|---  
  
Returns the priority value. 

Returns
    int, the priority value. 

## ◆ setLifetime()

void IkePolicy::setLifetime  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the lifetime for the IKE policy. 

Parameters
     lifetime,the| lifetime value.   
---|---  
  
## ◆ setPriorityNum()

void IkePolicy::setPriorityNum  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the priority value. 

Parameters
     number,the| priority value.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CIkePolicy.pki](_c_ike_policy_8pki.html)


