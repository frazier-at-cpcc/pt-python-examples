# Cisco Packet Tracer Extensions API: ModulePhysicalView Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_module_physical_view.html

---

Physical view for module. [More...](class_module_physical_view.html#details)

##  Public Member Functions  
  
---  
void | [setIsPower](class_module_physical_view.html#a3be9e1fdb6b661f47300c06ff5df7a0c) (bool)  
| Sets if the power is on or off. [More...](class_module_physical_view.html#a3be9e1fdb6b661f47300c06ff5df7a0c)  
  
bool | [isPower](class_module_physical_view.html#af257a835219047a933c36cca92780f03) ()  
| Gets if the power is on or off. [More...](class_module_physical_view.html#af257a835219047a933c36cca92780f03)  
  
void | [setSlotNum](class_module_physical_view.html#a72712e3a65d9144d6677f0fad3cdb789) (int)  
| Sets the slot number used by the view. [More...](class_module_physical_view.html#a72712e3a65d9144d6677f0fad3cdb789)  
  
int | [getSlotNum](class_module_physical_view.html#a94fa7f88788d76a5e3a50ed19f16b5ca) ()  
| Gets the slot number used by the view. [More...](class_module_physical_view.html#a94fa7f88788d76a5e3a50ed19f16b5ca)  
  
void | [setModuleAdded](class_module_physical_view.html#ab744ee4738cebd71704fb4f2a45744c5) (bool)  
| Sets weither a module is in the view. [More...](class_module_physical_view.html#ab744ee4738cebd71704fb4f2a45744c5)  
  
bool | [getModuleAdded](class_module_physical_view.html#ab1c2b1d6962bf9d675941a450f71985a) ()  
| Gets weither a module is in the view. [More...](class_module_physical_view.html#ab1c2b1d6962bf9d675941a450f71985a)  
  
void | [setIsNonRemovable](class_module_physical_view.html#a2ba0a64e0a7ad986adfe4af9d5332d5c) (bool)  
| Sets weither it is non-removable. [More...](class_module_physical_view.html#a2ba0a64e0a7ad986adfe4af9d5332d5c)  
  
bool | [isNonRemovable](class_module_physical_view.html#ac6fda3f394453a2b449bc78efa23c4b0) ()  
| Gets weither it is non-removable. [More...](class_module_physical_view.html#ac6fda3f394453a2b449bc78efa23c4b0)  
  
void | [setHorizontal](class_module_physical_view.html#ad6d0d8e46fa0230339cc9a2fdab76b3c) (bool)  
| Used for power buttons, sets if it is a horzontal button or a vertical button. [More...](class_module_physical_view.html#ad6d0d8e46fa0230339cc9a2fdab76b3c)  
  
bool | [isHorizontal](class_module_physical_view.html#a4d85d857784f53743a7e16d58bde4b24) ()  
| Used for power buttons, Gets if it is a horzontal button or a vertical button. [More...](class_module_physical_view.html#a4d85d857784f53743a7e16d58bde4b24)  
  
void | [setX1](class_module_physical_view.html#ab7364958b39ba764e56a71a31ae81047) (int)  
| Sets leftmost x coordintate. [More...](class_module_physical_view.html#ab7364958b39ba764e56a71a31ae81047)  
  
int | [getX1](class_module_physical_view.html#a486896e0d8e98c144c116b7178d1c033) ()  
| Gets leftmost x coordintate. [More...](class_module_physical_view.html#a486896e0d8e98c144c116b7178d1c033)  
  
void | [setX2](class_module_physical_view.html#a805e94c775dd37b2a9f41541c574feef) (int)  
| Sets rightmost x coordintate. [More...](class_module_physical_view.html#a805e94c775dd37b2a9f41541c574feef)  
  
int | [getX2](class_module_physical_view.html#a4cb42d9d487150183fc9af23e30adec3) ()  
| Gets rightmost x coordintate. [More...](class_module_physical_view.html#a4cb42d9d487150183fc9af23e30adec3)  
  
void | [setY1](class_module_physical_view.html#a7ce458378964dc1dedc948d04579c9aa) (int)  
| Sets top y coordintate. [More...](class_module_physical_view.html#a7ce458378964dc1dedc948d04579c9aa)  
  
int | [getY1](class_module_physical_view.html#a5360619034baff80d3a71c18c552b99a) ()  
| Gets top y coordintate. [More...](class_module_physical_view.html#a5360619034baff80d3a71c18c552b99a)  
  
void | [setY2](class_module_physical_view.html#aa8a80958bfde740c75238ad589a0fb7b) (int)  
| Sets bottom y coordintate. [More...](class_module_physical_view.html#aa8a80958bfde740c75238ad589a0fb7b)  
  
int | [getY2](class_module_physical_view.html#aaef033895cf873b68b0c1b86220a3e65) ()  
| Gets bottom y coordintate. [More...](class_module_physical_view.html#aaef033895cf873b68b0c1b86220a3e65)  
  
  
## Detailed Description

Physical view for module. 

## Member Function Documentation

## ◆ getModuleAdded()

bool ModulePhysicalView::getModuleAdded  | ( | | ) |   
---|---|---|---|---  
  
Gets weither a module is in the view. 

Returns
    bool, true if a module is in the view, false if not. 

## ◆ getSlotNum()

int ModulePhysicalView::getSlotNum  | ( | | ) |   
---|---|---|---|---  
  
Gets the slot number used by the view. 

Returns
    int, slot number to use. 

## ◆ getX1()

int ModulePhysicalView::getX1  | ( | | ) |   
---|---|---|---|---  
  
Gets leftmost x coordintate. 

Returns
    int, the leftmost x coordintate. 

## ◆ getX2()

int ModulePhysicalView::getX2  | ( | | ) |   
---|---|---|---|---  
  
Gets rightmost x coordintate. 

Returns
    int, the rightmost x coordintate. 

## ◆ getY1()

int ModulePhysicalView::getY1  | ( | | ) |   
---|---|---|---|---  
  
Gets top y coordintate. 

Returns
    int, the top y coordintate. 

## ◆ getY2()

int ModulePhysicalView::getY2  | ( | | ) |   
---|---|---|---|---  
  
Gets bottom y coordintate. 

Returns
    int, the bottom y coordintate. 

## ◆ isHorizontal()

bool ModulePhysicalView::isHorizontal  | ( | | ) |   
---|---|---|---|---  
  
Used for power buttons, Gets if it is a horzontal button or a vertical button. 

Returns
    bool, true if it is a horizontal button, false if it is vertical. 

## ◆ isNonRemovable()

bool ModulePhysicalView::isNonRemovable  | ( | | ) |   
---|---|---|---|---  
  
Gets weither it is non-removable. 

Returns
    bool, true if it can't be removed, false if it can. 

## ◆ isPower()

bool ModulePhysicalView::isPower  | ( | | ) |   
---|---|---|---|---  
  
Gets if the power is on or off. 

Returns
    bool, true if power on, false for off. 

## ◆ setHorizontal()

void ModulePhysicalView::setHorizontal  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Used for power buttons, sets if it is a horzontal button or a vertical button. 

Parameters
     bHor,true| if it is a horizontal button, false if it is vertical.   
---|---  
  
## ◆ setIsNonRemovable()

void ModulePhysicalView::setIsNonRemovable  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Sets weither it is non-removable. 

Parameters
     bNonRemovable,true| if it can't be removed, false if it can.   
---|---  
  
## ◆ setIsPower()

void ModulePhysicalView::setIsPower  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Sets if the power is on or off. 

Parameters
     bPower,true| to set power on, false for off.   
---|---  
  
## ◆ setModuleAdded()

void ModulePhysicalView::setModuleAdded  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Sets weither a module is in the view. 

Parameters
     bAdded,true| if a module is in the view, false if not.   
---|---  
  
## ◆ setSlotNum()

void ModulePhysicalView::setSlotNum  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the slot number used by the view. 

Parameters
     slotNum,slot| number to use.   
---|---  
  
## ◆ setX1()

void ModulePhysicalView::setX1  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets leftmost x coordintate. 

Parameters
     X1,the| leftmost x coordintate.   
---|---  
  
## ◆ setX2()

void ModulePhysicalView::setX2  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets rightmost x coordintate. 

Parameters
     X2,the| rightmost x coordintate.   
---|---  
  
## ◆ setY1()

void ModulePhysicalView::setY1  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets top y coordintate. 

Parameters
     Y1,the| top y coordintate.   
---|---  
  
## ◆ setY2()

void ModulePhysicalView::setY2  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets bottom y coordintate. 

Parameters
     Y2,the| bottom y coordintate.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [PhysicalView.pki](_physical_view_8pki.html)


