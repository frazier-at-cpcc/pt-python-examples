# Cisco Packet Tracer Extensions API: Ipv6Header Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_ipv6_header.html

---

IPv6 header structure. [More...](struct_ipv6_header.html#details)

##  Public Attributes  
  
---  
[Ipv6NextHeader](struct_ipv6_next_header.html) | [nextHeader](struct_ipv6_header.html#afc7d4acb5f205b7c0ea5beb7b4c992b3)  
byte | [version](struct_ipv6_header.html#a24a58f76f90b4c482b318977fecef183)  
byte | [headerLength](struct_ipv6_header.html#ab8ac254956c910cedfa9a9365378309d)  
byte | [typeOfService](struct_ipv6_header.html#afa85f5a2d295500a6a97f2e177e5a559)  
short | [totalLength](struct_ipv6_header.html#a96954bf990553eba3e8c1d515412f3fe)  
short | [identification](struct_ipv6_header.html#ab94fee91cd4862ed5d8cdd7c83732c9d)  
byte | [flags](struct_ipv6_header.html#a713edbe56fd4a9bb7809ca4d8ad15871)  
short | [fragmentOffset](struct_ipv6_header.html#aba45971e48e7c11404f2db01eba4cff6)  
short | [protocol](struct_ipv6_header.html#a24f68df53e12a46ea6824e869eb907ee)  
short | [headerChecksum](struct_ipv6_header.html#acd8728cfdff893a9e2ee6a25ec9af166)  
int | [options](struct_ipv6_header.html#a319c03bfff2fc95b8fe66e927470c3fa)  
int | [padding](struct_ipv6_header.html#af9c18c02a9d19fb24a17a89941619e05)  
ipv6 | [sourceAddress](struct_ipv6_header.html#ac12addf4a12b435b1385f1ddfbd204fe)  
ipv6 | [destinationAddress](struct_ipv6_header.html#a2e56e4df40110487bf4704b48274cbf1)  
Public Attributes inherited from [Header](struct_header.html)  
[Pdu](struct_pdu.html) | [payload](struct_header.html#a07ee8693faef1e16c65765b5bcdc366d)  
  
## Detailed Description

IPv6 header structure. 

## Member Data Documentation

## ◆ destinationAddress

ipv6 Ipv6Header::destinationAddress  
---  
  
## ◆ flags

byte Ipv6Header::flags  
---  
  
## ◆ fragmentOffset

short Ipv6Header::fragmentOffset  
---  
  
## ◆ headerChecksum

short Ipv6Header::headerChecksum  
---  
  
## ◆ headerLength

byte Ipv6Header::headerLength  
---  
  
## ◆ identification

short Ipv6Header::identification  
---  
  
## ◆ nextHeader

[Ipv6NextHeader](struct_ipv6_next_header.html) Ipv6Header::nextHeader  
---  
  
## ◆ options

int Ipv6Header::options  
---  
  
## ◆ padding

int Ipv6Header::padding  
---  
  
## ◆ protocol

short Ipv6Header::protocol  
---  
  
## ◆ sourceAddress

ipv6 Ipv6Header::sourceAddress  
---  
  
## ◆ totalLength

short Ipv6Header::totalLength  
---  
  
## ◆ typeOfService

byte Ipv6Header::typeOfService  
---  
  
## ◆ version

byte Ipv6Header::version  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [CIpv6Header.pki](_c_ipv6_header_8pki.html)


