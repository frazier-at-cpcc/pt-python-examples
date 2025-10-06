# Cisco Packet Tracer Extensions API: CapwapUdpPacket Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_capwap_udp_packet.html

---

[CapwapUdpPacket](struct_capwap_udp_packet.html "CapwapUdpPacket packet structure.") packet structure. [More...](struct_capwap_udp_packet.html#details)

##  Public Attributes  
  
---  
int | [preamble](struct_capwap_udp_packet.html#ad76553d60aae0dc09ee069cb24f454d3)  
int | [fragments](struct_capwap_udp_packet.html#ab149d05ad4ec6f7b923de46874addb33)  
byte | [macLength](struct_capwap_udp_packet.html#a2ee89e634f1c9e3afbd48ab439b974d5)  
mac | [radioMacAddress](struct_capwap_udp_packet.html#a712edc05c098bdff6a4deb1ed5ff7874)  
byte | [wirelessInfoLength](struct_capwap_udp_packet.html#a73982356578caf869758aec3b1116385)  
string | [wirelessInfo](struct_capwap_udp_packet.html#accb16a4c758f67fab2eed98c2c156505)  
string | [payloadType](struct_capwap_udp_packet.html#a3dae60238285e38ad402a189e5dbbcb6)  
vector< [CCapwapControlMessage](class_c_capwap_control_message.html) > | [controls](struct_capwap_udp_packet.html#a547a6262fb49d00ec06e4c349b8bdca1)  
bool | [isFakeTls](struct_capwap_udp_packet.html#a82d58fc064e9dcf40cef9485bd962c04)  
  
## Detailed Description

[CapwapUdpPacket](struct_capwap_udp_packet.html "CapwapUdpPacket packet structure.") packet structure. 

## Member Data Documentation

## ◆ controls

vector<[CCapwapControlMessage](class_c_capwap_control_message.html)> CapwapUdpPacket::controls  
---  
  
## ◆ fragments

int CapwapUdpPacket::fragments  
---  
  
## ◆ isFakeTls

bool CapwapUdpPacket::isFakeTls  
---  
  
## ◆ macLength

byte CapwapUdpPacket::macLength  
---  
  
## ◆ payloadType

string CapwapUdpPacket::payloadType  
---  
  
## ◆ preamble

int CapwapUdpPacket::preamble  
---  
  
## ◆ radioMacAddress

mac CapwapUdpPacket::radioMacAddress  
---  
  
## ◆ wirelessInfo

string CapwapUdpPacket::wirelessInfo  
---  
  
## ◆ wirelessInfoLength

byte CapwapUdpPacket::wirelessInfoLength  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [CCapwapUdpPacket.pki](_c_capwap_udp_packet_8pki.html)


