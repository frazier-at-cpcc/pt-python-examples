# Cisco Packet Tracer Extensions API: OspfLSAckPacket Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_ospf_l_s_ack_packet.html

---

OSPF LSA ACK packet structure. [More...](struct_ospf_l_s_ack_packet.html#details)

##  Public Attributes  
  
---  
vector< [OspfLSAHeader](struct_ospf_l_s_a_header.html) > | [lsas](struct_ospf_l_s_ack_packet.html#ab5528280844958452e28d1d5e425a899)  
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

OSPF LSA ACK packet structure. 

## Member Data Documentation

## ◆ lsas

vector<[OspfLSAHeader](struct_ospf_l_s_a_header.html)> OspfLSAckPacket::lsas  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [COspfLSAckPacket.pki](_c_ospf_l_s_ack_packet_8pki.html)


