# Cisco Packet Tracer Extensions API: LogicalToolbar Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_logical_toolbar.html

---

[LogicalToolbar](class_logical_toolbar.html "LogicalToolbar allows manipulation of the Logical toolbar. It is the toolbar that has cluster creatio...") allows manipulation of the Logical toolbar. It is the toolbar that has cluster creation, environment, background and other controls. [More...](class_logical_toolbar.html#details)

##  Public Member Functions  
  
---  
void | [setVisible](class_logical_toolbar.html#a19997acb979a64a9a5912bb2cc954437) (bool)  
| Shows or hides this widget from view. [More...](class_logical_toolbar.html#a19997acb979a64a9a5912bb2cc954437)  
  
void | [setWidgetVisible](class_logical_toolbar.html#ad22999ea0fc9192f93cfea62a97a9ebf) (string, bool)  
| Shows or hides the specified child widget. [More...](class_logical_toolbar.html#ad22999ea0fc9192f93cfea62a97a9ebf)  
  
void | [setDisabled](class_logical_toolbar.html#a2f91a99410246bcdfe224355bdd681a6) (bool)  
| Enables or disables input events to this widget. [More...](class_logical_toolbar.html#a2f91a99410246bcdfe224355bdd681a6)  
  
void | [setWidgetDisable](class_logical_toolbar.html#a1645d67d579832b387b555520e9ebb0a) (string, bool)  
| Enables or disables input events to the specified child widget. [More...](class_logical_toolbar.html#a1645d67d579832b387b555520e9ebb0a)  
  
void | [createCluster](class_logical_toolbar.html#aca6a57afbdf284ee42449daed07de2a0) ()  
| Creates a new cluster with the currently selected objects. [More...](class_logical_toolbar.html#aca6a57afbdf284ee42449daed07de2a0)  
  
void | [moveBack](class_logical_toolbar.html#a2094cf40eae6d20521bd21bbb77bd483) ()  
| Moves back out of a cluster. [More...](class_logical_toolbar.html#a2094cf40eae6d20521bd21bbb77bd483)  
  
void | [showViewPort](class_logical_toolbar.html#a94b6ad5a862fc71460df3f5620ec1bf9) ()  
| Shows the Viewport. [More...](class_logical_toolbar.html#a94b6ad5a862fc71460df3f5620ec1bf9)  
  
  
## Detailed Description

[LogicalToolbar](class_logical_toolbar.html "LogicalToolbar allows manipulation of the Logical toolbar. It is the toolbar that has cluster creatio...") allows manipulation of the Logical toolbar. It is the toolbar that has cluster creation, environment, background and other controls. 

## Member Function Documentation

## ◆ createCluster()

void LogicalToolbar::createCluster  | ( | | ) |   
---|---|---|---|---  
  
Creates a new cluster with the currently selected objects. 

## ◆ moveBack()

void LogicalToolbar::moveBack  | ( | | ) |   
---|---|---|---|---  
  
Moves back out of a cluster. 

## ◆ setDisabled()

void LogicalToolbar::setDisabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables input events to this widget. 

Parameters
     bDisabled,true| to disable input events to this widget, false to enable input events.   
---|---  
  
## ◆ setVisible()

void LogicalToolbar::setVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows or hides this widget from view. 

Parameters
     bVisible,true| to show this widget, false to hide it.   
---|---  
  
## ◆ setWidgetDisable()

void LogicalToolbar::setWidgetDisable  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Enables or disables input events to the specified child widget. 

Parameters
     widgetName,where| widgetName can be one of the following: setBGImageBtn, MoveBtn, CreateClusterBtn, BackBtn, CurrentClusterBtn, MiniCanvasBtn.   
---|---  
bDisabled,true| to disable input events to this widget, false to enable input events.   
  
## ◆ setWidgetVisible()

void LogicalToolbar::setWidgetVisible  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Shows or hides the specified child widget. 

Parameters
     widgetName,where| widgetName can be one of the following: setBGImageBtn, MoveBtn, CreateClusterBtn, BackBtn, CurrentClusterBtn, MiniCanvasBtn.   
---|---  
bVisible,true| to show this child widget, false to hide it.   
  
## ◆ showViewPort()

void LogicalToolbar::showViewPort  | ( | | ) |   
---|---|---|---|---  
  
Shows the Viewport. 

* * *

The documentation for this class was generated from the following file:

  * [LogicalToolbar.pki](_logical_toolbar_8pki.html)


