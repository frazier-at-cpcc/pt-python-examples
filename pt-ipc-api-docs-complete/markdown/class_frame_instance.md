# Cisco Packet Tracer Extensions API: FrameInstance Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_frame_instance.html

---

[FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") holds traffic details such as PDUs, ports, etc. [More...](class_frame_instance.html#details)

##  Public Member Functions  
  
---  
TrafficType | [getUserTrafficType](class_frame_instance.html#a000b8638b7218e9542ea5fd00c8e6b68) ()  
| Returns the user traffic type. [More...](class_frame_instance.html#a000b8638b7218e9542ea5fd00c8e6b68)  
  
QString | [getDestinationString](class_frame_instance.html#a1245e5f0330b96704fbd4f820add19c2) ()  
| Returns the destination. [More...](class_frame_instance.html#a1245e5f0330b96704fbd4f820add19c2)  
  
QString | [getSourceString](class_frame_instance.html#a2d524d8113a41fb641663fc2dbe707c0) ()  
| Returns the source. [More...](class_frame_instance.html#a2d524d8113a41fb641663fc2dbe707c0)  
  
[Device](class_device.html) | [getDevice](class_frame_instance.html#a49ebc84a363ca6d2962286a3d64839ec) ()  
| Returns the current device the frame instance is at. [More...](class_frame_instance.html#a49ebc84a363ca6d2962286a3d64839ec)  
  
[Device](class_device.html) | [getPreviousDevice](class_frame_instance.html#a9bec3f6b8bf2cda473f7a719e57d3a12) ()  
| Returns the previous device the frame instance was at. [More...](class_frame_instance.html#a9bec3f6b8bf2cda473f7a719e57d3a12)  
  
[Pdu](struct_pdu.html) | [getInFrame](class_frame_instance.html#a9a8622f2260aa9e7140a3c76daf55a0c) ()  
| Returns the inbound frame. [More...](class_frame_instance.html#a9a8622f2260aa9e7140a3c76daf55a0c)  
  
[Pdu](struct_pdu.html) | [getOutFrame](class_frame_instance.html#a41b003eed5ab49a264ae56670fa1b3b4) ()  
| Returns the outbound frame. [More...](class_frame_instance.html#a41b003eed5ab49a264ae56670fa1b3b4)  
  
[Port](class_port.html) | [getInPort](class_frame_instance.html#aee167562e89d3ac9b8bc5170fef48a0c) ()  
| Returns the inbound port. [More...](class_frame_instance.html#aee167562e89d3ac9b8bc5170fef48a0c)  
  
[Port](class_port.html) | [getOutPort](class_frame_instance.html#af6ab56698e7f0f6522495a901add478c) (int)  
| returns the outbound port at the specified index. [More...](class_frame_instance.html#af6ab56698e7f0f6522495a901add478c)  
  
int | [getOutPortCount](class_frame_instance.html#a923813cf1816ac957e8718e6dc8e2fca) ()  
| Returns the number of outbound ports. [More...](class_frame_instance.html#a923813cf1816ac957e8718e6dc8e2fca)  
  
void | [addDecision](class_frame_instance.html#ac9bf1f4bde8c83c8fede28ea37870262) (string, QString, bool, int)  
| Adds a flowchart decision with the specified ID and description at the specified layer. [More...](class_frame_instance.html#ac9bf1f4bde8c83c8fede28ea37870262)  
  
[FlowChartNode](struct_flow_chart_node.html) | [getFlowChartNodeAt](class_frame_instance.html#a5a4103cef16b09283380d90e202639cb) (int)  
| Returns the flowchart node at the specified index. [More...](class_frame_instance.html#a5a4103cef16b09283380d90e202639cb)  
  
[FrameDecision](struct_frame_decision.html) | [getFrameDecsionAt](class_frame_instance.html#ae1ee34dcc669e490f90457ad288c6561) (int)  
| Returns the frame decision at the specified index. [More...](class_frame_instance.html#ae1ee34dcc669e490f90457ad288c6561)  
  
int | [getFlowChartNodeCount](class_frame_instance.html#a70f5dcc9bedc5070a94a3f8b286c889c) ()  
| Returns the number of flowchart nodes. [More...](class_frame_instance.html#a70f5dcc9bedc5070a94a3f8b286c889c)  
  
QString | [getDecisionAt](class_frame_instance.html#a140e11ba8b30f9db70fe291784ede4eb) (int)  
| Returns the decision at the specified index. [More...](class_frame_instance.html#a140e11ba8b30f9db70fe291784ede4eb)  
  
void | [setFrameSent](class_frame_instance.html#a28010fd8fc7c381fcd0c0dc51fa58936) (bool)  
| Sets the frame as sent or unsent. [More...](class_frame_instance.html#a28010fd8fc7c381fcd0c0dc51fa58936)  
  
bool | [isFrameSent](class_frame_instance.html#a8d4b79167544688fcb37f7f97017c261) ()  
| Returns true if the the frame is sent, otherwise false. [More...](class_frame_instance.html#a8d4b79167544688fcb37f7f97017c261)  
  
void | [setFrameBuffered](class_frame_instance.html#a3b81d08800ede774d401390c519e8878) (bool)  
| Sets the frame as buffered or unbuffered. [More...](class_frame_instance.html#a3b81d08800ede774d401390c519e8878)  
  
bool | [isFrameBuffered](class_frame_instance.html#af7e2ee315018a66ef21940953f5de64a) ()  
| Returns true if the the frame is buffered, otherwise false. [More...](class_frame_instance.html#af7e2ee315018a66ef21940953f5de64a)  
  
void | [setFrameDropped](class_frame_instance.html#ad7a80fea3926424de115edbd04433f91) (bool)  
| Sets the frame as dropped or not dropped. [More...](class_frame_instance.html#ad7a80fea3926424de115edbd04433f91)  
  
bool | [isFrameDropped](class_frame_instance.html#aac29c656cd1d9334d0bc90cf9394fbc3) ()  
| Returns true if the the frame is dropped, otherwise false. [More...](class_frame_instance.html#aac29c656cd1d9334d0bc90cf9394fbc3)  
  
void | [setFrameNotForwarded](class_frame_instance.html#ab39f3abbdb0f8f725b16c749801e26ff) (bool)  
| Sets the frame as not forwarded or forwarded. [More...](class_frame_instance.html#ab39f3abbdb0f8f725b16c749801e26ff)  
  
bool | [isFrameNotForwarded](class_frame_instance.html#a5b71dedc51cc68f70d6be6e5fb2aefb9) ()  
| Returns true if the the frame is not forwarded, otherwise false. [More...](class_frame_instance.html#a5b71dedc51cc68f70d6be6e5fb2aefb9)  
  
void | [setFrameAccepted](class_frame_instance.html#a833dbbe4d081c6144d4de7e9f829c7a2) (bool)  
| Sets the frame as accepted or not accepted. [More...](class_frame_instance.html#a833dbbe4d081c6144d4de7e9f829c7a2)  
  
bool | [isFrameAccepted](class_frame_instance.html#aead28efc1b9ef7cec6f7b680c0aa8313) ()  
| Returns true if the the frame is accepted, otherwise false. [More...](class_frame_instance.html#aead28efc1b9ef7cec6f7b680c0aa8313)  
  
void | [setFrameUnexpected](class_frame_instance.html#a52e8eb898fae2ec0f8a9ee4b52581384) (bool)  
| Sets the frame as unexpected or expected. [More...](class_frame_instance.html#a52e8eb898fae2ec0f8a9ee4b52581384)  
  
bool | [isFrameUnexpected](class_frame_instance.html#a23a50ed5940987c95e8b581a26411943) ()  
| Returns true if the the frame is unexpected, otherwise false. [More...](class_frame_instance.html#a23a50ed5940987c95e8b581a26411943)  
  
bool | [isFrameCollidedOnLink](class_frame_instance.html#a41de27a5a5ef89d0b61b83627471c81e) ()  
| Returns true if the frame collided on the link, otherwise false. [More...](class_frame_instance.html#a41de27a5a5ef89d0b61b83627471c81e)  
  
bool | [isFrameCollidedAtDevice](class_frame_instance.html#adb63dcb8b3c718868b6b175f8ac1e229) ()  
| Returns true if the frame collided at the device, otherwise false. [More...](class_frame_instance.html#adb63dcb8b3c718868b6b175f8ac1e229)  
  
bool | [isFrameOnTransit](class_frame_instance.html#ac39daec7685f7962f2f79417c7f591a6) ()  
| Returns true if the frame is in transit, otherwise false. [More...](class_frame_instance.html#ac39daec7685f7962f2f79417c7f591a6)  
  
int | [getQosStampColorCode](class_frame_instance.html#a3badda541c4f4a1d768ac8b0816cb95d) ()  
| Returns the QoS stamp color code. [More...](class_frame_instance.html#a3badda541c4f4a1d768ac8b0816cb95d)  
  
int | [getInQosStampColorCode](class_frame_instance.html#ac0b2ab0430ff3fd2bc783a1ad8789691) ()  
| Returns the inbound QoS stamp color code. [More...](class_frame_instance.html#ac0b2ab0430ff3fd2bc783a1ad8789691)  
  
int | [getOutQosStampColorCode](class_frame_instance.html#acf202e1f66670812a464993b3d85852e) ()  
| Returns the outbound QoS stamp color code. [More...](class_frame_instance.html#acf202e1f66670812a464993b3d85852e)  
  
int | [getTransitTime](class_frame_instance.html#a10cfabed53c49017673669dba0512c8c) ()  
| Returns the transit time. [More...](class_frame_instance.html#a10cfabed53c49017673669dba0512c8c)  
  
int | [getPercentageSent](class_frame_instance.html#abb430b394615365ea2a6a37b00a4def2) ()  
| Returns the percentage of the frame that was sent. [More...](class_frame_instance.html#abb430b394615365ea2a6a37b00a4def2)  
  
long | [getStartSimTime](class_frame_instance.html#aebe0a4352d10309f9f7f406175441aee) ()  
| Returns the simulation start time. [More...](class_frame_instance.html#aebe0a4352d10309f9f7f406175441aee)  
  
[UserTraffic](class_user_traffic.html) | [getTrafficSource](class_frame_instance.html#a3ce071f475797f92ed00b28f9b7d7fe6) ()  
| Returns the traffic source. [More...](class_frame_instance.html#a3ce071f475797f92ed00b28f9b7d7fe6)  
  
int | [getTime](class_frame_instance.html#ac63d70fdf52ab9dadc0d631fbb9019d8) ()  
| Returns time of the frame instance. [More...](class_frame_instance.html#ac63d70fdf52ab9dadc0d631fbb9019d8)  
  
  
## Detailed Description

[FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") holds traffic details such as PDUs, ports, etc. 

## Member Function Documentation

## ◆ addDecision()

void FrameInstance::addDecision  | ( | string  | ,   
---|---|---|---  
|  | QString  | ,   
|  | bool  | ,   
|  | int  |   
| ) | |   
  
Adds a flowchart decision with the specified ID and description at the specified layer. 

Parameters
     id,the| flowchart ID.   
---|---  
description,the| flowchart description.   
isOsiIn,true| if inbound layer decision, false if outbound layer decision.   
osiLayer,the| OSI layer.   
  
## ◆ getDecisionAt()

QString FrameInstance::getDecisionAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the decision at the specified index. 

Parameters
     index,the| index of the decision of interest.  
---|---  
  
Returns
    QString, the decision at the specified index. 

## ◆ getDestinationString()

QString FrameInstance::getDestinationString  | ( | | ) |   
---|---|---|---|---  
  
Returns the destination. 

Returns
    QString, the destination. 

## ◆ getDevice()

[Device](class_device.html) FrameInstance::getDevice  | ( | | ) |   
---|---|---|---|---  
  
Returns the current device the frame instance is at. 

Returns
    [Device](class_device.html "Device is the base class for all device objects."), the [Device](class_device.html "Device is the base class for all device objects.") object the frame instance is at. 

## ◆ getFlowChartNodeAt()

[FlowChartNode](struct_flow_chart_node.html) FrameInstance::getFlowChartNodeAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the flowchart node at the specified index. 

Parameters
     nodeIndex,the| index of the flowchart node of interest.  
---|---  
  
Returns
    [FlowChartNode](struct_flow_chart_node.html "Data element for flow chart nodes."), the [FlowChartNode](struct_flow_chart_node.html "Data element for flow chart nodes.") object att he specified index. 

## ◆ getFlowChartNodeCount()

int FrameInstance::getFlowChartNodeCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of flowchart nodes. 

Returns
    int, the number of flowchart nodes. 

## ◆ getFrameDecsionAt()

[FrameDecision](struct_frame_decision.html) FrameInstance::getFrameDecsionAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the frame decision at the specified index. 

Parameters
     index,the| index of the frame decision of interest.  
---|---  
  
Returns
    [FrameDecision](struct_frame_decision.html "Data element for FrameDecision."), the [FrameDecision](struct_frame_decision.html "Data element for FrameDecision.") at the specified index. 

## ◆ getInFrame()

[Pdu](struct_pdu.html) FrameInstance::getInFrame  | ( | | ) |   
---|---|---|---|---  
  
Returns the inbound frame. 

Returns
    [Pdu](struct_pdu.html "Pdu structure."), the inbound frame [Pdu](struct_pdu.html "Pdu structure.") object. 

## ◆ getInPort()

[Port](class_port.html) FrameInstance::getInPort  | ( | | ) |   
---|---|---|---|---  
  
Returns the inbound port. 

Returns
    [Port](class_port.html "Port holds and manipulates the ports on devices."), the inbound [Port](class_port.html "Port holds and manipulates the ports on devices.") object. 

## ◆ getInQosStampColorCode()

int FrameInstance::getInQosStampColorCode  | ( | | ) |   
---|---|---|---|---  
  
Returns the inbound QoS stamp color code. 

Returns
    int, the inbound QoS stamp color code. 

## ◆ getOutFrame()

[Pdu](struct_pdu.html) FrameInstance::getOutFrame  | ( | | ) |   
---|---|---|---|---  
  
Returns the outbound frame. 

Returns
    [Pdu](struct_pdu.html "Pdu structure."), the outbound frame [Pdu](struct_pdu.html "Pdu structure.") object. 

## ◆ getOutPort()

[Port](class_port.html) FrameInstance::getOutPort  | ( | int  | | ) |   
---|---|---|---|---|---  
  
returns the outbound port at the specified index. 

Parameters
     outPortIndex,the| index of the outbound port of interest.  
---|---  
  
Returns
    [Port](class_port.html "Port holds and manipulates the ports on devices."), the outbound [Port](class_port.html "Port holds and manipulates the ports on devices.") object at the specified index. 

## ◆ getOutPortCount()

int FrameInstance::getOutPortCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of outbound ports. 

Returns
    int, the number of outbound ports. 

## ◆ getOutQosStampColorCode()

int FrameInstance::getOutQosStampColorCode  | ( | | ) |   
---|---|---|---|---  
  
Returns the outbound QoS stamp color code. 

Returns
    int, the outbound QoS stamp color code. 

## ◆ getPercentageSent()

int FrameInstance::getPercentageSent  | ( | | ) |   
---|---|---|---|---  
  
Returns the percentage of the frame that was sent. 

Returns
    int, the percentage of the frame that was sent. 

## ◆ getPreviousDevice()

[Device](class_device.html) FrameInstance::getPreviousDevice  | ( | | ) |   
---|---|---|---|---  
  
Returns the previous device the frame instance was at. 

Returns
    [Device](class_device.html "Device is the base class for all device objects."), the [Device](class_device.html "Device is the base class for all device objects.") object the frame instance was at. 

## ◆ getQosStampColorCode()

int FrameInstance::getQosStampColorCode  | ( | | ) |   
---|---|---|---|---  
  
Returns the QoS stamp color code. 

Returns
    int, the QoS stamp color code. 

## ◆ getSourceString()

QString FrameInstance::getSourceString  | ( | | ) |   
---|---|---|---|---  
  
Returns the source. 

Returns
    QString, the source. 

## ◆ getStartSimTime()

long FrameInstance::getStartSimTime  | ( | | ) |   
---|---|---|---|---  
  
Returns the simulation start time. 

Returns
    int, the simulation start time. 

## ◆ getTime()

int FrameInstance::getTime  | ( | | ) |   
---|---|---|---|---  
  
Returns time of the frame instance. 

Returns
    int, time of the frame instance. 

## ◆ getTrafficSource()

[UserTraffic](class_user_traffic.html) FrameInstance::getTrafficSource  | ( | | ) |   
---|---|---|---|---  
  
Returns the traffic source. 

Returns
    [UserTraffic](class_user_traffic.html "UserTraffic represents the user traffic information \(PDU\)."), the soure [UserTraffic](class_user_traffic.html "UserTraffic represents the user traffic information \(PDU\).") object. 

## ◆ getTransitTime()

int FrameInstance::getTransitTime  | ( | | ) |   
---|---|---|---|---  
  
Returns the transit time. 

Returns
    int, the transit time. 

## ◆ getUserTrafficType()

TrafficType FrameInstance::getUserTrafficType  | ( | | ) |   
---|---|---|---|---  
  
Returns the user traffic type. 

Returns
    enum<TrafficType>, the user traffic type. User traffic types: eTrafficType_Icmp = 0, eTrafficType_Tcp = 1, eTrafficType_Udp = 2, eTrafficType_RipV1 = 3, eTrafficType_RipV2 = 4, eTrafficType_Arp = 5, eTrafficType_Cdp = 6, eTrafficType_Dhcp = 7, eTrafficType_Nat = 8, eTrafficType_Eigrp = 9, eTrafficType_Vtp = 10, eTrafficType_Stp = 11, eTrafficType_Ospf = 12, eTrafficType_Dtp = 13, eTrafficType_Telnet = 14, eTrafficType_Ssh = 15, eTrafficType_Tftp = 16, eTrafficType_Http = 17, eTrafficType_Https = 18, eTrafficType_Dns = 19, eTrafficType_Icmpv6 = 20, eTrafficType_Lacp = 21, eTrafficType_Pagp = 22, eTrafficType_Ipsec = 23, eTrafficType_Ike = 24, eTrafficType_Syslog = 25, eTrafficType_Tacacs = 26, eTrafficType_Radius = 27, eTrafficType_Snmp = 28, eTrafficType_Ntp = 29, eTrafficType_Ftp = 30, eTrafficType_Smtp = 31, eTrafficType_Pop3 = 32, eTrafficType_Sccp = 33, eTrafficType_Rtp = 34, eTrafficType_H323 = 35, eTrafficType_Bgp = 36, eTrafficType_Hsrp = 37, eTrafficType_Hsrpv6 = 38, eTrafficType_Netflow = 39, eTrafficType_Ndv6 = 40, eTrafficType_Ripng = 41, eTrafficType_Dhcpv6 = 42, eTrafficType_Eigrpv6 = 43, eTrafficType_Ospfv6 = 44, eTrafficType_IoE = 45, eTrafficType_Ptp = 46, eTrafficType_Rep = 47, eTrafficType_CapwapUdp = 48, eTrafficType_Lldp = 49, eTrafficType_Span = 50, eTrafficType_IoETcp = 51, eTrafficType_Usb = 52, eTrafficType_Bluetooth = 53, eTrafficType_Custom = 1000 

## ◆ isFrameAccepted()

bool FrameInstance::isFrameAccepted  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the the frame is accepted, otherwise false. 

Returns
    bool, true if the the frame is accepted, otherwise false. 

## ◆ isFrameBuffered()

bool FrameInstance::isFrameBuffered  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the the frame is buffered, otherwise false. 

Returns
    bool, true if the the frame is buffered, otherwise false. 

## ◆ isFrameCollidedAtDevice()

bool FrameInstance::isFrameCollidedAtDevice  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the frame collided at the device, otherwise false. 

Returns
    bool, true if the frame collided at the device, otherwise false. 

## ◆ isFrameCollidedOnLink()

bool FrameInstance::isFrameCollidedOnLink  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the frame collided on the link, otherwise false. 

Returns
    bool, true if the frame collided on the link, otherwise false. 

## ◆ isFrameDropped()

bool FrameInstance::isFrameDropped  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the the frame is dropped, otherwise false. 

Returns
    bool, true if the the frame is dropped, otherwise false. 

## ◆ isFrameNotForwarded()

bool FrameInstance::isFrameNotForwarded  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the the frame is not forwarded, otherwise false. 

Returns
    bool, true if the the frame is not forwarded, otherwise false. 

## ◆ isFrameOnTransit()

bool FrameInstance::isFrameOnTransit  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the frame is in transit, otherwise false. 

Returns
    bool, true if the frame is in transit, otherwise false. 

## ◆ isFrameSent()

bool FrameInstance::isFrameSent  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the the frame is sent, otherwise false. 

Returns
    bool, true if the the frame is sent, otherwise false. 

## ◆ isFrameUnexpected()

bool FrameInstance::isFrameUnexpected  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the the frame is unexpected, otherwise false. 

Returns
    bool, true if the the frame is unexpected, otherwise false. 

## ◆ setFrameAccepted()

void FrameInstance::setFrameAccepted  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Sets the frame as accepted or not accepted. 

Parameters
     accepted,true| for accepted, false for not accepted.   
---|---  
  
## ◆ setFrameBuffered()

void FrameInstance::setFrameBuffered  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Sets the frame as buffered or unbuffered. 

Parameters
     buffered,true| for buffered, false for unbuffered.   
---|---  
  
## ◆ setFrameDropped()

void FrameInstance::setFrameDropped  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Sets the frame as dropped or not dropped. 

Parameters
     dropped,true| for dropped, false for not dropped.   
---|---  
  
## ◆ setFrameNotForwarded()

void FrameInstance::setFrameNotForwarded  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Sets the frame as not forwarded or forwarded. 

Parameters
     notForwarded,true| for not forwarded, false for forwarded.   
---|---  
  
## ◆ setFrameSent()

void FrameInstance::setFrameSent  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Sets the frame as sent or unsent. 

Parameters
     sent,true| for sent, false for unsent.   
---|---  
  
## ◆ setFrameUnexpected()

void FrameInstance::setFrameUnexpected  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Sets the frame as unexpected or expected. 

Parameters
     unexpected,true| for unexpected, false for expected.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CFrameInstance.pki](_c_frame_instance_8pki.html)


