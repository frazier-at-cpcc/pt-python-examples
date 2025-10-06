# Cisco Packet Tracer Extensions API: IpHeader Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_ip_header.html

---

IP header structure. [More...](struct_ip_header.html#details)

##  Public Attributes  
  
---  
byte | [version](struct_ip_header.html#a6a985695c9f2f5a405189f4feb33b884)  
byte | [headerLength](struct_ip_header.html#aab215281411d0796800c3cf5ff420323)  
byte | [typeOfService](struct_ip_header.html#adee3a4431f217f5d31e9fe476b28bad0)  
short | [totalLength](struct_ip_header.html#ac64946718328f020e6eaa803fbc965e8)  
short | [identification](struct_ip_header.html#a9aee18e9c0b1fb417fb7aa54453d1e93)  
byte | [flags](struct_ip_header.html#a1b104e7ab69bffbd083d5c046b3aabcc)  
short | [fragmentOffset](struct_ip_header.html#a7acc86425db3e9bbd63776f0da7b9e6e)  
short | [ttl](struct_ip_header.html#a55ce41a066f91be81a925f2b614a2fd3)  
short | [protocol](struct_ip_header.html#acf063de61e1b74a874c58a8dc71e7165)  
short | [checksum](struct_ip_header.html#acdfca981ffa5ac03af6d5674f34a6150)  
ip | [srcAddress](struct_ip_header.html#af1bb07450056591bbc37f053d36dcad0)  
ip | [dstAddress](struct_ip_header.html#a136b706573280c7ff9a39c507237f0b5)  
int | [options](struct_ip_header.html#a53d85aa266878b66b4e01ee1ca896dc9)  
int | [padding](struct_ip_header.html#a9e67ebb5ddb2a614badff44df9442267)  
Public Attributes inherited from [Header](struct_header.html)  
[Pdu](struct_pdu.html) | [payload](struct_header.html#a07ee8693faef1e16c65765b5bcdc366d)  
  
## Detailed Description

IP header structure. 

## Member Data Documentation

## ◆ checksum

short IpHeader::checksum  
---  
  
## ◆ dstAddress

ip IpHeader::dstAddress  
---  
  
## ◆ flags

byte IpHeader::flags  
---  
  
## ◆ fragmentOffset

short IpHeader::fragmentOffset  
---  
  
## ◆ headerLength

byte IpHeader::headerLength  
---  
  
## ◆ identification

short IpHeader::identification  
---  
  
## ◆ options

int IpHeader::options  
---  
  
## ◆ padding

int IpHeader::padding  
---  
  
## ◆ protocol

short IpHeader::protocol  
---  
  
## ◆ srcAddress

ip IpHeader::srcAddress  
---  
  
## ◆ totalLength

short IpHeader::totalLength  
---  
  
## ◆ ttl

short IpHeader::ttl  
---  
  
## ◆ typeOfService

byte IpHeader::typeOfService  
---  
  
## ◆ version

byte IpHeader::version  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [CIpHeader.pki](_c_ip_header_8pki.html)


