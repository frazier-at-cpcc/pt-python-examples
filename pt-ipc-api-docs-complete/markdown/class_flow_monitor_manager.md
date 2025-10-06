# Cisco Packet Tracer Extensions API: FlowMonitorManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_flow_monitor_manager.html

---

[FlowMonitorManager](class_flow_monitor_manager.html "FlowMonitorManager manages all the flow monitors defined on a device.") manages all the flow monitors defined on a device. [More...](class_flow_monitor_manager.html#details)

##  Public Member Functions  
  
---  
int | [getMonitorCount](class_flow_monitor_manager.html#ab3527fb271fe25e86e8a8052c62f7ffe) ()  
| Returns the number of flow monitors. [More...](class_flow_monitor_manager.html#ab3527fb271fe25e86e8a8052c62f7ffe)  
  
[FlowMonitor](class_flow_monitor.html) | [getMonitorAt](class_flow_monitor_manager.html#ac2a637f3530aed9b5ab0fab8134c8f8b) (int)  
| Returns the flow monitor at the specified index. [More...](class_flow_monitor_manager.html#ac2a637f3530aed9b5ab0fab8134c8f8b)  
  
[FlowMonitor](class_flow_monitor.html) | [getMonitor](class_flow_monitor_manager.html#ac07614fe5369ebcff38db7286d267dda) (string)  
| Returns the flow monitor with the specified name. [More...](class_flow_monitor_manager.html#ac07614fe5369ebcff38db7286d267dda)  
  
[FlowMonitor](class_flow_monitor.html) | [createMonitor](class_flow_monitor_manager.html#a584f65121537eb8e42292419a9390d21) (string)  
| Creates a flow monitor with the specified name. [More...](class_flow_monitor_manager.html#a584f65121537eb8e42292419a9390d21)  
  
void | [removeMonitor](class_flow_monitor_manager.html#a95700873fb988a08aff502320b0b32a4) (string)  
| Removes the flow monitor with the specified name. [More...](class_flow_monitor_manager.html#a95700873fb988a08aff502320b0b32a4)  
  
  
## Detailed Description

[FlowMonitorManager](class_flow_monitor_manager.html "FlowMonitorManager manages all the flow monitors defined on a device.") manages all the flow monitors defined on a device. 

## Member Function Documentation

## ◆ createMonitor()

[FlowMonitor](class_flow_monitor.html) FlowMonitorManager::createMonitor  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Creates a flow monitor with the specified name. 

Parameters
     monitorName,the| name of the flow monitor.  
---|---  
  
Returns
    [FlowMonitor](class_flow_monitor.html "FlowMonitor holds and manipulates the flow monitor."), the flow monitor with the specified name. 

## ◆ getMonitor()

[FlowMonitor](class_flow_monitor.html) FlowMonitorManager::getMonitor  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the flow monitor with the specified name. 

Parameters
     monitorName,the| name of the flow monitor of interest.  
---|---  
  
Returns
    [FlowMonitor](class_flow_monitor.html "FlowMonitor holds and manipulates the flow monitor."), the flow monitor with the specified name. 

## ◆ getMonitorAt()

[FlowMonitor](class_flow_monitor.html) FlowMonitorManager::getMonitorAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the flow monitor at the specified index. 

Parameters
     index,the| index of the flow monitor of interest.  
---|---  
  
Returns
    [FlowMonitor](class_flow_monitor.html "FlowMonitor holds and manipulates the flow monitor."), the flow monitor at the specified index. 

## ◆ getMonitorCount()

int FlowMonitorManager::getMonitorCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of flow monitors. 

Returns
    int, the number of flow monitors. 

## ◆ removeMonitor()

void FlowMonitorManager::removeMonitor  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes the flow monitor with the specified name. 

Parameters
     monitorName,the| name of the flow monitor of interest.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CFlowMonitorManager.pki](_c_flow_monitor_manager_8pki.html)


