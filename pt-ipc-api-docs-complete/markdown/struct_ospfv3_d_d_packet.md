# Cisco Packet Tracer Extensions API: Ospfv3DDPacket Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_ospfv3_d_d_packet.html

---

OSPFv3 database description structure. [More...](struct_ospfv3_d_d_packet.html#details)

##  Public Attributes  
  
---  
int | [optionV3](struct_ospfv3_d_d_packet.html#a291b4c321b363ce41eaeb64ea98eebde)  
Public Attributes inherited from [OspfDDPacket](struct_ospf_d_d_packet.html)  
short | [mtu](struct_ospf_d_d_packet.html#a8c800b69dcda35f3cf4024578ad780ec)  
byte | [option](struct_ospf_d_d_packet.html#a970bcbf71fe80ad83338c70be26afba2)  
bool | [initBit](struct_ospf_d_d_packet.html#ab2aab2ee8af60cb0ddfd78f29af9f92e)  
bool | [masterBit](struct_ospf_d_d_packet.html#ac65b672eb7c1315502aadf61e1290037)  
bool | [moreBit](struct_ospf_d_d_packet.html#a21cc0cab77872af5d7c1f276383ba133)  
int | [seqNumber](struct_ospf_d_d_packet.html#a627ae3d4e8749151bbaa4b77f7152f75)  
vector< [OspfLSAHeader](struct_ospf_l_s_a_header.html) > | [listLSAHeaders](struct_ospf_d_d_packet.html#a013c6d77a605180c1d92c8461a31fd58)  
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

OSPFv3 database description structure. 

## Member Data Documentation

## ◆ optionV3

int Ospfv3DDPacket::optionV3  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [COspfv3DDPacket.pki](_c_ospfv3_d_d_packet_8pki.html)


