# Cisco Packet Tracer Extensions API: HardwareQueue Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_hardware_queue.html

---

##  Public Member Functions  
  
---  
void | [updateTableEvent](class_hardware_queue.html#ae28d3ea7bb93d5e69dcb8802e158f076) ()  
| This event is emitted when update event table. [More...](class_hardware_queue.html#ae28d3ea7bb93d5e69dcb8802e158f076)  
  
int | [getPacketCnt](class_hardware_queue.html#a85767cf28c41e3cb6887b983d8b94fc9) ()  
| Returns the number of packets. [More...](class_hardware_queue.html#a85767cf28c41e3cb6887b983d8b94fc9)  
  
[UserTraffic](class_user_traffic.html) | [getUserTrafficAt](class_hardware_queue.html#a4033baf2c266ed87b29631dcbbe3d6ec) (int)  
| Returns the [UserTraffic](class_user_traffic.html "UserTraffic represents the user traffic information \(PDU\).") object. [More...](class_hardware_queue.html#a4033baf2c266ed87b29631dcbbe3d6ec)  
  
  
## Detailed Description
    
    
    \brief HardwareQueue handles and manipulates switch ports.
    

## Member Function Documentation

## ◆ getPacketCnt()

int HardwareQueue::getPacketCnt  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of packets. 

Returns
    int, the number of packets. 

## ◆ getUserTrafficAt()

[UserTraffic](class_user_traffic.html) HardwareQueue::getUserTrafficAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the [UserTraffic](class_user_traffic.html "UserTraffic represents the user traffic information \(PDU\).") object. 

Parameters
     int,index| of [UserTraffic](class_user_traffic.html "UserTraffic represents the user traffic information \(PDU\).") in the queue.  
---|---  
  
Returns
    [UserTraffic](class_user_traffic.html "UserTraffic represents the user traffic information \(PDU\)."), the [UserTraffic](class_user_traffic.html "UserTraffic represents the user traffic information \(PDU\).") object. 

## ◆ updateTableEvent()

void HardwareQueue::updateTableEvent  | ( | | ) |   
---|---|---|---|---  
  
This event is emitted when update event table. 

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

* * *

The documentation for this class was generated from the following file:

  * [CHardwareQueue.pki](_c_hardware_queue_8pki.html)


