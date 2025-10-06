# Cisco Packet Tracer Extensions API: UserTraffic Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_user_traffic.html

---

[UserTraffic](class_user_traffic.html "UserTraffic represents the user traffic information \(PDU\).") represents the user traffic information (PDU). [More...](class_user_traffic.html#details)

##  Public Member Functions  
  
---  
int | [getTrafficColorCode](class_user_traffic.html#aa642e9015cd2f4d71b7a91208602174e) ()  
| Returns the color code of this PDU. [More...](class_user_traffic.html#aa642e9015cd2f4d71b7a91208602174e)  
  
QString | [getTrafficTypeString](class_user_traffic.html#a8bf20c4aecdb1cc18925d6f7f6d9d7ed) ()  
| Returns the traffic type of this PDU. [More...](class_user_traffic.html#a8bf20c4aecdb1cc18925d6f7f6d9d7ed)  
  
[Device](class_device.html) | [getSourceDevice](class_user_traffic.html#a2e0adbb9ffd369c757f819bae51ead0a) ()  
| Returns the source device of this PDU. [More...](class_user_traffic.html#a2e0adbb9ffd369c757f819bae51ead0a)  
  
[Device](class_device.html) | [getDestinationDevice](class_user_traffic.html#a062452b46a973713c89dba1ce5e08898) ()  
| Returns the destination device of this PDU. [More...](class_user_traffic.html#a062452b46a973713c89dba1ce5e08898)  
  
[Pdu](struct_pdu.html) | [getPdu](class_user_traffic.html#ab65cd06072d4f9b2c0433e2780290344) ()  
| Returns the PDU object of this PDU. [More...](class_user_traffic.html#ab65cd06072d4f9b2c0433e2780290344)  
  
[Port](class_port.html) | [getSendPort](class_user_traffic.html#a10ed6ffea9e0e45b2421e85edd941356) ()  
| Returns the sending port of this PDU. [More...](class_user_traffic.html#a10ed6ffea9e0e45b2421e85edd941356)  
  
QString | [getCanonicalSource](class_user_traffic.html#aaadad21e6654232ac55cca54fa775dcb) ()  
| Returns the name of the source of this PDU. [More...](class_user_traffic.html#aaadad21e6654232ac55cca54fa775dcb)  
  
QString | [getCanonicalDestination](class_user_traffic.html#a804a6ae684e3a5995e9249e49a8b1448) ()  
| Returns the name of the destination of this PDU. [More...](class_user_traffic.html#a804a6ae684e3a5995e9249e49a8b1448)  
  
TrafficStatus | [getStatus](class_user_traffic.html#a445d44ea6c0b187bc0fb2114737a6314) ()  
| Returns the status of this PDU. [More...](class_user_traffic.html#a445d44ea6c0b187bc0fb2114737a6314)  
  
TrafficStatus | [getTestCondition](class_user_traffic.html#aa80ffb77cdcddd961d22b6dded1dcd09) ()  
| Returns the connectivity test status of this PDU. [More...](class_user_traffic.html#aa80ffb77cdcddd961d22b6dded1dcd09)  
  
int | [getPoints](class_user_traffic.html#aeb2e212ae5b96ab986c6f968f044aa10) ()  
| Returns the point value of this PDU. [More...](class_user_traffic.html#aeb2e212ae5b96ab986c6f968f044aa10)  
  
int | [getPduSize](class_user_traffic.html#aeb0e517232e170afddc25908255bd8f2) ()  
| Returns the size of this PDU. [More...](class_user_traffic.html#aeb0e517232e170afddc25908255bd8f2)  
  
  
## Detailed Description

[UserTraffic](class_user_traffic.html "UserTraffic represents the user traffic information \(PDU\).") represents the user traffic information (PDU). 

## Member Function Documentation

## ◆ getCanonicalDestination()

QString UserTraffic::getCanonicalDestination  | ( | | ) |   
---|---|---|---|---  
  
Returns the name of the destination of this PDU. 

Returns
    QString, the name of the destination of this PDU. 

## ◆ getCanonicalSource()

QString UserTraffic::getCanonicalSource  | ( | | ) |   
---|---|---|---|---  
  
Returns the name of the source of this PDU. 

Returns
    QString, the name of the source of this PDU. 

## ◆ getDestinationDevice()

[Device](class_device.html) UserTraffic::getDestinationDevice  | ( | | ) |   
---|---|---|---|---  
  
Returns the destination device of this PDU. 

Returns
    [Device](class_device.html "Device is the base class for all device objects."), the [Device](class_device.html "Device is the base class for all device objects.") object of the destination device of this PDU. 

## ◆ getPdu()

[Pdu](struct_pdu.html) UserTraffic::getPdu  | ( | | ) |   
---|---|---|---|---  
  
Returns the PDU object of this PDU. 

Returns
    PDU, the PDU object of this PDU. 

## ◆ getPduSize()

int UserTraffic::getPduSize  | ( | | ) |   
---|---|---|---|---  
  
Returns the size of this PDU. 

Returns
    int, the size of this PDU. 

## ◆ getPoints()

int UserTraffic::getPoints  | ( | | ) |   
---|---|---|---|---  
  
Returns the point value of this PDU. 

Returns
    int, the point value of this PDU. 

## ◆ getSendPort()

[Port](class_port.html) UserTraffic::getSendPort  | ( | | ) |   
---|---|---|---|---  
  
Returns the sending port of this PDU. 

Returns
    [Port](class_port.html "Port holds and manipulates the ports on devices."), the [Port](class_port.html "Port holds and manipulates the ports on devices.") object of the sending port of this PDU. 

## ◆ getSourceDevice()

[Device](class_device.html) UserTraffic::getSourceDevice  | ( | | ) |   
---|---|---|---|---  
  
Returns the source device of this PDU. 

Returns
    [Device](class_device.html "Device is the base class for all device objects."), the [Device](class_device.html "Device is the base class for all device objects.") object of the source device of this PDU. 

## ◆ getStatus()

TrafficStatus UserTraffic::getStatus  | ( | | ) |   
---|---|---|---|---  
  
Returns the status of this PDU. 

Returns
    enum<TrafficStatus>, the status of this PDU. Traffic statuses: eTrafficNotSend = 0, eTrafficInProgress = 1, eTrafficFailed = 2, eTrafficSuccessful = 3 

## ◆ getTestCondition()

TrafficStatus UserTraffic::getTestCondition  | ( | | ) |   
---|---|---|---|---  
  
Returns the connectivity test status of this PDU. 

Returns
    enum<TrafficStatus>, the the test condition status of this PDU. Traffic statuses: eTrafficNotSend = 0, eTrafficInProgress = 1, eTrafficFailed = 2, eTrafficSuccessful = 3 

## ◆ getTrafficColorCode()

int UserTraffic::getTrafficColorCode  | ( | | ) |   
---|---|---|---|---  
  
Returns the color code of this PDU. 

Returns
    int, the color code of this PDU. 

## ◆ getTrafficTypeString()

QString UserTraffic::getTrafficTypeString  | ( | | ) |   
---|---|---|---|---  
  
Returns the traffic type of this PDU. 

Returns
    QString, the traffic type of this PDU. 

* * *

The documentation for this class was generated from the following file:

  * [CUserTraffic.pki](_c_user_traffic_8pki.html)


