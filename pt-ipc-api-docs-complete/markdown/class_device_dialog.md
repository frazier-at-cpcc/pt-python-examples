# Cisco Packet Tracer Extensions API: DeviceDialog Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_device_dialog.html

---

[DeviceDialog](class_device_dialog.html "DeviceDialog are the collection of dialogs used to edit the devices.") are the collection of dialogs used to edit the devices. [More...](class_device_dialog.html#details)

##  Public Member Functions  
  
---  
void | [setVisible](class_device_dialog.html#a14398d81f3ecf27abce602239d3025f5) (bool)  
| Shows or hides this device dialog widget from view. [More...](class_device_dialog.html#a14398d81f3ecf27abce602239d3025f5)  
  
void | [setWidgetVisible](class_device_dialog.html#aa6d2094ab2eea62fa6ddc03797173fda) (string, bool)  
| Shows or hides the specified child widget. [More...](class_device_dialog.html#aa6d2094ab2eea62fa6ddc03797173fda)  
  
void | [setDisabled](class_device_dialog.html#abf15fb12b384a2d02df8fa95a387ddda) (bool)  
| Enables or disables input events to this device dialog widget. [More...](class_device_dialog.html#abf15fb12b384a2d02df8fa95a387ddda)  
  
void | [setWidgetDisable](class_device_dialog.html#ae6980016994fdafaedcc535a217a7646) (string, bool)  
| Enables or disables the specified child widget. [More...](class_device_dialog.html#ae6980016994fdafaedcc535a217a7646)  
  
void | [disableCLIImportExport](class_device_dialog.html#ac467b480c42456cabc28f91c0defe47b) (bool)  
| Enable or disable copying and pasting from the CLI. [More...](class_device_dialog.html#ac467b480c42456cabc28f91c0defe47b)  
  
void | [reloadCustomHtmlTab](class_device_dialog.html#aa093baf53160236e8a78f1c9f0c1ae53) ()  
| Reload custom html tab. [More...](class_device_dialog.html#aa093baf53160236e8a78f1c9f0c1ae53)  
  
bool | [hasDesktop](class_device_dialog.html#a9288c9c8dcacfa3de077b00a83ef62fd) ()  
| Check if the device dialog has desktop tab. [More...](class_device_dialog.html#a9288c9c8dcacfa3de077b00a83ef62fd)  
  
bool | [setTabVisible](class_device_dialog.html#aa80982203c967c46384423883a19f0d8) (QString, bool)  
| Shows or hides a tab in the device dialog. [More...](class_device_dialog.html#aa80982203c967c46384423883a19f0d8)  
  
bool | [addCustomDesktopApp](class_device_dialog.html#ad34ed3a25198f452fa391a7062b29b96) (QString, QString, QString, QString)  
| Add custom desktop app. [More...](class_device_dialog.html#ad34ed3a25198f452fa391a7062b29b96)  
  
void | [desktopAppOpened](class_device_dialog.html#abee8fd4d011f7155252b4e761c02fccf) (QString)  
| This event is emitted when an app in the desktop tab is opened. [More...](class_device_dialog.html#abee8fd4d011f7155252b4e761c02fccf)  
  
void | [tabChanged](class_device_dialog.html#a5b2cc3a87ad47d26b7b844b9b23a6ae9) (QString)  
| This event is emitted when the current tab changes. [More...](class_device_dialog.html#a5b2cc3a87ad47d26b7b844b9b23a6ae9)  
  
  
## Detailed Description

[DeviceDialog](class_device_dialog.html "DeviceDialog are the collection of dialogs used to edit the devices.") are the collection of dialogs used to edit the devices. 

Remarks
    To manipulate the device configuration, use the [Device](class_device.html "Device is the base class for all device objects.") object. 

## Member Function Documentation

## ◆ addCustomDesktopApp()

bool DeviceDialog::addCustomDesktopApp  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | QString  | ,   
|  | QString  |   
| ) | |   
  
Add custom desktop app. 

Parameters
     name,application| name  
---|---  
description,desktop| app description  
iconPath,icon| path  
customInterface,custom| Interface name   
  
## ◆ desktopAppOpened()

void DeviceDialog::desktopAppOpened  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when an app in the desktop tab is opened. 

  * appName, name of the desktop app



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ disableCLIImportExport()

void DeviceDialog::disableCLIImportExport  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enable or disable copying and pasting from the CLI. 

Parameters
     bDisable,true| to disable copying and pasting from the CLI, false to enable it.   
---|---  
  
## ◆ hasDesktop()

bool DeviceDialog::hasDesktop  | ( | | ) |   
---|---|---|---|---  
  
Check if the device dialog has desktop tab. 

Returns
    bool, true if it does and false if it does not 

## ◆ reloadCustomHtmlTab()

void DeviceDialog::reloadCustomHtmlTab  | ( | | ) |   
---|---|---|---|---  
  
Reload custom html tab. 

## ◆ setDisabled()

void DeviceDialog::setDisabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables input events to this device dialog widget. 

Parameters
     bDisabled,true| to disable this device dialog, false to enable it.   
---|---  
  
## ◆ setTabVisible()

bool DeviceDialog::setTabVisible  | ( | QString  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Shows or hides a tab in the device dialog. 

Parameters
     tabName,the| name of the tab (case-insensitive) e.g. "physical", "config", "cli", etc.  
---|---  
visible,true| to to show the tab, false to hide it.  
  
Returns
    bool, true if the tab was successfully shown or hidden, false otherwise. 

## ◆ setVisible()

void DeviceDialog::setVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows or hides this device dialog widget from view. 

Parameters
     bVisible,true| to show this device dialog, false to hide it.   
---|---  
  
## ◆ setWidgetDisable()

void DeviceDialog::setWidgetDisable  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Enables or disables the specified child widget. 

Parameters
     name| where name can be one of the following: IPConfigBtn, IPConfigLbl, DialupBtn, DialupLbl, TerminalBtn, TerminalLbl, CommandPromptBtn, CommandPromptLbl, WebBrowserBtn, WebBrowserLbl, PCWirelessBtn, PCWirelessLbl, VPNBtn, VPNLbl, TrafficGeneratorBtn, TrafficGeneratorLbl, MIBBroswerBtn, MIBBrowserLbl, IPCommunicatorBtn, IPCommunicatorLbl, EmailBtn, EmailLbl, PPPoEDialerBtn, PPPoEDialerLbl, TextEditorBtn, TextEditorLbl, FirewallBtn, FirewallLbl, IPv6FirewallBtn, IPv6FirewallLbl, AAAAccountingBtn, AAAAccountingLbl, NetflowCollectorBtn, NetflowCollectorLbl, IoXSdkBtn, IoXSdkLbl, TftpLbl, TftpBtn, SshClientBtn, SshClientLbl, BluetoothBtn, BluetoothLbl, IoT Monitor_btn, IoT Monitor_lbl, IoT IDE_btn, IoT IDE_lbl, User Apps Manager_btn, User Apps Manager_lbl   
---|---  
bDisabled,true| to disable the child widget, false to enable it.   
  
## ◆ setWidgetVisible()

void DeviceDialog::setWidgetVisible  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Shows or hides the specified child widget. 

Parameters
     name| where name can be one of the following: IPConfigBtn, IPConfigLbl, DialupBtn, DialupLbl, TerminalBtn, TerminalLbl, CommandPromptBtn, CommandPromptLbl, WebBrowserBtn, WebBrowserLbl, PCWirelessBtn, PCWirelessLbl, VPNBtn, VPNLbl, TrafficGeneratorBtn, TrafficGeneratorLbl, MIBBroswerBtn, MIBBrowserLbl, IPCommunicatorBtn, IPCommunicatorLbl, EmailBtn, EmailLbl, PPPoEDialerBtn, PPPoEDialerLbl, TextEditorBtn, TextEditorLbl, FirewallBtn, FirewallLbl, IPv6FirewallBtn, IPv6FirewallLbl, AAAAccountingBtn, AAAAccountingLbl, NetflowCollectorBtn, NetflowCollectorLbl, IoXSdkBtn, IoXSdkLbl, TftpLbl, TftpBtn, SshClientBtn, SshClientLbl, BluetoothBtn, BluetoothLbl, IoT Monitor_btn, IoT Monitor_lbl, IoT IDE_btn, IoT IDE_lbl, User Apps Manager_btn, User Apps Manager_lbl   
---|---  
bVisible,true| to show the child widget, false to hide it.   
  
## ◆ tabChanged()

void DeviceDialog::tabChanged  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when the current tab changes. 

  * tabName, name of the currently tab



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

* * *

The documentation for this class was generated from the following file:

  * [CDeviceDialog.pki](_c_device_dialog_8pki.html)


