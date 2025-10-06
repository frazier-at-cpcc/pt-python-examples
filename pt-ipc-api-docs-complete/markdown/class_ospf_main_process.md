# Cisco Packet Tracer Extensions API: OspfMainProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_ospf_main_process.html

---

[OspfMainProcess](class_ospf_main_process.html "OspfMainProcess is the main process that handles all OSPF processes.") is the main process that handles all OSPF processes. [More...](class_ospf_main_process.html#details)

##  Public Member Functions  
  
---  
bool | [addOspfProcess](class_ospf_main_process.html#af9533f524dc402280189c321f253b262) (int)  
| Adds an OSPF process with the specified ID. [More...](class_ospf_main_process.html#af9533f524dc402280189c321f253b262)  
  
bool | [removeOspfProcess](class_ospf_main_process.html#aeb1f2a7c3748d038621dbbba14a5cdd0) (int)  
| Removes the OSPF process with the specified ID. [More...](class_ospf_main_process.html#aeb1f2a7c3748d038621dbbba14a5cdd0)  
  
[Process](class_process.html) | [getOspfProcessAt](class_ospf_main_process.html#a5853beb7852b92c1bf7033288c3fd161) (int)  
| Returns the OSPF process at the specified index. [More...](class_ospf_main_process.html#a5853beb7852b92c1bf7033288c3fd161)  
  
[Process](class_process.html) | [getOspfProcess](class_ospf_main_process.html#a45a410dfc529ba6e90a72f4526c44121) (int)  
| Returns the OSPF process with the specified ID. [More...](class_ospf_main_process.html#a45a410dfc529ba6e90a72f4526c44121)  
  
int | [getOspfProcessCount](class_ospf_main_process.html#aacd90485969114016fb4320041d841ff) ()  
| Returns the number of OSPF processes. [More...](class_ospf_main_process.html#aacd90485969114016fb4320041d841ff)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[OspfMainProcess](class_ospf_main_process.html "OspfMainProcess is the main process that handles all OSPF processes.") is the main process that handles all OSPF processes. 

## Member Function Documentation

## ◆ addOspfProcess()

bool OspfMainProcess::addOspfProcess  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Adds an OSPF process with the specified ID. 

Parameters
     id,the| ID for the OSPF process.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ getOspfProcess()

[Process](class_process.html) OspfMainProcess::getOspfProcess  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the OSPF process with the specified ID. 

Parameters
     id,the| ID of the OSPF process of interest.  
---|---  
  
Returns
    [Process](class_process.html "Process is the base class for all device processes."), the [Process](class_process.html "Process is the base class for all device processes.") object with the specified ID. 

## ◆ getOspfProcessAt()

[Process](class_process.html) OspfMainProcess::getOspfProcessAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the OSPF process at the specified index. 

Parameters
     index,the| index of the OSPF process of interest.  
---|---  
  
Returns
    [Process](class_process.html "Process is the base class for all device processes."), the [Process](class_process.html "Process is the base class for all device processes.") object at the specified index. 

## ◆ getOspfProcessCount()

int OspfMainProcess::getOspfProcessCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of OSPF processes. 

Returns
    int, the number of OSPF processes. 

## ◆ removeOspfProcess()

bool OspfMainProcess::removeOspfProcess  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Removes the OSPF process with the specified ID. 

Parameters
     id,the| ID of the OSPF process.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

* * *

The documentation for this class was generated from the following file:

  * [COspfMainProcess.pki](_c_ospf_main_process_8pki.html)


