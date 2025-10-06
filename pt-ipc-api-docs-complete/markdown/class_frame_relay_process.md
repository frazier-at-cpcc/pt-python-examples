# Cisco Packet Tracer Extensions API: FrameRelayProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_frame_relay_process.html

---

[FrameRelayProcess](class_frame_relay_process.html "FrameRelayProcess handles and manipulates the Frame Relay process.") handles and manipulates the Frame Relay process. [More...](class_frame_relay_process.html#details)

##  Public Member Functions  
  
---  
void | [setLmiType](class_frame_relay_process.html#abbf06b5e645f458140db2144ce84f7ad) (LmiType)  
| Sets the LMI type for this Frame Relay process. [More...](class_frame_relay_process.html#abbf06b5e645f458140db2144ce84f7ad)  
  
void | [setEncapType](class_frame_relay_process.html#a0808a603b9401c7edcc230b6c6d370c1) (FrameRelayEncapType)  
| Sets the encapsulation type for this Frame Relay process. [More...](class_frame_relay_process.html#a0808a603b9401c7edcc230b6c6d370c1)  
  
FrameRelayEncapType | [getEncapType](class_frame_relay_process.html#a0fb28bc6c633254020a609b172c166d8) ()  
| Returns the encapsulation type of this Frame Relay process. [More...](class_frame_relay_process.html#a0fb28bc6c633254020a609b172c166d8)  
  
LmiType | [getLmiType](class_frame_relay_process.html#a94f2c5ea00d2fe68b68b9875784aaf80) ()  
| Returns the encapsulation type of this Frame Relay process. [More...](class_frame_relay_process.html#a94f2c5ea00d2fe68b68b9875784aaf80)  
  
bool | [addMapEntry](class_frame_relay_process.html#aaf3779341a421035479d1a3805e4589c) (ip, int, bool, FrameRelayEncapType, string)  
| Adds a map entry to the specified port. [More...](class_frame_relay_process.html#aaf3779341a421035479d1a3805e4589c)  
  
bool | [addIntDlciEntry](class_frame_relay_process.html#a18ed96ce1ab6f5851ef187c904b783e2) (string, int)  
| Adds a interface-DLCI entry the specified port. [More...](class_frame_relay_process.html#a18ed96ce1ab6f5851ef187c904b783e2)  
  
bool | [deleteMapEntry](class_frame_relay_process.html#aff0be488903d5390f0bcd0ed03d9fe5c) (string, ip)  
| Removes the map entry from the specified port. [More...](class_frame_relay_process.html#aff0be488903d5390f0bcd0ed03d9fe5c)  
  
bool | [deleteIntDlciEntry](class_frame_relay_process.html#a70da8b7641d84b9a19a16fdc49b7646c) (string, int)  
| Removes the interface-DLCI entry from the specified port. [More...](class_frame_relay_process.html#a70da8b7641d84b9a19a16fdc49b7646c)  
  
[FrameRelayMapEntry](struct_frame_relay_map_entry.html) | [getMapEntryAt](class_frame_relay_process.html#a5ead448d028376d00ad54fa60e8ac2ae) (int, string)  
| Returns the map entry at the specified index on the specified port. [More...](class_frame_relay_process.html#a5ead448d028376d00ad54fa60e8ac2ae)  
  
short | [getIntDlciEntryAt](class_frame_relay_process.html#a078abee66984d44f4fff7eb029ca5de6) (int, string)  
| Returns the interface-DLCI number at the specified index on the specified port. [More...](class_frame_relay_process.html#a078abee66984d44f4fff7eb029ca5de6)  
  
short | [getLmiDlciEntryAt](class_frame_relay_process.html#a4ce7fe2aef215e906c7df9aad4e7cff5) (int)  
| Returns LMI DLCI at the specified index. [More...](class_frame_relay_process.html#a4ce7fe2aef215e906c7df9aad4e7cff5)  
  
bool | [getLmiDlciStatusEntryAt](class_frame_relay_process.html#a06a46ff1ca6dcb16f39d86623508af7a) (int)  
| Returns true if the LMI DLCI at the specified index is active, otherwise false. [More...](class_frame_relay_process.html#a06a46ff1ca6dcb16f39d86623508af7a)  
  
int | [getMapEntryCount](class_frame_relay_process.html#a5ca937b737f22f660632828e6a6bfa5c) (string)  
| Returns the number of map entries. [More...](class_frame_relay_process.html#a5ca937b737f22f660632828e6a6bfa5c)  
  
int | [getIntDlciEntryCount](class_frame_relay_process.html#ac62874881fee077c03b1b3dd83358121) (string)  
| Returns the number of interface-DLCI entries. [More...](class_frame_relay_process.html#ac62874881fee077c03b1b3dd83358121)  
  
int | [getLmiDlciEntryCount](class_frame_relay_process.html#a0737d4e71b40cd6fb1092c298426bebb) ()  
| Returns the number of LMI DLCI entries. [More...](class_frame_relay_process.html#a0737d4e71b40cd6fb1092c298426bebb)  
  
[Port](class_port.html) | [getIntDlciToPort](class_frame_relay_process.html#ae0d68070f3b05d79edd1c1e49bfd77db) (int)  
| Returns the port of the specified interface-DLCI. [More...](class_frame_relay_process.html#ae0d68070f3b05d79edd1c1e49bfd77db)  
  
void | [clearInvArpEntries](class_frame_relay_process.html#a367a74947a70a685dd4d9a166dab16e4) ()  
| Clears the inverse ARP entries. [More...](class_frame_relay_process.html#a367a74947a70a685dd4d9a166dab16e4)  
  
[DlciTable](struct_dlci_table.html) | [getDlciTable](class_frame_relay_process.html#a7041bb2876bae600fcfbcbe552df74e6) ()  
| Returns the DLCI table. [More...](class_frame_relay_process.html#a7041bb2876bae600fcfbcbe552df74e6)  
  
Public Member Functions inherited from [PortKeepAliveProcess](class_port_keep_alive_process.html)  
void | [setKeepAliveOn](class_port_keep_alive_process.html#a35bfb062718b7507ec3f1fd71c62d4f1) (bool)  
bool | [isKeepAliveOn](class_port_keep_alive_process.html#aa9fe1c119e9f3365c4dec1cb65b13752) ()  
| Returns true if keepalive is enabled, otherwise false. [More...](class_port_keep_alive_process.html#aa9fe1c119e9f3365c4dec1cb65b13752)  
  
void | [setKeepAliveInterval](class_port_keep_alive_process.html#a2e003c5aa950a4a7c1548fcee456e667) (int)  
| Sets the keepalive interval. [More...](class_port_keep_alive_process.html#a2e003c5aa950a4a7c1548fcee456e667)  
  
int | [getKeepAliveInterval](class_port_keep_alive_process.html#adb100ad4b49d7678a1dd4059552f9ee1) ()  
| Returns the keepalive interval. [More...](class_port_keep_alive_process.html#adb100ad4b49d7678a1dd4059552f9ee1)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[FrameRelayProcess](class_frame_relay_process.html "FrameRelayProcess handles and manipulates the Frame Relay process.") handles and manipulates the Frame Relay process. 

## Member Function Documentation

## ◆ addIntDlciEntry()

bool FrameRelayProcess::addIntDlciEntry  | ( | string  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Adds a interface-DLCI entry the specified port. 

Parameters
     portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0   
---|---  
dlci,the| DLCI number.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ addMapEntry()

bool FrameRelayProcess::addMapEntry  | ( | ip  | ,   
---|---|---|---  
|  | int  | ,   
|  | bool  | ,   
|  | FrameRelayEncapType  | ,   
|  | string  |   
| ) | |   
  
Adds a map entry to the specified port. 

Parameters
     ipAddress,the| IP address to map.   
---|---  
dlci,the| DLCI number.   
bBroadcast,true| forwards broadcasts to this address, false does not forward broadcasts.   
encapType,the| encapsulation type of this Frame Relay process. Encapsulation types: eFrameRelayEncapCisco = 0, eFrameRelayEncapIetf = 1, eFrameRelayEncapDefault = 2   
portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0   
  
Returns
    bool, true if successful, otherwise false. 

## ◆ clearInvArpEntries()

void FrameRelayProcess::clearInvArpEntries  | ( | | ) |   
---|---|---|---|---  
  
Clears the inverse ARP entries. 

## ◆ deleteIntDlciEntry()

bool FrameRelayProcess::deleteIntDlciEntry  | ( | string  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Removes the interface-DLCI entry from the specified port. 

Parameters
     portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0   
---|---  
dlci,the| DLCI number.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ deleteMapEntry()

bool FrameRelayProcess::deleteMapEntry  | ( | string  | ,   
---|---|---|---  
|  | ip  |   
| ) | |   
  
Removes the map entry from the specified port. 

Parameters
     portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0   
---|---  
ipAddress,the| IP address of the map.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ getDlciTable()

[DlciTable](struct_dlci_table.html) FrameRelayProcess::getDlciTable  | ( | | ) |   
---|---|---|---|---  
  
Returns the DLCI table. 

Returns
    [DlciTable](struct_dlci_table.html "Data element for the DLCI table."), the [DlciTable](struct_dlci_table.html "Data element for the DLCI table.") object. 

## ◆ getEncapType()

FrameRelayEncapType FrameRelayProcess::getEncapType  | ( | | ) |   
---|---|---|---|---  
  
Returns the encapsulation type of this Frame Relay process. 

Returns
    enum<FrameRelayEncapType>, the encapsulation type of this Frame Relay process. Encapsulation types: eFrameRelayEncapCisco = 0, eFrameRelayEncapIetf = 1, eFrameRelayEncapDefault = 2 

## ◆ getIntDlciEntryAt()

short FrameRelayProcess::getIntDlciEntryAt  | ( | int  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Returns the interface-DLCI number at the specified index on the specified port. 

Parameters
     index,the| index of the interface-DLCI of interest.   
---|---  
portName| portName can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
  
Returns
    short, the interface-DLCI number at the specified index on the specified port. 

## ◆ getIntDlciEntryCount()

int FrameRelayProcess::getIntDlciEntryCount  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the number of interface-DLCI entries. 

Parameters
     portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
---|---  
  
Returns
    int, the number of interface-DLCI entries. 

## ◆ getIntDlciToPort()

[Port](class_port.html) FrameRelayProcess::getIntDlciToPort  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the port of the specified interface-DLCI. 

Parameters
     dlci,the| interface-DLCI of interest.  
---|---  
  
Returns
    [Port](class_port.html "Port holds and manipulates the ports on devices."), the [Port](class_port.html "Port holds and manipulates the ports on devices.") object of the specified interface-DLCI. 

## ◆ getLmiDlciEntryAt()

short FrameRelayProcess::getLmiDlciEntryAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns LMI DLCI at the specified index. 

Parameters
     index,the| index of the LMI DLCI of interest.  
---|---  
  
Returns
    short, the LMI DLCI at the specified index. 

## ◆ getLmiDlciEntryCount()

int FrameRelayProcess::getLmiDlciEntryCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of LMI DLCI entries. 

Returns
    int, the number of LMI DLCI entries. 

## ◆ getLmiDlciStatusEntryAt()

bool FrameRelayProcess::getLmiDlciStatusEntryAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns true if the LMI DLCI at the specified index is active, otherwise false. 

Parameters
     index,the| index of the LMI DLCI of interest.  
---|---  
  
Returns
    bool, true if the LMI DLCI at the specified index is active, otherwise false. 

## ◆ getLmiType()

LmiType FrameRelayProcess::getLmiType  | ( | | ) |   
---|---|---|---|---  
  
Returns the encapsulation type of this Frame Relay process. 

Returns
    enum<LmiType>, the LMI type of this Frame Relay process. LMI types: eLmiAnsi = 0, eLmiCisco = 1, eLmiQ933a = 2 

## ◆ getMapEntryAt()

[FrameRelayMapEntry](struct_frame_relay_map_entry.html) FrameRelayProcess::getMapEntryAt  | ( | int  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Returns the map entry at the specified index on the specified port. 

Parameters
     index,the| index of the map entry of interest.   
---|---  
portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
  
Returns
    [FrameRelayMapEntry](struct_frame_relay_map_entry.html "Data element for Frame Relay map entries."), the [FrameRelayMapEntry](struct_frame_relay_map_entry.html "Data element for Frame Relay map entries.") object at the specified index on the specified port. 

## ◆ getMapEntryCount()

int FrameRelayProcess::getMapEntryCount  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the number of map entries. 

Parameters
     portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
---|---  
  
Returns
    int, the number of map entries. 

## ◆ setEncapType()

void FrameRelayProcess::setEncapType  | ( | FrameRelayEncapType  | | ) |   
---|---|---|---|---|---  
  
Sets the encapsulation type for this Frame Relay process. 

Parameters
     encapType,the| encapsulation type. Encapsulation types: eFrameRelayEncapCisco = 0, eFrameRelayEncapIetf = 1, eFrameRelayEncapDefault = 2   
---|---  
  
## ◆ setLmiType()

void FrameRelayProcess::setLmiType  | ( | LmiType  | | ) |   
---|---|---|---|---|---  
  
Sets the LMI type for this Frame Relay process. 

Parameters
     lmiType,the| LMI type. LMI types: eLmiAnsi = 0, eLmiCisco = 1, eLmiQ933a = 2   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CFrameRelayProcess.pki](_c_frame_relay_process_8pki.html)


