# Cisco Packet Tracer Extensions API: RSSwitch Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_r_s_switch.html

---

[RSSwitch](class_r_s_switch.html "RSSwitch allows for manipulation of the Realtime and Simulation toggle switches.") allows for manipulation of the Realtime and [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") toggle switches. [More...](class_r_s_switch.html#details)

##  Public Member Functions  
  
---  
void | [setVisible](class_r_s_switch.html#acf5ad86ddf46096fac63be7d5cf0beb6) (bool)  
| Shows or hides this widget from view. [More...](class_r_s_switch.html#acf5ad86ddf46096fac63be7d5cf0beb6)  
  
void | [setWidgetVisible](class_r_s_switch.html#a40e40058db6ff132c5c64de952e3eda3) (string, bool)  
| Shows or hides the specified child widget. [More...](class_r_s_switch.html#a40e40058db6ff132c5c64de952e3eda3)  
  
void | [setDisabled](class_r_s_switch.html#a49905fae1937ff255f1cd1b926c403e5) (bool)  
| Enables or disables input events to this widget. [More...](class_r_s_switch.html#a49905fae1937ff255f1cd1b926c403e5)  
  
void | [setWidgetDisable](class_r_s_switch.html#ac80da812404856b299139971407f061d) (string, bool)  
| Enables or disables the specified child widget. [More...](class_r_s_switch.html#ac80da812404856b299139971407f061d)  
  
void | [showRealtimeMode](class_r_s_switch.html#a1c77c645e3bae1b9ed7492f4e037d273) ()  
| Switches to Realtime mode. [More...](class_r_s_switch.html#a1c77c645e3bae1b9ed7492f4e037d273)  
  
void | [showSimulationMode](class_r_s_switch.html#a93f197f8530f4b93efedec388ae6a4ab) ()  
| Switches to [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") mode. [More...](class_r_s_switch.html#a93f197f8530f4b93efedec388ae6a4ab)  
  
void | [modeSwitched](class_r_s_switch.html#a28d1081497f563ac963284138a68a44c) (bool)  
| This event is emitted when the mode is switched between Realtime and [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc."). [More...](class_r_s_switch.html#a28d1081497f563ac963284138a68a44c)  
  
  
## Detailed Description

[RSSwitch](class_r_s_switch.html "RSSwitch allows for manipulation of the Realtime and Simulation toggle switches.") allows for manipulation of the Realtime and [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") toggle switches. 

## Member Function Documentation

## ◆ modeSwitched()

void RSSwitch::modeSwitched  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when the mode is switched between Realtime and [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc."). 

  * isRealtime, true if the mode is switched to Realtime mode, otherwise false.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ setDisabled()

void RSSwitch::setDisabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables input events to this widget. 

Parameters
     bDisabled,true| to disable input events to this widget, false to enable input events.   
---|---  
  
## ◆ setVisible()

void RSSwitch::setVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows or hides this widget from view. 

Parameters
     bVisible,true| to show this widget, false to hide it.   
---|---  
  
## ◆ setWidgetDisable()

void RSSwitch::setWidgetDisable  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Enables or disables the specified child widget. 

Parameters
     widgetName,where| widgetName can be one of the following: RealtimeBtn, SimulationBtn.   
---|---  
bDisabled,true| to disable input events to this child widget, false to enable input events.   
  
## ◆ setWidgetVisible()

void RSSwitch::setWidgetVisible  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Shows or hides the specified child widget. 

Parameters
     widgetName,where| widgetName can be one of the following: RealtimeBtn, SimulationBtn.   
---|---  
bVisible,true| to show this child widget, false to hide it.   
  
## ◆ showRealtimeMode()

void RSSwitch::showRealtimeMode  | ( | | ) |   
---|---|---|---|---  
  
Switches to Realtime mode. 

## ◆ showSimulationMode()

void RSSwitch::showSimulationMode  | ( | | ) |   
---|---|---|---|---  
  
Switches to [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") mode. 

* * *

The documentation for this class was generated from the following file:

  * [RSSwitch.pki](_r_s_switch_8pki.html)


