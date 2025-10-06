# Cisco Packet Tracer Extensions API: FirewallProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_firewall_process.html

---

[FirewallProcess](class_firewall_process.html "FirewallProcess is the process that handles Firewall for asa.") is the process that handles Firewall for asa. [More...](class_firewall_process.html#details)

##  Public Member Functions  
  
---  
void | [updateZonePair](class_firewall_process.html#a878f961d8af60a3268577c92ccaae9ea) ()  
| Update the current zone pair list when there's a change with nameIf and security level. [More...](class_firewall_process.html#a878f961d8af60a3268577c92ccaae9ea)  
  
Public Member Functions inherited from [ZfwProcess](class_zfw_process.html)  
int | [getZoneNameCount](class_zfw_process.html#aac126715ecbcd1f22a4aabc2c46c8d84) ()  
| Returns the number of zones. [More...](class_zfw_process.html#aac126715ecbcd1f22a4aabc2c46c8d84)  
  
[Zone](class_zone.html) | [getZoneNameAt](class_zfw_process.html#ab766a0dd0ee4684a5028ebfb4d9def48) (int)  
| Returns the zone at specified index. [More...](class_zfw_process.html#ab766a0dd0ee4684a5028ebfb4d9def48)  
  
int | [getZonePairCount](class_zfw_process.html#ac8b36cdd46be8d558dceea2c52593aef) ()  
| Returns the number of zone pairs. [More...](class_zfw_process.html#ac8b36cdd46be8d558dceea2c52593aef)  
  
[ZonePair](class_zone_pair.html) | [getZonePairEntryAt](class_zfw_process.html#a9ed4a6443591beab8ae74f2464f0fa49) (int)  
| Returns the zone pair at specified index. [More...](class_zfw_process.html#a9ed4a6443591beab8ae74f2464f0fa49)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[FirewallProcess](class_firewall_process.html "FirewallProcess is the process that handles Firewall for asa.") is the process that handles Firewall for asa. 

## Member Function Documentation

## ◆ updateZonePair()

void FirewallProcess::updateZonePair  | ( | | ) |   
---|---|---|---|---  
  
Update the current zone pair list when there's a change with nameIf and security level. 

* * *

The documentation for this class was generated from the following file:

  * [CFirewallProcess.pki](_c_firewall_process_8pki.html)


