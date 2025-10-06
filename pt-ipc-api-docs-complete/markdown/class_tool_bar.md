# Cisco Packet Tracer Extensions API: ToolBar Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_tool_bar.html

---

[ToolBar](class_tool_bar.html "ToolBar is the QDocWindow instatiated in QMainWindow.") is the QDocWindow instatiated in QMainWindow. [More...](class_tool_bar.html#details)

##  Public Member Functions  
  
---  
void | [setVisible](class_tool_bar.html#aa33be57b6e89157e20c4c81774a01722) (bool)  
| Shows or hides this widget from view. [More...](class_tool_bar.html#aa33be57b6e89157e20c4c81774a01722)  
  
int | [count](class_tool_bar.html#a75a7b597b0b019644ab2aad8663980f8) ()  
| Returns the number of action items in this toolbar. [More...](class_tool_bar.html#a75a7b597b0b019644ab2aad8663980f8)  
  
void | [setItemAtVisible](class_tool_bar.html#a9a4b323d51ca8291c92f508743f51c32) (int, bool)  
| Shows or hides the action item at the specified index. [More...](class_tool_bar.html#a9a4b323d51ca8291c92f508743f51c32)  
  
void | [setItemAtEnabled](class_tool_bar.html#a7c40cfe5d63fd95614bd38af141a3137) (int, bool)  
| Enables or disables the action item at the specified index. [More...](class_tool_bar.html#a7c40cfe5d63fd95614bd38af141a3137)  
  
void | [setItemVisible](class_tool_bar.html#a34ea22ece1a6aef59d875964c90f2754) (string, bool)  
| Shows or hides the specified action item. [More...](class_tool_bar.html#a34ea22ece1a6aef59d875964c90f2754)  
  
void | [setItemEnabled](class_tool_bar.html#aa5a8204690b28b4647811f50e4c023b7) (string, bool)  
| Enables or disables the specified action item. [More...](class_tool_bar.html#aa5a8204690b28b4647811f50e4c023b7)  
  
uuid | [addItem](class_tool_bar.html#ae1339f46da1ca9d8bafab3e7084aa60d) (QString, QString)  
| Adds a action button item at the end of the toolbar. [More...](class_tool_bar.html#ae1339f46da1ca9d8bafab3e7084aa60d)  
  
void | [removeItemUuid](class_tool_bar.html#a128df6d2bcf31b7532010a80d6737b8b) (uuid)  
| Removes the action button item with the specified UUID. [More...](class_tool_bar.html#a128df6d2bcf31b7532010a80d6737b8b)  
  
[MenuItem](class_menu_item.html) | [getItemByUuid](class_tool_bar.html#ad2656fdb79e5481c0c20424d2427c4cc) (uuid)  
| Returns the action button item with the specified UUID. [More...](class_tool_bar.html#ad2656fdb79e5481c0c20424d2427c4cc)  
  
void | [setItemObjectEnabled](class_tool_bar.html#ac2033eee0e53d416bf1a881249dc8fd4) (string, bool)  
| Enables or disables the specified action item by using object name. [More...](class_tool_bar.html#ac2033eee0e53d416bf1a881249dc8fd4)  
  
uuid | [addItemWithName](class_tool_bar.html#a2542be3ba717beb5a7433997b30e2b12) (QString, QString, QString)  
| Adds a action button item at the end of the toolbar. [More...](class_tool_bar.html#a2542be3ba717beb5a7433997b30e2b12)  
  
  
## Detailed Description

[ToolBar](class_tool_bar.html "ToolBar is the QDocWindow instatiated in QMainWindow.") is the QDocWindow instatiated in QMainWindow. 

## Member Function Documentation

## ◆ addItem()

uuid ToolBar::addItem  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Adds a action button item at the end of the toolbar. 

Parameters
     text,the| name of the button.   
---|---  
iconPath,the| full path of the image to use in the button.  
  
Returns
    uuid, the UUID of the action button item that was added. 

## ◆ addItemWithName()

uuid ToolBar::addItemWithName  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | QString  |   
| ) | |   
  
Adds a action button item at the end of the toolbar. 

Parameters
     text,the| name of the button.   
---|---  
iconPath,the| full path of the image to use in the button.   
name,the| object name assigned to the button action.  
  
Returns
    uuid, the UUID of the action button item that was added. 

## ◆ count()

int ToolBar::count  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of action items in this toolbar. 

Returns
    int, the number of action items in this toolbar. 

## ◆ getItemByUuid()

[MenuItem](class_menu_item.html) ToolBar::getItemByUuid  | ( | uuid  | | ) |   
---|---|---|---|---|---  
  
Returns the action button item with the specified UUID. 

Parameters
     id,the| UUID of the action button item of interest.  
---|---  
  
Returns
    [MenuItem](class_menu_item.html "MenuItem is an item in the Menu object."), the action button item object with the specified UUID. 

## ◆ removeItemUuid()

void ToolBar::removeItemUuid  | ( | uuid  | | ) |   
---|---|---|---|---|---  
  
Removes the action button item with the specified UUID. 

Parameters
     id,the| UUID of the action button item of interest.   
---|---  
  
## ◆ setItemAtEnabled()

void ToolBar::setItemAtEnabled  | ( | int  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Enables or disables the action item at the specified index. 

Parameters
     index,the| index of the action item.   
---|---  
bEnabled,true| to enable the action item, false to disable it.   
  
## ◆ setItemAtVisible()

void ToolBar::setItemAtVisible  | ( | int  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Shows or hides the action item at the specified index. 

Parameters
     index,the| index of the action item.   
---|---  
bVisible,true| to show the action item, false to hide it.   
  
## ◆ setItemEnabled()

void ToolBar::setItemEnabled  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Enables or disables the specified action item. 

Parameters
     name,the| name of the action item.   
---|---  
bEnabled,true| to enable the action item, false to disable it.   
  
## ◆ setItemObjectEnabled()

void ToolBar::setItemObjectEnabled  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Enables or disables the specified action item by using object name. 

Parameters
     name,the| object name of the action item.   
---|---  
bEnabled,true| to enable the action item, false to disable it.   
  
## ◆ setItemVisible()

void ToolBar::setItemVisible  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Shows or hides the specified action item. 

Parameters
     name,the| name of the action item.   
---|---  
bVisible,true| to show the action item, false to hide it.   
  
## ◆ setVisible()

void ToolBar::setVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows or hides this widget from view. 

Parameters
     bVisible,true| to show this widget, false to hide it.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [ToolBar.pki](_tool_bar_8pki.html)


