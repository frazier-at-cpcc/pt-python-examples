# Cisco Packet Tracer Extensions API: PrivilegeManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_privilege_manager.html

---

[PrivilegeManager](class_privilege_manager.html "PrivilegeManager handles and manipulates privileges on routers and switches.") handles and manipulates privileges on routers and switches. [More...](class_privilege_manager.html#details)

##  Public Member Functions  
  
---  
bool | [addCommand](class_privilege_manager.html#aadf0fab816052a4eb916d13ab42b2c9f) (string, string, bool, int)  
| Adds the specified command to the specified mode at the specified privilege level. [More...](class_privilege_manager.html#aadf0fab816052a4eb916d13ab42b2c9f)  
  
bool | [removeCommand](class_privilege_manager.html#af486e201f84fe9053ce94254f1888377) (string, string)  
| Removes the specified command from the specified mode. [More...](class_privilege_manager.html#af486e201f84fe9053ce94254f1888377)  
  
int | [getModeCount](class_privilege_manager.html#a051cad2162c3344b7c8b5aab062a870f) ()  
| Returns the number of modes. [More...](class_privilege_manager.html#a051cad2162c3344b7c8b5aab062a870f)  
  
string | [getModeAt](class_privilege_manager.html#a38879b03175552c772e5e8827b154582) (int)  
| Returns the mode at the specified index. [More...](class_privilege_manager.html#a38879b03175552c772e5e8827b154582)  
  
int | [getCommandForModeCount](class_privilege_manager.html#a756c59b915d341ca3dd519c6206d863e) (string)  
| Returns the number of commands for the specified mode. [More...](class_privilege_manager.html#a756c59b915d341ca3dd519c6206d863e)  
  
pair< string, [CommandPrivilege](struct_command_privilege.html) > | [getCommandForModeAt](class_privilege_manager.html#a65fff9e16ee05af04d54bf91cd1be785) (string, int)  
| Returns the command string and [CommandPrivilege](struct_command_privilege.html "Data element for CommandPrivilege.") object in the specified mode at the specified index. [More...](class_privilege_manager.html#a65fff9e16ee05af04d54bf91cd1be785)  
  
pair< string, [CommandPrivilege](struct_command_privilege.html) > | [getCommandForMode](class_privilege_manager.html#ad7aa80e24b6b166a56f957c6b7d28f41) (string, string)  
| Returns the command string and [CommandPrivilege](struct_command_privilege.html "Data element for CommandPrivilege.") object in the specified mode for the specified command. [More...](class_privilege_manager.html#ad7aa80e24b6b166a56f957c6b7d28f41)  
  
bool | [isCommandAdded](class_privilege_manager.html#a18b93685038e3318a291945e597adef2) (string)  
| Returns true if the command is already added, otherwise false. [More...](class_privilege_manager.html#a18b93685038e3318a291945e597adef2)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[PrivilegeManager](class_privilege_manager.html "PrivilegeManager handles and manipulates privileges on routers and switches.") handles and manipulates privileges on routers and switches. 

## Member Function Documentation

## ◆ addCommand()

bool PrivilegeManager::addCommand  | ( | string  | ,   
---|---|---|---  
|  | string  | ,   
|  | bool  | ,   
|  | int  |   
| ) | |   
  
Adds the specified command to the specified mode at the specified privilege level. 

Parameters
     mode,the| mode to add the command to. Valid modes: user, enable, global.   
---|---  
command,the| command of interest.   
bAll,true| to include all, false to not include all.   
level,the| privilege level.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ getCommandForMode()

pair< string, [CommandPrivilege](struct_command_privilege.html) > PrivilegeManager::getCommandForMode  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Returns the command string and [CommandPrivilege](struct_command_privilege.html "Data element for CommandPrivilege.") object in the specified mode for the specified command. 

Parameters
     mode,the| mode of interest. Valid modes: user, enable, global.   
---|---  
command,the| command of interest.  
  
Returns
    pair<string, [CommandPrivilege](struct_command_privilege.html "Data element for CommandPrivilege.")"CommandSet::SCommandPrivilege">, the command and [CommandPrivilege](struct_command_privilege.html "Data element for CommandPrivilege.") object. 

## ◆ getCommandForModeAt()

pair< string, [CommandPrivilege](struct_command_privilege.html) > PrivilegeManager::getCommandForModeAt  | ( | string  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Returns the command string and [CommandPrivilege](struct_command_privilege.html "Data element for CommandPrivilege.") object in the specified mode at the specified index. 

Parameters
     mode,the| mode of interest. Valid modes: user, enable, global.   
---|---  
index,the| index of the command of interest.  
  
Returns
    pair<string, [CommandPrivilege](struct_command_privilege.html "Data element for CommandPrivilege.")"CommandSet::SCommandPrivilege">, the command and [CommandPrivilege](struct_command_privilege.html "Data element for CommandPrivilege.") object. 

## ◆ getCommandForModeCount()

int PrivilegeManager::getCommandForModeCount  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the number of commands for the specified mode. 

Parameters
     mode,the| mode of interest. Valid modes: user, enable, global.  
---|---  
  
Returns
    int, the number of commands for the specified mode. 

## ◆ getModeAt()

string PrivilegeManager::getModeAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the mode at the specified index. 

Parameters
     index,the| index of the mode of interest.  
---|---  
  
Returns
    string, the mode at the specified index. 

## ◆ getModeCount()

int PrivilegeManager::getModeCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of modes. 

Returns
    int, the number of modes. 

## ◆ isCommandAdded()

bool PrivilegeManager::isCommandAdded  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns true if the command is already added, otherwise false. 

Parameters
     commandStr,command| string to check for.  
---|---  
  
Returns
    bool, true if the command is already added, otherwise false. 

## ◆ removeCommand()

bool PrivilegeManager::removeCommand  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Removes the specified command from the specified mode. 

Parameters
     mode,the| mode to add the command to. Valid modes: user, enable, global.   
---|---  
command,the| command of interest.  
  
Returns
    bool, true if successful, otherwise false. 

* * *

The documentation for this class was generated from the following file:

  * [CPrivilegeManager.pki](_c_privilege_manager_8pki.html)


