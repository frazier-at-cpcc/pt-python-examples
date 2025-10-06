# Cisco Packet Tracer Extensions API: CommandLog Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_command_log.html

---

[CommandLog](class_command_log.html "CommandLog serves as the entry point to all command log objects.") serves as the entry point to all command log objects. [More...](class_command_log.html#details)

##  Public Member Functions  
  
---  
void | [clear](class_command_log.html#a9e919bca983ef944e6fd228ab8aa5e75) ()  
| Clears the command log. [More...](class_command_log.html#a9e919bca983ef944e6fd228ab8aa5e75)  
  
void | [setEnabled](class_command_log.html#a0cb1c1a4d00c15a31b7eaa8544d914f9) (bool)  
| Enables or disables the command log. [More...](class_command_log.html#a0cb1c1a4d00c15a31b7eaa8544d914f9)  
  
bool | [isEnabled](class_command_log.html#aac5e378c74ae114b2b42937c29ad3d39) ()  
| Returns true if the command log is enabled, otherwise false. [More...](class_command_log.html#aac5e378c74ae114b2b42937c29ad3d39)  
  
int | [getEntryCount](class_command_log.html#a567f0eb7e37399e9b9409e94d0912a7d) ()  
| Returns the command log entry count. [More...](class_command_log.html#a567f0eb7e37399e9b9409e94d0912a7d)  
  
[CommandLogEntry](class_command_log_entry.html) | [getEntryAt](class_command_log.html#a119b69dcd17b20bedea967c2c1888e56) (int)  
| Returns the [CommandLogEntry](class_command_log_entry.html "CommandLogEntry is a command log entry in the command log.") object at the specified index. [More...](class_command_log.html#a119b69dcd17b20bedea967c2c1888e56)  
  
void | [entryAdded](class_command_log.html#a13c7b11ebed6e4e6f10c039def95617f) (int)  
| This event is emitted when an entry is added to the command log. [More...](class_command_log.html#a13c7b11ebed6e4e6f10c039def95617f)  
  
  
## Detailed Description

[CommandLog](class_command_log.html "CommandLog serves as the entry point to all command log objects.") serves as the entry point to all command log objects. 

## Member Function Documentation

## ◆ clear()

void CommandLog::clear  | ( | | ) |   
---|---|---|---|---  
  
Clears the command log. 

## ◆ entryAdded()

void CommandLog::entryAdded  | ( | int  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when an entry is added to the command log. 

  * index, the index of the added entry.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ getEntryAt()

[CommandLogEntry](class_command_log_entry.html) CommandLog::getEntryAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the [CommandLogEntry](class_command_log_entry.html "CommandLogEntry is a command log entry in the command log.") object at the specified index. 

Parameters
     index,the| index of the [CommandLogEntry](class_command_log_entry.html "CommandLogEntry is a command log entry in the command log.") object of interest.  
---|---  
  
Returns
    [CommandLogEntry](class_command_log_entry.html "CommandLogEntry is a command log entry in the command log."), the [CommandLogEntry](class_command_log_entry.html "CommandLogEntry is a command log entry in the command log.") object at the specified index. 

## ◆ getEntryCount()

int CommandLog::getEntryCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the command log entry count. 

Returns
    int, the command log entry count. 

## ◆ isEnabled()

bool CommandLog::isEnabled  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the command log is enabled, otherwise false. 

Returns
    bool, true if the command log is enabled, otherwise false. 

## ◆ setEnabled()

void CommandLog::setEnabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables the command log. 

Parameters
     enabled,true| to enable the command log, false to disable it.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CCommandLog.pki](_c_command_log_8pki.html)


