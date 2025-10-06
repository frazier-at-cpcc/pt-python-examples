# Cisco Packet Tracer Extensions API: Menu Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_menu.html

---

[Menu](class_menu.html "Menu is the popup menu instantiated from the MenuBar object.") is the popup menu instantiated from the [MenuBar](class_menu_bar.html "MenuBar allows UI manipulation of the Main Menu Bar.") object. [More...](class_menu.html#details)

##  Public Member Functions  
  
---  
int | [count](class_menu.html#a9d1a99d9b0e7d3813eee6058b64e8926) ()  
| Returns the number of menu items in this menu. [More...](class_menu.html#a9d1a99d9b0e7d3813eee6058b64e8926)  
  
[MenuItem](class_menu_item.html) | [getMenuItemAt](class_menu.html#ac4bf9b6d183010f6b51052101c793379) (int)  
| Returns the menu item at the specified index. [More...](class_menu.html#ac4bf9b6d183010f6b51052101c793379)  
  
[MenuItem](class_menu_item.html) | [getMenuItemByUuid](class_menu.html#a94af83b443c1f081a42a7dda8aa3d86e) (uuid)  
| Returns the menu item with the specified UUID. [More...](class_menu.html#a94af83b443c1f081a42a7dda8aa3d86e)  
  
[MenuItem](class_menu_item.html) | [getMenuItemByName](class_menu.html#a6e148f78caebe7a7374da1c4a71a4966) (QString)  
| Returns the menu item with the specified name. [More...](class_menu.html#a6e148f78caebe7a7374da1c4a71a4966)  
  
uuid | [getMenuItemUuid](class_menu.html#a31eb59dd55cfa2b1d81ea614c5bf0aa8) (QString)  
| Returns the UUID of the menu item with the specified name. [More...](class_menu.html#a31eb59dd55cfa2b1d81ea614c5bf0aa8)  
  
void | [setItemVisibleUuid](class_menu.html#a2dc96c0367187a27f6fb3c17200aca6c) (uuid, bool)  
| Changes the visibility of the item with the specified UUID. [More...](class_menu.html#a2dc96c0367187a27f6fb3c17200aca6c)  
  
void | [setItemEnabledUuid](class_menu.html#ad812104b2c99de9364a8426175a533d3) (uuid, bool)  
| Enables or disables input events to the menu item with the specified UUID. [More...](class_menu.html#ad812104b2c99de9364a8426175a533d3)  
  
void | [removeItemUuid](class_menu.html#ad5d89de801cc2aeb6e2dd80972d94a69) (uuid)  
| Removes the menu item with the specified UUID. [More...](class_menu.html#ad5d89de801cc2aeb6e2dd80972d94a69)  
  
uuid | [insertItem](class_menu.html#a75b3423a78383bc0e8cfaa5cdee61432) (QString, QString)  
| Inserts an item before the specified item with the specified action. [More...](class_menu.html#a75b3423a78383bc0e8cfaa5cdee61432)  
  
uuid | [insertItemAfter](class_menu.html#ae062f89ce37bf7d2fc61c81c3b7922b0) (QString, QString)  
| Inserts an item after the specified item with the specified action. [More...](class_menu.html#ae062f89ce37bf7d2fc61c81c3b7922b0)  
  
uuid | [insertSeparator](class_menu.html#ab78b28102cbfc79dc189ab16ab45c459) (QString, QString)  
| Inserts a separator before the specified item with the specified name. [More...](class_menu.html#ab78b28102cbfc79dc189ab16ab45c459)  
  
uuid | [insertSeparatorAfter](class_menu.html#ae98f09b9e5d3666363fda02522119e79) (QString, QString)  
| Inserts a separator after the specified item with the specified name. [More...](class_menu.html#ae98f09b9e5d3666363fda02522119e79)  
  
void | [removeItem](class_menu.html#a8071a5b55fbcfdf7f265c900782492ec) (QString)  
| Removes the specified menu item. [More...](class_menu.html#a8071a5b55fbcfdf7f265c900782492ec)  
  
void | [setItemVisible](class_menu.html#a23a62efdf3dd3352c847c6cecba0bb3b) (string, bool)  
| Shows or hides the specified menu item. [More...](class_menu.html#a23a62efdf3dd3352c847c6cecba0bb3b)  
  
void | [setItemEnabled](class_menu.html#a1ce73c49ececc2c41ec83d4353c8f27e) (string, bool)  
| Enables or disables the specified menu item. [More...](class_menu.html#a1ce73c49ececc2c41ec83d4353c8f27e)  
  
void | [setItemObjectEnabled](class_menu.html#ab6daafa0e11aa191909b47688c8246c8) (string, bool)  
| Enables or disables the specified menu item using object name. [More...](class_menu.html#ab6daafa0e11aa191909b47688c8246c8)  
  
void | [setItemObjectEnabledFuzzy](class_menu.html#a0be013279cf69d342983c14f1c8d9405) (string, bool)  
| Enables or disables the specified menu item using any text. [More...](class_menu.html#a0be013279cf69d342983c14f1c8d9405)  
  
uuid | [insertItemWithName](class_menu.html#ad2291f57fbca216021ffeb0732f3a64b) (QString, QString, QString)  
| Inserts an item before the specified item with the specified action. [More...](class_menu.html#ad2291f57fbca216021ffeb0732f3a64b)  
  
uuid | [insertItemWithNameAfter](class_menu.html#aca576f25793f63bbcc9f6341a5bbd681) (QString, QString, QString)  
| Inserts an item after the specified item with the specified action. [More...](class_menu.html#aca576f25793f63bbcc9f6341a5bbd681)  
  
  
## Detailed Description

[Menu](class_menu.html "Menu is the popup menu instantiated from the MenuBar object.") is the popup menu instantiated from the [MenuBar](class_menu_bar.html "MenuBar allows UI manipulation of the Main Menu Bar.") object. 

Remarks
    The built-in menus Activity Wizard, Multiuser, [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality."), and the seperator can only be manipulated by name. These menus will not provide a UUID or [MenuItem](class_menu_item.html "MenuItem is an item in the Menu object.") class representation. Only items added via the [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") have a UUID and are a derivative of the [MenuItem](class_menu_item.html "MenuItem is an item in the Menu object.") class. 

## Member Function Documentation

## ◆ count()

int Menu::count  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of menu items in this menu. 

Returns
    int, the number of menu items in this menu. 

## ◆ getMenuItemAt()

[MenuItem](class_menu_item.html) Menu::getMenuItemAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the menu item at the specified index. 

Parameters
     index,the| index of the menu item of interest.  
---|---  
  
Returns
    [MenuItem](class_menu_item.html "MenuItem is an item in the Menu object."), the [MenuItem](class_menu_item.html "MenuItem is an item in the Menu object.") object at the specified index. 

## ◆ getMenuItemByName()

[MenuItem](class_menu_item.html) Menu::getMenuItemByName  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the menu item with the specified name. 

Parameters
     name,the| name of the menu item of interest.  
---|---  
  
Returns
    [MenuItem](class_menu_item.html "MenuItem is an item in the Menu object."), the [MenuItem](class_menu_item.html "MenuItem is an item in the Menu object.") object with the specified name. 

## ◆ getMenuItemByUuid()

[MenuItem](class_menu_item.html) Menu::getMenuItemByUuid  | ( | uuid  | | ) |   
---|---|---|---|---|---  
  
Returns the menu item with the specified UUID. 

Parameters
     id,the| UUID of the menu item of interest.  
---|---  
  
Returns
    [MenuItem](class_menu_item.html "MenuItem is an item in the Menu object."), the [MenuItem](class_menu_item.html "MenuItem is an item in the Menu object.") object with the specified UUID. 

## ◆ getMenuItemUuid()

uuid Menu::getMenuItemUuid  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the UUID of the menu item with the specified name. 

Parameters
     name,the| name of the menu item of interest.  
---|---  
  
Returns
    uuid, the UUID of the menu item with the specified name. 

## ◆ insertItem()

uuid Menu::insertItem  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Inserts an item before the specified item with the specified action. 

Parameters
     before,the| name of the menu item to insert before.   
---|---  
action,the| action of the menu item.  
  
Returns
    uuid, the UUID of the menu item that was inserted. 

## ◆ insertItemAfter()

uuid Menu::insertItemAfter  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Inserts an item after the specified item with the specified action. 

Parameters
     after,the| name of the menu item to insert after.   
---|---  
action,the| action of the menu item.  
  
Returns
    uuid, the UUID of the menu item that was inserted. 

## ◆ insertItemWithName()

uuid Menu::insertItemWithName  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | QString  |   
| ) | |   
  
Inserts an item before the specified item with the specified action. 

Parameters
     before,the| name of the menu item to insert before.   
---|---  
action,the| action of the menu item.   
name,object| name assigned to the action  
  
Returns
    uuid, the UUID of the menu item that was inserted. 

## ◆ insertItemWithNameAfter()

uuid Menu::insertItemWithNameAfter  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | QString  |   
| ) | |   
  
Inserts an item after the specified item with the specified action. 

Parameters
     after,the| name of the menu item to insert after.   
---|---  
action,the| action of the menu item.   
name,object| name assigned to the action  
  
Returns
    uuid, the UUID of the menu item that was inserted. 

## ◆ insertSeparator()

uuid Menu::insertSeparator  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Inserts a separator before the specified item with the specified name. 

Parameters
     before,the| name of the menu item to insert before.   
---|---  
name,the| name of the separator; not displayed but can be used to find it later.  
  
Returns
    uuid, the UUID of the menu item that was inserted. 

## ◆ insertSeparatorAfter()

uuid Menu::insertSeparatorAfter  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Inserts a separator after the specified item with the specified name. 

Parameters
     after,the| name of the menu item to insert after.   
---|---  
name,the| name of the separator; not displayed but can be used to find it later.  
  
Returns
    uuid, the UUID of the menu item that was inserted. 

## ◆ removeItem()

void Menu::removeItem  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Removes the specified menu item. 

Parameters
     name,the| name of the menu item.   
---|---  
  
## ◆ removeItemUuid()

void Menu::removeItemUuid  | ( | uuid  | | ) |   
---|---|---|---|---|---  
  
Removes the menu item with the specified UUID. 

Parameters
     id,the| UUID of the menu item of interest.   
---|---  
  
## ◆ setItemEnabled()

void Menu::setItemEnabled  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Enables or disables the specified menu item. 

Parameters
     name,the| name of the menu item.   
---|---  
bEnable,true| to enable the menu item, false to disable it.   
  
## ◆ setItemEnabledUuid()

void Menu::setItemEnabledUuid  | ( | uuid  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Enables or disables input events to the menu item with the specified UUID. 

Parameters
     id,the| UUID of the menu item of interest.   
---|---  
bEnabled,true| to enable input events to the menu item, false to disable it.   
  
## ◆ setItemObjectEnabled()

void Menu::setItemObjectEnabled  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Enables or disables the specified menu item using object name. 

Parameters
     name,the| name of the menu item.   
---|---  
bEnable,true| to enable the menu item, false to disable it.   
  
## ◆ setItemObjectEnabledFuzzy()

void Menu::setItemObjectEnabledFuzzy  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Enables or disables the specified menu item using any text. 

Parameters
     anyText,text| that is a portion of either object name or label.   
---|---  
bEnable,true| to enable the menu item, false to disable it.   
  
## ◆ setItemVisible()

void Menu::setItemVisible  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Shows or hides the specified menu item. 

Parameters
     name,the| name of the menu item.   
---|---  
bVisible,true| to show the menu item, false to hide it.   
  
## ◆ setItemVisibleUuid()

void Menu::setItemVisibleUuid  | ( | uuid  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Changes the visibility of the item with the specified UUID. 

Parameters
     id,the| UUID of the menu item of interest.   
---|---  
bVisibile,true| to show the menu item, false to hide it.   
  
* * *

The documentation for this class was generated from the following file:

  * [Menu.pki](_menu_8pki.html)


