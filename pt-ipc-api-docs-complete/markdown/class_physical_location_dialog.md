# Cisco Packet Tracer Extensions API: PhysicalLocationDialog Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_physical_location_dialog.html

---

[PhysicalLocationDialog](class_physical_location_dialog.html "PhysicalLocationDialog allows for UI manipulation of the Physical Location Dialog.") allows for UI manipulation of the Physical Location Dialog. [More...](class_physical_location_dialog.html#details)

##  Public Member Functions  
  
---  
void | [setVisible](class_physical_location_dialog.html#a5b6a7417fab5ce47185e5fc998cd8010) (bool)  
| Shows or hides this widget from view. [More...](class_physical_location_dialog.html#a5b6a7417fab5ce47185e5fc998cd8010)  
  
void | [setWidgetVisible](class_physical_location_dialog.html#ab0e21a99322b9034bbac600f0dbaf347) (string, bool)  
| Shows or hides the specified child widget. [More...](class_physical_location_dialog.html#ab0e21a99322b9034bbac600f0dbaf347)  
  
void | [setDisabled](class_physical_location_dialog.html#a5e2445a06ab4a491f176c166bcceec42) (bool)  
| Enables or disables input events to this widget. [More...](class_physical_location_dialog.html#a5e2445a06ab4a491f176c166bcceec42)  
  
void | [setWidgetDisable](class_physical_location_dialog.html#a2dead71b0da3a921388e7221dc4d99ce) (string, bool)  
| Enables or disables the specified child widget. [More...](class_physical_location_dialog.html#a2dead71b0da3a921388e7221dc4d99ce)  
  
void | [refreshTree](class_physical_location_dialog.html#a0a70560781afc983954dc74675c47435) ()  
| Updates the physical locations tree items. [More...](class_physical_location_dialog.html#a0a70560781afc983954dc74675c47435)  
  
void | [jumpBtn_clicked](class_physical_location_dialog.html#ac275bfe7c1c31f25a2e738141dc4a736) ()  
| Jumps to the selected physical location. [More...](class_physical_location_dialog.html#ac275bfe7c1c31f25a2e738141dc4a736)  
  
  
## Detailed Description

[PhysicalLocationDialog](class_physical_location_dialog.html "PhysicalLocationDialog allows for UI manipulation of the Physical Location Dialog.") allows for UI manipulation of the Physical Location Dialog. 

## Member Function Documentation

## ◆ jumpBtn_clicked()

void PhysicalLocationDialog::jumpBtn_clicked  | ( | | ) |   
---|---|---|---|---  
  
Jumps to the selected physical location. 

## ◆ refreshTree()

void PhysicalLocationDialog::refreshTree  | ( | | ) |   
---|---|---|---|---  
  
Updates the physical locations tree items. 

## ◆ setDisabled()

void PhysicalLocationDialog::setDisabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables input events to this widget. 

Parameters
     bDisabled,true| to disable input events to this widget, false to enable input events.   
---|---  
  
## ◆ setVisible()

void PhysicalLocationDialog::setVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows or hides this widget from view. 

Parameters
     bVisible,true| to show this widget, false to hide it.   
---|---  
  
## ◆ setWidgetDisable()

void PhysicalLocationDialog::setWidgetDisable  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Enables or disables the specified child widget. 

Parameters
     widgetName,where| widgetName can be one of the following: JumpBtn.   
---|---  
bDisabled,true| to disable input events to this child widget, false to enable input events.   
  
## ◆ setWidgetVisible()

void PhysicalLocationDialog::setWidgetVisible  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Shows or hides the specified child widget. 

Parameters
     widgetName,where| widgetName can be one of the following: JumpBtn.   
---|---  
bVisible,true| to show this child widget, false to hide it.   
  
* * *

The documentation for this class was generated from the following file:

  * [PhysicalLocationDialog.pki](_physical_location_dialog_8pki.html)


