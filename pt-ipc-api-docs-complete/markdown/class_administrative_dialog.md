# Cisco Packet Tracer Extensions API: AdministrativeDialog Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_administrative_dialog.html

---

[AdministrativeDialog](class_administrative_dialog.html "AdministrativeDialog serves as a frontend to Options class.") serves as a frontend to [Options](class_options.html "Options contains the current running options for the application.") class. [More...](class_administrative_dialog.html#details)

##  Public Member Functions  
  
---  
void | [setVisible](class_administrative_dialog.html#aa4fc33267e0f36056d0102adba5153ae) (bool)  
| Shows or hides the [AdministrativeDialog](class_administrative_dialog.html "AdministrativeDialog serves as a frontend to Options class.") widget from view. [More...](class_administrative_dialog.html#aa4fc33267e0f36056d0102adba5153ae)  
  
void | [setWidgetVisible](class_administrative_dialog.html#aa0ee44edf1cee8ce82ce1049f58e9a2d) (string, bool)  
| Shows or hides the specified [AdministrativeDialog](class_administrative_dialog.html "AdministrativeDialog serves as a frontend to Options class.") child widget. [More...](class_administrative_dialog.html#aa0ee44edf1cee8ce82ce1049f58e9a2d)  
  
void | [setDisabled](class_administrative_dialog.html#aa5fdb2913a7578ae08d8be0ec5ced38e) (bool)  
| Enables or disables input events to the [AdministrativeDialog](class_administrative_dialog.html "AdministrativeDialog serves as a frontend to Options class.") widget. [More...](class_administrative_dialog.html#aa5fdb2913a7578ae08d8be0ec5ced38e)  
  
void | [setWidgetDisable](class_administrative_dialog.html#a43f5a683635d69afbedf93112dbfb00f) (string, bool)  
| Enables or disables the specified [AdministrativeDialog](class_administrative_dialog.html "AdministrativeDialog serves as a frontend to Options class.") child widget. [More...](class_administrative_dialog.html#a43f5a683635d69afbedf93112dbfb00f)  
  
  
## Detailed Description

[AdministrativeDialog](class_administrative_dialog.html "AdministrativeDialog serves as a frontend to Options class.") serves as a frontend to [Options](class_options.html "Options contains the current running options for the application.") class. 

This dialog serves as a frontend to the [Options](class_options.html "Options contains the current running options for the application.") class. To manipulate the options, use the [Options](class_options.html "Options contains the current running options for the application.") class. 

## Member Function Documentation

## ◆ setDisabled()

void AdministrativeDialog::setDisabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables input events to the [AdministrativeDialog](class_administrative_dialog.html "AdministrativeDialog serves as a frontend to Options class.") widget. 

Parameters
     bDisabled,true| disables the widget, false enables it.   
---|---  
  
## ◆ setVisible()

void AdministrativeDialog::setVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows or hides the [AdministrativeDialog](class_administrative_dialog.html "AdministrativeDialog serves as a frontend to Options class.") widget from view. 

Parameters
     bVisible,true| shows the [AdministrativeDialog](class_administrative_dialog.html "AdministrativeDialog serves as a frontend to Options class.") widget, false hides it.   
---|---  
  
## ◆ setWidgetDisable()

void AdministrativeDialog::setWidgetDisable  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Enables or disables the specified [AdministrativeDialog](class_administrative_dialog.html "AdministrativeDialog serves as a frontend to Options class.") child widget. 

Parameters
     name,where| name is one of the following: AnimationGBox, ShowLinkLightsCB, SoundGBox, TelephonySoundGBox, iTbShowDeviceModelCkBox, HideQoSStampCB, HideDeviceLabelGBox, DontShowPortsCB, ShowPortsCB, EnableCableLengthsCB, iTbDisableAutoCableCkBox, UseCliDefaultTab, LogEnableCB, LogExportBtn, iTbLangListWidget, ChangeLangBtn, aTbPasswordEdit, aTbConfirmEdit, SetPasswordBtn, DisablePasswordBtn, aTbIntLockingGroupBox, aTbWriteButton, aTbBrowseButton, PhyiscalGBox, hTbHideConfigCkBox, CLIGBox, DesktopGBox, GUIGBox, GUIHTMLGBox, HTMLGBox, ApplyBtn, ResetBtn, mTbSimBufferFullGroupBox, mTbBufferFilteredEventsOnlyCkBox, mTbEnableScreenReaderCkBox, ShowDevTaskBar   
---|---  
bVisible,true| shows the child widget, false hides it.   
  
## ◆ setWidgetVisible()

void AdministrativeDialog::setWidgetVisible  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Shows or hides the specified [AdministrativeDialog](class_administrative_dialog.html "AdministrativeDialog serves as a frontend to Options class.") child widget. 

Parameters
     name,where| name is one of the following: AnimationGBox, ShowLinkLightsCB, SoundGBox, TelephonySoundGBox, iTbShowDeviceModelCkBox, HideQoSStampCB, HideDeviceLabelGBox, DontShowPortsCB, ShowPortsCB, EnableCableLengthsCB, iTbDisableAutoCableCkBox, UseCliDefaultTab, LogEnableCB, LogExportBtn, iTbLangListWidget, ChangeLangBtn, aTbPasswordEdit, aTbConfirmEdit, SetPasswordBtn, DisablePasswordBtn, aTbIntLockingGroupBox, aTbWriteButton, aTbBrowseButton, PhyiscalGBox, hTbHideConfigCkBox, CLIGBox, DesktopGBox, GUIGBox, GUIHTMLGBox, HTMLGBox, ApplyBtn, ResetBtn, mTbSimBufferFullGroupBox, mTbBufferFilteredEventsOnlyCkBox, mTbEnableScreenReaderCkBox, ShowDevTaskBar   
---|---  
bVisible,true| shows the child widget, false hides it.   
  
* * *

The documentation for this class was generated from the following file:

  * [AdministrativeDialog.pki](_administrative_dialog_8pki.html)


