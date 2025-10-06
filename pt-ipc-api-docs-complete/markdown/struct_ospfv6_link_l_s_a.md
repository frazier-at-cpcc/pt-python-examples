# Cisco Packet Tracer Extensions API: Ospfv6LinkLSA Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_ospfv6_link_l_s_a.html

---

OSPv6 link LSA structure. [More...](struct_ospfv6_link_l_s_a.html#details)

##  Public Attributes  
  
---  
byte | [routerPriority](struct_ospfv6_link_l_s_a.html#a45a842c21d71f9da4ea65488ecf4e2ea)  
[Ospfv6OptionField](struct_ospfv6_option_field.html) | [option](struct_ospfv6_link_l_s_a.html#afe5c2c1d4289f6697e8fe165d9b81800)  
ipv6 | [linkLocalInterfaceAddress](struct_ospfv6_link_l_s_a.html#a1a3466acf1cf28ed6492bed102c58e9d)  
vector< [Ospfv6Prefix](struct_ospfv6_prefix.html) > | [prefixes](struct_ospfv6_link_l_s_a.html#ad8b5ab168dc64ccab31951acf27cf1ad)  
Public Attributes inherited from [OspfLSA](struct_ospf_l_s_a.html)  
[OspfLSAHeader](struct_ospf_l_s_a_header.html) | [header](struct_ospf_l_s_a.html#ad9366b573d1cbfc17e6452f83eb69ed5)  
  
## Detailed Description

OSPv6 link LSA structure. 

## Member Data Documentation

## ◆ linkLocalInterfaceAddress

ipv6 Ospfv6LinkLSA::linkLocalInterfaceAddress  
---  
  
## ◆ option

[Ospfv6OptionField](struct_ospfv6_option_field.html) Ospfv6LinkLSA::option  
---  
  
## ◆ prefixes

vector<[Ospfv6Prefix](struct_ospfv6_prefix.html)> Ospfv6LinkLSA::prefixes  
---  
  
## ◆ routerPriority

byte Ospfv6LinkLSA::routerPriority  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [COspfv6LinkLSA.pki](_c_ospfv6_link_l_s_a_8pki.html)


