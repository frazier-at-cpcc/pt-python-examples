# Cisco Packet Tracer Extensions API: QueueProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_queue_process.html

---

##  Public Member Functions  
  
---  
QoS::EQueueType | [getQueueType](class_queue_process.html#a60bd0854344e36353cb87c8d34bc7cb0) ()  
| Returns the mode. [More...](class_queue_process.html#a60bd0854344e36353cb87c8d34bc7cb0)  
  
  
## Detailed Description
    
    
    \brief QueueProcess handles the class maps for QoS.
    

## Member Function Documentation

## ◆ getQueueType()

QoS::EQueueType QueueProcess::getQueueType  | ( | | ) |   
---|---|---|---|---  
  
Returns the mode. 

Returns
    enum<PTPMode>, the modes. Mode types: eFifoQueue = 0, ePriorityQueue = 1, eStrictPriorityQueue = 2, eCustomQueue = 3, eWeightedFairQueue = 4, eClassBasedWeightedFairQueue = 5, eLowLatencyQueue = 6 

* * *

The documentation for this class was generated from the following file:

  * [CQueueProcess.pki](_c_queue_process_8pki.html)


