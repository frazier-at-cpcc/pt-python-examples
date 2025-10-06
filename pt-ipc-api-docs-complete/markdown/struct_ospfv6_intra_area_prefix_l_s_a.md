# Cisco Packet Tracer Extensions API: Ospfv6IntraAreaPrefixLSA Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_ospfv6_intra_area_prefix_l_s_a.html

---

OSPv6 intra area prefix LSA structure. [More...](struct_ospfv6_intra_area_prefix_l_s_a.html#details)

##  Public Attributes  
  
---  
short | [referencedLSType](struct_ospfv6_intra_area_prefix_l_s_a.html#afe1be5ee9ccc24e532e92d5d34589596)  
int | [referencedLinkStateId](struct_ospfv6_intra_area_prefix_l_s_a.html#ad62bff065b23fbd874684fe4e4c49df8)  
ip | [refAdvertisingRouter](struct_ospfv6_intra_area_prefix_l_s_a.html#a1d1171d0c81e0bc4a1a2ece7f668def4)  
vector< [Ospfv6Prefix](struct_ospfv6_prefix.html) > | [ipv6AddressPrefixes](struct_ospfv6_intra_area_prefix_l_s_a.html#a89a42af1b4bd71e60192b097bf3a052f)  
Public Attributes inherited from [OspfLSA](struct_ospf_l_s_a.html)  
[OspfLSAHeader](struct_ospf_l_s_a_header.html) | [header](struct_ospf_l_s_a.html#ad9366b573d1cbfc17e6452f83eb69ed5)  
  
## Detailed Description

OSPv6 intra area prefix LSA structure. 

## Member Data Documentation

## ◆ ipv6AddressPrefixes

vector<[Ospfv6Prefix](struct_ospfv6_prefix.html)> Ospfv6IntraAreaPrefixLSA::ipv6AddressPrefixes  
---  
  
## ◆ refAdvertisingRouter

ip Ospfv6IntraAreaPrefixLSA::refAdvertisingRouter  
---  
  
## ◆ referencedLinkStateId

int Ospfv6IntraAreaPrefixLSA::referencedLinkStateId  
---  
  
## ◆ referencedLSType

short Ospfv6IntraAreaPrefixLSA::referencedLSType  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [COspfv6IntraAreaPrefixLSA.pki](_c_ospfv6_intra_area_prefix_l_s_a_8pki.html)


