# Cisco Packet Tracer Extensions API: PriorityQueue Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_priority_queue.html

---

##  Public Member Functions  
  
---  
int | [getQueueCount](class_priority_queue.html#a4c6e31f98650b2ea7b730408ade8076c) ()  
| Returns the queue count. [More...](class_priority_queue.html#a4c6e31f98650b2ea7b730408ade8076c)  
  
[Queue](class_queue.html) | [getQueueAt](class_priority_queue.html#a553d2a44c4f45ca9e7f291a5278349cc) (int)  
| Returns the queue at the specified index. [More...](class_priority_queue.html#a553d2a44c4f45ca9e7f291a5278349cc)  
  
Public Member Functions inherited from [QueueProcess](class_queue_process.html)  
QoS::EQueueType | [getQueueType](class_queue_process.html#a60bd0854344e36353cb87c8d34bc7cb0) ()  
| Returns the mode. [More...](class_queue_process.html#a60bd0854344e36353cb87c8d34bc7cb0)  
  
  
## Member Function Documentation

## ◆ getQueueAt()

[Queue](class_queue.html) PriorityQueue::getQueueAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the queue at the specified index. 

Parameters
     i,index| to get the queue at. Range(0, getQueueCount()).  
---|---  
  
Returns
    [Queue](class_queue.html), the queue at the specified index. 

## ◆ getQueueCount()

int PriorityQueue::getQueueCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the queue count. 

Returns
    int, the queue count. 

* * *

The documentation for this class was generated from the following file:

  * [CPriorityQueue.pki](_c_priority_queue_8pki.html)


