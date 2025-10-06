# Cisco Packet Tracer Extensions API: RipProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_rip_process.html

---

[RipProcess](class_rip_process.html "RipProcess handles and manipulates RIP routing.") handles and manipulates RIP routing. [More...](class_rip_process.html#details)

##  Public Member Functions  
  
---  
void | [setUpdateTimerInterval](class_rip_process.html#a4fc7416a8a961af05978c00dd38bdf05) (long)  
| Sets the update timer interval. [More...](class_rip_process.html#a4fc7416a8a961af05978c00dd38bdf05)  
  
void | [setAllRipTimerIntervals](class_rip_process.html#a338613ce16b7d8da15228f9d7271cb51) (long, long, long, long)  
| Sets the update timer interval, invalid timer interval, holddown timer interval, and flush interval. [More...](class_rip_process.html#a338613ce16b7d8da15228f9d7271cb51)  
  
void | [setTimersBasicFlag](class_rip_process.html#ae39be764f3a10f621a098f69ef4819a6) (bool)  
| Enables or disables the timers. [More...](class_rip_process.html#ae39be764f3a10f621a098f69ef4819a6)  
  
void | [setAutoSummaryFlag](class_rip_process.html#ac8cbcd0ec461e455c409c6eb3db053c6) (bool)  
| Enables or disables auto summary. [More...](class_rip_process.html#ac8cbcd0ec461e455c409c6eb3db053c6)  
  
void | [setDefaultPassiveInterface](class_rip_process.html#a86776d5a12e3f1fd8403fb5ceb0d0d85) (bool)  
| Enables or disables default passive interface. [More...](class_rip_process.html#a86776d5a12e3f1fd8403fb5ceb0d0d85)  
  
void | [setAdminDistance](class_rip_process.html#ad1f310053421bb3598d88a65227e3ee1) (int)  
| Sets the administrative distance. [More...](class_rip_process.html#ad1f310053421bb3598d88a65227e3ee1)  
  
void | [addRipConfigNetwork](class_rip_process.html#a55260f66dd9825fe1f4873c4b9a05674) (ip)  
| Adds RIP routing on the specified network. [More...](class_rip_process.html#a55260f66dd9825fe1f4873c4b9a05674)  
  
void | [removeRipConfigNetwork](class_rip_process.html#afcc97f92d8588e8d6c04dea48d10a69a) (ip)  
| Removes RIP routing on the specified network. [More...](class_rip_process.html#afcc97f92d8588e8d6c04dea48d10a69a)  
  
void | [addRipConfigNeighbor](class_rip_process.html#ae48eaaa935a2ec3d0980789ea79e5691) (ip)  
| Adds the specified address as a neighbor. [More...](class_rip_process.html#ae48eaaa935a2ec3d0980789ea79e5691)  
  
void | [removeRipConfigNeighbor](class_rip_process.html#a57a81500de0f5895a6e847ab3d17e1e6) (ip)  
| Removes the specified address as a neighbor. [More...](class_rip_process.html#a57a81500de0f5895a6e847ab3d17e1e6)  
  
void | [setDebugRipDatabaseFlag](class_rip_process.html#a81430e7eae9d1b38cc43f38d63d05d6d) (bool)  
| Enables or disables debug rip database. [More...](class_rip_process.html#a81430e7eae9d1b38cc43f38d63d05d6d)  
  
void | [setDebugRipFlag](class_rip_process.html#a3cca9c049211ab3872f56eea5f74329e) (bool)  
| Enables or disables debug rip. [More...](class_rip_process.html#a3cca9c049211ab3872f56eea5f74329e)  
  
void | [setDebugRipEventFlag](class_rip_process.html#a5bf1b74daee4ca7e9b81ce7e42da0f62) (bool)  
| Enables or disables debug rip events. [More...](class_rip_process.html#a5bf1b74daee4ca7e9b81ce7e42da0f62)  
  
void | [setDebugRipTriggerFlag](class_rip_process.html#a2c9651a0fc89ef500536629f4f091b79) (bool)  
| Enables or disables debug rip trigger. [More...](class_rip_process.html#a2c9651a0fc89ef500536629f4f091b79)  
  
void | [setDefaultInformationOriginate](class_rip_process.html#a1c1bf82b56ed556e83172cd7eaef2f69) (bool)  
| Enables or disables default information originate. [More...](class_rip_process.html#a1c1bf82b56ed556e83172cd7eaef2f69)  
  
Public Member Functions inherited from [RoutingProtocol](class_routing_protocol.html)  
void | [setAdminDistance](class_routing_protocol.html#a1f39516098814724cf82c520c510de71) (int)  
| Sets the administrative distance. [More...](class_routing_protocol.html#a1f39516098814724cf82c520c510de71)  
  
int | [getAdminDistance](class_routing_protocol.html#a297c8e3af679475657e71c9363970289) ()  
| Returns the administrative distance. [More...](class_routing_protocol.html#a297c8e3af679475657e71c9363970289)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[RipProcess](class_rip_process.html "RipProcess handles and manipulates RIP routing.") handles and manipulates RIP routing. 

## Member Function Documentation

## ◆ addRipConfigNeighbor()

void RipProcess::addRipConfigNeighbor  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Adds the specified address as a neighbor. 

Parameters
     neighborAddress,the| IP address of the neighbor.   
---|---  
  
## ◆ addRipConfigNetwork()

void RipProcess::addRipConfigNetwork  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Adds RIP routing on the specified network. 

Parameters
     networkAddress,the| network address to add.   
---|---  
  
## ◆ removeRipConfigNeighbor()

void RipProcess::removeRipConfigNeighbor  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Removes the specified address as a neighbor. 

Parameters
     neighborAddress,the| IP address of the neighbor.   
---|---  
  
## ◆ removeRipConfigNetwork()

void RipProcess::removeRipConfigNetwork  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Removes RIP routing on the specified network. 

Parameters
     networkAddress,the| network address to remove.   
---|---  
  
## ◆ setAdminDistance()

void RipProcess::setAdminDistance  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the administrative distance. 

Parameters
     adminDistance,the| administrative distance value.   
---|---  
  
## ◆ setAllRipTimerIntervals()

void RipProcess::setAllRipTimerIntervals  | ( | long  | ,   
---|---|---|---  
|  | long  | ,   
|  | long  | ,   
|  | long  |   
| ) | |   
  
Sets the update timer interval, invalid timer interval, holddown timer interval, and flush interval. 

Parameters
     updateTimerInterval,the| update timer interval.   
---|---  
invalidTimerInterval,invalid| (timeout) timer interval.   
holddownInterval,the| holddown timer interval.   
flushInterval,the| flush interval.   
  
## ◆ setAutoSummaryFlag()

void RipProcess::setAutoSummaryFlag  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables auto summary. 

Parameters
     bAutoSummary,true| to enable auto summary, false to disable it.   
---|---  
  
## ◆ setDebugRipDatabaseFlag()

void RipProcess::setDebugRipDatabaseFlag  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables debug rip database. 

Parameters
     bDebugRipDatabase,true| to enable debug rip database, false to disable it.   
---|---  
  
## ◆ setDebugRipEventFlag()

void RipProcess::setDebugRipEventFlag  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables debug rip events. 

Parameters
     bDebugRipEventFlag,true| to enable debug rip events, false to disable it.   
---|---  
  
## ◆ setDebugRipFlag()

void RipProcess::setDebugRipFlag  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables debug rip. 

Parameters
     bFlag,true| to enable debug rip, false to disable it.   
---|---  
  
## ◆ setDebugRipTriggerFlag()

void RipProcess::setDebugRipTriggerFlag  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables debug rip trigger. 

Parameters
     bDebugRipTriggerFlag,true| to enable debug rip trigger, false to disable it.   
---|---  
  
## ◆ setDefaultInformationOriginate()

void RipProcess::setDefaultInformationOriginate  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables default information originate. 

Parameters
     bOriginate,true| to enable default information originate, false to disable it.   
---|---  
  
## ◆ setDefaultPassiveInterface()

void RipProcess::setDefaultPassiveInterface  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables default passive interface. 

Parameters
     bAutoSummary,true| to enable default passive interface., false to disable it.   
---|---  
  
## ◆ setTimersBasicFlag()

void RipProcess::setTimersBasicFlag  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables the timers. 

Parameters
     isEnabled,true| to enable the timers, false to disable it.   
---|---  
  
## ◆ setUpdateTimerInterval()

void RipProcess::setUpdateTimerInterval  | ( | long  | | ) |   
---|---|---|---|---|---  
  
Sets the update timer interval. 

Parameters
     updateTimerInterval,the| update timer interval.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CRipProcess.pki](_c_rip_process_8pki.html)


