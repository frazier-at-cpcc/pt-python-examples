# Cisco Packet Tracer Extensions API: Antenna Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_antenna.html

---

The [Antenna](class_antenna.html "The Antenna class represents the wireless link.") class represents the wireless link. [More...](class_antenna.html#details)

##  Public Member Functions  
  
---  
[Port](class_port.html) | [getPort](class_antenna.html#a6485005818ad8c78304a3ae14f6dd130) ()  
| Returns the port object associated with this [Antenna](class_antenna.html "The Antenna class represents the wireless link."). [More...](class_antenna.html#a6485005818ad8c78304a3ae14f6dd130)  
  
int | [getReceiverCount](class_antenna.html#aba0d8cae00c1ce57e0a91b3f0995f0f4) ()  
| Returns the number of receivers associated with this [Antenna](class_antenna.html "The Antenna class represents the wireless link."). [More...](class_antenna.html#aba0d8cae00c1ce57e0a91b3f0995f0f4)  
  
[Antenna](class_antenna.html) | [getReceiverAt](class_antenna.html#adca7560c013cfb32cf98f897fc75de86) (int)  
| Returns the [Antenna](class_antenna.html "The Antenna class represents the wireless link.") receiver at the specified index. [More...](class_antenna.html#adca7560c013cfb32cf98f897fc75de86)  
  
Public Member Functions inherited from [Link](class_link.html)  
CONNECT_TYPES | [getConnectionType](class_link.html#aecc94aebc68660bfa68b14b99dd17fc7) ()  
| Returns the connection type. [More...](class_link.html#aecc94aebc68660bfa68b14b99dd17fc7)  
  
  
## Detailed Description

The [Antenna](class_antenna.html "The Antenna class represents the wireless link.") class represents the wireless link. 

## Member Function Documentation

## ◆ getPort()

[Port](class_port.html) Antenna::getPort  | ( | | ) |   
---|---|---|---|---  
  
Returns the port object associated with this [Antenna](class_antenna.html "The Antenna class represents the wireless link."). 

Returns
    [Port](class_port.html "Port holds and manipulates the ports on devices."), the port object associated with this [Antenna](class_antenna.html "The Antenna class represents the wireless link."). 

## ◆ getReceiverAt()

[Antenna](class_antenna.html) Antenna::getReceiverAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the [Antenna](class_antenna.html "The Antenna class represents the wireless link.") receiver at the specified index. 

Parameters
     int| index, the index of [Antenna](class_antenna.html "The Antenna class represents the wireless link.") receiver.  
---|---  
  
Returns
    [Antenna](class_antenna.html "The Antenna class represents the wireless link."), the [Antenna](class_antenna.html "The Antenna class represents the wireless link.") receiver at the specified index. 

## ◆ getReceiverCount()

int Antenna::getReceiverCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of receivers associated with this [Antenna](class_antenna.html "The Antenna class represents the wireless link."). 

Returns
    int, the number of receivers associated with this [Antenna](class_antenna.html "The Antenna class represents the wireless link."). 

* * *

The documentation for this class was generated from the following file:

  * [CAntenna.pki](_c_antenna_8pki.html)


