# Cisco Packet Tracer Extensions API: Cable Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_cable.html

---

[Cable](class_cable.html "Cable is the generic cable class with two endpoints.") is the generic cable class with two endpoints. [More...](class_cable.html#details)

##  Public Member Functions  
  
---  
[Port](class_port.html) | [getPort1](class_cable.html#a918433abcdfbb6f3818cb5758bc8cf67) ()  
| Returns the port on the first end of the cable. [More...](class_cable.html#a918433abcdfbb6f3818cb5758bc8cf67)  
  
[Port](class_port.html) | [getPort2](class_cable.html#a73396aa84d95b8b10ce444a7a443b257) ()  
| Returns the port on the second end of the cable. [More...](class_cable.html#a73396aa84d95b8b10ce444a7a443b257)  
  
[Port](class_port.html) | [getOtherPort](class_cable.html#a4bb8f15258031cfc8ce8def0a65b9361) (string, string)  
| Returns the other port based on the specified port on one side of the cable. [More...](class_cable.html#a4bb8f15258031cfc8ce8def0a65b9361)  
  
Public Member Functions inherited from [Link](class_link.html)  
CONNECT_TYPES | [getConnectionType](class_link.html#aecc94aebc68660bfa68b14b99dd17fc7) ()  
| Returns the connection type. [More...](class_link.html#aecc94aebc68660bfa68b14b99dd17fc7)  
  
  
## Detailed Description

[Cable](class_cable.html "Cable is the generic cable class with two endpoints.") is the generic cable class with two endpoints. 

## Member Function Documentation

## ◆ getOtherPort()

[Port](class_port.html) Cable::getOtherPort  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Returns the other port based on the specified port on one side of the cable. 

Parameters
     deviceName,name| of the device (not the IOS name)   
---|---  
portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
  
Returns
    [Port](class_port.html "Port holds and manipulates the ports on devices."), value is the other port based on the specified port on one side of the cable.   


## ◆ getPort1()

[Port](class_port.html) Cable::getPort1  | ( | | ) |   
---|---|---|---|---  
  
Returns the port on the first end of the cable. 

Returns
    [Port](class_port.html "Port holds and manipulates the ports on devices."), the port on the first end of the cable. 

## ◆ getPort2()

[Port](class_port.html) Cable::getPort2  | ( | | ) |   
---|---|---|---|---  
  
Returns the port on the second end of the cable. 

Returns
    [Port](class_port.html "Port holds and manipulates the ports on devices."), the port on the second end of the cable. 

* * *

The documentation for this class was generated from the following file:

  * [CCable.pki](_c_cable_8pki.html)


