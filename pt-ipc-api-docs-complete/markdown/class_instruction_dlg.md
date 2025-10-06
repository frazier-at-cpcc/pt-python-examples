# Cisco Packet Tracer Extensions API: InstructionDlg Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_instruction_dlg.html

---

[InstructionDlg](class_instruction_dlg.html "InstructionDlg is the instruction dialog associated with activity files.") is the instruction dialog associated with activity files. [More...](class_instruction_dlg.html#details)

##  Public Member Functions  
  
---  
void | [resetActivity](class_instruction_dlg.html#af371262ed7ba10bc62eceb4bcd988e35) ()  
| Resets the activity. [More...](class_instruction_dlg.html#af371262ed7ba10bc62eceb4bcd988e35)  
  
void | [showAnswerPage](class_instruction_dlg.html#adeeeaa736d5ab50bba106fbc4c5b27e7) (bool)  
| Shows the Check Results page. [More...](class_instruction_dlg.html#adeeeaa736d5ab50bba106fbc4c5b27e7)  
  
void | [closeAnswerPage](class_instruction_dlg.html#a773b091966b09a935fdbb84b20a824df) ()  
| Closes the Check Results page. [More...](class_instruction_dlg.html#a773b091966b09a935fdbb84b20a824df)  
  
void | [prev](class_instruction_dlg.html#a38a9fa20b4c282e852e2ce5818c56f8c) ()  
| Shows the previous instruction page. [More...](class_instruction_dlg.html#a38a9fa20b4c282e852e2ce5818c56f8c)  
  
void | [next](class_instruction_dlg.html#a58fdbc571f2cc494991dfcc921dd5f01) ()  
| Shows the next instruction page. [More...](class_instruction_dlg.html#a58fdbc571f2cc494991dfcc921dd5f01)  
  
void | [alwaysOnTop](class_instruction_dlg.html#afb6a8b04b1532ecdae8924db74970dba) (bool)  
| Enables or disables the always on top feature. [More...](class_instruction_dlg.html#afb6a8b04b1532ecdae8924db74970dba)  
  
void | [dock](class_instruction_dlg.html#a8ea450a1c8a47f8615bb92f7b126fd7a) ()  
| Dock the instructions dialog to the left of the main window. [More...](class_instruction_dlg.html#a8ea450a1c8a47f8615bb92f7b126fd7a)  
  
void | [undock](class_instruction_dlg.html#a57f79408e3e9b10110bfe55b65b5a082) ()  
| Undock the instructions dialog. [More...](class_instruction_dlg.html#a57f79408e3e9b10110bfe55b65b5a082)  
  
bool | [isDocked](class_instruction_dlg.html#a4e8d0d1622964f8c2c00422c05b8a326) ()  
| Returns true if instructions dialog is docked, false otherwise. [More...](class_instruction_dlg.html#a4e8d0d1622964f8c2c00422c05b8a326)  
  
void | [dockChanged](class_instruction_dlg.html#a8bcddf720a5d922fbfa1703cbf214633) (bool)  
| This event is emitted when this window is docked or undocked. [More...](class_instruction_dlg.html#a8bcddf720a5d922fbfa1703cbf214633)  
  
void | [setVisible](class_instruction_dlg.html#a37f06deff6479ba6d5203cbca10e1bcf) (bool)  
| Shows or hides this widget from view. [More...](class_instruction_dlg.html#a37f06deff6479ba6d5203cbca10e1bcf)  
  
void | [setWidgetVisible](class_instruction_dlg.html#a180afe29087696755ba41797240de8fe) (string, bool)  
| Shows or hides the specified child widget. [More...](class_instruction_dlg.html#a180afe29087696755ba41797240de8fe)  
  
void | [setDisabled](class_instruction_dlg.html#a74b9aa343b60e84dcccae90087359f7f) (bool)  
| Enables or disables input events to this widget. [More...](class_instruction_dlg.html#a74b9aa343b60e84dcccae90087359f7f)  
  
void | [setWidgetDisable](class_instruction_dlg.html#a708d9b40e2953d861e6cfd0ca5d14068) (string, bool)  
| Enables or disables the specified child widget. [More...](class_instruction_dlg.html#a708d9b40e2953d861e6cfd0ca5d14068)  
  
bool | [isEditInstructionsLocked](class_instruction_dlg.html#a1c5d45e9fb55f2406dfd85ba1404adb7) ()  
void | [setEditInstructionsLocked](class_instruction_dlg.html#a0037f23b9b8c10080a8c941bbf04d2de) (bool)  
void | [setWindowGeometry](class_instruction_dlg.html#a41341892fad69411d3173ac8bb963f25) (int, int, int, int)  
int | [getX](class_instruction_dlg.html#a20b8a00b0f1a25ebe603631fd2d4a6ba) ()  
int | [getY](class_instruction_dlg.html#a3b50f796e586d8dc9d33491eeb89ef5c) ()  
int | [getWidth](class_instruction_dlg.html#a1f4e90153205f035b67b812eaf146862) ()  
int | [getHeight](class_instruction_dlg.html#ad492455808c9f0f8e85f453611909d78) ()  
void | [raise](class_instruction_dlg.html#ad1078a1b6b3f46ff5d9f97e5035655c3) ()  
[WebView](class_web_view.html) | [getWebView](class_instruction_dlg.html#ae3b6b0a181279ee348591bc74ded81a3) ()  
void | [countdownExpired](class_instruction_dlg.html#ad23229d54fd409f1eeed091af39a159e) ()  
| This event is emitted when countdown expires. [More...](class_instruction_dlg.html#ad23229d54fd409f1eeed091af39a159e)  
  
bool | [isShowCheckResultsLockMessage](class_instruction_dlg.html#a629d1eaf2ebe8305d49527a6e83c6789) ()  
void | [setShowCheckResultsLockMessage](class_instruction_dlg.html#a238aceb196c5791d2072e967d624dd30) (bool)  
| set to show check results lock message or not. [More...](class_instruction_dlg.html#a238aceb196c5791d2072e967d624dd30)  
  
void | [overrideTimeLabel](class_instruction_dlg.html#ab2ccd31de8e948bf2511ccd7528b051f) (QString, QString)  
| Overrides the time label in the instruction box. [More...](class_instruction_dlg.html#ab2ccd31de8e948bf2511ccd7528b051f)  
  
void | [overrideProgressLabel](class_instruction_dlg.html#ad31244dba946fc5e6abca0a1430db090) (QString, QString)  
| Overrides the progress label in the instruction box. [More...](class_instruction_dlg.html#ad31244dba946fc5e6abca0a1430db090)  
  
void | [overrideInstructions](class_instruction_dlg.html#ab2afc986a0361c53ebbcb96c1fd5089d) ()  
| Overrides the instructions and the system will not update instructions anymore. [More...](class_instruction_dlg.html#ab2afc986a0361c53ebbcb96c1fd5089d)  
  
[WebView](class_web_view.html) | [getTabWebView](class_instruction_dlg.html#a9665df0b2f0550fd16a04bcdda7a9e71) (int)  
| Returns the web view in a tab. [More...](class_instruction_dlg.html#a9665df0b2f0550fd16a04bcdda7a9e71)  
  
void | [setTabVisible](class_instruction_dlg.html#a1571c2731113548b73ddc0c5c8bdbdf5) (int, bool)  
| Shows or hides a tab. [More...](class_instruction_dlg.html#a1571c2731113548b73ddc0c5c8bdbdf5)  
  
bool | [addButton](class_instruction_dlg.html#a0f0e9654e60b1a4ddc4dc2819a5afa00) (QString, QString, HorizontalAlignment, int, int)  
| Adds a button to the instruction dialog. [More...](class_instruction_dlg.html#a0f0e9654e60b1a4ddc4dc2819a5afa00)  
  
bool | [addSlider](class_instruction_dlg.html#ac8b4849560687ae64fd435a391a7bde0) (QString, int, int, int, HorizontalAlignment, int, int)  
| Adds a slider to the instruction dialog. [More...](class_instruction_dlg.html#ac8b4849560687ae64fd435a391a7bde0)  
  
bool | [addLabel](class_instruction_dlg.html#a443382cd545021e314d50c3fcd0b2341) (QString, QString, HorizontalAlignment)  
| Adds a label to the instruction dialog. [More...](class_instruction_dlg.html#a443382cd545021e314d50c3fcd0b2341)  
  
bool | [removeWidget](class_instruction_dlg.html#ac48e1091c4a73cf920be02155d14720f) (QString)  
| Removes a widget that was previously added to the instruction dialog. [More...](class_instruction_dlg.html#ac48e1091c4a73cf920be02155d14720f)  
  
bool | [setSliderValue](class_instruction_dlg.html#a32b68bb4344d1cee31099501a04e5196) (QString, int)  
| Sets the value of a slider that was previously added to the instruction dialog. [More...](class_instruction_dlg.html#a32b68bb4344d1cee31099501a04e5196)  
  
bool | [setLabelText](class_instruction_dlg.html#a282ebd9ba953bbc93fb6ad4f3493c54b) (QString, QString)  
| Sets the text on the label that was previously added to the instruction dialog. [More...](class_instruction_dlg.html#a282ebd9ba953bbc93fb6ad4f3493c54b)  
  
bool | [setWidgetToolTip](class_instruction_dlg.html#a9f30d43d62c517b9ece56fec405d7413) (QString, QString)  
| Sets the tooltip for a widget that was previously added to the instruction dialog. [More...](class_instruction_dlg.html#a9f30d43d62c517b9ece56fec405d7413)  
  
void | [buttonClicked](class_instruction_dlg.html#a9e06fd542e650a15e418a2e5c5e3d7fa) (QString)  
| This event is emitted when a button that was previously added to the instruction dialog is clicked. [More...](class_instruction_dlg.html#a9e06fd542e650a15e418a2e5c5e3d7fa)  
  
void | [sliderValueChanged](class_instruction_dlg.html#adbcdaec802617999fc5a9f311a3cefd2) (QString, int)  
| This event is emitted when the value of a slider that was previously added to the instruction dialog is changed. [More...](class_instruction_dlg.html#adbcdaec802617999fc5a9f311a3cefd2)  
  
  
## Detailed Description

[InstructionDlg](class_instruction_dlg.html "InstructionDlg is the instruction dialog associated with activity files.") is the instruction dialog associated with activity files. 

## Member Function Documentation

## ◆ addButton()

bool InstructionDlg::addButton  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | HorizontalAlignment  | ,   
|  | int  | ,   
|  | int  |   
| ) | |   
  
Adds a button to the instruction dialog. 

Parameters
     name,the| name of the widget   
---|---  
label,the| label on the button   
alignment,HorizontalAlignment| enum: Left = 0x00000001, Right = 0x00000002   
minWidth,the| minimum width of the widget   
maxWidth,the| maximum width of the widget   
  
## ◆ addLabel()

bool InstructionDlg::addLabel  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | HorizontalAlignment  |   
| ) | |   
  
Adds a label to the instruction dialog. 

Parameters
     name,the| name of the widget   
---|---  
text,the| text on the label   
alignment,HorizontalAlignment| enum: Left = 0x00000001, Right = 0x00000002   
  
## ◆ addSlider()

bool InstructionDlg::addSlider  | ( | QString  | ,   
---|---|---|---  
|  | int  | ,   
|  | int  | ,   
|  | int  | ,   
|  | HorizontalAlignment  | ,   
|  | int  | ,   
|  | int  |   
| ) | |   
  
Adds a slider to the instruction dialog. 

Parameters
     name,the| name of the widget   
---|---  
min,the| minimum value   
max,the| maximum value   
alignment,HorizontalAlignment| enum: Left = 0x00000001, Right = 0x00000002   
minWidth,the| minimum width of the widget   
maxWidth,the| maximum width of the widget   
  
## ◆ alwaysOnTop()

void InstructionDlg::alwaysOnTop  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables the always on top feature. 

Parameters
     bOn,true| to enable the always on top feature, false to disable it.   
---|---  
  
## ◆ buttonClicked()

void InstructionDlg::buttonClicked  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when a button that was previously added to the instruction dialog is clicked. 

Parameters
     name,the| name of the widget  
---|---  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ closeAnswerPage()

void InstructionDlg::closeAnswerPage  | ( | | ) |   
---|---|---|---|---  
  
Closes the Check Results page. 

## ◆ countdownExpired()

void InstructionDlg::countdownExpired  | ( | | ) |   
---|---|---|---|---  
  
This event is emitted when countdown expires. 

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ dock()

void InstructionDlg::dock  | ( | | ) |   
---|---|---|---|---  
  
Dock the instructions dialog to the left of the main window. 

## ◆ dockChanged()

void InstructionDlg::dockChanged  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when this window is docked or undocked. 

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ getHeight()

int InstructionDlg::getHeight  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getTabWebView()

[WebView](class_web_view.html) InstructionDlg::getTabWebView  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the web view in a tab. 

## ◆ getWebView()

[WebView](class_web_view.html) InstructionDlg::getWebView  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getWidth()

int InstructionDlg::getWidth  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getX()

int InstructionDlg::getX  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getY()

int InstructionDlg::getY  | ( | | ) |   
---|---|---|---|---  
  
## ◆ isDocked()

bool InstructionDlg::isDocked  | ( | | ) |   
---|---|---|---|---  
  
Returns true if instructions dialog is docked, false otherwise. 

Returns
    bool, true if instructions dialog is docked, false otherwise. 

## ◆ isEditInstructionsLocked()

bool InstructionDlg::isEditInstructionsLocked  | ( | | ) |   
---|---|---|---|---  
  
## ◆ isShowCheckResultsLockMessage()

bool InstructionDlg::isShowCheckResultsLockMessage  | ( | | ) |   
---|---|---|---|---  
  
## ◆ next()

void InstructionDlg::next  | ( | | ) |   
---|---|---|---|---  
  
Shows the next instruction page. 

## ◆ overrideInstructions()

void InstructionDlg::overrideInstructions  | ( | | ) |   
---|---|---|---|---  
  
Overrides the instructions and the system will not update instructions anymore. 

## ◆ overrideProgressLabel()

void InstructionDlg::overrideProgressLabel  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Overrides the progress label in the instruction box. 

## ◆ overrideTimeLabel()

void InstructionDlg::overrideTimeLabel  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Overrides the time label in the instruction box. 

## ◆ prev()

void InstructionDlg::prev  | ( | | ) |   
---|---|---|---|---  
  
Shows the previous instruction page. 

## ◆ raise()

void InstructionDlg::raise  | ( | | ) |   
---|---|---|---|---  
  
## ◆ removeWidget()

bool InstructionDlg::removeWidget  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Removes a widget that was previously added to the instruction dialog. 

Parameters
     name,the| name of the widget   
---|---  
  
## ◆ resetActivity()

void InstructionDlg::resetActivity  | ( | | ) |   
---|---|---|---|---  
  
Resets the activity. 

## ◆ setDisabled()

void InstructionDlg::setDisabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables input events to this widget. 

Parameters
     bDisabled,true| to disable input events to this widget, false to enable input events.   
---|---  
  
## ◆ setEditInstructionsLocked()

void InstructionDlg::setEditInstructionsLocked  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
## ◆ setLabelText()

bool InstructionDlg::setLabelText  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Sets the text on the label that was previously added to the instruction dialog. 

Parameters
     name,the| name of the widget   
---|---  
text,the| text   
  
## ◆ setShowCheckResultsLockMessage()

void InstructionDlg::setShowCheckResultsLockMessage  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
set to show check results lock message or not. 

Parameters
     bShow,true| to show check result lock message, false to not show.   
---|---  
  
## ◆ setSliderValue()

bool InstructionDlg::setSliderValue  | ( | QString  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Sets the value of a slider that was previously added to the instruction dialog. 

Parameters
     name,the| name of the widget   
---|---  
value,the| value   
  
## ◆ setTabVisible()

void InstructionDlg::setTabVisible  | ( | int  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Shows or hides a tab. 

## ◆ setVisible()

void InstructionDlg::setVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows or hides this widget from view. 

Parameters
     bVisible,true| to show this widget, false to hide it.   
---|---  
  
## ◆ setWidgetDisable()

void InstructionDlg::setWidgetDisable  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Enables or disables the specified child widget. 

Parameters
     widgetName,where| widgetName can be one of the following: checkAnswerBtn, resetBtn, prevBtn, nextBtn, topCB, progressLbl, timeLbl.   
---|---  
bDisabled,true| to disable input events to this child widget, false to enable input events.   
  
## ◆ setWidgetToolTip()

bool InstructionDlg::setWidgetToolTip  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Sets the tooltip for a widget that was previously added to the instruction dialog. 

Parameters
     name,the| name of the widget   
---|---  
tooltip,the| tooltip   
  
## ◆ setWidgetVisible()

void InstructionDlg::setWidgetVisible  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Shows or hides the specified child widget. 

Parameters
     widgetName,where| widgetName can be one of the following: checkAnswerBtn, resetBtn, prevBtn, nextBtn, topCB, progressLbl, timeLbl.   
---|---  
bVisible,true| to show this child widget, false to hide it.   
  
## ◆ setWindowGeometry()

void InstructionDlg::setWindowGeometry  | ( | int  | ,   
---|---|---|---  
|  | int  | ,   
|  | int  | ,   
|  | int  |   
| ) | |   
  
## ◆ showAnswerPage()

void InstructionDlg::showAnswerPage  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows the Check Results page. 

Parameters
     bResetOnClose,true| to reset the activity after closing the Check Results page, false to not reset the activity.   
---|---  
  
## ◆ sliderValueChanged()

void InstructionDlg::sliderValueChanged  | ( | QString  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
This event is emitted when the value of a slider that was previously added to the instruction dialog is changed. 

Parameters
     name,the| name of the widget   
---|---  
value,the| new value of the slider  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ undock()

void InstructionDlg::undock  | ( | | ) |   
---|---|---|---|---  
  
Undock the instructions dialog. 

* * *

The documentation for this class was generated from the following file:

  * [InstructionDialog.pki](_instruction_dialog_8pki.html)


