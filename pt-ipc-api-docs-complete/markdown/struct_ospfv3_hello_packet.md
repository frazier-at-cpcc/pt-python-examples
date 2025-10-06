# Cisco Packet Tracer Extensions API: Ospfv3HelloPacket Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_ospfv3_hello_packet.html

---

OSPFv3 hello packets structure. [More...](struct_ospfv3_hello_packet.html#details)

##  Public Attributes  
  
---  
int | [interfaceId](struct_ospfv3_hello_packet.html#a3a2a62873be321908f94ebf5673f4946)  
byte | [priority](struct_ospfv3_hello_packet.html#aef09ffb466e5ed44c59debd1f1d6f8ec)  
int | [optionV3](struct_ospfv3_hello_packet.html#a249f61d25f02f8d1743b1f8898e5e9f1)  
short | [helloInterval](struct_ospfv3_hello_packet.html#a9dfd5507ba1854f803817b9c739efc41)  
short | [deadInterval](struct_ospfv3_hello_packet.html#a758c6a02670405a1c6dc37a22fe82ad1)  
ip | [designatedRouter](struct_ospfv3_hello_packet.html#a353b2e2defd6cb25136a930500d15c68)  
ip | [backupDesignatedRouter](struct_ospfv3_hello_packet.html#ab5f992f84c297037a33866feb7193eed)  
vector< ip > | [neighbors](struct_ospfv3_hello_packet.html#aacc9fa7bb8701cd7231a949748032c11)  
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

OSPFv3 hello packets structure. 

## Member Data Documentation

## ◆ backupDesignatedRouter

ip Ospfv3HelloPacket::backupDesignatedRouter  
---  
  
## ◆ deadInterval

short Ospfv3HelloPacket::deadInterval  
---  
  
## ◆ designatedRouter

ip Ospfv3HelloPacket::designatedRouter  
---  
  
## ◆ helloInterval

short Ospfv3HelloPacket::helloInterval  
---  
  
## ◆ interfaceId

int Ospfv3HelloPacket::interfaceId  
---  
  
## ◆ neighbors

vector<ip> Ospfv3HelloPacket::neighbors  
---  
  
## ◆ optionV3

int Ospfv3HelloPacket::optionV3  
---  
  
## ◆ priority

byte Ospfv3HelloPacket::priority  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [COspfv3HelloPacket.pki](_c_ospfv3_hello_packet_8pki.html)


