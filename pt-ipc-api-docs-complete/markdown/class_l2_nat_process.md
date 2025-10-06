# Cisco Packet Tracer Extensions API: L2NatProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_l2_nat_process.html

---

[L2NatProcess](class_l2_nat_process.html "L2NatProcess is the process that handles Nat for asa.") is the process that handles Nat for asa. [More...](class_l2_nat_process.html#details)

##  Public Member Functions  
  
---  
vector< string > | [getInstanceNamesList](class_l2_nat_process.html#a6b3bbb3e20ca13d76ca8fc941406f62d) ()  
| Returns the instance names list. [More...](class_l2_nat_process.html#a6b3bbb3e20ca13d76ca8fc941406f62d)  
  
[L2NatInstance](class_l2_nat_instance.html) | [getNatInstance](class_l2_nat_process.html#a02b5c56762736411da82ad516558defc) (string)  
| Returns the nat instance. [More...](class_l2_nat_process.html#a02b5c56762736411da82ad516558defc)  
  
bool | [removeNatInstance](class_l2_nat_process.html#a1a5fcbfa7253fd15e3b81140e984ebdf) (string)  
| Removes the nat instance with the given name. [More...](class_l2_nat_process.html#a1a5fcbfa7253fd15e3b81140e984ebdf)  
  
bool | [addInstance](class_l2_nat_process.html#a2059f46ad500081355169014bcd0a25f) (string)  
| Adds a instance with the given name if no instance with that name already exists. [More...](class_l2_nat_process.html#a2059f46ad500081355169014bcd0a25f)  
  
int | [getTotalTranslation](class_l2_nat_process.html#ae74705f1cebb348359a15eec3e3f1300) ()  
| Returns the total translation count. [More...](class_l2_nat_process.html#ae74705f1cebb348359a15eec3e3f1300)  
  
int | [getTotalInstanceAttached](class_l2_nat_process.html#a8e0c2c4df93cc05107a35f4ecf94f050) ()  
| Returns the total instances attached. [More...](class_l2_nat_process.html#a8e0c2c4df93cc05107a35f4ecf94f050)  
  
vector< string > | [getAttachedNatInstanceList](class_l2_nat_process.html#a0decb4ea786aeaf577fecbc3e879f8cb) ()  
| Returns the list of attached nat instances. [More...](class_l2_nat_process.html#a0decb4ea786aeaf577fecbc3e879f8cb)  
  
int | [getTranslatedNatCount](class_l2_nat_process.html#a1ee5e999b45c47ed2ad901754cc0fd21) ()  
| Returns the total translated nat count. [More...](class_l2_nat_process.html#a1ee5e999b45c47ed2ad901754cc0fd21)  
  
int | [getArpFixupCount](class_l2_nat_process.html#a8eea9433e086c9ce2f49a8a52b26f9f0) ()  
| Returns the Arp Fixup count. [More...](class_l2_nat_process.html#a8eea9433e086c9ce2f49a8a52b26f9f0)  
  
int | [getTotalNatCount](class_l2_nat_process.html#ae47970a7405fd56c35d9ff3d1b2166ce) ()  
| Returns the total nat count. [More...](class_l2_nat_process.html#ae47970a7405fd56c35d9ff3d1b2166ce)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[L2NatProcess](class_l2_nat_process.html "L2NatProcess is the process that handles Nat for asa.") is the process that handles Nat for asa. 

## Member Function Documentation

## ◆ addInstance()

bool L2NatProcess::addInstance  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Adds a instance with the given name if no instance with that name already exists. 

Parameters
     instanceName,name| of the nat instance to add.  
---|---  
  
Returns
    bool, value is true if the instance could be added, false if not. 

## ◆ getArpFixupCount()

int L2NatProcess::getArpFixupCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the Arp Fixup count. 

Returns
    int, value is the Arp Fixup count. 

## ◆ getAttachedNatInstanceList()

vector< string > L2NatProcess::getAttachedNatInstanceList  | ( | | ) |   
---|---|---|---|---  
  
Returns the list of attached nat instances. 

Returns
    vector<string>, value is the list of attached nat instances. 

## ◆ getInstanceNamesList()

vector< string > L2NatProcess::getInstanceNamesList  | ( | | ) |   
---|---|---|---|---  
  
Returns the instance names list. 

Returns
    vector<string>, value is a list of the instance names. 

## ◆ getNatInstance()

[L2NatInstance](class_l2_nat_instance.html) L2NatProcess::getNatInstance  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the nat instance. 

Returns
    L2NatInsance, value is the nat instance. 

## ◆ getTotalInstanceAttached()

int L2NatProcess::getTotalInstanceAttached  | ( | | ) |   
---|---|---|---|---  
  
Returns the total instances attached. 

Returns
    int, value is the total instances attached to the instance. 

## ◆ getTotalNatCount()

int L2NatProcess::getTotalNatCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the total nat count. 

Returns
    int, value is the total nat count. 

## ◆ getTotalTranslation()

int L2NatProcess::getTotalTranslation  | ( | | ) |   
---|---|---|---|---  
  
Returns the total translation count. 

Returns
    int, value is the total translation count. 

## ◆ getTranslatedNatCount()

int L2NatProcess::getTranslatedNatCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the total translated nat count. 

Returns
    int, value is the total instances attached to the instance. 

## ◆ removeNatInstance()

bool L2NatProcess::removeNatInstance  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes the nat instance with the given name. 

Parameters
     instanceName,name| of the nat instance to remove.  
---|---  
  
Returns
    bool, value is true if a instance with the given name was removed, false if not. 

* * *

The documentation for this class was generated from the following file:

  * [CL2NatProcess.pki](_c_l2_nat_process_8pki.html)


