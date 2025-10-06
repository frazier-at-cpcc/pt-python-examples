# Cisco Packet Tracer Extensions API: StpProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_stp_process.html

---

[StpProcess](class_stp_process.html "StpProcess handles and manipulates STP processes.") handles and manipulates STP processes. [More...](class_stp_process.html#details)

##  Public Member Functions  
  
---  
int | [getSwitchPriority](class_stp_process.html#aee84227182018bb6ad901cc37ff0c6a5) ()  
| Returns the priority. [More...](class_stp_process.html#aee84227182018bb6ad901cc37ff0c6a5)  
  
string | [getRootBridgeId](class_stp_process.html#a5d1e2d6b201952210ea2d222485cc30a) ()  
| Returns the root bridge ID. [More...](class_stp_process.html#a5d1e2d6b201952210ea2d222485cc30a)  
  
int | [getPortCount](class_stp_process.html#ae54ec64b2468d5c83caab7f229694adb) ()  
| Returns the number of ports in the STP process. [More...](class_stp_process.html#ae54ec64b2468d5c83caab7f229694adb)  
  
bool | [isRootBridge](class_stp_process.html#a177630f85baaa13357246d0bcfef4ef3) ()  
| Returns true if this switch is the root bridge, otherwise false. [More...](class_stp_process.html#a177630f85baaa13357246d0bcfef4ef3)  
  
string | [getSwitchId](class_stp_process.html#a4e8a7d8c328ef497fd8b376c0e79bc8f) ()  
| Returns the ID for this switch. [More...](class_stp_process.html#a4e8a7d8c328ef497fd8b376c0e79bc8f)  
  
bool | [hasPort](class_stp_process.html#a37e1e793118c8bcdcd4b762f6d2e9720) (string)  
| Returns true if the specified port is in this STP process, otherwise false. [More...](class_stp_process.html#a37e1e793118c8bcdcd4b762f6d2e9720)  
  
[SwitchPort](class_switch_port.html) | [getRootPort](class_stp_process.html#a34f45d5e8085dd57deeee3218d0f5efa) ()  
| Returns the root port in this STP process. [More...](class_stp_process.html#a34f45d5e8085dd57deeee3218d0f5efa)  
  
int | [getRootPathCost](class_stp_process.html#a4f3bacd68b0ce01f5fc4076237e0ac6f) ()  
| Returns the root path cost. [More...](class_stp_process.html#a4f3bacd68b0ce01f5fc4076237e0ac6f)  
  
void | [rootChanged](class_stp_process.html#a6466ae6c171352b042c611d6dde0d99a) (QString, int, mac, int, mac, int)  
| This event is emitted when the root bridge is changed. [More...](class_stp_process.html#a6466ae6c171352b042c611d6dde0d99a)  
  
void | [stpPortStateChanged](class_stp_process.html#a08bfbf6fed6897743a24adb346568d6f) (QString, int, int, StpPortState, StpPortState)  
| This event is emitted when the PVST+ port state for this VLAN changes. [More...](class_stp_process.html#a08bfbf6fed6897743a24adb346568d6f)  
  
void | [rstpPortStateChanged](class_stp_process.html#ad01f4832e6e5cea755e62044f1013243) (QString, int, int, RstpPortState, RstpPortState)  
| This event is emitted when the Rapid-PVST port state for this VLAN changes. [More...](class_stp_process.html#ad01f4832e6e5cea755e62044f1013243)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[StpProcess](class_stp_process.html "StpProcess handles and manipulates STP processes.") handles and manipulates STP processes. 

## Member Function Documentation

## ◆ getPortCount()

int StpProcess::getPortCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of ports in the STP process. 

Returns
    int, the number of ports in the STP process. 

## ◆ getRootBridgeId()

string StpProcess::getRootBridgeId  | ( | | ) |   
---|---|---|---|---  
  
Returns the root bridge ID. 

Returns
    string, the root bridge ID. 

## ◆ getRootPathCost()

int StpProcess::getRootPathCost  | ( | | ) |   
---|---|---|---|---  
  
Returns the root path cost. 

Returns
    int, the root path cost. 

## ◆ getRootPort()

[SwitchPort](class_switch_port.html) StpProcess::getRootPort  | ( | | ) |   
---|---|---|---|---  
  
Returns the root port in this STP process. 

Returns
    [SwitchPort](class_switch_port.html "SwitchPort handles and manipulates switch ports."), the [SwitchPort](class_switch_port.html "SwitchPort handles and manipulates switch ports.") object. 

## ◆ getSwitchId()

string StpProcess::getSwitchId  | ( | | ) |   
---|---|---|---|---  
  
Returns the ID for this switch. 

Returns
    string, the ID for this switch. 

## ◆ getSwitchPriority()

int StpProcess::getSwitchPriority  | ( | | ) |   
---|---|---|---|---  
  
Returns the priority. 

Returns
    int, the priority. 

## ◆ hasPort()

bool StpProcess::hasPort  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns true if the specified port is in this STP process, otherwise false. 

Parameters
     portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
---|---  
  
Returns
    bool, true if the specified port is in this STP process, otherwise false. 

## ◆ isRootBridge()

bool StpProcess::isRootBridge  | ( | | ) |   
---|---|---|---|---  
  
Returns true if this switch is the root bridge, otherwise false. 

Returns
    bool, true if this switch is the root bridge, otherwise false. 

## ◆ rootChanged()

void StpProcess::rootChanged  | ( | QString  | ,   
---|---|---|---  
|  | int  | ,   
|  | mac  | ,   
|  | int  | ,   
|  | mac  | ,   
|  | int  |   
| ) | |   
  
This event is emitted when the root bridge is changed. 

  * ownerSwitch, the new root switch. 
  * vlan, the VLAN number. 
  * oldMac, the MAC address of the old root. 
  * oldPriority, the priority of the old root. 
  * newMac, the MAC address of the new root. 
  * newPriority, the priority of the new root.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ rstpPortStateChanged()

void StpProcess::rstpPortStateChanged  | ( | QString  | ,   
---|---|---|---  
|  | int  | ,   
|  | int  | ,   
|  | RstpPortState  | ,   
|  | RstpPortState  |   
| ) | |   
  
This event is emitted when the Rapid-PVST port state for this VLAN changes. 

  * ownerSwitch, the switch this event occurred on. 
  * vlan, the VLAN number. 
  * portNumber, the port number. 
  * oldStatus, the old STP port state. STP port states: eStpDisabled = 0, eStpBlocking = 1, eStpListening = 2, eStpLearning = 3, eStpForwarding = 4, eStpInconsistent = 5, eStpErrorDisabled = 6 
  * newStatus, the new port state.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ stpPortStateChanged()

void StpProcess::stpPortStateChanged  | ( | QString  | ,   
---|---|---|---  
|  | int  | ,   
|  | int  | ,   
|  | StpPortState  | ,   
|  | StpPortState  |   
| ) | |   
  
This event is emitted when the PVST+ port state for this VLAN changes. 

  * ownerSwitch, the switch this event occurred on. 
  * vlan, the VLAN number. 
  * portNumber, the port number. 
  * oldStatus, the old STP port state. STP port states: eStpDisabled = 0, eStpBlocking = 1, eStpListening = 2, eStpLearning = 3, eStpForwarding = 4, eStpInconsistent = 5, eStpErrorDisabled = 6 
  * newStatus, the new port state.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

* * *

The documentation for this class was generated from the following file:

  * [CStpProcess.pki](_c_stp_process_8pki.html)


