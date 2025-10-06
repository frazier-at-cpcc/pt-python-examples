# Cisco Packet Tracer Extensions API: FlowMonitorData Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_flow_monitor_data.html

---

[FlowMonitorData](class_flow_monitor_data.html "FlowMonitorData tracks a monitor that has been assigned to an interface.") tracks a monitor that has been assigned to an interface. [More...](class_flow_monitor_data.html#details)

##  Public Member Functions  
  
---  
Netflow::ENetflowDirection | [getDirection](class_flow_monitor_data.html#a635df60ef50de6cd9dd620a27ac40da1) ()  
| Returns the direction of the flow. [More...](class_flow_monitor_data.html#a635df60ef50de6cd9dd620a27ac40da1)  
  
void | [setDirection](class_flow_monitor_data.html#aad2cf025794ff33229f289314b4e6e7f) (Netflow::ENetflowDirection)  
| Sets the direction of the flow. [More...](class_flow_monitor_data.html#aad2cf025794ff33229f289314b4e6e7f)  
  
string | [getInterfaceName](class_flow_monitor_data.html#aca32255133e4219b0d9f31ed0c46c34d) ()  
| Returns the name of the interface. [More...](class_flow_monitor_data.html#aca32255133e4219b0d9f31ed0c46c34d)  
  
int | [getFlowCount](class_flow_monitor_data.html#a8c298caafa982d9575d448c336124dbc) ()  
| Returns the number of flows. [More...](class_flow_monitor_data.html#a8c298caafa982d9575d448c336124dbc)  
  
[NetflowFlow](class_netflow_flow.html) | [getFlowAt](class_flow_monitor_data.html#adfda6e9481d841010a49267dfa7d06fa) (int)  
| Returns the flow at the specified index. [More...](class_flow_monitor_data.html#adfda6e9481d841010a49267dfa7d06fa)  
  
int | [getTotalFlowCount](class_flow_monitor_data.html#ad04d2d1271247360bdab9133e59e5ef0) ()  
| Returns the total number of flows that were created by this monitor on this interface. [More...](class_flow_monitor_data.html#ad04d2d1271247360bdab9133e59e5ef0)  
  
int | [getWaterMarkCount](class_flow_monitor_data.html#aac585e902078fd05661e112e03d8bd5b) ()  
| Returns the number of watermarks. [More...](class_flow_monitor_data.html#aac585e902078fd05661e112e03d8bd5b)  
  
int | [getInactiveExpireCount](class_flow_monitor_data.html#afd0d479d6403701615101ab8e551a736) ()  
| Returns the total number of flows that were closed due to inactivity. [More...](class_flow_monitor_data.html#afd0d479d6403701615101ab8e551a736)  
  
int | [getActiveExpireCount](class_flow_monitor_data.html#a5011807d18d7772d529e77aae577d050) ()  
| Returns the total number of flows that were closed due to long activity. [More...](class_flow_monitor_data.html#a5011807d18d7772d529e77aae577d050)  
  
bool | [isIpv6](class_flow_monitor_data.html#a881deabd8f158bad9b8d95dcf5e3f822) ()  
| Returns true if this flow monitor data is IPv6, otherwise false. [More...](class_flow_monitor_data.html#a881deabd8f158bad9b8d95dcf5e3f822)  
  
bool | [isSameMonitor](class_flow_monitor_data.html#abf63c9d779a186f8bf5fa1522fc74164) (string, bool)  
| Returns true if the specified interface is the same flow monitor data, otherwise false. [More...](class_flow_monitor_data.html#abf63c9d779a186f8bf5fa1522fc74164)  
  
bool | [hasInput](class_flow_monitor_data.html#a5571bad032791664242de5bdc5eb6065) ()  
| Returns true if this flow monitor data has input, otherwise false. [More...](class_flow_monitor_data.html#a5571bad032791664242de5bdc5eb6065)  
  
bool | [hasOutput](class_flow_monitor_data.html#a5fcd1ef0d2fabf599c3c5efdeca49ae1) ()  
| Returns true if this flow monitor data has output, otherwise false. [More...](class_flow_monitor_data.html#a5fcd1ef0d2fabf599c3c5efdeca49ae1)  
  
[FlowMonitor](class_flow_monitor.html) | [getFlowMonitor](class_flow_monitor_data.html#a77661784db282b60fcefc2d710456343) ()  
| Returns the flow monitor associated with this flow monitor data. [More...](class_flow_monitor_data.html#a77661784db282b60fcefc2d710456343)  
  
  
## Detailed Description

[FlowMonitorData](class_flow_monitor_data.html "FlowMonitorData tracks a monitor that has been assigned to an interface.") tracks a monitor that has been assigned to an interface. 

## Member Function Documentation

## ◆ getActiveExpireCount()

int FlowMonitorData::getActiveExpireCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the total number of flows that were closed due to long activity. 

Returns
    int, the total number of flows that were closed due to long activity. 

## ◆ getDirection()

Netflow::ENetflowDirection FlowMonitorData::getDirection  | ( | | ) |   
---|---|---|---|---  
  
Returns the direction of the flow. 

Returns
    enum<Netflow::ENetflowDirection>, the direction of the flow. [Flow](class_flow.html "Flow holds and manipulates the flow routes in FlowTable objects.") directions: eInput = 0, eOutput = 1, eInputOutput = 2 

## ◆ getFlowAt()

[NetflowFlow](class_netflow_flow.html) FlowMonitorData::getFlowAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the flow at the specified index. 

Parameters
     index,the| index of the flow of interest.  
---|---  
  
Returns
    [NetflowFlow](class_netflow_flow.html "NetflowFlow holds and manipulates NetFlow flows."), the [NetflowFlow](class_netflow_flow.html "NetflowFlow holds and manipulates NetFlow flows.") object at the specified index. 

## ◆ getFlowCount()

int FlowMonitorData::getFlowCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of flows. 

Returns
    string, the number of flows. 

## ◆ getFlowMonitor()

[FlowMonitor](class_flow_monitor.html) FlowMonitorData::getFlowMonitor  | ( | | ) |   
---|---|---|---|---  
  
Returns the flow monitor associated with this flow monitor data. 

Returns
    [FlowMonitor](class_flow_monitor.html "FlowMonitor holds and manipulates the flow monitor."), the [FlowMonitor](class_flow_monitor.html "FlowMonitor holds and manipulates the flow monitor.") object associated with this flow monitor data. 

## ◆ getInactiveExpireCount()

int FlowMonitorData::getInactiveExpireCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the total number of flows that were closed due to inactivity. 

Returns
    int, the total number of flows that were closed due to inactivity. 

## ◆ getInterfaceName()

string FlowMonitorData::getInterfaceName  | ( | | ) |   
---|---|---|---|---  
  
Returns the name of the interface. 

Returns
    string, the name of the interface. 

## ◆ getTotalFlowCount()

int FlowMonitorData::getTotalFlowCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the total number of flows that were created by this monitor on this interface. 

Returns
    int, the total number of flows that were created by this monitor on this interface. 

## ◆ getWaterMarkCount()

int FlowMonitorData::getWaterMarkCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of watermarks. 

Returns
    int, the number of watermarks. 

## ◆ hasInput()

bool FlowMonitorData::hasInput  | ( | | ) |   
---|---|---|---|---  
  
Returns true if this flow monitor data has input, otherwise false. 

Returns
    bool, true if this flow monitor data has input, otherwise false. 

## ◆ hasOutput()

bool FlowMonitorData::hasOutput  | ( | | ) |   
---|---|---|---|---  
  
Returns true if this flow monitor data has output, otherwise false. 

Returns
    bool, true if this flow monitor data has output, otherwise false. 

## ◆ isIpv6()

bool FlowMonitorData::isIpv6  | ( | | ) |   
---|---|---|---|---  
  
Returns true if this flow monitor data is IPv6, otherwise false. 

Returns
    bool, true if this flow monitor data is IPv6, otherwise false. 

## ◆ isSameMonitor()

bool FlowMonitorData::isSameMonitor  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Returns true if the specified interface is the same flow monitor data, otherwise false. 

Parameters
     intName,intName| can be one of the following plus an interface number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0   
---|---  
isIpv6,true| if IPv6, false if IPv4.  
  
Returns
    bool, true if the specified interface is the same flow monitor data, otherwise false. 

## ◆ setDirection()

void FlowMonitorData::setDirection  | ( | Netflow::ENetflowDirection  | | ) |   
---|---|---|---|---|---  
  
Sets the direction of the flow. 

Parameters
     direction,the| direction of the flow. [Flow](class_flow.html "Flow holds and manipulates the flow routes in FlowTable objects.") directions: eInput = 0, eOutput = 1, eInputOutput=2   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CFlowMonitorData.pki](_c_flow_monitor_data_8pki.html)


