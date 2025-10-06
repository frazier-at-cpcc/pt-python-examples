# Cisco Packet Tracer Extensions API: AhHeader Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_ah_header.html

---

Authentication [Header](struct_header.html "Header structure.") structure. [More...](struct_ah_header.html#details)

##  Public Attributes  
  
---  
int | [nextHeader](struct_ah_header.html#a8b83c564d1693fba51ae673a8a809147)  
int | [payloadLength](struct_ah_header.html#aeb4538d7909caf36379fea8d6ffaae92)  
byte | [reserved](struct_ah_header.html#a1f332c30472aab393931a3ebaedb17e3)  
int | [spi](struct_ah_header.html#a17b76f8698383a4a8e9226d658b2737d)  
int | [sequenceNumber](struct_ah_header.html#a0427df6afb5c8d9f9bfd9a24bb3f3906)  
string | [authenticationData](struct_ah_header.html#a0aca5a64ac67b0bcbd06ca1549d9f3c3)  
AhAuth | [m_eAhAuth](struct_ah_header.html#af82604aa0593131c3f21dd0ed1ef6ac5)  
int | [icv0](struct_ah_header.html#a60235db250b9c0328d1d41d30b74881a)  
int | [icv1](struct_ah_header.html#a60536e3c9cc2c734750aa6eecd1526aa)  
int | [icv2](struct_ah_header.html#aa657776bceed788fc3ecb5c65d70a3d2)  
Public Attributes inherited from [Header](struct_header.html)  
[Pdu](struct_pdu.html) | [payload](struct_header.html#a07ee8693faef1e16c65765b5bcdc366d)  
  
## Detailed Description

Authentication [Header](struct_header.html "Header structure.") structure. 

## Member Data Documentation

## ◆ authenticationData

string AhHeader::authenticationData  
---  
  
## ◆ icv0

int AhHeader::icv0  
---  
  
## ◆ icv1

int AhHeader::icv1  
---  
  
## ◆ icv2

int AhHeader::icv2  
---  
  
## ◆ m_eAhAuth

AhAuth AhHeader::m_eAhAuth  
---  
  
## ◆ nextHeader

int AhHeader::nextHeader  
---  
  
## ◆ payloadLength

int AhHeader::payloadLength  
---  
  
## ◆ reserved

byte AhHeader::reserved  
---  
  
## ◆ sequenceNumber

int AhHeader::sequenceNumber  
---  
  
## ◆ spi

int AhHeader::spi  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [CAhHeader.pki](_c_ah_header_8pki.html)


