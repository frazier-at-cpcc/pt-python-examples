# Cisco Packet Tracer Extensions API: PLSwitch Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_p_l_switch.html

---

[PLSwitch](class_p_l_switch.html "PLSwitch allows for UI manipulation of the Physical and Logical workspace toggle switches.") allows for UI manipulation of the Physical and Logical workspace toggle switches. [More...](class_p_l_switch.html#details)

##  Public Member Functions  
  
---  
void | [setVisible](class_p_l_switch.html#ac891e38380a4bb61ade2a3156dad99c3) (bool)  
| Shows or hides this widget from view. [More...](class_p_l_switch.html#ac891e38380a4bb61ade2a3156dad99c3)  
  
void | [setWidgetVisible](class_p_l_switch.html#a242a8484b450b2b5bcf95462dd6d6ea9) (string, bool)  
| Shows or hides the specified child widget. [More...](class_p_l_switch.html#a242a8484b450b2b5bcf95462dd6d6ea9)  
  
void | [setDisabled](class_p_l_switch.html#a993868d584999c1da8c2ae2858cd0e1d) (bool)  
| Enables or disables input events to this widget. [More...](class_p_l_switch.html#a993868d584999c1da8c2ae2858cd0e1d)  
  
void | [setWidgetDisable](class_p_l_switch.html#a871c77a775c2e0caad94b4835e4721b2) (string, bool)  
| Enables or disables the specified child widget. [More...](class_p_l_switch.html#a871c77a775c2e0caad94b4835e4721b2)  
  
void | [showLogicalMode](class_p_l_switch.html#a5c621a1ad4ed27587f237b69f6eedd96) ()  
| Shows the Logical workspace. [More...](class_p_l_switch.html#a5c621a1ad4ed27587f237b69f6eedd96)  
  
void | [showPhysicalMode](class_p_l_switch.html#ada72a5c4086c7bfaf84a1ee887c2ecf4) ()  
| Shows the Physical workspace. [More...](class_p_l_switch.html#ada72a5c4086c7bfaf84a1ee887c2ecf4)  
  
void | [modeSwitched](class_p_l_switch.html#a910202e2233cbed80eff612bdedc2529) (bool)  
| This event is emitted when the workspace is changed to either Logical or Physical. [More...](class_p_l_switch.html#a910202e2233cbed80eff612bdedc2529)  
  
  
## Detailed Description

[PLSwitch](class_p_l_switch.html "PLSwitch allows for UI manipulation of the Physical and Logical workspace toggle switches.") allows for UI manipulation of the Physical and Logical workspace toggle switches. 

## Member Function Documentation

## ◆ modeSwitched()

void PLSwitch::modeSwitched  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when the workspace is changed to either Logical or Physical. 

  * isLogical, true if the new workspace is Logical, false if the new workspace is Physical.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ setDisabled()

void PLSwitch::setDisabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables input events to this widget. 

Parameters
     bDisabled,true| to disable input events to this widget, false to enable input events.   
---|---  
  
## ◆ setVisible()

void PLSwitch::setVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows or hides this widget from view. 

Parameters
     bVisible,true| to show this widget, false to hide it.   
---|---  
  
## ◆ setWidgetDisable()

void PLSwitch::setWidgetDisable  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Enables or disables the specified child widget. 

Parameters
     widgetName,where| widgetName can be one of the following: LogicalBtn, PhysicalBtn.   
---|---  
bDisabled,true| to disable input events to this child widget, false to enable input events.   
  
## ◆ setWidgetVisible()

void PLSwitch::setWidgetVisible  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Shows or hides the specified child widget. 

Parameters
     widgetName,where| widgetName can be one of the following: LogicalBtn, PhysicalBtn.   
---|---  
bVisible,true| to show this child widget, false to hide it.   
  
## ◆ showLogicalMode()

void PLSwitch::showLogicalMode  | ( | | ) |   
---|---|---|---|---  
  
Shows the Logical workspace. 

## ◆ showPhysicalMode()

void PLSwitch::showPhysicalMode  | ( | | ) |   
---|---|---|---|---  
  
Shows the Physical workspace. 

* * *

The documentation for this class was generated from the following file:

  * [PLSwitch.pki](_p_l_switch_8pki.html)


