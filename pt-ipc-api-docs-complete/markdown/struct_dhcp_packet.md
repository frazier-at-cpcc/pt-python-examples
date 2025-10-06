# Cisco Packet Tracer Extensions API: DhcpPacket Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_dhcp_packet.html

---

DHCP packet structure. [More...](struct_dhcp_packet.html#details)

##  Public Attributes  
  
---  
byte | [messageOpCode](struct_dhcp_packet.html#a7e3da166cdde6627ca4d0bae61850880)  
byte | [messageType](struct_dhcp_packet.html#a4ff86827a13d01af244eb1fa2be41fa1)  
byte | [hardwareAddressType](struct_dhcp_packet.html#a30f4987f19712b5a191c484dc4d1b7a9)  
byte | [hardwareAddressLength](struct_dhcp_packet.html#a3c3e9156615939de661a9b6459159f2c)  
byte | [hops](struct_dhcp_packet.html#ae95a94a67dd018103fa19bf2e3623afe)  
string | [transactionID](struct_dhcp_packet.html#a16bfe4606c49694af99742cfd4fab9cb)  
short | [timeInSeconds](struct_dhcp_packet.html#ade6e50876cf432f479dec17c7d2887f1)  
short | [flags](struct_dhcp_packet.html#a22f7e8f5ba1e5cb32681e70d921aa4d4)  
ip | [clientIpAddress](struct_dhcp_packet.html#aa3707baa17eed90f2297762b065e10c4)  
ip | [yourIpAddress](struct_dhcp_packet.html#ab15f213bf3f1c017bdf6db931a5b03eb)  
ip | [serverIpAddress](struct_dhcp_packet.html#a23b25428da5b45f94602313a9e92e715)  
ip | [relayAgentIpAddress](struct_dhcp_packet.html#aeae1ca87072b3435c3a85100b144ab77)  
ip | [gatewayIpAddress](struct_dhcp_packet.html#a6a2c0d00b89bef5c0ae88b07b0cf42b2)  
mac | [clientMacAddress](struct_dhcp_packet.html#a5fbe5fc441ee8aee93c69b7c5ccb0e0b)  
string | [serverName](struct_dhcp_packet.html#af950951f4912092b2cf08b4cf51d4e0a)  
string | [domainName](struct_dhcp_packet.html#a160d6c7fefcd18433b07a8e777c08316)  
string | [bootFileName](struct_dhcp_packet.html#a00b01c269cfc52b649b2c4da42e137a0)  
vector< [DhcpOption](struct_dhcp_option.html) > | [listOptions](struct_dhcp_packet.html#a94391879dfebc42b3cb6a1fb7914078e)  
int | [leaseTime](struct_dhcp_packet.html#a8dd60245de58eec353223aeddfba9139)  
int | [rebindTime](struct_dhcp_packet.html#a6532700abc541661e603ca2337fcba1d)  
int | [renewTime](struct_dhcp_packet.html#a1833fadca9d7c905a9cb2e0d324a50f8)  
ip | [gatewaySubnetAddress](struct_dhcp_packet.html#a6e2d7aeade155906c30c46b6fddc2a60)  
ip | [tftpAddress](struct_dhcp_packet.html#aac613910ee029d7518f8f4af0d1976e8)  
ip | [requestIp](struct_dhcp_packet.html#a261598f88903635bdbb6a812ba837d5f)  
vector< byte > | [rawOptions](struct_dhcp_packet.html#aa929a31495ddda3d86aef302773d631c)  
ip | [wlcAddress](struct_dhcp_packet.html#ab29751febd858a872ab964946b9ee9e9)  
  
## Detailed Description

DHCP packet structure. 

## Member Data Documentation

## ◆ bootFileName

string DhcpPacket::bootFileName  
---  
  
## ◆ clientIpAddress

ip DhcpPacket::clientIpAddress  
---  
  
## ◆ clientMacAddress

mac DhcpPacket::clientMacAddress  
---  
  
## ◆ domainName

string DhcpPacket::domainName  
---  
  
## ◆ flags

short DhcpPacket::flags  
---  
  
## ◆ gatewayIpAddress

ip DhcpPacket::gatewayIpAddress  
---  
  
## ◆ gatewaySubnetAddress

ip DhcpPacket::gatewaySubnetAddress  
---  
  
## ◆ hardwareAddressLength

byte DhcpPacket::hardwareAddressLength  
---  
  
## ◆ hardwareAddressType

byte DhcpPacket::hardwareAddressType  
---  
  
## ◆ hops

byte DhcpPacket::hops  
---  
  
## ◆ leaseTime

int DhcpPacket::leaseTime  
---  
  
## ◆ listOptions

vector<[DhcpOption](struct_dhcp_option.html)> DhcpPacket::listOptions  
---  
  
## ◆ messageOpCode

byte DhcpPacket::messageOpCode  
---  
  
## ◆ messageType

byte DhcpPacket::messageType  
---  
  
## ◆ rawOptions

vector<byte> DhcpPacket::rawOptions  
---  
  
## ◆ rebindTime

int DhcpPacket::rebindTime  
---  
  
## ◆ relayAgentIpAddress

ip DhcpPacket::relayAgentIpAddress  
---  
  
## ◆ renewTime

int DhcpPacket::renewTime  
---  
  
## ◆ requestIp

ip DhcpPacket::requestIp  
---  
  
## ◆ serverIpAddress

ip DhcpPacket::serverIpAddress  
---  
  
## ◆ serverName

string DhcpPacket::serverName  
---  
  
## ◆ tftpAddress

ip DhcpPacket::tftpAddress  
---  
  
## ◆ timeInSeconds

short DhcpPacket::timeInSeconds  
---  
  
## ◆ transactionID

string DhcpPacket::transactionID  
---  
  
## ◆ wlcAddress

ip DhcpPacket::wlcAddress  
---  
  
## ◆ yourIpAddress

ip DhcpPacket::yourIpAddress  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [CDhcpPacket.pki](_c_dhcp_packet_8pki.html)


