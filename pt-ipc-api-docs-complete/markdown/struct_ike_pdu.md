# Cisco Packet Tracer Extensions API: IkePdu Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_ike_pdu.html

---

IKE PDU structure. [More...](struct_ike_pdu.html#details)

##  Public Attributes  
  
---  
long | [initCookie](struct_ike_pdu.html#a54697120fc97efb25cc7c5acb69ce26e)  
long | [responseCookie](struct_ike_pdu.html#a1b4a19f4a9e3bc33fe08ec104378d186)  
byte | [nextPayload](struct_ike_pdu.html#a9b2efd3de4c2d4cc85d1b29003643486)  
byte | [versionNumber](struct_ike_pdu.html#ae0123ef48cefd87e6c550d0309fab627)  
byte | [exchangeType](struct_ike_pdu.html#aec7aca9a687cde012ea0a6f410e7b36b)  
byte | [flag](struct_ike_pdu.html#af866237b6fa4c00738a33acd840750dc)  
int | [msgId](struct_ike_pdu.html#a09604e7712822b97e5ed8715b3bf1693)  
int | [msgLength](struct_ike_pdu.html#af16513cce3ac5f29a685db3a5837c3bb)  
vector< [IkePayload](struct_ike_payload.html) > | [payloadList](struct_ike_pdu.html#adf4880957bb2ab0b4af7d812f07d88b4)  
string | [data](struct_ike_pdu.html#ad2f1337231cc26f902379a3f9a5b75da)  
  
## Detailed Description

IKE PDU structure. 

## Member Data Documentation

## ◆ data

string IkePdu::data  
---  
  
## ◆ exchangeType

byte IkePdu::exchangeType  
---  
  
## ◆ flag

byte IkePdu::flag  
---  
  
## ◆ initCookie

long IkePdu::initCookie  
---  
  
## ◆ msgId

int IkePdu::msgId  
---  
  
## ◆ msgLength

int IkePdu::msgLength  
---  
  
## ◆ nextPayload

byte IkePdu::nextPayload  
---  
  
## ◆ payloadList

vector<[IkePayload](struct_ike_payload.html)> IkePdu::payloadList  
---  
  
## ◆ responseCookie

long IkePdu::responseCookie  
---  
  
## ◆ versionNumber

byte IkePdu::versionNumber  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [CIkePdu.pki](_c_ike_pdu_8pki.html)


