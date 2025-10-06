# Cisco Packet Tracer Extensions API: FlowMonitor Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_flow_monitor.html

---

[FlowMonitor](class_flow_monitor.html "FlowMonitor holds and manipulates the flow monitor.") holds and manipulates the flow monitor. [More...](class_flow_monitor.html#details)

##  Public Member Functions  
  
---  
string | [getMonitorName](class_flow_monitor.html#a244e6c25257126a54e21e5639a62398c) ()  
| Returns the name of the flow monitor. [More...](class_flow_monitor.html#a244e6c25257126a54e21e5639a62398c)  
  
[FlowRecord](struct_flow_record.html) | [getRecord](class_flow_monitor.html#acbf49eab64f8d34a65183905b213fde0) ()  
| Returns the flow record. [More...](class_flow_monitor.html#acbf49eab64f8d34a65183905b213fde0)  
  
void | [unsetRecord](class_flow_monitor.html#adc0bdcbef1fc1f6586eef0ec212a105a) ()  
| Unsets the flow record. [More...](class_flow_monitor.html#adc0bdcbef1fc1f6586eef0ec212a105a)  
  
[FlowMonitorData](class_flow_monitor_data.html) | [getInterfaceInput](class_flow_monitor.html#a1ee01646398c2def89fc327cc73653a5) (string, bool)  
| Returns the input flow monitor data on the specified interface. [More...](class_flow_monitor.html#a1ee01646398c2def89fc327cc73653a5)  
  
[FlowMonitorData](class_flow_monitor_data.html) | [getInterfaceOutput](class_flow_monitor.html#aff5e2c8aecb6f9460533cb0704d515db) (string, bool)  
| Returns the output flow monitor data on the specified interface. [More...](class_flow_monitor.html#aff5e2c8aecb6f9460533cb0704d515db)  
  
int | [getActiveFlowCount](class_flow_monitor.html#a7477acb1b13dac235b86bb6efbd1be50) ()  
| Returns the number of active flows. [More...](class_flow_monitor.html#a7477acb1b13dac235b86bb6efbd1be50)  
  
int | [getTotalFlowAdded](class_flow_monitor.html#a1ae9a41e6a343ec8d78fb649f31057be) ()  
| Returns the total number of flows. [More...](class_flow_monitor.html#a1ae9a41e6a343ec8d78fb649f31057be)  
  
int | [getMonitorDataCount](class_flow_monitor.html#a53577f587d6c085fb18de6efe8895fec) ()  
| Returns the number of flow monitor data. [More...](class_flow_monitor.html#a53577f587d6c085fb18de6efe8895fec)  
  
[FlowMonitorData](class_flow_monitor_data.html) | [getMonitorDataAt](class_flow_monitor.html#a11395de1cb4178fd856a36ebb8e661f0) (int)  
| Returns the flow monitor data at the specified index. [More...](class_flow_monitor.html#a11395de1cb4178fd856a36ebb8e661f0)  
  
int | [getExporterCount](class_flow_monitor.html#a00c9e78987e22edab698b616a3f819b8) ()  
| Returns the number of NetFlow exporters. [More...](class_flow_monitor.html#a00c9e78987e22edab698b616a3f819b8)  
  
[NFExporter](class_n_f_exporter.html) | [getExporterAt](class_flow_monitor.html#a59af53d7e3f7220141e0d68be25221f9) (int)  
| Returns the NetFlow exporter at the specified index. [More...](class_flow_monitor.html#a59af53d7e3f7220141e0d68be25221f9)  
  
string | [toString](class_flow_monitor.html#abbd9ebfcb82184ee5ab2e9ea8209cc18) ()  
| Returns the flow record output. [More...](class_flow_monitor.html#abbd9ebfcb82184ee5ab2e9ea8209cc18)  
  
bool | [monitorInUse](class_flow_monitor.html#a58ad0209141cbc59a2079d5c86102938) ()  
| Returns true if the flow monitor is in use, otherwise false. [More...](class_flow_monitor.html#a58ad0209141cbc59a2079d5c86102938)  
  
int | [getCurrentEntryCount](class_flow_monitor.html#a284334503cd69f3027b5b947d79c1460) ()  
| Returns the number of flows. [More...](class_flow_monitor.html#a284334503cd69f3027b5b947d79c1460)  
  
int | [getHighWaterMark](class_flow_monitor.html#a1c5e3ef6866ca065d0d3f7ac8431cc1d) ()  
| Returns the high watermark value. [More...](class_flow_monitor.html#a1c5e3ef6866ca065d0d3f7ac8431cc1d)  
  
int | [getFlowsAddedCount](class_flow_monitor.html#a5da9c26acbf649ae9a91e2f938c2d24b) ()  
| Returns the total number of flows. [More...](class_flow_monitor.html#a5da9c26acbf649ae9a91e2f938c2d24b)  
  
int | [getFlowsAgedCount](class_flow_monitor.html#afd698e9a9118f937f87c52f51eb32e11) ()  
| Returns the total number of expired flows. [More...](class_flow_monitor.html#afd698e9a9118f937f87c52f51eb32e11)  
  
int | [getActiveTimeoutCount](class_flow_monitor.html#a532d43803b355d588d67e4314a81e197) ()  
| Returns the total number of flows that were closed due to long activity. [More...](class_flow_monitor.html#a532d43803b355d588d67e4314a81e197)  
  
int | [getInactiveTimeoutCount](class_flow_monitor.html#aa1f9e77c4ac866b9362095e966049d92) ()  
| Returns the total number of flows that were closed due to inactivity. [More...](class_flow_monitor.html#aa1f9e77c4ac866b9362095e966049d92)  
  
[CacheFlowDatabase](class_cache_flow_database.html) | [getCacheDatabase](class_flow_monitor.html#a16d93171bd19456510d78d20659c6705) ()  
| Returns cache flow database. [More...](class_flow_monitor.html#a16d93171bd19456510d78d20659c6705)  
  
  
## Detailed Description

[FlowMonitor](class_flow_monitor.html "FlowMonitor holds and manipulates the flow monitor.") holds and manipulates the flow monitor. 

## Member Function Documentation

## ◆ getActiveFlowCount()

int FlowMonitor::getActiveFlowCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of active flows. 

Returns
    int, the number of active flows. 

## ◆ getActiveTimeoutCount()

int FlowMonitor::getActiveTimeoutCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the total number of flows that were closed due to long activity. 

Returns
    int, the total number of flows that were closed due to long activity. 

## ◆ getCacheDatabase()

[CacheFlowDatabase](class_cache_flow_database.html) FlowMonitor::getCacheDatabase  | ( | | ) |   
---|---|---|---|---  
  
Returns cache flow database. 

Returns
    [CacheFlowDatabase](class_cache_flow_database.html "CacheFlowDatabase handles and manipulates the NetFlow cache database."), the [CacheFlowDatabase](class_cache_flow_database.html "CacheFlowDatabase handles and manipulates the NetFlow cache database.") object. 

## ◆ getCurrentEntryCount()

int FlowMonitor::getCurrentEntryCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of flows. 

Returns
    int, the number of flows. 

## ◆ getExporterAt()

[NFExporter](class_n_f_exporter.html) FlowMonitor::getExporterAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the NetFlow exporter at the specified index. 

Parameters
     index,the| index of the NetFlow exporter of interest.  
---|---  
  
Returns
    [NFExporter](class_n_f_exporter.html "NFExporter handles and manipulates NetFlow exporters."), the [NFExporter](class_n_f_exporter.html "NFExporter handles and manipulates NetFlow exporters.") object at the specified index. 

## ◆ getExporterCount()

int FlowMonitor::getExporterCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of NetFlow exporters. 

Returns
    int, the number of NetFlow exporters. 

## ◆ getFlowsAddedCount()

int FlowMonitor::getFlowsAddedCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the total number of flows. 

Returns
    int, the total number of flows. 

## ◆ getFlowsAgedCount()

int FlowMonitor::getFlowsAgedCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the total number of expired flows. 

Returns
    int, the total number of expired flows. 

## ◆ getHighWaterMark()

int FlowMonitor::getHighWaterMark  | ( | | ) |   
---|---|---|---|---  
  
Returns the high watermark value. 

Returns
    int, the high watermark value. 

## ◆ getInactiveTimeoutCount()

int FlowMonitor::getInactiveTimeoutCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the total number of flows that were closed due to inactivity. 

Returns
    int, the total number of flows that were closed due to inactivity. 

## ◆ getInterfaceInput()

[FlowMonitorData](class_flow_monitor_data.html) FlowMonitor::getInterfaceInput  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Returns the input flow monitor data on the specified interface. 

Parameters
     interfaceName,interfaceName| can be one of the following plus an interface number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0   
---|---  
isIpv6,true| if IPv6, false if IPv4.  
  
Returns
    [FlowMonitorData](class_flow_monitor_data.html "FlowMonitorData tracks a monitor that has been assigned to an interface."), the [FlowMonitorData](class_flow_monitor_data.html "FlowMonitorData tracks a monitor that has been assigned to an interface.") object. 

## ◆ getInterfaceOutput()

[FlowMonitorData](class_flow_monitor_data.html) FlowMonitor::getInterfaceOutput  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Returns the output flow monitor data on the specified interface. 

Parameters
     interfaceName,interfaceName| can be one of the following plus an interface number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0   
---|---  
isIpv6,true| if IPv6, false if IPv4.  
  
Returns
    [FlowMonitorData](class_flow_monitor_data.html "FlowMonitorData tracks a monitor that has been assigned to an interface."), the [FlowMonitorData](class_flow_monitor_data.html "FlowMonitorData tracks a monitor that has been assigned to an interface.") object. 

## ◆ getMonitorDataAt()

[FlowMonitorData](class_flow_monitor_data.html) FlowMonitor::getMonitorDataAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the flow monitor data at the specified index. 

Parameters
     index,the| index of the flow monitor data of interest.  
---|---  
  
Returns
    [FlowMonitorData](class_flow_monitor_data.html "FlowMonitorData tracks a monitor that has been assigned to an interface."), the [FlowMonitorData](class_flow_monitor_data.html "FlowMonitorData tracks a monitor that has been assigned to an interface.") object at the specified index. 

## ◆ getMonitorDataCount()

int FlowMonitor::getMonitorDataCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of flow monitor data. 

Returns
    int, the number of flow monitor data. 

## ◆ getMonitorName()

string FlowMonitor::getMonitorName  | ( | | ) |   
---|---|---|---|---  
  
Returns the name of the flow monitor. 

Returns
    string, the name of the flow monitor. 

## ◆ getRecord()

[FlowRecord](struct_flow_record.html) FlowMonitor::getRecord  | ( | | ) |   
---|---|---|---|---  
  
Returns the flow record. 

Returns
    [FlowRecord](struct_flow_record.html "FlowRecord structure."), the [FlowRecord](struct_flow_record.html "FlowRecord structure.") object. 

## ◆ getTotalFlowAdded()

int FlowMonitor::getTotalFlowAdded  | ( | | ) |   
---|---|---|---|---  
  
Returns the total number of flows. 

Returns
    int, the total number of flows. 

## ◆ monitorInUse()

bool FlowMonitor::monitorInUse  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the flow monitor is in use, otherwise false. 

Returns
    bool, true if the flow monitor is in use, otherwise false. 

## ◆ toString()

string FlowMonitor::toString  | ( | | ) |   
---|---|---|---|---  
  
Returns the flow record output. 

Returns
    string, the flow record output. 

## ◆ unsetRecord()

void FlowMonitor::unsetRecord  | ( | | ) |   
---|---|---|---|---  
  
Unsets the flow record. 

* * *

The documentation for this class was generated from the following file:

  * [CFlowMonitor.pki](_c_flow_monitor_8pki.html)


