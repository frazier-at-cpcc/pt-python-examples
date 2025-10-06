# Cisco Packet Tracer Extensions API: ActivityWizard Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_activity_wizard.html

---

[ActivityWizard](class_activity_wizard.html "ActivityWizard is an assessment creation tool.") is an assessment creation tool. [More...](class_activity_wizard.html#details)

##  Public Member Functions  
  
---  
void | [setVisible](class_activity_wizard.html#a6c9b4f13110fc4335fd69eefaf72d019) (bool)  
| Shows or hides the Activity Wizard widget from view. [More...](class_activity_wizard.html#a6c9b4f13110fc4335fd69eefaf72d019)  
  
void | [setWidgetVisible](class_activity_wizard.html#aa9a803673d669fc393e2d65d1c9d7ad1) (string, bool)  
| Shows or hides the specified Activity Wizard child widget. [More...](class_activity_wizard.html#aa9a803673d669fc393e2d65d1c9d7ad1)  
  
void | [setDisabled](class_activity_wizard.html#a77e78e3df2dc126cd23e822a9cfd870b) (bool)  
| Enables or disables input events to the Activity Wizard widget. [More...](class_activity_wizard.html#a77e78e3df2dc126cd23e822a9cfd870b)  
  
void | [setWidgetDisable](class_activity_wizard.html#a4c867a6dcfeb5fa61ba19dfaa10f0b13) (string, bool)  
| Enables or disables the specified Activity Wizard child widget. [More...](class_activity_wizard.html#a4c867a6dcfeb5fa61ba19dfaa10f0b13)  
  
  
## Detailed Description

[ActivityWizard](class_activity_wizard.html "ActivityWizard is an assessment creation tool.") is an assessment creation tool. 

The activity wizard is an assessment tool that allows the user to create highly specific networking scenarios for other users.

In this version of the API, [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") controlled activity creation via the activity wizard is not supported. However, certain aspects of an activity may still be manipulated using the [ActivityFile](class_activity_file.html "ActivityFile extends from NetworkFile. It adds the activity layer to the file.") class. 

## Member Function Documentation

## ◆ setDisabled()

void ActivityWizard::setDisabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables input events to the Activity Wizard widget. 

Parameters
     bDisabled,true| disables input events to the widget, false enables it.   
---|---  
  
## ◆ setVisible()

void ActivityWizard::setVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows or hides the Activity Wizard widget from view. 

Parameters
     bVisible,true| shows the widget, false hides it.   
---|---  
  
## ◆ setWidgetDisable()

void ActivityWizard::setWidgetDisable  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Enables or disables the specified Activity Wizard child widget. 

Parameters
     name,where| name is one of the following: WelcomeBtn, VariableManagerBtn, InstructionsBtn, AnswerNetworkBtn, InitialNetworkBtn, PasswordBtn, TestActivityBtn, CheckActivityBtn, ExitBtn, SaveBtn, SaveAsBtn, SaveAsPkzBtn, SaveAsCCBtn, InstPrevBtn, InstNextBtn, InstRemoveBtn, InsertBtn, ImportBtn, ImportAllBtn, ExportBtn, ExportAllBtn, AutoLoadCB, ShowAnsNetBtn, ExportAnsNetBtn, ImportAnsNetBtn, ShowInitNetworkBtn, ExportInitNetworkBtn, ImportInitNetworkBtn, CopyAnsNetBtn, EnablePassBtn, DisablePassBtn, AddShapeBtn   
---|---  
bDisabled,true| disables the child widget, false enables it.   
  
## ◆ setWidgetVisible()

void ActivityWizard::setWidgetVisible  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Shows or hides the specified Activity Wizard child widget. 
    
    
    \param name,    where name is one of the following: WelcomeBtn, VariableManagerBtn, InstructionsBtn, AnswerNetworkBtn,
                    InitialNetworkBtn, PasswordBtn, TestActivityBtn, CheckActivityBtn, ExitBtn, SaveBtn, SaveAsBtn,
                    SaveAsPkzBtn, SaveAsCCBtn, InstPrevBtn, InstNextBtn, InstRemoveBtn, InsertBtn, ImportBtn,
                    ImportAllBtn, ExportBtn, ExportAllBtn, AutoLoadCB, ShowAnsNetBtn, ExportAnsNetBtn,
                    ImportAnsNetBtn, ShowInitNetworkBtn, ExportInitNetworkBtn, ImportInitNetworkBtn, CopyAnsNetBtn,
                    EnablePassBtn, DisablePassBtn, AddShapeBtn
    \param bVisible, true shows the child widget, false hides it.
    

* * *

The documentation for this class was generated from the following file:

  * [ActivityWizard.pki](_activity_wizard_8pki.html)


