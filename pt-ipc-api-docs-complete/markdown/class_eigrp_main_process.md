# Cisco Packet Tracer Extensions API: EigrpMainProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_eigrp_main_process.html

---

[EigrpMainProcess](class_eigrp_main_process.html "EigrpMainProcess is the main process that handles all EIGRP processes.") is the main process that handles all EIGRP processes. [More...](class_eigrp_main_process.html#details)

##  Public Member Functions  
  
---  
void | [addEigrpProcess](class_eigrp_main_process.html#af5f4419ce0861f0eeb5aaf2d965fc28c) (int)  
| Adds the EIGRP process with the specified AS number. [More...](class_eigrp_main_process.html#af5f4419ce0861f0eeb5aaf2d965fc28c)  
  
void | [removeEigrpProcess](class_eigrp_main_process.html#a7bdf12bad3d7e389f3bd4533397a9f76) (int)  
| Removes the EIGRP process with the specified AS number. [More...](class_eigrp_main_process.html#a7bdf12bad3d7e389f3bd4533397a9f76)  
  
[EigrpProcess](class_eigrp_process.html) | [getEigrpProcessAt](class_eigrp_main_process.html#a13675588486c1941328b4e63f784e1a0) (int)  
| Returns the EIGRP process at the specified index. [More...](class_eigrp_main_process.html#a13675588486c1941328b4e63f784e1a0)  
  
[EigrpProcess](class_eigrp_process.html) | [getEigrpProcess](class_eigrp_main_process.html#a5b8910bf8af49a71afbf5b5d32e6dac8) (int)  
| Returns the EIGRP process with the specified AS number. [More...](class_eigrp_main_process.html#a5b8910bf8af49a71afbf5b5d32e6dac8)  
  
int | [getEigrpProcessCount](class_eigrp_main_process.html#a1e3bbb04ecc4e477029aa08b978eca77) ()  
| Returns the number of EIGRP processes. [More...](class_eigrp_main_process.html#a1e3bbb04ecc4e477029aa08b978eca77)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[EigrpMainProcess](class_eigrp_main_process.html "EigrpMainProcess is the main process that handles all EIGRP processes.") is the main process that handles all EIGRP processes. 

## Member Function Documentation

## ◆ addEigrpProcess()

void EigrpMainProcess::addEigrpProcess  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Adds the EIGRP process with the specified AS number. 

Parameters
     as,the| AS number of the EIGRP process.   
---|---  
  
## ◆ getEigrpProcess()

[EigrpProcess](class_eigrp_process.html) EigrpMainProcess::getEigrpProcess  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the EIGRP process with the specified AS number. 

Parameters
     as,the| AS number of the EIGRP process of interest.  
---|---  
  
Returns
    [EigrpProcess](class_eigrp_process.html "EigrpProcess is the process that handles the individual EIGRP AS process."), the [EigrpProcess](class_eigrp_process.html "EigrpProcess is the process that handles the individual EIGRP AS process.") object with the specified AS number. 

## ◆ getEigrpProcessAt()

[EigrpProcess](class_eigrp_process.html) EigrpMainProcess::getEigrpProcessAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the EIGRP process at the specified index. 

Parameters
     index,the| index of the EIGRP process of interest.  
---|---  
  
Returns
    [EigrpProcess](class_eigrp_process.html "EigrpProcess is the process that handles the individual EIGRP AS process."), the [EigrpProcess](class_eigrp_process.html "EigrpProcess is the process that handles the individual EIGRP AS process.") object at the specified index. 

## ◆ getEigrpProcessCount()

int EigrpMainProcess::getEigrpProcessCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of EIGRP processes. 

Returns
    int, the number of EIGRP processes. 

## ◆ removeEigrpProcess()

void EigrpMainProcess::removeEigrpProcess  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Removes the EIGRP process with the specified AS number. 

Parameters
     as,the| AS number of the EIGRP process of interest.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CEigrpMainProcess.pki](_c_eigrp_main_process_8pki.html)


