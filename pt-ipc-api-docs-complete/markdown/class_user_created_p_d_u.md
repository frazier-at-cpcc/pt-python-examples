# Cisco Packet Tracer Extensions API: UserCreatedPDU Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_user_created_p_d_u.html

---

The [UserCreatedPDU](class_user_created_p_d_u.html "The UserCreatedPDU widget holds all the user created pdus for different scenarios.") widget holds all the user created pdus for different scenarios. [More...](class_user_created_p_d_u.html#details)

##  Public Member Functions  
  
---  
void | [setVisible](class_user_created_p_d_u.html#a3056991029d7e8991950e71d29b7c117) (bool)  
| Shows or hides this widget from view. [More...](class_user_created_p_d_u.html#a3056991029d7e8991950e71d29b7c117)  
  
void | [setWidgetVisible](class_user_created_p_d_u.html#a1b091e945686744708d8e15ab24b3bef) (string, bool)  
| Shows or hides the specified child widget. [More...](class_user_created_p_d_u.html#a1b091e945686744708d8e15ab24b3bef)  
  
void | [setDisabled](class_user_created_p_d_u.html#ac5f160e3df407bc9c313e8a9aa92c4e3) (bool)  
| Enables or disables input events to this widget. [More...](class_user_created_p_d_u.html#ac5f160e3df407bc9c313e8a9aa92c4e3)  
  
void | [setWidgetDisable](class_user_created_p_d_u.html#a70ad4e6466ef145d2518f7281835b053) (string, bool)  
| Enables or disables the specified child widget. [More...](class_user_created_p_d_u.html#a70ad4e6466ef145d2518f7281835b053)  
  
void | [activateScenario](class_user_created_p_d_u.html#aa195e3a4b7e7bbcb0880a3dae74b51ce) (int)  
| Changes the scenario to the specified index. [More...](class_user_created_p_d_u.html#aa195e3a4b7e7bbcb0880a3dae74b51ce)  
  
void | [deleteScenarioBtn_clicked](class_user_created_p_d_u.html#aef40d889aee302253d9a5d31644738d0) ()  
| Simulates clicking on the Delete scenario button. [More...](class_user_created_p_d_u.html#aef40d889aee302253d9a5d31644738d0)  
  
void | [newScenarioBtn_clicked](class_user_created_p_d_u.html#ab960e9604bf78b3242f8d50001a2971c) ()  
| Simulates clicking on the New scenario button. [More...](class_user_created_p_d_u.html#ab960e9604bf78b3242f8d50001a2971c)  
  
void | [scenarioInfoBtn_clicked](class_user_created_p_d_u.html#a8e285a4115de510a1c0c111df4d5ef20) ()  
void | [toggleOpenListWindowBtn](class_user_created_p_d_u.html#a36450bc1683213378d1989d8eaaef76f) (bool)  
| Shows or hides the Toggle PDU List Window. [More...](class_user_created_p_d_u.html#a36450bc1683213378d1989d8eaaef76f)  
  
void | [setScenarioDescription](class_user_created_p_d_u.html#a38c35445991d6f83713287da5f847922) (string)  
| Sets the description for the current scenario. [More...](class_user_created_p_d_u.html#a38c35445991d6f83713287da5f847922)  
  
void | [firePDU](class_user_created_p_d_u.html#a773b612f0f7f51989bd7776bec2ea29d) (int)  
| Sends out the PDU at the specified index. [More...](class_user_created_p_d_u.html#a773b612f0f7f51989bd7776bec2ea29d)  
  
void | [colorPDU](class_user_created_p_d_u.html#abe27118e05677866a55eb079ca2d44ba) (int)  
| Opens the color picker for the PDU at the specified index. [More...](class_user_created_p_d_u.html#abe27118e05677866a55eb079ca2d44ba)  
  
void | [editPDU](class_user_created_p_d_u.html#a10b221d381acb9f46e79e5f350fdd409) (int)  
| Opens the edit pdu dialog for the pdu at the specified index. [More...](class_user_created_p_d_u.html#a10b221d381acb9f46e79e5f350fdd409)  
  
void | [deletePDU](class_user_created_p_d_u.html#a2372c336cb994c255aafac6eee98c734) (int)  
| Removes the PDU at the specified index. [More...](class_user_created_p_d_u.html#a2372c336cb994c255aafac6eee98c734)  
  
ADD_PDU_ERROR | [addSimplePdu](class_user_created_p_d_u.html#a3837de445a74588477426b93a574d2d5) (QString, QString)  
| Adds a simple pdu to the simulation using only device names. [More...](class_user_created_p_d_u.html#a3837de445a74588477426b93a574d2d5)  
  
void | [simplePduAdded](class_user_created_p_d_u.html#a4ff70fab2726d6f57083b4e87c61b175) ([UserTraffic](class_user_traffic.html))  
| This event is emitted when a user successfully adds a Simple PDU to the network. [More...](class_user_created_p_d_u.html#a4ff70fab2726d6f57083b4e87c61b175)  
  
void | [complexPduAdded](class_user_created_p_d_u.html#af3350d6c833967ecf10f93ecfa25968e) ([UserTraffic](class_user_traffic.html))  
| [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. [More...](class_user_created_p_d_u.html#af3350d6c833967ecf10f93ecfa25968e)  
  
  
## Detailed Description

The [UserCreatedPDU](class_user_created_p_d_u.html "The UserCreatedPDU widget holds all the user created pdus for different scenarios.") widget holds all the user created pdus for different scenarios. 

## Member Function Documentation

## ◆ activateScenario()

void UserCreatedPDU::activateScenario  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Changes the scenario to the specified index. 

Parameters
     index,the| index of the scenario of interest.   
---|---  
  
## ◆ addSimplePdu()

ADD_PDU_ERROR UserCreatedPDU::addSimplePdu  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Adds a simple pdu to the simulation using only device names. 

Parameters
     src,the| source device name   
---|---  
dst,the| destination device name   
  
## ◆ colorPDU()

void UserCreatedPDU::colorPDU  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Opens the color picker for the PDU at the specified index. 

Parameters
     index,the| index of the PDU of interest.   
---|---  
  
## ◆ complexPduAdded()

void UserCreatedPDU::complexPduAdded  | ( | [UserTraffic](class_user_traffic.html) | | ) |   
---|---|---|---|---|---  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

This event is emitted when a user successfully adds a Complex PDU to the network.

  * traffic, the [UserTraffic](class_user_traffic.html "UserTraffic represents the user traffic information \(PDU\).") object that was added. 



## ◆ deletePDU()

void UserCreatedPDU::deletePDU  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Removes the PDU at the specified index. 

Parameters
     index,the| index of the PDU of interest.   
---|---  
  
## ◆ deleteScenarioBtn_clicked()

void UserCreatedPDU::deleteScenarioBtn_clicked  | ( | | ) |   
---|---|---|---|---  
  
Simulates clicking on the Delete scenario button. 

## ◆ editPDU()

void UserCreatedPDU::editPDU  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Opens the edit pdu dialog for the pdu at the specified index. 

Parameters
     int| index, the index of interest   
---|---  
  
## ◆ firePDU()

void UserCreatedPDU::firePDU  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sends out the PDU at the specified index. 

Parameters
     index,the| index of the PDU of interest.   
---|---  
  
## ◆ newScenarioBtn_clicked()

void UserCreatedPDU::newScenarioBtn_clicked  | ( | | ) |   
---|---|---|---|---  
  
Simulates clicking on the New scenario button. 

## ◆ scenarioInfoBtn_clicked()

void UserCreatedPDU::scenarioInfoBtn_clicked  | ( | | ) |   
---|---|---|---|---  
  
## ◆ setDisabled()

void UserCreatedPDU::setDisabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables input events to this widget. 

Parameters
     bDisabled,true| to disable input events to this widget, false to enable input events.   
---|---  
  
## ◆ setScenarioDescription()

void UserCreatedPDU::setScenarioDescription  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the description for the current scenario. 

Parameters
     description,the| description for the current scenario.   
---|---  
  
## ◆ setVisible()

void UserCreatedPDU::setVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows or hides this widget from view. 

Parameters
     bVisible,true| to show this widget, false to hide it.   
---|---  
  
## ◆ setWidgetDisable()

void UserCreatedPDU::setWidgetDisable  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Enables or disables the specified child widget. 

Parameters
     widgetName,where| widgetName can be one of the following: NewScenarioBtn, DeleteScenarioBtn, OpenListWindowBtn, RemovePDUBtn.   
---|---  
bDisabled,true| to disable input events to this child widget, false to enable input events.   
  
## ◆ setWidgetVisible()

void UserCreatedPDU::setWidgetVisible  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Shows or hides the specified child widget. 

Parameters
     widgetName,where| widgetName can be one of the following: NewScenarioBtn, DeleteScenarioBtn, OpenListWindowBtn, RemovePDUBtn.   
---|---  
bVisible,true| to show this child widget, false to hide it.   
  
## ◆ simplePduAdded()

void UserCreatedPDU::simplePduAdded  | ( | [UserTraffic](class_user_traffic.html) | | ) |   
---|---|---|---|---|---  
  
This event is emitted when a user successfully adds a Simple PDU to the network. 

  * traffic, the [UserTraffic](class_user_traffic.html "UserTraffic represents the user traffic information \(PDU\).") object that was added.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ toggleOpenListWindowBtn()

void UserCreatedPDU::toggleOpenListWindowBtn  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows or hides the Toggle PDU List Window. 

Parameters
     bEnable,true| to show the Toggle PDU List Window, false to hide it.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [UserCreatedPDU.pki](_user_created_p_d_u_8pki.html)


