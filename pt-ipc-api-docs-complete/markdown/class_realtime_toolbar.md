# Cisco Packet Tracer Extensions API: RealtimeToolbar Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_realtime_toolbar.html

---

[RealtimeToolbar](class_realtime_toolbar.html "RealtimeToolbar allows for UI manipulation of the Realtime toolbar.") allows for UI manipulation of the Realtime toolbar. [More...](class_realtime_toolbar.html#details)

##  Public Member Functions  
  
---  
void | [setVisible](class_realtime_toolbar.html#a9f1dfc3ca90ef78575caa5214c759999) (bool)  
| Shows or hides this widget from view. [More...](class_realtime_toolbar.html#a9f1dfc3ca90ef78575caa5214c759999)  
  
void | [setWidgetVisible](class_realtime_toolbar.html#a10b566472a9223d99d1220f8bb3f1b1d) (string, bool)  
| Shows or hides the specified child widget. [More...](class_realtime_toolbar.html#a10b566472a9223d99d1220f8bb3f1b1d)  
  
void | [setDisabled](class_realtime_toolbar.html#a863f2a87a9520266895c20d0def2ac50) (bool)  
| Enables or disables input events to this widget. [More...](class_realtime_toolbar.html#a863f2a87a9520266895c20d0def2ac50)  
  
void | [setWidgetDisable](class_realtime_toolbar.html#a1b870879efca6c75bea352b9800e5f8d) (string, bool)  
| Enables or disables the specified child widget. [More...](class_realtime_toolbar.html#a1b870879efca6c75bea352b9800e5f8d)  
  
void | [resetNetwork](class_realtime_toolbar.html#af0e711663e946b838f7ee51bfe5a9664) ()  
| Simulates clicking on the Power Cycle Devices button on the Realtime toolbar. [More...](class_realtime_toolbar.html#af0e711663e946b838f7ee51bfe5a9664)  
  
void | [fastForwardTime](class_realtime_toolbar.html#a95dfffda5d839b990c0d0b22c972561d) ()  
| Simulates clicking on the Fast Forward button on the Realtime toolbar. [More...](class_realtime_toolbar.html#a95dfffda5d839b990c0d0b22c972561d)  
  
  
## Detailed Description

[RealtimeToolbar](class_realtime_toolbar.html "RealtimeToolbar allows for UI manipulation of the Realtime toolbar.") allows for UI manipulation of the Realtime toolbar. 

## Member Function Documentation

## ◆ fastForwardTime()

void RealtimeToolbar::fastForwardTime  | ( | | ) |   
---|---|---|---|---  
  
Simulates clicking on the Fast Forward button on the Realtime toolbar. 

## ◆ resetNetwork()

void RealtimeToolbar::resetNetwork  | ( | | ) |   
---|---|---|---|---  
  
Simulates clicking on the Power Cycle Devices button on the Realtime toolbar. 

## ◆ setDisabled()

void RealtimeToolbar::setDisabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables input events to this widget. 

Parameters
     bDisabled,true| to disable input events to this widget, false to enable input events.   
---|---  
  
## ◆ setVisible()

void RealtimeToolbar::setVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows or hides this widget from view. 

Parameters
     bVisible,true| to show this widget, false to hide it.   
---|---  
  
## ◆ setWidgetDisable()

void RealtimeToolbar::setWidgetDisable  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Enables or disables the specified child widget. 

Parameters
     widgetName,where| widgetName can be one of the following: ResetNetworkBtn, FastForwardTimeBtn.   
---|---  
bDisabled,true| to disable input events to this child widget, false to enable input events.   
  
## ◆ setWidgetVisible()

void RealtimeToolbar::setWidgetVisible  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Shows or hides the specified child widget. 

Parameters
     widgetName,where| widgetName can be one of the following: ResetNetworkBtn, FastForwardTimeBtn.   
---|---  
bVisible,true| to show this child widget, false to hide it.   
  
* * *

The documentation for this class was generated from the following file:

  * [RealtimeToolbar.pki](_realtime_toolbar_8pki.html)


