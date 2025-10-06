# Cisco Packet Tracer Extensions API: CableSignaling Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_cable_signaling.html

---

##  Public Member Functions  
  
---  
void | [updateTableEvent](class_cable_signaling.html#a257955224ff6dde811ab4eaa46126316) ()  
| This event is emitted when the device table is updated. [More...](class_cable_signaling.html#a257955224ff6dde811ab4eaa46126316)  
  
int | [getPacketCnt](class_cable_signaling.html#ac084edd05891ed1eed53b2788e706bfc) ()  
| Returns how many packets have been evaluated. [More...](class_cable_signaling.html#ac084edd05891ed1eed53b2788e706bfc)  
  
[UserTraffic](class_user_traffic.html) | [getUserTrafficAt](class_cable_signaling.html#a626e8c84a58577660c5cc45812bc1a6e) (int)  
| Returns the user traffic at the supplied index. [More...](class_cable_signaling.html#a626e8c84a58577660c5cc45812bc1a6e)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description
    
    
    \brief CableSignaling handles and manipulates the PPP encapsulation process.
    
    \example network().getDevice("Router0").getProcess("CableSignaling")
    

## Member Function Documentation

## ◆ getPacketCnt()

int CableSignaling::getPacketCnt  | ( | | ) |   
---|---|---|---|---  
  
Returns how many packets have been evaluated. 

Returns
    int, value is how many packets have been evaluated. 

## ◆ getUserTrafficAt()

[UserTraffic](class_user_traffic.html) CableSignaling::getUserTrafficAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the user traffic at the supplied index. 

Parameters
     index,index| to get the user traffic at.  
---|---  
  
Returns
    UserTrafic, value is the user traffic at the supplied index. 

## ◆ updateTableEvent()

void CableSignaling::updateTableEvent  | ( | | ) |   
---|---|---|---|---  
  
This event is emitted when the device table is updated. 

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

* * *

The documentation for this class was generated from the following file:

  * [CCableSignaling.pki](_c_cable_signaling_8pki.html)


