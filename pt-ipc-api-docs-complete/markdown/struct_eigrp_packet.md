# Cisco Packet Tracer Extensions API: EigrpPacket Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_eigrp_packet.html

---

EIGRP packet structure. [More...](struct_eigrp_packet.html#details)

##  Public Attributes  
  
---  
byte | [version](struct_eigrp_packet.html#a4e81023aa5446e56ca6bbb639987fa67)  
byte | [operationCode](struct_eigrp_packet.html#a8a8788b184515e64d07579d4c1cfd3cf)  
short | [checkSum](struct_eigrp_packet.html#a77396ce9942c0dbc53a92b7a2ccdb480)  
int | [flag](struct_eigrp_packet.html#a7270b5a505682b514a0483b1b5bb9713)  
int | [sequenceNumber](struct_eigrp_packet.html#a1e55507d13d4252c04d8825f3a83ac7c)  
int | [ackNumber](struct_eigrp_packet.html#aec4666828a3075c01d71a55d9e04e4af)  
int | [asNumber](struct_eigrp_packet.html#af53db4e983df1336e36c0877d45d5eb9)  
vector< [EigrpTlv](struct_eigrp_tlv.html) > | [listTlv](struct_eigrp_packet.html#acd3384f8210c42d141b57864f53c49a1)  
  
## Detailed Description

EIGRP packet structure. 

## Member Data Documentation

## ◆ ackNumber

int EigrpPacket::ackNumber  
---  
  
## ◆ asNumber

int EigrpPacket::asNumber  
---  
  
## ◆ checkSum

short EigrpPacket::checkSum  
---  
  
## ◆ flag

int EigrpPacket::flag  
---  
  
## ◆ listTlv

vector<[EigrpTlv](struct_eigrp_tlv.html)> EigrpPacket::listTlv  
---  
  
## ◆ operationCode

byte EigrpPacket::operationCode  
---  
  
## ◆ sequenceNumber

int EigrpPacket::sequenceNumber  
---  
  
## ◆ version

byte EigrpPacket::version  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [CEigrpPacket.pki](_c_eigrp_packet_8pki.html)


