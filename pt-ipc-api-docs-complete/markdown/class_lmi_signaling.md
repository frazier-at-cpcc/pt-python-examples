# Cisco Packet Tracer Extensions API: LmiSignaling Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_lmi_signaling.html

---

##  Public Member Functions  
  
---  
void | [updateTableEvent](class_lmi_signaling.html#acb71d60f1ccafac52d127ec1b504a597) ()  
| This event is emitted when the table is updated. [More...](class_lmi_signaling.html#acb71d60f1ccafac52d127ec1b504a597)  
  
int | [getPacketCnt](class_lmi_signaling.html#a0cdd655bfa8f9c2557129cf9243e1137) ()  
[UserTraffic](class_user_traffic.html) | [getUserTrafficAt](class_lmi_signaling.html#a742ffda2a630e2c9f11acd30599941fe) (int)  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description
    
    
    \brief LmiSignaling handles and manipulates the PPP encapsulation process.
    
    \example network().getDevice("Router0").getProcess("LmiSignaling")
    

## Member Function Documentation

## ◆ getPacketCnt()

int LmiSignaling::getPacketCnt  | ( | | ) |   
---|---|---|---|---  
  
Returns
    int, value is the packet count. 

## ◆ getUserTrafficAt()

[UserTraffic](class_user_traffic.html) LmiSignaling::getUserTrafficAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns
    [UserTraffic](class_user_traffic.html "UserTraffic represents the user traffic information \(PDU\)."), value is the user traffic at the given index. Range (0, [getPacketCnt()](class_lmi_signaling.html#a0cdd655bfa8f9c2557129cf9243e1137)-1). 

## ◆ updateTableEvent()

void LmiSignaling::updateTableEvent  | ( | | ) |   
---|---|---|---|---  
  
This event is emitted when the table is updated. 

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

* * *

The documentation for this class was generated from the following file:

  * [CLmiSignaling.pki](_c_lmi_signaling_8pki.html)


