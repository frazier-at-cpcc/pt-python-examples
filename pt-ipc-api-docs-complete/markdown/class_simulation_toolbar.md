# Cisco Packet Tracer Extensions API: SimulationToolbar Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_simulation_toolbar.html

---

[SimulationToolbar](class_simulation_toolbar.html "SimulationToolbar allows UI for manipulation of the Simulation toolbar.") allows UI for manipulation of the [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") toolbar. [More...](class_simulation_toolbar.html#details)

##  Public Member Functions  
  
---  
void | [setVisible](class_simulation_toolbar.html#ad5cf42664958a28b71847fd23e869c7e) (bool)  
| Shows or hides this widget from view. [More...](class_simulation_toolbar.html#ad5cf42664958a28b71847fd23e869c7e)  
  
void | [setWidgetVisible](class_simulation_toolbar.html#a674ef974a6346ad2cd38c6814f85727a) (string, bool)  
| Shows or hides the specified child widget. [More...](class_simulation_toolbar.html#a674ef974a6346ad2cd38c6814f85727a)  
  
void | [setDisabled](class_simulation_toolbar.html#a370c528d150efea1d2f494339fe2029a) (bool)  
| Enables or disables input events to this widget. [More...](class_simulation_toolbar.html#a370c528d150efea1d2f494339fe2029a)  
  
void | [setWidgetDisable](class_simulation_toolbar.html#a6cef18dec132a6856312950538f75921) (string, bool)  
| Enables or disables the specified child widget. [More...](class_simulation_toolbar.html#a6cef18dec132a6856312950538f75921)  
  
bool | [isEventListOn](class_simulation_toolbar.html#af93047ee6d6802cb02eb248cdb27ffbd) ()  
| Returns true if the [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") Panel is shown, otherwise false. [More...](class_simulation_toolbar.html#af93047ee6d6802cb02eb248cdb27ffbd)  
  
void | [setEventListToggle](class_simulation_toolbar.html#ab48cd6297f4322faeca30a38ac149f5f) (bool)  
| Shows or hides the [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") Panel. [More...](class_simulation_toolbar.html#ab48cd6297f4322faeca30a38ac149f5f)  
  
void | [resetNetwork](class_simulation_toolbar.html#a2ad8a5092c706c2cbf64460657f749fe) ()  
| Simulations clicking on the Power Cycle Devices button on the [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") toolbar. [More...](class_simulation_toolbar.html#a2ad8a5092c706c2cbf64460657f749fe)  
  
  
## Detailed Description

[SimulationToolbar](class_simulation_toolbar.html "SimulationToolbar allows UI for manipulation of the Simulation toolbar.") allows UI for manipulation of the [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") toolbar. 

## Member Function Documentation

## ◆ isEventListOn()

bool SimulationToolbar::isEventListOn  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") Panel is shown, otherwise false. 

Returns
    bool, true if the [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") Panel is shown, otherwise false. 

## ◆ resetNetwork()

void SimulationToolbar::resetNetwork  | ( | | ) |   
---|---|---|---|---  
  
Simulations clicking on the Power Cycle Devices button on the [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") toolbar. 

## ◆ setDisabled()

void SimulationToolbar::setDisabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables input events to this widget. 

Parameters
     bDisabled,true| to disable input events to this widget, false to enable input events.   
---|---  
  
## ◆ setEventListToggle()

void SimulationToolbar::setEventListToggle  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows or hides the [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") Panel. 

Parameters
     bEnable,true| to show the [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") Panel, false to hide it.   
---|---  
  
## ◆ setVisible()

void SimulationToolbar::setVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows or hides this widget from view. 

Parameters
     bVisible,true| to show this widget, false to hide it.   
---|---  
  
## ◆ setWidgetDisable()

void SimulationToolbar::setWidgetDisable  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Enables or disables the specified child widget. 

Parameters
     widgetName,where| widgetName can be one of the following: ResetNetworkBtn, BackBtn, PlayBtn, ForwardBtn, EventListBtn.   
---|---  
bDisabled,true| to disable input events to this child widget, false to enable input events.   
  
## ◆ setWidgetVisible()

void SimulationToolbar::setWidgetVisible  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Shows or hides the specified child widget. 

Parameters
     widgetName,where| widgetName can be one of the following: ResetNetworkBtn, BackBtn, PlayBtn, ForwardBtn, EventListBtn.   
---|---  
bVisible,true| to show this child widget, false to hide it.   
  
* * *

The documentation for this class was generated from the following file:

  * [SimulationToolbar.pki](_simulation_toolbar_8pki.html)


