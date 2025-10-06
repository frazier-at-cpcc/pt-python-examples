# Cisco Packet Tracer Extensions API: PortSecurity Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_port_security.html

---

[PortSecurity](class_port_security.html "PortSecurity handles and manipulates port security on switch ports.") handles and manipulates port security on switch ports. [More...](class_port_security.html#details)

##  Public Member Functions  
  
---  
bool | [isEnabled](class_port_security.html#a17eacece8850d86bd88d6dd43838caea) ()  
| Returns true if port security is enabled, otherwise false. [More...](class_port_security.html#a17eacece8850d86bd88d6dd43838caea)  
  
void | [setEnabled](class_port_security.html#aaf69434e7ef8acfefc6f64990d73cafe) (bool)  
| Enables or disables port security. [More...](class_port_security.html#aaf69434e7ef8acfefc6f64990d73cafe)  
  
bool | [setMaxMacNumber](class_port_security.html#ac076705f6f6405d573ea7a477cf48167) (int)  
| Sets the port security max-mac-count. [More...](class_port_security.html#ac076705f6f6405d573ea7a477cf48167)  
  
int | [getMaxMacNumber](class_port_security.html#af53f8846c1e7e252d0ebc1251687334a) ()  
| Returns the port security max-mac-count. [More...](class_port_security.html#af53f8846c1e7e252d0ebc1251687334a)  
  
int | [getTotalMac](class_port_security.html#a384fe33faea029d98d9a297c8d45e4f6) ()  
| Returns the total number of MAC addresses. [More...](class_port_security.html#a384fe33faea029d98d9a297c8d45e4f6)  
  
int | [getViolationCount](class_port_security.html#af75e1296c75d529b442a36c4663c07e9) ()  
| Returns the number of violations. [More...](class_port_security.html#af75e1296c75d529b442a36c4663c07e9)  
  
pair< mac, int > | [getLastSourceMacVlan](class_port_security.html#aa43eea3ccd51a2a36c60baeeaecbfaaf) ()  
| Returns the last source MAC address and VLAN number. [More...](class_port_security.html#aa43eea3ccd51a2a36c60baeeaecbfaaf)  
  
void | [setViolationMode](class_port_security.html#a4b57af0338a6c641686504132653fe53) (PortViolation)  
| Sets the violation mode. [More...](class_port_security.html#a4b57af0338a6c641686504132653fe53)  
  
bool | [addSecureMacEntry](class_port_security.html#aeff14bf673538472ee5e0b764cffe9d5) (mac, bool)  
| Adds a secure MAC address entry. [More...](class_port_security.html#aeff14bf673538472ee5e0b764cffe9d5)  
  
bool | [removeSecureMacEntry](class_port_security.html#afcfd21e6c75fd01a691f44c709c75bef) (mac)  
| Removes the specified secure MAC address entry. [More...](class_port_security.html#afcfd21e6c75fd01a691f44c709c75bef)  
  
int | [getSecureMacCount](class_port_security.html#afb4f0c56b7af2656aee542ebf528e482) ()  
| Returns the number of secure MAC addresses. [More...](class_port_security.html#afb4f0c56b7af2656aee542ebf528e482)  
  
bool | [secureMacExist](class_port_security.html#a9556acad8b9fea3f08acea540d8fd855) (mac)  
| Returns true if the specified secure MAC address exists, otherwise false. [More...](class_port_security.html#a9556acad8b9fea3f08acea540d8fd855)  
  
[Port](class_port.html) | [getPort](class_port_security.html#a4c263f59c2a5c7b66d9f80223ccf2c3c) ()  
| Returns the switch port. [More...](class_port_security.html#a4c263f59c2a5c7b66d9f80223ccf2c3c)  
  
bool | [isStickyOn](class_port_security.html#a72e7dfbefa75a1bdae668d2214094da6) ()  
| Returns true if sticky is enabled, otherwise false. [More...](class_port_security.html#a72e7dfbefa75a1bdae668d2214094da6)  
  
void | [setStickyflag](class_port_security.html#aad407c24d83ba7cff8280dc8c0597d3e) (bool)  
| Enables or disables sticky. [More...](class_port_security.html#aad407c24d83ba7cff8280dc8c0597d3e)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[PortSecurity](class_port_security.html "PortSecurity handles and manipulates port security on switch ports.") handles and manipulates port security on switch ports. 

## Member Function Documentation

## ◆ addSecureMacEntry()

bool PortSecurity::addSecureMacEntry  | ( | mac  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Adds a secure MAC address entry. 

Parameters
     macAddress,the| MAC address to add.   
---|---  
isSticky,true| for sticky, false for not sticky.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ getLastSourceMacVlan()

pair< mac, int > PortSecurity::getLastSourceMacVlan  | ( | | ) |   
---|---|---|---|---  
  
Returns the last source MAC address and VLAN number. 

Returns
    pair<mac, int>, the last source MAC address and VLAN number. 

## ◆ getMaxMacNumber()

int PortSecurity::getMaxMacNumber  | ( | | ) |   
---|---|---|---|---  
  
Returns the port security max-mac-count. 

Returns
    int, the port security max-mac-count value. 

## ◆ getPort()

[Port](class_port.html) PortSecurity::getPort  | ( | | ) |   
---|---|---|---|---  
  
Returns the switch port. 

Returns
    [Port](class_port.html "Port holds and manipulates the ports on devices."), the [Port](class_port.html "Port holds and manipulates the ports on devices.") object. 

## ◆ getSecureMacCount()

int PortSecurity::getSecureMacCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of secure MAC addresses. 

Returns
    int, the number of secure MAC addresses. 

## ◆ getTotalMac()

int PortSecurity::getTotalMac  | ( | | ) |   
---|---|---|---|---  
  
Returns the total number of MAC addresses. 

Returns
    int, the total number of MAC addresses. 

## ◆ getViolationCount()

int PortSecurity::getViolationCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of violations. 

Returns
    int, the number of violations. 

## ◆ isEnabled()

bool PortSecurity::isEnabled  | ( | | ) |   
---|---|---|---|---  
  
Returns true if port security is enabled, otherwise false. 

Returns
    bool, true if port security is enabled, otherwise false. 

## ◆ isStickyOn()

bool PortSecurity::isStickyOn  | ( | | ) |   
---|---|---|---|---  
  
Returns true if sticky is enabled, otherwise false. 

Returns
    bool, true if sticky is enabled, otherwise false. 

## ◆ removeSecureMacEntry()

bool PortSecurity::removeSecureMacEntry  | ( | mac  | | ) |   
---|---|---|---|---|---  
  
Removes the specified secure MAC address entry. 

Parameters
     macAddress,the| MAC address to remove.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ secureMacExist()

bool PortSecurity::secureMacExist  | ( | mac  | | ) |   
---|---|---|---|---|---  
  
Returns true if the specified secure MAC address exists, otherwise false. 

Parameters
     macAddress,the| MAC address of interest.  
---|---  
  
Returns
    bool, true if the specified secure MAC address exists, otherwise false. 

## ◆ setEnabled()

void PortSecurity::setEnabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables port security. 

Parameters
     bEnable,true| to enable port security, false to disable it.   
---|---  
  
## ◆ setMaxMacNumber()

bool PortSecurity::setMaxMacNumber  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the port security max-mac-count. 

Parameters
     max,the| port security max-mac-count value.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ setStickyflag()

void PortSecurity::setStickyflag  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables sticky. 

Parameters
     isSticky,true| to enable sticky, false to disable it.   
---|---  
  
## ◆ setViolationMode()

void PortSecurity::setViolationMode  | ( | PortViolation  | | ) |   
---|---|---|---|---|---  
  
Sets the violation mode. 

Parameters
     type,the| violation mode. Violation modes: eShutdown = 0, eProtect = 1, eRestrict = 2   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CPortSecurity.pki](_c_port_security_8pki.html)


