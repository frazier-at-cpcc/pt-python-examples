# Cisco Packet Tracer Extensions API: RipPacket Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_rip_packet.html

---

RIP packet structure. [More...](struct_rip_packet.html#details)

##  Public Attributes  
  
---  
byte | [command](struct_rip_packet.html#a548d950308bf09d127123d0d6aa19c5b)  
byte | [version](struct_rip_packet.html#a5e5ea7be1d246af542d0e97bdab0be74)  
short | [routingDomain](struct_rip_packet.html#abc3212e1f679bfbc3d0394de16209144)  
vector< [RipRoutePacket](struct_rip_route_packet.html) > | [routes](struct_rip_packet.html#a2ed72c6edc098adbf23773cdbac86b1f)  
bool | [isRedistributed](struct_rip_packet.html#a8f5c6a7439d7c8b7b8ac4820a22b261d)  
  
## Detailed Description

RIP packet structure. 

## Member Data Documentation

## ◆ command

byte RipPacket::command  
---  
  
## ◆ isRedistributed

bool RipPacket::isRedistributed  
---  
  
## ◆ routes

vector<[RipRoutePacket](struct_rip_route_packet.html)> RipPacket::routes  
---  
  
## ◆ routingDomain

short RipPacket::routingDomain  
---  
  
## ◆ version

byte RipPacket::version  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [CRipPacket.pki](_c_rip_packet_8pki.html)


