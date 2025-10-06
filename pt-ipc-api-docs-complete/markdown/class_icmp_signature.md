# Cisco Packet Tracer Extensions API: IcmpSignature Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_icmp_signature.html

---

[IcmpSignature](class_icmp_signature.html "IcmpSignature handles and manipulates ICMP signatures.") handles and manipulates ICMP signatures. [More...](class_icmp_signature.html#details)

##  Public Member Functions  
  
---  
int | [getSigId](class_icmp_signature.html#a9f1a81b3f7152cd5d7138f785efaac3f) ()  
| Returns the signature ID. [More...](class_icmp_signature.html#a9f1a81b3f7152cd5d7138f785efaac3f)  
  
int | [getSubId](class_icmp_signature.html#ab01799c66194e6eed904d66a1e5241a4) ()  
| Returns the signature sub-id. [More...](class_icmp_signature.html#ab01799c66194e6eed904d66a1e5241a4)  
  
Bool | [getRetired](class_icmp_signature.html#ad4ee6382098ffcd10feb4391787ec1af) ()  
| Returns the retired value for the ICMP signature. [More...](class_icmp_signature.html#ad4ee6382098ffcd10feb4391787ec1af)  
  
Bool | [getEnabled](class_icmp_signature.html#a507bae27e9571f33ddb1fbdabacd74b0) ()  
| Returns the enabled value. [More...](class_icmp_signature.html#a507bae27e9571f33ddb1fbdabacd74b0)  
  
int | [getEventActionCount](class_icmp_signature.html#a88bb03b5795ba92dba6e373d4d7d0111) ()  
| Returns the event action count. [More...](class_icmp_signature.html#a88bb03b5795ba92dba6e373d4d7d0111)  
  
SigEventAction | [getEventActionAt](class_icmp_signature.html#ab0ec75119230dfd178f36565d4a73158) (int)  
| Returns the event action at the specified index. [More...](class_icmp_signature.html#ab0ec75119230dfd178f36565d4a73158)  
  
void | [setRetired](class_icmp_signature.html#a7c722bbbdd782f88b71cff53f0fc3833) (Bool)  
| Sets the retired value. [More...](class_icmp_signature.html#a7c722bbbdd782f88b71cff53f0fc3833)  
  
void | [setEnabled](class_icmp_signature.html#a45bc3ed7aa38ed816711c23e078d5df9) (Bool)  
| Sets the enabled value. [More...](class_icmp_signature.html#a45bc3ed7aa38ed816711c23e078d5df9)  
  
void | [setEventAction](class_icmp_signature.html#a88e41ef5d113710f142c155897ba81e9) (SigEventAction)  
| Sets the event action for the ICMP signature. [More...](class_icmp_signature.html#a88e41ef5d113710f142c155897ba81e9)  
  
  
## Detailed Description

[IcmpSignature](class_icmp_signature.html "IcmpSignature handles and manipulates ICMP signatures.") handles and manipulates ICMP signatures. 

## Member Function Documentation

## ◆ getEnabled()

Bool IcmpSignature::getEnabled  | ( | | ) |   
---|---|---|---|---  
  
Returns the enabled value. 

Returns
    enum<Bool>, the enabled value. Enabled values: eDefault = 0, eFalse = 1, eTrue = 2 

## ◆ getEventActionAt()

SigEventAction IcmpSignature::getEventActionAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the event action at the specified index. 

Parameters
     index,the| index of the event action of interest.  
---|---  
  
Returns
    enum<SigEventAction>, the event action at the specified index. Event actions: eInvalid = -1, eProduceAlert = 0, eDenyPacketInline = 1, eDenyAttackerInline = 2, eDenyConnInline = 3, eRstTCPConn = 4, 

## ◆ getEventActionCount()

int IcmpSignature::getEventActionCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the event action count. 

Returns
    int, the event action count. 

## ◆ getRetired()

Bool IcmpSignature::getRetired  | ( | | ) |   
---|---|---|---|---  
  
Returns the retired value for the ICMP signature. 

Returns
    enum<Bool>, the retired value. Retired values: eDefault = 0, eFalse = 1, eTrue = 2 

## ◆ getSigId()

int IcmpSignature::getSigId  | ( | | ) |   
---|---|---|---|---  
  
Returns the signature ID. 

Returns
    int, the signature ID. 

## ◆ getSubId()

int IcmpSignature::getSubId  | ( | | ) |   
---|---|---|---|---  
  
Returns the signature sub-id. 

Returns
    int, the signature sub-id. 

## ◆ setEnabled()

void IcmpSignature::setEnabled  | ( | Bool  | | ) |   
---|---|---|---|---|---  
  
Sets the enabled value. 

Parameters
     enum<Bool>,the| enable value. Enabled values: eDefault = 0, eFalse = 1, eTrue = 2   
---|---  
  
## ◆ setEventAction()

void IcmpSignature::setEventAction  | ( | SigEventAction  | | ) |   
---|---|---|---|---|---  
  
Sets the event action for the ICMP signature. 

Parameters
     eAction,the| event action at the specified index. Event actions: eInvalid = -1, eProduceAlert = 0, eDenyPacketInline = 1, eDenyAttackerInline = 2, eDenyConnInline = 3, eRstTCPConn = 4,   
---|---  
  
## ◆ setRetired()

void IcmpSignature::setRetired  | ( | Bool  | | ) |   
---|---|---|---|---|---  
  
Sets the retired value. 

Parameters
     enum<Bool>,the| retired value. Retired values: eDefault = 0, eFalse = 1, eTrue = 2   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CIcmpSignature.pki](_c_icmp_signature_8pki.html)


