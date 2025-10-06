# Cisco Packet Tracer Extensions API: NeighborMessage Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_neighbor_message.html

---

Neighbor message structure. [More...](struct_neighbor_message.html#details)

##  Public Attributes  
  
---  
bool | [isRouter](struct_neighbor_message.html#acc78d0a167c7aceb49397cb9b099937a)  
bool | [isSolicited](struct_neighbor_message.html#a76256e35fcae2bd0caa6ac146b3a9bc1)  
bool | [isOverride](struct_neighbor_message.html#a5b3947c7876ee16c2b7b14a16ed60df4)  
ipv6 | [targetAddress](struct_neighbor_message.html#aae953485d694a01d940cfdb417ab8147)  
Public Attributes inherited from [NdMessage](struct_nd_message.html)  
vector< [NdOption](struct_nd_option.html) > | [options](struct_nd_message.html#ac5a421f6f344db491ddaa9cd880790db)  
Public Attributes inherited from [Icmpv6Message](struct_icmpv6_message.html)  
Icmpv6MessageType | [type](struct_icmpv6_message.html#ac2e04a595d1a58e650b611f66cb27fd4)  
byte | [code](struct_icmpv6_message.html#a5287359ba10784ecd87d9904fba548f0)  
short | [checksum](struct_icmpv6_message.html#a0989e68c86c7e8449086fba804af6de2)  
Public Attributes inherited from [Header](struct_header.html)  
[Pdu](struct_pdu.html) | [payload](struct_header.html#a07ee8693faef1e16c65765b5bcdc366d)  
  
## Detailed Description

Neighbor message structure. 

## Member Data Documentation

## ◆ isOverride

bool NeighborMessage::isOverride  
---  
  
## ◆ isRouter

bool NeighborMessage::isRouter  
---  
  
## ◆ isSolicited

bool NeighborMessage::isSolicited  
---  
  
## ◆ targetAddress

ipv6 NeighborMessage::targetAddress  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [CNeighborMessage.pki](_c_neighbor_message_8pki.html)


