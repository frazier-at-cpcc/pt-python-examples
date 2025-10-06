# Cisco Packet Tracer Extensions API: SimulationPanel Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_simulation_panel.html

---

[SimulationPanel](class_simulation_panel.html "SimulationPanel allows for UI manipulation of the Simulation Panel.") allows for UI manipulation of the [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") Panel. [More...](class_simulation_panel.html#details)

##  Public Member Functions  
  
---  
void | [setVisible](class_simulation_panel.html#a327334eee0039463c6c860b1c6a598c5) (bool)  
| Shows or hides this widget from view. [More...](class_simulation_panel.html#a327334eee0039463c6c860b1c6a598c5)  
  
void | [setWidgetVisible](class_simulation_panel.html#a241a108fc329c419b20e9a60c8874105) (string, bool)  
| Shows or hides the specified child widget. [More...](class_simulation_panel.html#a241a108fc329c419b20e9a60c8874105)  
  
void | [setDisabled](class_simulation_panel.html#a73ba1ebe695606cd6cbf228983266606) (bool)  
| Enables or disables input events to this widget. [More...](class_simulation_panel.html#a73ba1ebe695606cd6cbf228983266606)  
  
void | [setWidgetDisable](class_simulation_panel.html#a66f1d84313cd6fa97e5c09b2d1c74649) (string, bool)  
| Enables or disables the specified child widget. [More...](class_simulation_panel.html#a66f1d84313cd6fa97e5c09b2d1c74649)  
  
void | [resetSimulation](class_simulation_panel.html#a709c94305179d19938a57400fe9b5fbb) ()  
| Simulates clicking on the Reset [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") button. [More...](class_simulation_panel.html#a709c94305179d19938a57400fe9b5fbb)  
  
void | [play](class_simulation_panel.html#aee49dafaa6b1f20a4a7d51327152d96f) ()  
| Simulates clicking on the Auto Capture / Play button. [More...](class_simulation_panel.html#aee49dafaa6b1f20a4a7d51327152d96f)  
  
void | [back](class_simulation_panel.html#ae827d4bc71f49418814f9664f6eb4a83) ()  
| Simulates clicking on the Back button. [More...](class_simulation_panel.html#ae827d4bc71f49418814f9664f6eb4a83)  
  
void | [forward](class_simulation_panel.html#a9bfb39d6200e2a30f47c359746476439) ()  
| Simulates clicking on the Capture / Forward button. [More...](class_simulation_panel.html#a9bfb39d6200e2a30f47c359746476439)  
  
bool | [isPlaying](class_simulation_panel.html#aada03bb24914f04ad8f9af3fa5916d83) ()  
| Returns true if the simulation is currently playing, otherwise false. [More...](class_simulation_panel.html#aada03bb24914f04ad8f9af3fa5916d83)  
  
void | [populateEventList](class_simulation_panel.html#a2720b0c54dce2039d87ffdee565bc4af) ()  
| Refreshes the display of the event list. [More...](class_simulation_panel.html#a2720b0c54dce2039d87ffdee565bc4af)  
  
void | [changePlaySpeed](class_simulation_panel.html#a9a19b834db3a7835f0da0a085a87d2f3) (int)  
| Changes the play speed of the simulation. [More...](class_simulation_panel.html#a9a19b834db3a7835f0da0a085a87d2f3)  
  
void | [setFilter](class_simulation_panel.html#a2f31a13568b4f1031fdfa93a3dadf86d) (QString, bool)  
| Enables or disables the specified event list filter. [More...](class_simulation_panel.html#a2f31a13568b4f1031fdfa93a3dadf86d)  
  
void | [setAllFilters](class_simulation_panel.html#ab0eb586a068af64cca03f6348c110559) ()  
| Enables or disables all of the event list filters. [More...](class_simulation_panel.html#ab0eb586a068af64cca03f6348c110559)  
  
void | [showFiltersDialog](class_simulation_panel.html#abe77f20856400a7dfafd08909bb3e20a) ()  
| Simulates clicking on the Edit Filters button. [More...](class_simulation_panel.html#abe77f20856400a7dfafd08909bb3e20a)  
  
void | [setConstantDelay](class_simulation_panel.html#a555f5700d77a6d3f795389ffdf6431c9) (bool)  
| Enables or disables constant delay. [More...](class_simulation_panel.html#a555f5700d77a6d3f795389ffdf6431c9)  
  
  
## Detailed Description

[SimulationPanel](class_simulation_panel.html "SimulationPanel allows for UI manipulation of the Simulation Panel.") allows for UI manipulation of the [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") Panel. 

## Member Function Documentation

## ◆ back()

void SimulationPanel::back  | ( | | ) |   
---|---|---|---|---  
  
Simulates clicking on the Back button. 

## ◆ changePlaySpeed()

void SimulationPanel::changePlaySpeed  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Changes the play speed of the simulation. 

Parameters
     value,the| value of the play speed.   
---|---  
  
## ◆ forward()

void SimulationPanel::forward  | ( | | ) |   
---|---|---|---|---  
  
Simulates clicking on the Capture / Forward button. 

## ◆ isPlaying()

bool SimulationPanel::isPlaying  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the simulation is currently playing, otherwise false. 

Returns
    bool, true if the simulation is currently playing, otherwise false. 

## ◆ play()

void SimulationPanel::play  | ( | | ) |   
---|---|---|---|---  
  
Simulates clicking on the Auto Capture / Play button. 

## ◆ populateEventList()

void SimulationPanel::populateEventList  | ( | | ) |   
---|---|---|---|---  
  
Refreshes the display of the event list. 

Remarks
    This function is generally not required unless there was direct manipulate of the events in the engine. 

## ◆ resetSimulation()

void SimulationPanel::resetSimulation  | ( | | ) |   
---|---|---|---|---  
  
Simulates clicking on the Reset [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") button. 

## ◆ setAllFilters()

void SimulationPanel::setAllFilters  | ( | | ) |   
---|---|---|---|---  
  
Enables or disables all of the event list filters. 

## ◆ setConstantDelay()

void SimulationPanel::setConstantDelay  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables constant delay. 

Parameters
     bSet,true| to enable constant delay, false to disable it.   
---|---  
  
## ◆ setDisabled()

void SimulationPanel::setDisabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables input events to this widget. 

Parameters
     bDisabled,true| to disable input events to this widget, false to enable input events.   
---|---  
  
## ◆ setFilter()

void SimulationPanel::setFilter  | ( | QString  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Enables or disables the specified event list filter. 

Parameters
     protocol,the| name of the protocol.   
---|---  
bSet,true| to check the event list filter, false to uncheck it.   
  
## ◆ setVisible()

void SimulationPanel::setVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows or hides this widget from view. 

Parameters
     bVisible,true| to show this widget, false to hide it.   
---|---  
  
## ◆ setWidgetDisable()

void SimulationPanel::setWidgetDisable  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Enables or disables the specified child widget. 

Parameters
     widgetName,where| widgetName can be one of the following: ResetSimulationBtn, BackBtn, PlayBtn, ForwardBtn, EditFilterBtn, ShowAllBtn, ConstantDelayBtn.   
---|---  
bDisabled,true| to disable input events to this child widget, false to enable input events.   
  
## ◆ setWidgetVisible()

void SimulationPanel::setWidgetVisible  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Shows or hides the specified child widget. 

Parameters
     widgetName,where| widgetName can be one of the following: ResetSimulationBtn, BackBtn, PlayBtn, ForwardBtn, EditFilterBtn, ShowAllBtn, ConstantDelayBtn.   
---|---  
bVisible,true| to show this child widget, false to hide it.   
  
## ◆ showFiltersDialog()

void SimulationPanel::showFiltersDialog  | ( | | ) |   
---|---|---|---|---  
  
Simulates clicking on the Edit Filters button. 

* * *

The documentation for this class was generated from the following file:

  * [SimulationPanel.pki](_simulation_panel_8pki.html)


