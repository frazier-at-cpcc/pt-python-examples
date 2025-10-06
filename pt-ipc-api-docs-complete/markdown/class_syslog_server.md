# Cisco Packet Tracer Extensions API: SyslogServer Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_syslog_server.html

---

[SyslogServer](class_syslog_server.html "SyslogServer handles and manipulates the Syslog service.") handles and manipulates the Syslog service. [More...](class_syslog_server.html#details)

##  Public Member Functions  
  
---  
void | [setEnable](class_syslog_server.html#a5c0dcd510c885e64ec423fc9de290e4d) (bool)  
| Enables or disables the Syslog service. [More...](class_syslog_server.html#a5c0dcd510c885e64ec423fc9de290e4d)  
  
bool | [isEnabled](class_syslog_server.html#a441a7b327bbfc57c79e174c3cfb18a41) ()  
| Returns true if the Syslog service is enabled, otherwise false. [More...](class_syslog_server.html#a441a7b327bbfc57c79e174c3cfb18a41)  
  
void | [setPortNumber](class_syslog_server.html#ad2168338acffe31bac16c9d55825d9b3) (short)  
| Sets the port number for the Syslog service. [More...](class_syslog_server.html#ad2168338acffe31bac16c9d55825d9b3)  
  
short | [getPortNumber](class_syslog_server.html#aec120236499f14adc13c8fadf1245748) ()  
| Returns the port number for the Syslog service. [More...](class_syslog_server.html#aec120236499f14adc13c8fadf1245748)  
  
void | [SyslogEntryAdded](class_syslog_server.html#a979068eac212cb64752497919594b2a7) ([SyslogEntry](struct_syslog_entry.html))  
| This event is emitted when a new syslog entry is added. [More...](class_syslog_server.html#a979068eac212cb64752497919594b2a7)  
  
vector< [SyslogEntry](struct_syslog_entry.html) > | [getAllEntries](class_syslog_server.html#ad3b975d65c46884389a1514b2d9e76b9) ()  
| Returns all Syslog entries. [More...](class_syslog_server.html#ad3b975d65c46884389a1514b2d9e76b9)  
  
void | [clearAllSysLogEntries](class_syslog_server.html#aeb467b70cba0e68b7053af51dd5d09e7) ()  
| Clear all syslog entries. [More...](class_syslog_server.html#aeb467b70cba0e68b7053af51dd5d09e7)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[SyslogServer](class_syslog_server.html "SyslogServer handles and manipulates the Syslog service.") handles and manipulates the Syslog service. 

## Member Function Documentation

## ◆ clearAllSysLogEntries()

void SyslogServer::clearAllSysLogEntries  | ( | | ) |   
---|---|---|---|---  
  
Clear all syslog entries. 

## ◆ getAllEntries()

vector< [SyslogEntry](struct_syslog_entry.html) > SyslogServer::getAllEntries  | ( | | ) |   
---|---|---|---|---  
  
Returns all Syslog entries. 

Returns
    vector of Syslog Entry 

## ◆ getPortNumber()

short SyslogServer::getPortNumber  | ( | | ) |   
---|---|---|---|---  
  
Returns the port number for the Syslog service. 

Returns
    short, the port number for the Syslog service. 

## ◆ isEnabled()

bool SyslogServer::isEnabled  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the Syslog service is enabled, otherwise false. 

Returns
    bool, true if the Syslog service is enabled, otherwise false. 

## ◆ setEnable()

void SyslogServer::setEnable  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables the Syslog service. 

Parameters
     bEnable,true| to enable the Syslog service, false to disable it.   
---|---  
  
## ◆ setPortNumber()

void SyslogServer::setPortNumber  | ( | short  | | ) |   
---|---|---|---|---|---  
  
Sets the port number for the Syslog service. 

Parameters
     portNum,the| port number for the Syslog service.   
---|---  
  
## ◆ SyslogEntryAdded()

void SyslogServer::SyslogEntryAdded  | ( | [SyslogEntry](struct_syslog_entry.html) | | ) |   
---|---|---|---|---|---  
  
This event is emitted when a new syslog entry is added. 

  * [SyslogEntry](struct_syslog_entry.html "Syslog entry structure."), the name of the external process source. 
  * srcCepInstanceId, the UUID of the external process source. 
  * message, the message from the external process source.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

* * *

The documentation for this class was generated from the following file:

  * [CSyslogServer.pki](_c_syslog_server_8pki.html)


