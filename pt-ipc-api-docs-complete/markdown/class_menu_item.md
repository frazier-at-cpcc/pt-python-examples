# Cisco Packet Tracer Extensions API: MenuItem Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_menu_item.html

---

[MenuItem](class_menu_item.html "MenuItem is an item in the Menu object.") is an item in the [Menu](class_menu.html "Menu is the popup menu instantiated from the MenuBar object.") object. [More...](class_menu_item.html#details)

##  Public Member Functions  
  
---  
uuid | [getUuid](class_menu_item.html#a5df53c455f495eab503a37714613c602) ()  
| Returns the UUID of this menu item. [More...](class_menu_item.html#a5df53c455f495eab503a37714613c602)  
  
void | [removeItem](class_menu_item.html#ad89bcebf02890a9c1bf992102b194088) ()  
| Removes this menu item from the parent menu. [More...](class_menu_item.html#ad89bcebf02890a9c1bf992102b194088)  
  
QString | [getLabel](class_menu_item.html#aa38069e531b5dd785661997dc7c7e818) ()  
| Returns the label for this menu item. [More...](class_menu_item.html#aa38069e531b5dd785661997dc7c7e818)  
  
void | [setEnabled](class_menu_item.html#aff2988723875a6e9343e55f29d422d02) (bool)  
| Enables or disables this menu item. [More...](class_menu_item.html#aff2988723875a6e9343e55f29d422d02)  
  
void | [setVisible](class_menu_item.html#a3fcccc968362ed97745bc6a6ade24212) (bool)  
| Shows or hides this menu item. [More...](class_menu_item.html#a3fcccc968362ed97745bc6a6ade24212)  
  
void | [onClicked](class_menu_item.html#af37ae441e63a2621505e2fa98becb059) ()  
| This event is emitted when this menu item is clicked. [More...](class_menu_item.html#af37ae441e63a2621505e2fa98becb059)  
  
  
## Detailed Description

[MenuItem](class_menu_item.html "MenuItem is an item in the Menu object.") is an item in the [Menu](class_menu.html "Menu is the popup menu instantiated from the MenuBar object.") object. 

## Member Function Documentation

## ◆ getLabel()

QString MenuItem::getLabel  | ( | | ) |   
---|---|---|---|---  
  
Returns the label for this menu item. 

Returns
    QString, the label for this menu item. 

## ◆ getUuid()

uuid MenuItem::getUuid  | ( | | ) |   
---|---|---|---|---  
  
Returns the UUID of this menu item. 

Returns
    uuid, the UUID of this menu item. 

## ◆ onClicked()

void MenuItem::onClicked  | ( | | ) |   
---|---|---|---|---  
  
This event is emitted when this menu item is clicked. 

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ removeItem()

void MenuItem::removeItem  | ( | | ) |   
---|---|---|---|---  
  
Removes this menu item from the parent menu. 

## ◆ setEnabled()

void MenuItem::setEnabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables this menu item. 

Parameters
     bEnabled,true| to enable this menu item, false to disable it.   
---|---  
  
## ◆ setVisible()

void MenuItem::setVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows or hides this menu item. 

Parameters
     bVisible,true| to show this menu item, false to hide it.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [MenuItem.pki](_menu_item_8pki.html)


