# Cisco Packet Tracer Extensions API: PhoneSignaling Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_phone_signaling.html

---

##  Public Member Functions  
  
---  
void | [updateTableEvent](class_phone_signaling.html#a0b0b00ea35695365a7bf7b099b0fba54) ()  
| Triggered when the table is updated. [More...](class_phone_signaling.html#a0b0b00ea35695365a7bf7b099b0fba54)  
  
int | [getPacketCnt](class_phone_signaling.html#ab6b36d17f58c0817de259f82f15de0c7) ()  
| Returns the packet count. [More...](class_phone_signaling.html#ab6b36d17f58c0817de259f82f15de0c7)  
  
[UserTraffic](class_user_traffic.html) | [getUserTrafficAt](class_phone_signaling.html#a441fbc251e7c9e2e46c62a1b916b3b36) (int)  
| Returns the user traffic at the given index. [More...](class_phone_signaling.html#a441fbc251e7c9e2e46c62a1b916b3b36)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description
    
    
    \brief PhoneSignaling handles and manipulates the PPP encapsulation process.
    
    \example network().getDevice("Router0").getProcess("PhoneSignaling")
    

## Member Function Documentation

## ◆ getPacketCnt()

int PhoneSignaling::getPacketCnt  | ( | | ) |   
---|---|---|---|---  
  
Returns the packet count. 

Returns
    int, the packet count. 

## ◆ getUserTrafficAt()

[UserTraffic](class_user_traffic.html) PhoneSignaling::getUserTrafficAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the user traffic at the given index. 

Parameters
     index,index| to get the traffic at.  
---|---  
  
Returns
    [UserTraffic](class_user_traffic.html "UserTraffic represents the user traffic information \(PDU\)."), traffic at the specified index. 

## ◆ updateTableEvent()

void PhoneSignaling::updateTableEvent  | ( | | ) |   
---|---|---|---|---  
  
Triggered when the table is updated. 

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

* * *

The documentation for this class was generated from the following file:

  * [CPhoneSignaling.pki](_c_phone_signaling_8pki.html)


