# Cisco Packet Tracer Extensions API: Link Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_link.html

---

[Link](class_link.html "Link is the class that handles the connection link.") is the class that handles the connection link. [More...](class_link.html#details)

##  Public Member Functions  
  
---  
CONNECT_TYPES | [getConnectionType](class_link.html#aecc94aebc68660bfa68b14b99dd17fc7) ()  
| Returns the connection type. [More...](class_link.html#aecc94aebc68660bfa68b14b99dd17fc7)  
  
  
## Detailed Description

[Link](class_link.html "Link is the class that handles the connection link.") is the class that handles the connection link. 

## Member Function Documentation

## ◆ getConnectionType()

CONNECT_TYPES Link::getConnectionType  | ( | | ) |   
---|---|---|---|---  
  
Returns the connection type. 

Returns
    enum<CONNECT_TYPES>, the connection type. Connection types: FIRST_TYPE = 8100, ETHERNET_STRAIGHT = FIRST_TYPE, ETHERNET_CROSS, ETHERNET_ROLL, FIBER, PHONE, CABLE, SERIAL, AUTO, CONSOLE, WIRELESS, COAXIAL, OCTAL, CELLULAR, USB, CUSTOM_IO, BLUETOOTH_PAIRED, BLUETOOTH_BROADCAST, LAST_TYPE = BLUETOOTH_BROADCAST 

* * *

The documentation for this class was generated from the following file:

  * [CLink.pki](_c_link_8pki.html)


