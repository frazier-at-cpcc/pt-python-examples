# Cisco Packet Tracer Extensions API: RouterAdvertisementMessage Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_router_advertisement_message.html

---

[Router](class_router.html "Router is the base class for all router devices.") advertisement message structure. [More...](struct_router_advertisement_message.html#details)

##  Public Attributes  
  
---  
byte | [curHopLimit](struct_router_advertisement_message.html#aaea5c1803d7682440d26de75d1586403)  
bool | [isManagedConfig](struct_router_advertisement_message.html#a54b82a37fb370556753c7bbb9c3edbc5)  
bool | [isOtherConfig](struct_router_advertisement_message.html#ab0064434f8297a7c59c90e8a09ff8ece)  
short | [routerLifetime](struct_router_advertisement_message.html#abe3531bfbdce71f3251930fe14b5532d)  
int | [reachableTime](struct_router_advertisement_message.html#a9071840ba51b5034824cc40ac19bda9b)  
int | [retransTime](struct_router_advertisement_message.html#a851f142b6b8c18c6ab015a3389cf07bf)  
Public Attributes inherited from [NdMessage](struct_nd_message.html)  
vector< [NdOption](struct_nd_option.html) > | [options](struct_nd_message.html#ac5a421f6f344db491ddaa9cd880790db)  
Public Attributes inherited from [Icmpv6Message](struct_icmpv6_message.html)  
Icmpv6MessageType | [type](struct_icmpv6_message.html#ac2e04a595d1a58e650b611f66cb27fd4)  
byte | [code](struct_icmpv6_message.html#a5287359ba10784ecd87d9904fba548f0)  
short | [checksum](struct_icmpv6_message.html#a0989e68c86c7e8449086fba804af6de2)  
Public Attributes inherited from [Header](struct_header.html)  
[Pdu](struct_pdu.html) | [payload](struct_header.html#a07ee8693faef1e16c65765b5bcdc366d)  
  
## Detailed Description

[Router](class_router.html "Router is the base class for all router devices.") advertisement message structure. 

## Member Data Documentation

## ◆ curHopLimit

byte RouterAdvertisementMessage::curHopLimit  
---  
  
## ◆ isManagedConfig

bool RouterAdvertisementMessage::isManagedConfig  
---  
  
## ◆ isOtherConfig

bool RouterAdvertisementMessage::isOtherConfig  
---  
  
## ◆ reachableTime

int RouterAdvertisementMessage::reachableTime  
---  
  
## ◆ retransTime

int RouterAdvertisementMessage::retransTime  
---  
  
## ◆ routerLifetime

short RouterAdvertisementMessage::routerLifetime  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [CRouterAdvertisementMessage.pki](_c_router_advertisement_message_8pki.html)


