# Cisco Packet Tracer Extensions API: VlanManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_vlan_manager.html

---

[VlanManager](class_vlan_manager.html "VlanManager holds and manipulates VLANs on routers and switches.") holds and manipulates VLANs on routers and switches. [More...](class_vlan_manager.html#details)

##  Public Member Functions  
  
---  
[Vlan](class_vlan.html) | [getVlan](class_vlan_manager.html#a2be97c4705fa01d78686c750b4998cb6) (int)  
| Returns the VLAN with the specified VLAN number. [More...](class_vlan_manager.html#a2be97c4705fa01d78686c750b4998cb6)  
  
[Vlan](class_vlan.html) | [getVlanAt](class_vlan_manager.html#a78613c6939cc02492745179ab4645af7) (int)  
| Returns the VLAN at the specified index. [More...](class_vlan_manager.html#a78613c6939cc02492745179ab4645af7)  
  
bool | [addVlan](class_vlan_manager.html#a8f80cc2fa59e15e19d009d50d58352a6) (int, string)  
| Adds a VLAN. [More...](class_vlan_manager.html#a8f80cc2fa59e15e19d009d50d58352a6)  
  
bool | [removeVlan](class_vlan_manager.html#ab9521473574025f61ef1f2ef1d847909) (int)  
| Removes the VLAN with the specified VLAN number. [More...](class_vlan_manager.html#ab9521473574025f61ef1f2ef1d847909)  
  
int | [getVlanCount](class_vlan_manager.html#ad2c39deb1c781255c3f068c25d55c789) ()  
| Returns the number of VLANs. [More...](class_vlan_manager.html#ad2c39deb1c781255c3f068c25d55c789)  
  
int | [getMaxVlans](class_vlan_manager.html#a5031a73239ebfc0f18cef1e68471ae7c) ()  
| Returns the maximum number of VLANs. [More...](class_vlan_manager.html#a5031a73239ebfc0f18cef1e68471ae7c)  
  
[Vlan](class_vlan.html) | [getVlanByName](class_vlan_manager.html#ab8f4dfa9baf38fd048652dbb1ec64a13) (string)  
| Returns the VLAN with the specified VLAN name. [More...](class_vlan_manager.html#ab8f4dfa9baf38fd048652dbb1ec64a13)  
  
bool | [changeVlanName](class_vlan_manager.html#aa0e23d1cc95575a8f68891c5f77f3b9e) (int, string)  
| Changes the VLAN name. [More...](class_vlan_manager.html#aa0e23d1cc95575a8f68891c5f77f3b9e)  
  
bool | [addVlanInt](class_vlan_manager.html#aebb1f7bb99755faa6251fc30ed0cb202) (int)  
| Adds a VLAN interface with the specified VLAN number. [More...](class_vlan_manager.html#aebb1f7bb99755faa6251fc30ed0cb202)  
  
bool | [removeVlanInt](class_vlan_manager.html#ac97bda14c92095b4e147e122d8cacfb3) (int)  
| Removes the VLAN interface with the specified VLAN number. [More...](class_vlan_manager.html#ac97bda14c92095b4e147e122d8cacfb3)  
  
[RouterPort](class_router_port.html) | [getVlanInt](class_vlan_manager.html#ae95f9aaad0fe110f50f66d2852e4e0a0) (int)  
| Returns the VLAN interface with the specified VLAN number. [More...](class_vlan_manager.html#ae95f9aaad0fe110f50f66d2852e4e0a0)  
  
[RouterPort](class_router_port.html) | [getVlanIntAt](class_vlan_manager.html#a454fb239e60cc7bc0a1626a37321dcf8) (int)  
| Returns the VLAN interface at the specified index. [More...](class_vlan_manager.html#a454fb239e60cc7bc0a1626a37321dcf8)  
  
int | [getVlanIntCount](class_vlan_manager.html#aecd2b669ddf2db1f6c7662dacca4103e) ()  
| Returns the number of VLAN interfaces. [More...](class_vlan_manager.html#aecd2b669ddf2db1f6c7662dacca4103e)  
  
void | [updateTableEvent](class_vlan_manager.html#ab49a9225635bd207ad37a24090d7f189) ()  
| This event is emitted when the vlan table is updated. [More...](class_vlan_manager.html#ab49a9225635bd207ad37a24090d7f189)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[VlanManager](class_vlan_manager.html "VlanManager holds and manipulates VLANs on routers and switches.") holds and manipulates VLANs on routers and switches. 

## Member Function Documentation

## ◆ addVlan()

bool VlanManager::addVlan  | ( | int  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Adds a VLAN. 

Parameters
     vlandID,the| number for the VLAN.   
---|---  
vlanName,the| name for the VLAN.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ addVlanInt()

bool VlanManager::addVlanInt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Adds a VLAN interface with the specified VLAN number. 

Parameters
     vlanID,the| VLAN number for the VLAN interface.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ changeVlanName()

bool VlanManager::changeVlanName  | ( | int  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Changes the VLAN name. 

Parameters
     vlanID,the| VLAN number of interest.   
---|---  
name,the| name for the VLAN.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ getMaxVlans()

int VlanManager::getMaxVlans  | ( | | ) |   
---|---|---|---|---  
  
Returns the maximum number of VLANs. 

Returns
    int, the maximum number of VLANs. 

## ◆ getVlan()

[Vlan](class_vlan.html) VlanManager::getVlan  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the VLAN with the specified VLAN number. 

Parameters
     vlanID,the| number of the VLAN of interest.  
---|---  
  
Returns
    [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), the [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN.") object with the specified VLAN number. 

## ◆ getVlanAt()

[Vlan](class_vlan.html) VlanManager::getVlanAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the VLAN at the specified index. 

Parameters
     index,the| index of the VLAN of interest.  
---|---  
  
Returns
    [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), the [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN.") object at the specified index. 

## ◆ getVlanByName()

[Vlan](class_vlan.html) VlanManager::getVlanByName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the VLAN with the specified VLAN name. 

Parameters
     name,the| name of the VLAN of interest.  
---|---  
  
Returns
    [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), the [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN.") object with the specified VLAN name. 

## ◆ getVlanCount()

int VlanManager::getVlanCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of VLANs. 

Returns
    int, the number of VLANs. 

## ◆ getVlanInt()

[RouterPort](class_router_port.html) VlanManager::getVlanInt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the VLAN interface with the specified VLAN number. 

Parameters
     vlanID,the| VLAN number of interest.  
---|---  
  
Returns
    [RouterPort](class_router_port.html "RouterPort handles and manipulates the router port."), the [RouterPort](class_router_port.html "RouterPort handles and manipulates the router port.") object of the VLAN interface with the specified VLAN number. 

## ◆ getVlanIntAt()

[RouterPort](class_router_port.html) VlanManager::getVlanIntAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the VLAN interface at the specified index. 

Parameters
     index,the| index of the VLAN interface of interest.  
---|---  
  
Returns
    [RouterPort](class_router_port.html "RouterPort handles and manipulates the router port."), the [RouterPort](class_router_port.html "RouterPort handles and manipulates the router port.") object of the VLAN interface at the specified index. 

## ◆ getVlanIntCount()

int VlanManager::getVlanIntCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of VLAN interfaces. 

Returns
    int, the number of VLAN interfaces. 

## ◆ removeVlan()

bool VlanManager::removeVlan  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Removes the VLAN with the specified VLAN number. 

Parameters
     vlandID,the| VLAN number of interest.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ removeVlanInt()

bool VlanManager::removeVlanInt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Removes the VLAN interface with the specified VLAN number. 

Parameters
     vlanID,the| VLAN number of interest.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ updateTableEvent()

void VlanManager::updateTableEvent  | ( | | ) |   
---|---|---|---|---  
  
This event is emitted when the vlan table is updated. 

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

* * *

The documentation for this class was generated from the following file:

  * [CVLANManager.pki](_c_v_l_a_n_manager_8pki.html)


