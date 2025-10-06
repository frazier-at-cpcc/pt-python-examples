# Cisco Packet Tracer Extensions API: TacacsPacket Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_tacacs_packet.html

---

TACACS packet structure. [More...](struct_tacacs_packet.html#details)

##  Public Attributes  
  
---  
short | [majorVersion](struct_tacacs_packet.html#a8c45b3d5f1d7e382076acd99578d5785)  
short | [minorVersion](struct_tacacs_packet.html#ac1623dc41dd42cf30f00df68c120f8a5)  
short | [type](struct_tacacs_packet.html#adfb05d53a9d0831901f6859d34fd856e)  
short | [m_seqNo](struct_tacacs_packet.html#a09d4becaa638ca6e43ea363192b40240)  
short | [m_flags](struct_tacacs_packet.html#a8bab9e5b65cc45642cfc3c50bf3f9bc3)  
int | [m_sessionId](struct_tacacs_packet.html#aa7da2ec88e767a381b8f344165ee1c3e)  
int | [m_length](struct_tacacs_packet.html#a6b860c68117b55af673b06a710807c70)  
AttribType | [attribType](struct_tacacs_packet.html#a89375e47280cd713bbe507e395814c69)  
byte | [length](struct_tacacs_packet.html#ac3b863124318591cf964759eed357fe0)  
string | [attribValue](struct_tacacs_packet.html#a2dde62de6a925f30218c73b280da1fca)  
Public Attributes inherited from [Header](struct_header.html)  
[Pdu](struct_pdu.html) | [payload](struct_header.html#a07ee8693faef1e16c65765b5bcdc366d)  
  
## Detailed Description

TACACS packet structure. 

## Member Data Documentation

## ◆ attribType

AttribType TacacsPacket::attribType  
---  
  
## ◆ attribValue

string TacacsPacket::attribValue  
---  
  
## ◆ length

byte TacacsPacket::length  
---  
  
## ◆ m_flags

short TacacsPacket::m_flags  
---  
  
## ◆ m_length

int TacacsPacket::m_length  
---  
  
## ◆ m_seqNo

short TacacsPacket::m_seqNo  
---  
  
## ◆ m_sessionId

int TacacsPacket::m_sessionId  
---  
  
## ◆ majorVersion

short TacacsPacket::majorVersion  
---  
  
## ◆ minorVersion

short TacacsPacket::minorVersion  
---  
  
## ◆ type

short TacacsPacket::type  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [CTacacsPacket.pki](_c_tacacs_packet_8pki.html)


