# Cisco Packet Tracer Extensions API: AsaNatv6Process Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_asa_natv6_process.html

---

[AsaNatv6Process](class_asa_natv6_process.html "AsaNatv6Process is the process that handles Nat for asa.") is the process that handles Nat for asa. [More...](class_asa_natv6_process.html#details)

##  Additional Inherited Members  
  
---  
Public Member Functions inherited from [NatProcess](class_nat_process.html)  
bool | [addNatPool](class_nat_process.html#aa93cdc94dfe5b63429dc92d9edd6f651) (string)  
| Adds a NAT pool with the specified name. [More...](class_nat_process.html#aa93cdc94dfe5b63429dc92d9edd6f651)  
  
[NatPool](struct_nat_pool.html) | [getNatPool](class_nat_process.html#ae11cd3176c8e2d8bf69e94b0881efe7f) (string)  
| Returns the NAT pool with the specified name. [More...](class_nat_process.html#ae11cd3176c8e2d8bf69e94b0881efe7f)  
  
[NatPool](struct_nat_pool.html) | [getNatPoolAt](class_nat_process.html#a27f9747cf9e0a2f40c8df392bac87f06) (int)  
| Returns the NAT pool at the specified index. [More...](class_nat_process.html#a27f9747cf9e0a2f40c8df392bac87f06)  
  
bool | [removeNatPool](class_nat_process.html#af823055efb58d2aa6707edef57473675) (string)  
| Removes the NAT pool with the specified name. [More...](class_nat_process.html#af823055efb58d2aa6707edef57473675)  
  
int | [getNatPoolCount](class_nat_process.html#a7d837f53976445e6b6108ca8f3ebf179) ()  
| Returns the number of NAT pools. [More...](class_nat_process.html#a7d837f53976445e6b6108ca8f3ebf179)  
  
int | [getInSrcStaticCount](class_nat_process.html#a654c1d261bd66da96b3db003aac2ede2) ()  
| Returns the number of inside source static entries. [More...](class_nat_process.html#a654c1d261bd66da96b3db003aac2ede2)  
  
int | [getOutSrcStaticCount](class_nat_process.html#a19ee96f832e2f2645b57677f22340355) ()  
| Returns the number of outside source static entries. [More...](class_nat_process.html#a19ee96f832e2f2645b57677f22340355)  
  
[NatEntry](struct_nat_entry.html) | [getInSrcStaticAt](class_nat_process.html#ab93d459865a45e39e8e85829186ebf72) (int)  
| Returns the inside source static entry at the specified index. [More...](class_nat_process.html#ab93d459865a45e39e8e85829186ebf72)  
  
[NatEntry](struct_nat_entry.html) | [getOutSrcStaticAt](class_nat_process.html#ad45ddcc9cfbbdfc26c26c10481e99ea8) (int)  
| Returns the inside source static entry at the specified index. [More...](class_nat_process.html#ad45ddcc9cfbbdfc26c26c10481e99ea8)  
  
void | [clearAllTranslations](class_nat_process.html#a4b4710e90f546354bc7cb6e602247153) ()  
| Clears all NAT translations. [More...](class_nat_process.html#a4b4710e90f546354bc7cb6e602247153)  
  
bool | [removeInSrcList](class_nat_process.html#a21fe7e531aace9a06a3f7ae949bb0aea) (string)  
| Removes the inside source list entry with the specified ACL ID. [More...](class_nat_process.html#a21fe7e531aace9a06a3f7ae949bb0aea)  
  
bool | [removeOutSrcList](class_nat_process.html#afbb9f15d0ed3a83106de0f470f329ebd) (string)  
| Removes the outside source list entry with the specified ACL ID. [More...](class_nat_process.html#afbb9f15d0ed3a83106de0f470f329ebd)  
  
[NatList](struct_nat_list.html) | [getInSrcList](class_nat_process.html#ab40fdda6e78eaddb06127537f84e84ec) (string)  
| Returns the inside source list entry with the specified ACL ID. [More...](class_nat_process.html#ab40fdda6e78eaddb06127537f84e84ec)  
  
[NatList](struct_nat_list.html) | [getOutSrcList](class_nat_process.html#aa1b95328e2508117afd159e0e2b36116) (string)  
| Returns the outside source list entry with the specified ACL ID. [More...](class_nat_process.html#aa1b95328e2508117afd159e0e2b36116)  
  
[NatList](struct_nat_list.html) | [getInSrcListAt](class_nat_process.html#a847151199f629087ab84921b66d45bc2) (int)  
| Returns the inside source list entry at the specified index. [More...](class_nat_process.html#a847151199f629087ab84921b66d45bc2)  
  
[NatList](struct_nat_list.html) | [getOutSrcListAt](class_nat_process.html#ab3d14e250626443d65e76fadd5ed91c7) (int)  
| Returns the outside source list entry at the specified index. [More...](class_nat_process.html#ab3d14e250626443d65e76fadd5ed91c7)  
  
int | [getInSrcListCount](class_nat_process.html#ac6c864d9dcaf36ea3e9cb802d7d35527) ()  
| Returns the number of inside source list entries. [More...](class_nat_process.html#ac6c864d9dcaf36ea3e9cb802d7d35527)  
  
int | [getOutSrcListCount](class_nat_process.html#a0cfb9c70e846b0e94acf8fd92d6e7688) ()  
| Returns the number of outside source list entries. [More...](class_nat_process.html#a0cfb9c70e846b0e94acf8fd92d6e7688)  
  
[NatTable](struct_nat_table.html) | [getNatTable](class_nat_process.html#a8a8a9248567126df34a05922d7aa55af) ()  
| Returns the NAT table. [More...](class_nat_process.html#a8a8a9248567126df34a05922d7aa55af)  
  
void | [updateTableEvent](class_nat_process.html#a9e0addd301caec78b4a22d4cf1ffd15b) ()  
| Event triggered when the table is updated. [More...](class_nat_process.html#a9e0addd301caec78b4a22d4cf1ffd15b)  
  
void | [closeTableEvent](class_nat_process.html#ac86366987488dc26ae84773b2483fc4e) ()  
| Event triggered when the table is closed, deleted. [More...](class_nat_process.html#ac86366987488dc26ae84773b2483fc4e)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[AsaNatv6Process](class_asa_natv6_process.html "AsaNatv6Process is the process that handles Nat for asa.") is the process that handles Nat for asa. 

* * *

The documentation for this class was generated from the following file:

  * [CAsaNatv6Process.pki](_c_asa_natv6_process_8pki.html)


