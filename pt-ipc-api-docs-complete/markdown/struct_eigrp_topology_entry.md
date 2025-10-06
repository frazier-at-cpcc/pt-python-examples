# Cisco Packet Tracer Extensions API: EigrpTopologyEntry Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_eigrp_topology_entry.html

---

Data element for EIGRP topology entries. [More...](struct_eigrp_topology_entry.html#details)

##  Public Attributes  
  
---  
ip | [network](struct_eigrp_topology_entry.html#a19595cd224c2bf2d7d46fb9f6da1bfeb)  
ip | [subnetMask](struct_eigrp_topology_entry.html#a6baa3bfaf0d4280100ab336db9aa6ca7)  
EigrpTopologyEntryState | [state](struct_eigrp_topology_entry.html#a447cdac32bc491843c78a1638d1a3a67)  
int | [feasibleDistance](struct_eigrp_topology_entry.html#a33e54ac754a83582b034c76fd6800e9e)  
int | [reportedDistance](struct_eigrp_topology_entry.html#a4aac3d028431066ca81e853db0f68384)  
int | [successorCount](struct_eigrp_topology_entry.html#a572573abfedfdd68e6f6474f7b0aa5c2)  
vector< [EigrpRoutingEntry](struct_eigrp_routing_entry.html) > | [routingEntries](struct_eigrp_topology_entry.html#affd800c4ac095219e845cbdd37920a3c)  
  
## Detailed Description

Data element for EIGRP topology entries. 

## Member Data Documentation

## ◆ feasibleDistance

int EigrpTopologyEntry::feasibleDistance  
---  
  
## ◆ network

ip EigrpTopologyEntry::network  
---  
  
## ◆ reportedDistance

int EigrpTopologyEntry::reportedDistance  
---  
  
## ◆ routingEntries

vector<[EigrpRoutingEntry](struct_eigrp_routing_entry.html)> EigrpTopologyEntry::routingEntries  
---  
  
## ◆ state

EigrpTopologyEntryState EigrpTopologyEntry::state  
---  
  
## ◆ subnetMask

ip EigrpTopologyEntry::subnetMask  
---  
  
## ◆ successorCount

int EigrpTopologyEntry::successorCount  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [CEigrpTopologyEntry.pki](_c_eigrp_topology_entry_8pki.html)


