# Cisco Packet Tracer Extensions API: Dot1qHeader Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_dot1q_header.html

---

IEEE 802.1Q header structure. [More...](struct_dot1q_header.html#details)

##  Public Attributes  
  
---  
short | [tpid](struct_dot1q_header.html#ab28d214d21face8ce710f441952e74f1)  
byte | [userPriority](struct_dot1q_header.html#a175f2b1571270be78b5525e715e3086d)  
byte | [cfi](struct_dot1q_header.html#aeca5a46aaf43bf646546c3484ca1d693)  
short | [vlanId](struct_dot1q_header.html#a242b4b042a8b005e459d19e3c10a3739)  
short | [typeLength](struct_dot1q_header.html#a7edaa4f20e1cfb85fdd00586f8707cc6)  
Public Attributes inherited from [EthernetHeader](struct_ethernet_header.html)  
mac | [dstMacAddress](struct_ethernet_header.html#acf9e852025be702005cbb9214b3f713d)  
mac | [srcMacAddress](struct_ethernet_header.html#a44a906963db6ad34302a2a1b800cb846)  
int | [frameCheckSequence](struct_ethernet_header.html#af3932041331efb3e19060de85b1aedde)  
Public Attributes inherited from [Header](struct_header.html)  
[Pdu](struct_pdu.html) | [payload](struct_header.html#a07ee8693faef1e16c65765b5bcdc366d)  
  
## Detailed Description

IEEE 802.1Q header structure. 

## Member Data Documentation

## ◆ cfi

byte Dot1qHeader::cfi  
---  
  
## ◆ tpid

short Dot1qHeader::tpid  
---  
  
## ◆ typeLength

short Dot1qHeader::typeLength  
---  
  
## ◆ userPriority

byte Dot1qHeader::userPriority  
---  
  
## ◆ vlanId

short Dot1qHeader::vlanId  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [CDot1qHeader.pki](_c_dot1q_header_8pki.html)


