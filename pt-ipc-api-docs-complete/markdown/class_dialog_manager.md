# Cisco Packet Tracer Extensions API: DialogManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_dialog_manager.html

---

[DialogManager](class_dialog_manager.html "DialogManager manages all the device dialogs.") manages all the device dialogs. [More...](class_dialog_manager.html#details)

##  Public Member Functions  
  
---  
void | [closeAll](class_dialog_manager.html#a6c02eb52c8957ded0daf9baf0ced1659) ()  
| Closes all the device dialogs. [More...](class_dialog_manager.html#a6c02eb52c8957ded0daf9baf0ced1659)  
  
[DeviceDialog](class_device_dialog.html) | [getCurrentDialog](class_dialog_manager.html#a3c405d4e659e4c7c4e60a4af7b9a2aab) ()  
| Returns the currently focused dialog. [More...](class_dialog_manager.html#a3c405d4e659e4c7c4e60a4af7b9a2aab)  
  
[DeviceDialog](class_device_dialog.html) | [getDialog](class_dialog_manager.html#a4571da11382686762603fd2101588f03) (string)  
| Returns the device dialog with the specified device name. [More...](class_dialog_manager.html#a4571da11382686762603fd2101588f03)  
  
void | [dialogOpened](class_dialog_manager.html#a868c0a6e8ddd8117c66c124b82da39de) (QString)  
| This event is emitted when the dialog for the specified device is opened. [More...](class_dialog_manager.html#a868c0a6e8ddd8117c66c124b82da39de)  
  
void | [dialogClosed](class_dialog_manager.html#a721416df6b9f0e3536a88d94e2fdf828) (QString)  
| This event is emitted when the dialog for the specified device is closed. [More...](class_dialog_manager.html#a721416df6b9f0e3536a88d94e2fdf828)  
  
void | [dialogFocused](class_dialog_manager.html#aed34e0ed5ea4fe7f388e2901c0643335) (QString)  
| This event is emitted when a dialog gets focused. [More...](class_dialog_manager.html#aed34e0ed5ea4fe7f388e2901c0643335)  
  
QString | [getFocusedDialogName](class_dialog_manager.html#acd7c97744c7849c78973a432e53a090b) ()  
| Returns the device name of the dialog that is currently in focus. [More...](class_dialog_manager.html#acd7c97744c7849c78973a432e53a090b)  
  
  
## Detailed Description

[DialogManager](class_dialog_manager.html "DialogManager manages all the device dialogs.") manages all the device dialogs. 

## Member Function Documentation

## ◆ closeAll()

void DialogManager::closeAll  | ( | | ) |   
---|---|---|---|---  
  
Closes all the device dialogs. 

## ◆ dialogClosed()

void DialogManager::dialogClosed  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when the dialog for the specified device is closed. 

  * deviceName, name of the device the event is for.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ dialogFocused()

void DialogManager::dialogFocused  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when a dialog gets focused. 

  * deviceName, name of the device



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ dialogOpened()

void DialogManager::dialogOpened  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when the dialog for the specified device is opened. 

  * deviceName, name of the device the event is for..



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ getCurrentDialog()

[DeviceDialog](class_device_dialog.html) DialogManager::getCurrentDialog  | ( | | ) |   
---|---|---|---|---  
  
Returns the currently focused dialog. 

Returns
    [DeviceDialog](class_device_dialog.html "DeviceDialog are the collection of dialogs used to edit the devices."), the [DeviceDialog](class_device_dialog.html "DeviceDialog are the collection of dialogs used to edit the devices.") object of the currently focused dialog. 

## ◆ getDialog()

[DeviceDialog](class_device_dialog.html) DialogManager::getDialog  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the device dialog with the specified device name. 

Parameters
     deviceName,the| name of the device of interest.  
---|---  
  
Returns
    [DeviceDialog](class_device_dialog.html "DeviceDialog are the collection of dialogs used to edit the devices."), the [DeviceDialog](class_device_dialog.html "DeviceDialog are the collection of dialogs used to edit the devices.") object with the specified device name. 

## ◆ getFocusedDialogName()

QString DialogManager::getFocusedDialogName  | ( | | ) |   
---|---|---|---|---  
  
Returns the device name of the dialog that is currently in focus. 

Returns
    QString, the name of the device 

* * *

The documentation for this class was generated from the following file:

  * [DialogManager.pki](_dialog_manager_8pki.html)


