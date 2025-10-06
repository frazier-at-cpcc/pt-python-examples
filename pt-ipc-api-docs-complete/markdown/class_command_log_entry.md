# Cisco Packet Tracer Extensions API: CommandLogEntry Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_command_log_entry.html

---

[CommandLogEntry](class_command_log_entry.html "CommandLogEntry is a command log entry in the command log.") is a command log entry in the command log. [More...](class_command_log_entry.html#details)

##  Public Member Functions  
  
---  
QString | [getTimeToString](class_command_log_entry.html#aff60068b733e64ece19e36efec0d29a2) ()  
| Returns the timestamp of this command log entry. [More...](class_command_log_entry.html#aff60068b733e64ece19e36efec0d29a2)  
  
QString | [getDeviceName](class_command_log_entry.html#a83178423cc3649cb1898867258b38b13) ()  
| Returns the device name where this command log entry originated from. [More...](class_command_log_entry.html#a83178423cc3649cb1898867258b38b13)  
  
string | [getPrompt](class_command_log_entry.html#a626393279f0f2eee39e6c92fe2000894) ()  
| Returns the command prompt of this command log entry. [More...](class_command_log_entry.html#a626393279f0f2eee39e6c92fe2000894)  
  
string | [getCommand](class_command_log_entry.html#a2b8528a94a2eb66030ec675c1d7b9fae) ()  
| Returns the command of this command log entry. [More...](class_command_log_entry.html#a2b8528a94a2eb66030ec675c1d7b9fae)  
  
string | [getResolvedCommand](class_command_log_entry.html#a5625fa4bded83d3397cac0bbe663193d) ()  
| Returns the resolved command of this command log entry. [More...](class_command_log_entry.html#a5625fa4bded83d3397cac0bbe663193d)  
  
  
## Detailed Description

[CommandLogEntry](class_command_log_entry.html "CommandLogEntry is a command log entry in the command log.") is a command log entry in the command log. 

## Member Function Documentation

## ◆ getCommand()

string CommandLogEntry::getCommand  | ( | | ) |   
---|---|---|---|---  
  
Returns the command of this command log entry. 

Returns
    string, the command prompt of this command log entry. 

## ◆ getDeviceName()

QString CommandLogEntry::getDeviceName  | ( | | ) |   
---|---|---|---|---  
  
Returns the device name where this command log entry originated from. 

Returns
    QString, the device name where this command log entry originated from. 

## ◆ getPrompt()

string CommandLogEntry::getPrompt  | ( | | ) |   
---|---|---|---|---  
  
Returns the command prompt of this command log entry. 

Returns
    QString, the command prompt of this command log entry. 

## ◆ getResolvedCommand()

string CommandLogEntry::getResolvedCommand  | ( | | ) |   
---|---|---|---|---  
  
Returns the resolved command of this command log entry. 

Returns
    string, the resolved command of this command log entry. 

## ◆ getTimeToString()

QString CommandLogEntry::getTimeToString  | ( | | ) |   
---|---|---|---|---  
  
Returns the timestamp of this command log entry. 

Returns
    QString, the timestamp of this command log entry. 

* * *

The documentation for this class was generated from the following file:

  * [CCommandLogEntry.pki](_c_command_log_entry_8pki.html)


