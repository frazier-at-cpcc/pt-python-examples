# Cisco Packet Tracer Extensions API: FifoQueue Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_fifo_queue.html

---

##  Public Member Functions  
  
---  
int | [getQueueCount](class_fifo_queue.html#a66396dd0169c4b90d8930c83da6f6cef) ()  
| Returns queue count which is 1. [More...](class_fifo_queue.html#a66396dd0169c4b90d8930c83da6f6cef)  
  
[Queue](class_queue.html) | [getQueueAt](class_fifo_queue.html#ad43d98389e7b6ce9d7117c55b6723ae0) (int)  
| Returns the queue but if i > queue count throw exception. [More...](class_fifo_queue.html#ad43d98389e7b6ce9d7117c55b6723ae0)  
  
Public Member Functions inherited from [QueueProcess](class_queue_process.html)  
QoS::EQueueType | [getQueueType](class_queue_process.html#a60bd0854344e36353cb87c8d34bc7cb0) ()  
| Returns the mode. [More...](class_queue_process.html#a60bd0854344e36353cb87c8d34bc7cb0)  
  
  
## Member Function Documentation

## ◆ getQueueAt()

[Queue](class_queue.html) FifoQueue::getQueueAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the queue but if i > queue count throw exception. 

Returns
    [Queue](class_queue.html), the queue. 

## ◆ getQueueCount()

int FifoQueue::getQueueCount  | ( | | ) |   
---|---|---|---|---  
  
Returns queue count which is 1. 

Returns
    int, queue count which is 1. 

* * *

The documentation for this class was generated from the following file:

  * [CFifoQueue.pki](_c_fifo_queue_8pki.html)


