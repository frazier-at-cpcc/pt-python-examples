# Cisco Packet Tracer Extensions API: OspfHelloPacket Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_ospf_hello_packet.html

---

OSPF hello packet structure. [More...](struct_ospf_hello_packet.html#details)

##  Public Attributes  
  
---  
ip | [networkMask](struct_ospf_hello_packet.html#a9a3d6cc9eaf3bed080462a4b98efc42c)  
short | [helloInterval](struct_ospf_hello_packet.html#af89a091940cfe0ba4d4ad82cb8bdca6f)  
byte | [option](struct_ospf_hello_packet.html#a28288d0181053c75f2eb94a62ebc4bc6)  
byte | [priority](struct_ospf_hello_packet.html#af37ed0d2b8d2bd0bf1b863c597b1b894)  
int | [deadInterval](struct_ospf_hello_packet.html#abc5d93b6f816aff657d887d67b40dae9)  
ip | [designatedRouter](struct_ospf_hello_packet.html#aaa0fe19298f6352e271dc81d4144c3d0)  
ip | [backupDesignatedRouter](struct_ospf_hello_packet.html#a2c7e8ad16f03a25139fbcd1b45d0ae58)  
vector< ip > | [neighbors](struct_ospf_hello_packet.html#a8327868bdfd14e4e320efddf03353abc)  
Public Attributes inherited from [OspfPacket](struct_ospf_packet.html)  
byte | [version](struct_ospf_packet.html#a9002258dde6f3b492ed4e5ee232b44b9)  
byte | [typeCode](struct_ospf_packet.html#a9a1767abf821c220b09f7366037d40d3)  
short | [length](struct_ospf_packet.html#a24cb13316ac718e1f2e8a95aeeeff074)  
ip | [routerId](struct_ospf_packet.html#abf2ca93eb25626e7eb4b1c580d9188d8)  
ip | [areaId](struct_ospf_packet.html#a498610703e88fc32d78f7917e5245b08)  
short | [checkSum](struct_ospf_packet.html#a5b6083cfa5bc16aa434c280868335b98)  
short | [authenticationType](struct_ospf_packet.html#a9fe5c8dda025572f0b04abaea94098aa)  
int | [sequence](struct_ospf_packet.html#afb262e670885f7761e0de218db37fd1a)  
  
## Detailed Description

OSPF hello packet structure. 

## Member Data Documentation

## ◆ backupDesignatedRouter

ip OspfHelloPacket::backupDesignatedRouter  
---  
  
## ◆ deadInterval

int OspfHelloPacket::deadInterval  
---  
  
## ◆ designatedRouter

ip OspfHelloPacket::designatedRouter  
---  
  
## ◆ helloInterval

short OspfHelloPacket::helloInterval  
---  
  
## ◆ neighbors

vector<ip> OspfHelloPacket::neighbors  
---  
  
## ◆ networkMask

ip OspfHelloPacket::networkMask  
---  
  
## ◆ option

byte OspfHelloPacket::option  
---  
  
## ◆ priority

byte OspfHelloPacket::priority  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [COspfHelloPacket.pki](_c_ospf_hello_packet_8pki.html)


