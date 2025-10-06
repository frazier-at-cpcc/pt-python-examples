# Cisco Packet Tracer Extensions API: TcpHeader Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_tcp_header.html

---

TCP header structure. [More...](struct_tcp_header.html#details)

##  Public Attributes  
  
---  
int | [seqNumber](struct_tcp_header.html#a449344ecc8aed7ea8dd049c27c451781)  
int | [ackNumber](struct_tcp_header.html#a34c4baca773022db8854ea084afd3799)  
byte | [dataOffset](struct_tcp_header.html#a94fa6f59575a8a337c8896c87378c38b)  
byte | [reserved](struct_tcp_header.html#afe5f1fee31c3c687812d6b33a6f8e5a0)  
byte | [controlBits](struct_tcp_header.html#acd2b1d6bf9045a1154e17974db91000b)  
short | [windowSize](struct_tcp_header.html#a2119d32b501c3424529c0d1cd903375f)  
short | [urgentPtr](struct_tcp_header.html#a5645fa3a90d20296c9bc2635748b0f93)  
vector< [TcpOption](struct_tcp_option.html) > | [options](struct_tcp_header.html#ac4aa26057a48776f213f565bc0c81f39)  
vector< byte > | [rawOptions](struct_tcp_header.html#a6815c8019a2e0e199d6596c54923d19b)  
int | [payloadSize](struct_tcp_header.html#aecf083c6881412b9abdb648609b72bd9)  
Public Attributes inherited from [SegmentHeader](struct_segment_header.html)  
short | [srcPort](struct_segment_header.html#afee4d687f2b06e520bd69e333a247309)  
short | [dstPort](struct_segment_header.html#a372de6e3e0736d767c8b41792baae5ed)  
short | [checkSum](struct_segment_header.html#a2155643254e8af5e8d03c8da8f006699)  
Public Attributes inherited from [Header](struct_header.html)  
[Pdu](struct_pdu.html) | [payload](struct_header.html#a07ee8693faef1e16c65765b5bcdc366d)  
  
## Detailed Description

TCP header structure. 

## Member Data Documentation

## ◆ ackNumber

int TcpHeader::ackNumber  
---  
  
## ◆ controlBits

byte TcpHeader::controlBits  
---  
  
## ◆ dataOffset

byte TcpHeader::dataOffset  
---  
  
## ◆ options

vector<[TcpOption](struct_tcp_option.html)> TcpHeader::options  
---  
  
## ◆ payloadSize

int TcpHeader::payloadSize  
---  
  
## ◆ rawOptions

vector<byte> TcpHeader::rawOptions  
---  
  
## ◆ reserved

byte TcpHeader::reserved  
---  
  
## ◆ seqNumber

int TcpHeader::seqNumber  
---  
  
## ◆ urgentPtr

short TcpHeader::urgentPtr  
---  
  
## ◆ windowSize

short TcpHeader::windowSize  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [CTcpHeader.pki](_c_tcp_header_8pki.html)


