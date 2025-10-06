# Cisco Packet Tracer Extensions API: NetworkComponentBox Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_network_component_box.html

---

[NetworkComponentBox](class_network_component_box.html "NetworkComponentBox allows UI manipulation of the Network Component Box.") allows UI manipulation of the [Network](class_network.html "Network is the entry point for all device configurations in the network. It retrieves devices.") Component Box. [More...](class_network_component_box.html#details)

##  Public Member Functions  
  
---  
void | [setVisible](class_network_component_box.html#a1ce88d3036d1284828578e4a56e6d332) (bool)  
| Shows or hides this widget from view. [More...](class_network_component_box.html#a1ce88d3036d1284828578e4a56e6d332)  
  
void | [setFrameVisible](class_network_component_box.html#aafbffbdeb33770996a7b4fde1d2919d7) (bool)  
| Shows or hides this whole frame (bottom toolbar) from view. [More...](class_network_component_box.html#aafbffbdeb33770996a7b4fde1d2919d7)  
  
void | [setWidgetVisible](class_network_component_box.html#acc29e49c95991d5285eba6431ee6cacb) (string, bool)  
| Shows or hides the specified child widget. [More...](class_network_component_box.html#acc29e49c95991d5285eba6431ee6cacb)  
  
void | [setAllWidgetsVisible](class_network_component_box.html#a4daa837cabdf169905dd0146b14b4356) (bool)  
| Shows or hides all child widgets. [More...](class_network_component_box.html#a4daa837cabdf169905dd0146b14b4356)  
  
void | [setDisabled](class_network_component_box.html#a8c7655b217beef5f5e00f08e00604637) (bool)  
| Enables or disables input events to this widget. [More...](class_network_component_box.html#a8c7655b217beef5f5e00f08e00604637)  
  
void | [setWidgetDisable](class_network_component_box.html#ae45486109add328ae64302065d808048) (string, bool)  
| Enables or disables the specified child widget. [More...](class_network_component_box.html#ae45486109add328ae64302065d808048)  
  
void | [setAllWidgetsDisable](class_network_component_box.html#a9c5acc8bc23957866270b410783b538f) (bool)  
| Enables or disables all child widgets. [More...](class_network_component_box.html#a9c5acc8bc23957866270b410783b538f)  
  
vector< string > | [getDeviceTypes](class_network_component_box.html#a8c1f573fa49b352fc82f86f6937c6a48) ()  
vector< string > | [getConnectionTypes](class_network_component_box.html#ad9586f09ddb127901685eede2e16b69b) ()  
vector< string > | [getDeviceModels](class_network_component_box.html#ac30dbd579e29dea5b75b50e120926366) (string)  
  
## Detailed Description

[NetworkComponentBox](class_network_component_box.html "NetworkComponentBox allows UI manipulation of the Network Component Box.") allows UI manipulation of the [Network](class_network.html "Network is the entry point for all device configurations in the network. It retrieves devices.") Component Box. 

## Member Function Documentation

## ◆ getConnectionTypes()

vector< string > NetworkComponentBox::getConnectionTypes  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getDeviceModels()

vector< string > NetworkComponentBox::getDeviceModels  | ( | string  | | ) |   
---|---|---|---|---|---  
  
## ◆ getDeviceTypes()

vector< string > NetworkComponentBox::getDeviceTypes  | ( | | ) |   
---|---|---|---|---  
  
## ◆ setAllWidgetsDisable()

void NetworkComponentBox::setAllWidgetsDisable  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables all child widgets. 

Parameters
     bDisabled,true| to disable input events to all child widgets, false to enable input events.   
---|---  
  
## ◆ setAllWidgetsVisible()

void NetworkComponentBox::setAllWidgetsVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows or hides all child widgets. 

Parameters
     bVisible,true| to show all child widgets, false to hide them.   
---|---  
  
## ◆ setDisabled()

void NetworkComponentBox::setDisabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables input events to this widget. 

Parameters
     bDisabled,true| to disable input events to this widget, false to enable input events.   
---|---  
  
## ◆ setFrameVisible()

void NetworkComponentBox::setFrameVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows or hides this whole frame (bottom toolbar) from view. 

Parameters
     bVisible,true| to show this whole frame (bottom toolbar), false to hide it.   
---|---  
  
## ◆ setVisible()

void NetworkComponentBox::setVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows or hides this widget from view. 

Parameters
     bVisible,true| to show this widget, false to hide it.   
---|---  
  
## ◆ setWidgetDisable()

void NetworkComponentBox::setWidgetDisable  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Enables or disables the specified child widget. 

Parameters
     widgetName,where| widgetName can be one of the following: DeviceTypesWidget, DeviceSpecificWidget.   
---|---  
bDisabled,true| to disable input events to this child widget, false to enable input events.   
  
## ◆ setWidgetVisible()

void NetworkComponentBox::setWidgetVisible  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Shows or hides the specified child widget. 

Parameters
     widgetName,where| widgetName can be one of the following: DeviceTypesWidget, DeviceSpecificWidget.   
---|---  
bVisible,true| to show this child widget, false to hide it.   
  
* * *

The documentation for this class was generated from the following file:

  * [NetworkComponentBox.pki](_network_component_box_8pki.html)


