# Cisco Packet Tracer Extensions API: ArpProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_arp_process.html

---

[ArpProcess](class_arp_process.html "ArpProcess is the process that handles ARP.") is the process that handles ARP. [More...](class_arp_process.html#details)

##  Public Member Functions  
  
---  
[ArpTable](struct_arp_table.html) | [getArpTable](class_arp_process.html#aaf0b136ec9cad62015c92b894d458657) ()  
| Returns the ARP table. [More...](class_arp_process.html#aaf0b136ec9cad62015c92b894d458657)  
  
vector< [ArpRequest](struct_arp_request.html) > | [getArpRequestTable](class_arp_process.html#a59d26868e655eeaf30b65b8aabcaf66b) ()  
| This event is emitted when an ARP entry is added. [More...](class_arp_process.html#a59d26868e655eeaf30b65b8aabcaf66b)  
  
void | [arpEntryAdded](class_arp_process.html#aa188c51a9816d2fc6547627944c33946) (ip, mac, string)  
| [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. [More...](class_arp_process.html#aa188c51a9816d2fc6547627944c33946)  
  
void | [arpEntryRemoved](class_arp_process.html#a352cd2b7a08f4f18c5e2339fafe4482b) (ip, mac, string)  
| This event is emitted when an ARP entry is removed. [More...](class_arp_process.html#a352cd2b7a08f4f18c5e2339fafe4482b)  
  
void | [foundTakingMyIp](class_arp_process.html#a5f890cab82c1b1518eadabcac85adcdb) (ip, mac, string)  
| This event is emitted when this device discovers another device is taking its IP address. [More...](class_arp_process.html#a5f890cab82c1b1518eadabcac85adcdb)  
  
void | [foundMyIpTaken](class_arp_process.html#aa7159288ac2d647f2a903815fc894a72) (ip, mac, string)  
| This event is emitted when this device discovers another device has taken its IP address. [More...](class_arp_process.html#aa7159288ac2d647f2a903815fc894a72)  
  
void | [closeTableEvent](class_arp_process.html#a85d3efc00fc8985b98c8b87fc94f314e) ()  
| [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. [More...](class_arp_process.html#a85d3efc00fc8985b98c8b87fc94f314e)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[ArpProcess](class_arp_process.html "ArpProcess is the process that handles ARP.") is the process that handles ARP. 

## Member Function Documentation

## ◆ arpEntryAdded()

void ArpProcess::arpEntryAdded  | ( | ip  | ,   
---|---|---|---  
|  | mac  | ,   
|  | string  |   
| ) | |   
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ arpEntryRemoved()

void ArpProcess::arpEntryRemoved  | ( | ip  | ,   
---|---|---|---  
|  | mac  | ,   
|  | string  |   
| ) | |   
  
This event is emitted when an ARP entry is removed. 

  * ip, the IP address associated with the ARP entry that was removed. 
  * mac, the MAC address associated with the ARP entry that was removed. 
  * portName, the port associated with the ARP entry that was removed.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ closeTableEvent()

void ArpProcess::closeTableEvent  | ( | | ) |   
---|---|---|---|---  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ foundMyIpTaken()

void ArpProcess::foundMyIpTaken  | ( | ip  | ,   
---|---|---|---  
|  | mac  | ,   
|  | string  |   
| ) | |   
  
This event is emitted when this device discovers another device has taken its IP address. 

  * ip, the IP address of the other device. 
  * mac, the MAC address of the other device. 
  * portName, the port where this event was discovered from.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ foundTakingMyIp()

void ArpProcess::foundTakingMyIp  | ( | ip  | ,   
---|---|---|---  
|  | mac  | ,   
|  | string  |   
| ) | |   
  
This event is emitted when this device discovers another device is taking its IP address. 

  * ip, the IP address of the other device. 
  * mac, the MAC address of the other device. 
  * portName, the port where this event was discovered from.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ getArpRequestTable()

vector< [ArpRequest](struct_arp_request.html) > ArpProcess::getArpRequestTable  | ( | | ) |   
---|---|---|---|---  
  
This event is emitted when an ARP entry is added. 

  * ip, the IP address associated with the ARP entry that was added. 
  * mac, the MAC address associated with the ARP entry that was added. 
  * portName, the port associated with the ARP entry that was added. 



## ◆ getArpTable()

[ArpTable](struct_arp_table.html) ArpProcess::getArpTable  | ( | | ) |   
---|---|---|---|---  
  
Returns the ARP table. 

Returns
    [ArpTable](struct_arp_table.html "Data element for ArpTable."), the ARP table. 

* * *

The documentation for this class was generated from the following file:

  * [CArpProcess.pki](_c_arp_process_8pki.html)


