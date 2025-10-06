# Cisco Packet Tracer Extensions API: Ipv6FragmentExtensionHeader Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_ipv6_fragment_extension_header.html

---

IPv6 fragment extension header structure. [More...](struct_ipv6_fragment_extension_header.html#details)

##  Public Attributes  
  
---  
[Ipv6NextHeader](struct_ipv6_next_header.html) | [exFragmentNextHeader](struct_ipv6_fragment_extension_header.html#a16602876c8d965c2aded1d263cfb9c5a)  
byte | [extReserved](struct_ipv6_fragment_extension_header.html#a80a31c8e01e5895a15dbdadc9e2fe4c6)  
short | [extFragmentOffset](struct_ipv6_fragment_extension_header.html#ad7ac19b0b582b96b4b593527d02ca2bb)  
byte | [extMfFlag](struct_ipv6_fragment_extension_header.html#aa2a9e0c9340d8aca2cebebfc437becf5)  
int | [exIdentification](struct_ipv6_fragment_extension_header.html#ad0b689a220427f235e926d9acbef7a79)  
Public Attributes inherited from [Ipv6Header](struct_ipv6_header.html)  
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

IPv6 fragment extension header structure. 

## Member Data Documentation

## ◆ exFragmentNextHeader

[Ipv6NextHeader](struct_ipv6_next_header.html) Ipv6FragmentExtensionHeader::exFragmentNextHeader  
---  
  
## ◆ exIdentification

int Ipv6FragmentExtensionHeader::exIdentification  
---  
  
## ◆ extFragmentOffset

short Ipv6FragmentExtensionHeader::extFragmentOffset  
---  
  
## ◆ extMfFlag

byte Ipv6FragmentExtensionHeader::extMfFlag  
---  
  
## ◆ extReserved

byte Ipv6FragmentExtensionHeader::extReserved  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [CIpv6FragmentExtensionHeader.pki](_c_ipv6_fragment_extension_header_8pki.html)


