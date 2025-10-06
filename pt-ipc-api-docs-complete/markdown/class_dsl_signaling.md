# Cisco Packet Tracer Extensions API: DslSignaling Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_dsl_signaling.html

---

##  Public Member Functions  
  
---  
void | [updateTableEvent](class_dsl_signaling.html#a0262f3287bfc89fdd040571e47a3b286) ()  
| Event is emitted when the hardware queue table is updated. [More...](class_dsl_signaling.html#a0262f3287bfc89fdd040571e47a3b286)  
  
int | [getPacketCnt](class_dsl_signaling.html#a1d585358f7e811cc42124522d52a37d5) ()  
| Returns the number of packets. [More...](class_dsl_signaling.html#a1d585358f7e811cc42124522d52a37d5)  
  
[UserTraffic](class_user_traffic.html) | [getUserTrafficAt](class_dsl_signaling.html#ae88a374f7eab954f7a19400515b339ee) (int)  
| Returns the [UserTraffic](class_user_traffic.html "UserTraffic represents the user traffic information \(PDU\).") at the specified index. [More...](class_dsl_signaling.html#ae88a374f7eab954f7a19400515b339ee)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description
    
    
    \brief DslSignaling handles and manipulates the PPP encapsulation process.
    
    \example network().getDevice("Router0").getProcess("DslSignaling")
    

## Member Function Documentation

## ◆ getPacketCnt()

int DslSignaling::getPacketCnt  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of packets. 

Returns
    int, number of packets 

## ◆ getUserTrafficAt()

[UserTraffic](class_user_traffic.html) DslSignaling::getUserTrafficAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the [UserTraffic](class_user_traffic.html "UserTraffic represents the user traffic information \(PDU\).") at the specified index. 

Parameters
     index,specified| index  
---|---  
  
Returns
    [UserTraffic](class_user_traffic.html "UserTraffic represents the user traffic information \(PDU\)."), [UserTraffic](class_user_traffic.html "UserTraffic represents the user traffic information \(PDU\).") boject 

## ◆ updateTableEvent()

void DslSignaling::updateTableEvent  | ( | | ) |   
---|---|---|---|---  
  
Event is emitted when the hardware queue table is updated. 

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

* * *

The documentation for this class was generated from the following file:

  * [CDslSignaling.pki](_c_dsl_signaling_8pki.html)


