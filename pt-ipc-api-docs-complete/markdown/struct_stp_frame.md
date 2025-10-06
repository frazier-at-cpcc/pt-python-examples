# Cisco Packet Tracer Extensions API: StpFrame Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_stp_frame.html

---

STP frame structure. [More...](struct_stp_frame.html#details)

##  Public Attributes  
  
---  
short | [protocolId](struct_stp_frame.html#a37057fef63b4dbc3248bcee8b0a348ac)  
byte | [version](struct_stp_frame.html#ae1c6f20f88e22a10f85a4a520ea22495)  
StpBpduType | [messageType](struct_stp_frame.html#a37742878b8ff893c752546df6ce71805)  
byte | [flags](struct_stp_frame.html#ae02978f00d0be3b7e566fa5cd0182c73)  
[StpId](struct_stp_id.html) | [rootBridgeId](struct_stp_frame.html#a24ed6921dbe44580e45feb87ebe9d29d)  
int | [rootPathCost](struct_stp_frame.html#a37d45e6ac6336db3cd73fcb7ba6dc99b)  
[StpId](struct_stp_id.html) | [bridgeId](struct_stp_frame.html#a7b2dded310a1a4d37d5cf90e1fb64990)  
short | [portId](struct_stp_frame.html#a97936318ce899cf88e27af9d813866a0)  
short | [messageAge](struct_stp_frame.html#a28d5c0148abf0d405f8fc6047d597729)  
short | [maxAge](struct_stp_frame.html#a4e17fdf5ac6b52e17b3495209bc9d0f3)  
short | [helloTime](struct_stp_frame.html#a5e1b87877fdc105adb051f6adcbabe76)  
short | [forwardDelay](struct_stp_frame.html#a3e089779efdfa173dd45ba8ca17ec47b)  
vector< [StpTypeLengthValue](struct_stp_type_length_value.html) > | [lengthValues](struct_stp_frame.html#a5acc289d93eb23be9914c7c522b915e4)  
  
## Detailed Description

STP frame structure. 

## Member Data Documentation

## ◆ bridgeId

[StpId](struct_stp_id.html) StpFrame::bridgeId  
---  
  
## ◆ flags

byte StpFrame::flags  
---  
  
## ◆ forwardDelay

short StpFrame::forwardDelay  
---  
  
## ◆ helloTime

short StpFrame::helloTime  
---  
  
## ◆ lengthValues

vector<[StpTypeLengthValue](struct_stp_type_length_value.html)> StpFrame::lengthValues  
---  
  
## ◆ maxAge

short StpFrame::maxAge  
---  
  
## ◆ messageAge

short StpFrame::messageAge  
---  
  
## ◆ messageType

StpBpduType StpFrame::messageType  
---  
  
## ◆ portId

short StpFrame::portId  
---  
  
## ◆ protocolId

short StpFrame::protocolId  
---  
  
## ◆ rootBridgeId

[StpId](struct_stp_id.html) StpFrame::rootBridgeId  
---  
  
## ◆ rootPathCost

int StpFrame::rootPathCost  
---  
  
## ◆ version

byte StpFrame::version  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [CStpFrame.pki](_c_stp_frame_8pki.html)


