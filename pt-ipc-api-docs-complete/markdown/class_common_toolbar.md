# Cisco Packet Tracer Extensions API: CommonToolbar Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_common_toolbar.html

---

[CommonToolbar](class_common_toolbar.html "CommonToolbar allows UI manipulation of the right most vertical toolbar.") allows UI manipulation of the right most vertical toolbar. [More...](class_common_toolbar.html#details)

##  Public Member Functions  
  
---  
void | [setVisible](class_common_toolbar.html#a5f642107c8b18368cc75c5629193c512) (bool)  
| Shows or hides this widget from view. [More...](class_common_toolbar.html#a5f642107c8b18368cc75c5629193c512)  
  
void | [setWidgetVisible](class_common_toolbar.html#a54735e078093829f0c09ff4d0c7d6341) (string, bool)  
| Shows or hides the specified child widget. [More...](class_common_toolbar.html#a54735e078093829f0c09ff4d0c7d6341)  
  
void | [setDisabled](class_common_toolbar.html#aa75b2386e5b3eabbbe9938203b373787) (bool)  
| Enables or disables input events to this widget. [More...](class_common_toolbar.html#aa75b2386e5b3eabbbe9938203b373787)  
  
void | [setWidgetDisable](class_common_toolbar.html#a1392ad18b3b88c57d79df4c8d537e53d) (string, bool)  
| Enables or disables the specified child widget. [More...](class_common_toolbar.html#a1392ad18b3b88c57d79df4c8d537e53d)  
  
void | [changeState](class_common_toolbar.html#abf5b6432190dbfc1658d862cc25288cf) (string)  
| Changes the state of the common toolbar. [More...](class_common_toolbar.html#abf5b6432190dbfc1658d862cc25288cf)  
  
  
## Detailed Description

[CommonToolbar](class_common_toolbar.html "CommonToolbar allows UI manipulation of the right most vertical toolbar.") allows UI manipulation of the right most vertical toolbar. 

## Member Function Documentation

## ◆ changeState()

void CommonToolbar::changeState  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Changes the state of the common toolbar. 

Parameters
     state,the| new state for the Common Toolbar. Allowed states: select, move, note, delete, inspect, drawpolygon, addsimple, addcomplex   
---|---  
  
## ◆ setDisabled()

void CommonToolbar::setDisabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables input events to this widget. 

Parameters
     bDisabled,true| to disable input events to this widget, false to enable input events.   
---|---  
  
## ◆ setVisible()

void CommonToolbar::setVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows or hides this widget from view. 

Parameters
     bVisible,true| to show this widget, false to hide it.   
---|---  
  
## ◆ setWidgetDisable()

void CommonToolbar::setWidgetDisable  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Enables or disables the specified child widget. 

Parameters
     widgetName,where| widgetName can be one of the following: SelectBtn, MoveBtn, NoteBtn, DeleteBtn, InspectBtn, DrawPolyBtn, AddSimpleBtn, AddComplexPDUBtn.   
---|---  
bDisabled,true| to disable input events to this child widget, false to enable input events.   
  
## ◆ setWidgetVisible()

void CommonToolbar::setWidgetVisible  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Shows or hides the specified child widget. 

Parameters
     widgetName,where| widgetName can be one of the following: SelectBtn, MoveBtn, NoteBtn, DeleteBtn, InspectBtn, DrawPolyBtn, AddSimpleBtn, AddComplexPDUBtn.   
---|---  
bVisible,true| to show this child widget, false to hide it.   
  
* * *

The documentation for this class was generated from the following file:

  * [PLToolBox_impl.pki](_p_l_tool_box__impl_8pki.html)


