# Cisco Packet Tracer Extensions API: CAsaNetworkObject Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_c_asa_network_object.html

---

[CAsaNetworkObject](class_c_asa_network_object.html "CAsaNetworkObject is the asa network object.") is the asa network object. [More...](class_c_asa_network_object.html#details)

##  Public Member Functions  
  
---  
void | [setHostIp](class_c_asa_network_object.html#a246ea0be30600b91e650de2f12d2a64c) (ip)  
| set the host ip address to the asa network object [More...](class_c_asa_network_object.html#a246ea0be30600b91e650de2f12d2a64c)  
  
ip | [getHostIp](class_c_asa_network_object.html#a0ff9becc4593fcec2e75158a0887d625) ()  
| Returns the host ip address/network address that is set to the asa network object. [More...](class_c_asa_network_object.html#a0ff9becc4593fcec2e75158a0887d625)  
  
ip | [getHostMask](class_c_asa_network_object.html#a5296da79e619dc68ba557ccc9aacd4d7) ()  
| Returns the subnet mask that is set to the asa network object. [More...](class_c_asa_network_object.html#a5296da79e619dc68ba557ccc9aacd4d7)  
  
ip | [getInvHostMask](class_c_asa_network_object.html#aab88edfee4504515854184e5e892b6a9) ()  
| Returns the inverse subnet mask that is set to the asa network object. [More...](class_c_asa_network_object.html#aab88edfee4504515854184e5e892b6a9)  
  
bool | [removeHostIp](class_c_asa_network_object.html#ace6bcc6f85c52d060aa9a48aa8c8c2ff) (ip)  
| Remove the host ip address that is set to the asa network object. [More...](class_c_asa_network_object.html#ace6bcc6f85c52d060aa9a48aa8c8c2ff)  
  
void | [setSubnet](class_c_asa_network_object.html#a28a6e41e7600800bb9dc984fb8491e9c) (ip, ip)  
| Set the subnet/mask to the asa network object. [More...](class_c_asa_network_object.html#a28a6e41e7600800bb9dc984fb8491e9c)  
  
bool | [removeSubnet](class_c_asa_network_object.html#a07483f82fba89187b00d878963f8dbce) (ip, ip)  
| Remove the subnet/mask that is set to the asa network object. [More...](class_c_asa_network_object.html#a07483f82fba89187b00d878963f8dbce)  
  
[NatEntry](struct_nat_entry.html) | [getNatEntry](class_c_asa_network_object.html#a636a5d4cb632cc5935e7b68f6cdb5c32) ()  
| Returns static nat entry that is set to the asa network object. [More...](class_c_asa_network_object.html#a636a5d4cb632cc5935e7b68f6cdb5c32)  
  
void | [deleteNatEntry](class_c_asa_network_object.html#a45c9ccb88b200350039b006b1a285d2b) ()  
| Remove static nat entry that is set to the asa network object. [More...](class_c_asa_network_object.html#a45c9ccb88b200350039b006b1a285d2b)  
  
[NatListInterface](struct_nat_list_interface.html) | [getNatList](class_c_asa_network_object.html#a739d376cff1dbe7e86f075608eaa7b14) ()  
| Returns dynamic nat entry that is set to the asa network object. [More...](class_c_asa_network_object.html#a739d376cff1dbe7e86f075608eaa7b14)  
  
void | [deleteNatList](class_c_asa_network_object.html#a24a7c6fa060e1fc62e4ab4bb05f24985) ()  
| Remove dynamic nat entry that is set to the asa network object. [More...](class_c_asa_network_object.html#a24a7c6fa060e1fc62e4ab4bb05f24985)  
  
void | [nameifChanged](class_c_asa_network_object.html#a389fc2906ee32ebc527cd67bd4c41282) (string, string)  
| Remove nat entry when the referenced nameif is changed. [More...](class_c_asa_network_object.html#a389fc2906ee32ebc527cd67bd4c41282)  
  
vector< string > | [getRunningConfig](class_c_asa_network_object.html#a6f86d29aa3b00633e085dc4ae6f161e3) ()  
| Returns all object configuration strings in show run. [More...](class_c_asa_network_object.html#a6f86d29aa3b00633e085dc4ae6f161e3)  
  
vector< string > | [getNatRunningConfig](class_c_asa_network_object.html#ae209cd8eddbb317fabd80f05ec00123c) ()  
| Returns object + nat configuration strings in show run. [More...](class_c_asa_network_object.html#ae209cd8eddbb317fabd80f05ec00123c)  
  
string | [getNatStatement](class_c_asa_network_object.html#a990abb51bb713c48bfe0599790181961) ()  
| Returns the nat statement configuration string in show run. [More...](class_c_asa_network_object.html#a990abb51bb713c48bfe0599790181961)  
  
string | [getAddressStatement](class_c_asa_network_object.html#a3955a681a1670f614d02b759c0d6470c) ()  
| Returns the host address/subnet mask statement configuration string in show run. [More...](class_c_asa_network_object.html#a3955a681a1670f614d02b759c0d6470c)  
  
void | [updateAsaAclStatement](class_c_asa_network_object.html#aa60fc4cf95676e6c605c53440766af9a) ()  
| Update the corresponding acl statements that have reference to this asa network object. [More...](class_c_asa_network_object.html#aa60fc4cf95676e6c605c53440766af9a)  
  
  
## Detailed Description

[CAsaNetworkObject](class_c_asa_network_object.html "CAsaNetworkObject is the asa network object.") is the asa network object. 

## Member Function Documentation

## ◆ deleteNatEntry()

void CAsaNetworkObject::deleteNatEntry  | ( | | ) |   
---|---|---|---|---  
  
Remove static nat entry that is set to the asa network object. 

## ◆ deleteNatList()

void CAsaNetworkObject::deleteNatList  | ( | | ) |   
---|---|---|---|---  
  
Remove dynamic nat entry that is set to the asa network object. 

## ◆ getAddressStatement()

string CAsaNetworkObject::getAddressStatement  | ( | | ) |   
---|---|---|---|---  
  
Returns the host address/subnet mask statement configuration string in show run. 

Returns
    string, value is the host address/subnet mask statement configuration string in show run. 

## ◆ getHostIp()

ip CAsaNetworkObject::getHostIp  | ( | | ) |   
---|---|---|---|---  
  
Returns the host ip address/network address that is set to the asa network object. 

Returns
    ip, value is the host ip address/network address that is set to the asa network object. 

## ◆ getHostMask()

ip CAsaNetworkObject::getHostMask  | ( | | ) |   
---|---|---|---|---  
  
Returns the subnet mask that is set to the asa network object. 

Returns
    ip, value is the the subnet mask that is set to the asa network object. 

## ◆ getInvHostMask()

ip CAsaNetworkObject::getInvHostMask  | ( | | ) |   
---|---|---|---|---  
  
Returns the inverse subnet mask that is set to the asa network object. 

Returns
    ip, value is the the inverse subnet mask that is set to the asa network object. 

## ◆ getNatEntry()

[NatEntry](struct_nat_entry.html) CAsaNetworkObject::getNatEntry  | ( | | ) |   
---|---|---|---|---  
  
Returns static nat entry that is set to the asa network object. 

Returns
    [NatEntry](struct_nat_entry.html "Data element for NatEntry."), value is the static nat entry. 

## ◆ getNatList()

[NatListInterface](struct_nat_list_interface.html) CAsaNetworkObject::getNatList  | ( | | ) |   
---|---|---|---|---  
  
Returns dynamic nat entry that is set to the asa network object. 

Returns
    [NatListInterface](struct_nat_list_interface.html "Data element for NatListInterface."), value is the nat list interface. 

## ◆ getNatRunningConfig()

vector< string > CAsaNetworkObject::getNatRunningConfig  | ( | | ) |   
---|---|---|---|---  
  
Returns object + nat configuration strings in show run. 

Returns
    vector<string>, value object + nat configuration strings in show run 

## ◆ getNatStatement()

string CAsaNetworkObject::getNatStatement  | ( | | ) |   
---|---|---|---|---  
  
Returns the nat statement configuration string in show run. 

return string, value is the nat statement configuration string in show run. 

## ◆ getRunningConfig()

vector< string > CAsaNetworkObject::getRunningConfig  | ( | | ) |   
---|---|---|---|---  
  
Returns all object configuration strings in show run. 

Returns
    vector<string>, value is all object configuration strings in show run. 

## ◆ nameifChanged()

void CAsaNetworkObject::nameifChanged  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Remove nat entry when the referenced nameif is changed. 

Parameters
     newName,new| nameif   
---|---  
oldName,old| nameif   
  
## ◆ removeHostIp()

bool CAsaNetworkObject::removeHostIp  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Remove the host ip address that is set to the asa network object. 

Parameters
     hostIp,hos| ip address to remove.  
---|---  
  
Returns
    bool, value is true if the host was removed, false if not. 

## ◆ removeSubnet()

bool CAsaNetworkObject::removeSubnet  | ( | ip  | ,   
---|---|---|---  
|  | ip  |   
| ) | |   
  
Remove the subnet/mask that is set to the asa network object. 

Parameters
     hostIp,Host| ip address to remove for.   
---|---  
hostMask,Host| mask to remove for.  
  
Returns
    bool, return is true if the subnet was removed, false if not.   


## ◆ setHostIp()

void CAsaNetworkObject::setHostIp  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
set the host ip address to the asa network object 

Parameters
     hostIp,ip| address to use as the host.   
---|---  
  
## ◆ setSubnet()

void CAsaNetworkObject::setSubnet  | ( | ip  | ,   
---|---|---|---  
|  | ip  |   
| ) | |   
  
Set the subnet/mask to the asa network object. 

Parameters
     hostIp,Host| ip address to set with.   
---|---  
hostMask,Host| mask to set with.   
  
## ◆ updateAsaAclStatement()

void CAsaNetworkObject::updateAsaAclStatement  | ( | | ) |   
---|---|---|---|---  
  
Update the corresponding acl statements that have reference to this asa network object. 

* * *

The documentation for this class was generated from the following file:

  * [CAsaNetworkObject.pki](_c_asa_network_object_8pki.html)


