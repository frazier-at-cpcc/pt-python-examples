# Cisco Packet Tracer Extensions API: LowLatencyQueue Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_low_latency_queue.html

---

##  Public Member Functions  
  
---  
int | [getQueueCount](class_low_latency_queue.html#abd2a4584ccbfe28445e793e237a27d33) ()  
| Returns the number of entries in the queue. [More...](class_low_latency_queue.html#abd2a4584ccbfe28445e793e237a27d33)  
  
[Queue](class_queue.html) | [getQueueAt](class_low_latency_queue.html#afcef851966bb707c7131e823e5c1d4b8) (int)  
| Returns the queue entery at the given index. [More...](class_low_latency_queue.html#afcef851966bb707c7131e823e5c1d4b8)  
  
Public Member Functions inherited from [QueueProcess](class_queue_process.html)  
QoS::EQueueType | [getQueueType](class_queue_process.html#a60bd0854344e36353cb87c8d34bc7cb0) ()  
| Returns the mode. [More...](class_queue_process.html#a60bd0854344e36353cb87c8d34bc7cb0)  
  
  
## Member Function Documentation

## ◆ getQueueAt()

[Queue](class_queue.html) LowLatencyQueue::getQueueAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the queue entery at the given index. 

Returns
    [Queue](class_queue.html), value is the queue entry at the given index. Range(0, [getQueueCount()](class_low_latency_queue.html#abd2a4584ccbfe28445e793e237a27d33 "Returns the number of entries in the queue.")-1). 

## ◆ getQueueCount()

int LowLatencyQueue::getQueueCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of entries in the queue. 

Returns
    int, value is the number of entries in the queue. 

* * *

The documentation for this class was generated from the following file:

  * [CLowLatencyQueue.pki](_c_low_latency_queue_8pki.html)


