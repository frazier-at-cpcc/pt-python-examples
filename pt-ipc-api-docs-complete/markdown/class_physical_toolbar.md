# Cisco Packet Tracer Extensions API: PhysicalToolbar Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_physical_toolbar.html

---

[PhysicalToolbar](class_physical_toolbar.html "PhysicalToolbar allows for UI manipulation of the Physical toolbar.") allows for UI manipulation of the Physical toolbar. [More...](class_physical_toolbar.html#details)

##  Public Member Functions  
  
---  
void | [setVisible](class_physical_toolbar.html#a44e90f29b85e34ea8fa962423a23e0e0) (bool)  
| Shows or hides this widget from view. [More...](class_physical_toolbar.html#a44e90f29b85e34ea8fa962423a23e0e0)  
  
void | [setWidgetVisible](class_physical_toolbar.html#ad087e456ba41132464cec51e721f54a2) (string, bool)  
| Shows or hides the specified child widget. [More...](class_physical_toolbar.html#ad087e456ba41132464cec51e721f54a2)  
  
void | [setDisabled](class_physical_toolbar.html#a1a5a9bb7e303d91467419ab77a268661) (bool)  
| Enables or disables input events to this widget. [More...](class_physical_toolbar.html#a1a5a9bb7e303d91467419ab77a268661)  
  
void | [setWidgetDisable](class_physical_toolbar.html#ace79ac6bbbf7ac9e28d208cfd9df603c) (string, bool)  
| Enables or disables the specified child widget. [More...](class_physical_toolbar.html#ace79ac6bbbf7ac9e28d208cfd9df603c)  
  
void | [showPhysicalLocationDialog](class_physical_toolbar.html#ad88a45b7309a46ce4da3881c92991015) ()  
| Simulates clicking on the Navigation button. [More...](class_physical_toolbar.html#ad88a45b7309a46ce4da3881c92991015)  
  
void | [physicalLocationDialogShown](class_physical_toolbar.html#a7e18e044df168349544763893232e853) ()  
| This event is emitted when the physical location dialog is shown. [More...](class_physical_toolbar.html#a7e18e044df168349544763893232e853)  
  
void | [switchToHomeRack](class_physical_toolbar.html#a49450117821925f349a2d2c7710ea9c1) ()  
| Simulates clicking on the Working Closet button. [More...](class_physical_toolbar.html#a49450117821925f349a2d2c7710ea9c1)  
  
void | [switchToTopView](class_physical_toolbar.html#a8fd224a4fe3acdbb6534d7b6762ac927) ()  
| Simulates clicking on the Intercity button. [More...](class_physical_toolbar.html#a8fd224a4fe3acdbb6534d7b6762ac927)  
  
void | [moveObject](class_physical_toolbar.html#a14c64b1101db1ada8569cf43721e7fd5) ()  
| Simulates clicking on the Move Object button. [More...](class_physical_toolbar.html#a14c64b1101db1ada8569cf43721e7fd5)  
  
void | [addCity](class_physical_toolbar.html#a91edbf4ed9ca1868a920a8e2cee0dcbd) ()  
| Simulates clicking on the New City button. [More...](class_physical_toolbar.html#a91edbf4ed9ca1868a920a8e2cee0dcbd)  
  
void | [addCloset](class_physical_toolbar.html#a375d044351e1bb0c81526afbd234f627) ()  
| Simulates clicking on the New Closet button. [More...](class_physical_toolbar.html#a375d044351e1bb0c81526afbd234f627)  
  
void | [setBGImage](class_physical_toolbar.html#a66b3e16242c63fa88562983a844ddc88) ()  
| Simulates clicking on the Set Background button. [More...](class_physical_toolbar.html#a66b3e16242c63fa88562983a844ddc88)  
  
void | [addGrid](class_physical_toolbar.html#af3a0a9a81c2a0ac33c6dbaa50bb6de9b) ()  
| Simulates clicking on the Grid button. [More...](class_physical_toolbar.html#af3a0a9a81c2a0ac33c6dbaa50bb6de9b)  
  
  
## Detailed Description

[PhysicalToolbar](class_physical_toolbar.html "PhysicalToolbar allows for UI manipulation of the Physical toolbar.") allows for UI manipulation of the Physical toolbar. 

## Member Function Documentation

## ◆ addCity()

void PhysicalToolbar::addCity  | ( | | ) |   
---|---|---|---|---  
  
Simulates clicking on the New City button. 

## ◆ addCloset()

void PhysicalToolbar::addCloset  | ( | | ) |   
---|---|---|---|---  
  
Simulates clicking on the New Closet button. 

## ◆ addGrid()

void PhysicalToolbar::addGrid  | ( | | ) |   
---|---|---|---|---  
  
Simulates clicking on the Grid button. 

## ◆ moveObject()

void PhysicalToolbar::moveObject  | ( | | ) |   
---|---|---|---|---  
  
Simulates clicking on the Move Object button. 

## ◆ physicalLocationDialogShown()

void PhysicalToolbar::physicalLocationDialogShown  | ( | | ) |   
---|---|---|---|---  
  
This event is emitted when the physical location dialog is shown. 

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ setBGImage()

void PhysicalToolbar::setBGImage  | ( | | ) |   
---|---|---|---|---  
  
Simulates clicking on the Set Background button. 

## ◆ setDisabled()

void PhysicalToolbar::setDisabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables input events to this widget. 

Parameters
     bDisabled,true| to disable input events to this widget, false to enable input events.   
---|---  
  
## ◆ setVisible()

void PhysicalToolbar::setVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows or hides this widget from view. 

Parameters
     bVisible,true| to show this widget, false to hide it.   
---|---  
  
## ◆ setWidgetDisable()

void PhysicalToolbar::setWidgetDisable  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Enables or disables the specified child widget. 

Parameters
     widgetName,where| widgetName can be one of the following: NavigationBtn, GotoTopBtn, GotoCityBtn, GotoBuildingBtn, GotoClosetBtn, NewCityBtn, NewBuildingBtn, NewRackBtn, MoveObjBtn, SetBGImageBtn, GridBtn, HomeBtn.   
---|---  
bDisabled,true| to disable input events to this child widget, false to enable input events.   
  
## ◆ setWidgetVisible()

void PhysicalToolbar::setWidgetVisible  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Shows or hides the specified child widget. 

Parameters
     widgetName,where| widgetName can be one of the following: NavigationBtn, GotoTopBtn, GotoCityBtn, GotoBuildingBtn, GotoClosetBtn, NewCityBtn, NewBuildingBtn, NewRackBtn, MoveObjBtn, SetBGImageBtn, GridBtn, HomeBtn.   
---|---  
bVisible,true| to show this child widget, false to hide it.   
  
## ◆ showPhysicalLocationDialog()

void PhysicalToolbar::showPhysicalLocationDialog  | ( | | ) |   
---|---|---|---|---  
  
Simulates clicking on the Navigation button. 

## ◆ switchToHomeRack()

void PhysicalToolbar::switchToHomeRack  | ( | | ) |   
---|---|---|---|---  
  
Simulates clicking on the Working Closet button. 

## ◆ switchToTopView()

void PhysicalToolbar::switchToTopView  | ( | | ) |   
---|---|---|---|---  
  
Simulates clicking on the Intercity button. 

* * *

The documentation for this class was generated from the following file:

  * [PhysicalToolbar.pki](_physical_toolbar_8pki.html)


