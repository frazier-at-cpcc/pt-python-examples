# Cisco Packet Tracer Extensions API: HsrpMessage Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_hsrp_message.html

---

HSRP message structure. [More...](struct_hsrp_message.html#details)

##  Public Attributes  
  
---  
int | [version](struct_hsrp_message.html#aa3dab975e1629ba150e191def2c25bd9)  
HsrpMsgType | [type](struct_hsrp_message.html#ac52bbb335b80425bc5f065d72b92c598)  
HsrpState | [hsrpState](struct_hsrp_message.html#ac02962059d1ca8e021478dd6a8b271ae)  
int | [priority](struct_hsrp_message.html#af97093f5c3f802d43bca116ce7156988)  
int | [holdTime](struct_hsrp_message.html#a12b42ed6e4bb20fdace4cb6ecbdccb11)  
int | [helloTime](struct_hsrp_message.html#a1ad43a6a48694f01e87aded9a08205bc)  
int | [groupNum](struct_hsrp_message.html#aa4d943a1216fb19c77327e67a05ec11a)  
string | [ipVersion](struct_hsrp_message.html#ad3a7e99d594c182065f21ff91cff80bd)  
ip | [virtIp](struct_hsrp_message.html#a06b1eb692a35b4b670578084d5cc34bd)  
Public Attributes inherited from [Header](struct_header.html)  
[Pdu](struct_pdu.html) | [payload](struct_header.html#a07ee8693faef1e16c65765b5bcdc366d)  
  
## Detailed Description

HSRP message structure. 

## Member Data Documentation

## ◆ groupNum

int HsrpMessage::groupNum  
---  
  
## ◆ helloTime

int HsrpMessage::helloTime  
---  
  
## ◆ holdTime

int HsrpMessage::holdTime  
---  
  
## ◆ hsrpState

HsrpState HsrpMessage::hsrpState  
---  
  
## ◆ ipVersion

string HsrpMessage::ipVersion  
---  
  
## ◆ priority

int HsrpMessage::priority  
---  
  
## ◆ type

HsrpMsgType HsrpMessage::type  
---  
  
## ◆ version

int HsrpMessage::version  
---  
  
## ◆ virtIp

ip HsrpMessage::virtIp  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [CHsrpMessage.pki](_c_hsrp_message_8pki.html)


