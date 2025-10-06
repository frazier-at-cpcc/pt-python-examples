# Cisco Packet Tracer Extensions API: ComponentItem Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_component_item.html

---

[ComponentItem](class_component_item.html "ComponentItem handles and manipulates component items, such as devices, on the workspace.") handles and manipulates component items, such as devices, on the workspace. [More...](class_component_item.html#details)

##  Public Member Functions  
  
---  
QString | [getName](class_component_item.html#a4f7226a889fca366a0172c842b5bb5d2) ()  
| Returns the name of this component item. [More...](class_component_item.html#a4f7226a889fca366a0172c842b5bb5d2)  
  
void | [setVisible](class_component_item.html#a4652203c80e65fbbd08df9d9e91b4666) (bool)  
| Shows or hides the component item. [More...](class_component_item.html#a4652203c80e65fbbd08df9d9e91b4666)  
  
int | [type](class_component_item.html#a186c2799aedacfc098839af0bf33c1db) ()  
| Returns the type of the component item. [More...](class_component_item.html#a186c2799aedacfc098839af0bf33c1db)  
  
void | [moveBy](class_component_item.html#a4e8487d5f194a582d1bf6cd1e3255bbd) (double, double)  
| Moves the component item by the specified x and y values. [More...](class_component_item.html#a4e8487d5f194a582d1bf6cd1e3255bbd)  
  
void | [moveTo](class_component_item.html#a98f9bf665667e732211c624ad9bac606) (double, double)  
| Moves the component item to the specified coordinates. [More...](class_component_item.html#a98f9bf665667e732211c624ad9bac606)  
  
[Device](class_device.html) | [device](class_component_item.html#ad32e3c19667fc6cd0f811bdc298a4a8a) ()  
| Returns the device. [More...](class_component_item.html#ad32e3c19667fc6cd0f811bdc298a4a8a)  
  
int | [getXCoordinate](class_component_item.html#adc8cfa9797d5db690cee1eb9cf74cde4) ()  
| Returns the x-coordinate of the component item. [More...](class_component_item.html#adc8cfa9797d5db690cee1eb9cf74cde4)  
  
int | [getXCoordinateCenter](class_component_item.html#a2763fde2489139f2eba09e9490b2a911) ()  
| Returns the center x-coordinate of the component item. [More...](class_component_item.html#a2763fde2489139f2eba09e9490b2a911)  
  
int | [getYCoordinate](class_component_item.html#ac502259c8dc912efbedf29a5d92bc3f7) ()  
| Returns the y-coordinate of the component item. [More...](class_component_item.html#ac502259c8dc912efbedf29a5d92bc3f7)  
  
int | [getYCoordinateCenter](class_component_item.html#ac70a122ea5ff37e4f5ab5f3f516bad4a) ()  
| Returns the center y-coordinate of the component item. [More...](class_component_item.html#ac70a122ea5ff37e4f5ab5f3f516bad4a)  
  
void | [setX](class_component_item.html#a9493bd3a3677c7e3587f268f5a7382df) (double)  
| Sets the x-coordinate of the component item. [More...](class_component_item.html#a9493bd3a3677c7e3587f268f5a7382df)  
  
void | [setXCenter](class_component_item.html#a673fdeb51d5471fad1dee4fbb7d9a66a) (int)  
| Sets the center x-coordinate of the component item. [More...](class_component_item.html#a673fdeb51d5471fad1dee4fbb7d9a66a)  
  
void | [setY](class_component_item.html#a13d1d05645fe1b602cbdddb944b16d54) (double)  
| Sets the y-coordinate of the component item. [More...](class_component_item.html#a13d1d05645fe1b602cbdddb944b16d54)  
  
void | [setYCenter](class_component_item.html#af0cb0016d14c2986d4ba741c7d26c0fe) (int)  
| Sets the center y-coordinate of the component item. [More...](class_component_item.html#af0cb0016d14c2986d4ba741c7d26c0fe)  
  
int | [getWidth](class_component_item.html#a604963253acf6e873a65744502d8b197) ()  
int | [getHeight](class_component_item.html#af7e091aaea2ebc5b2124cba8be82dc4d) ()  
void | [setXVelocity](class_component_item.html#af31d90a25fd33f72226a0501696345e1) (double)  
| Sets the x-axis velocity of the component item. [More...](class_component_item.html#af31d90a25fd33f72226a0501696345e1)  
  
void | [setYVelocity](class_component_item.html#a79028b79344e5e2041dbf5ef38e8acc3) (double)  
| Sets the y-axis velocity of the component item. [More...](class_component_item.html#a79028b79344e5e2041dbf5ef38e8acc3)  
  
void | [setVelocity](class_component_item.html#a973a59cb338aba72fd0badb391b7bdec) (double, double)  
| Sets the x-axis and y-axis velocity of the component item. [More...](class_component_item.html#a973a59cb338aba72fd0badb391b7bdec)  
  
double | [xVelocity](class_component_item.html#a1ca6bef742c97eeb394fb44327e9edfd) ()  
| Returns the x-axis velocity of the component item. [More...](class_component_item.html#a1ca6bef742c97eeb394fb44327e9edfd)  
  
double | [yVelocity](class_component_item.html#a3dc56d116949a27382c2c766112700e7) ()  
| Returns the y-axis velocity of the component item. [More...](class_component_item.html#a3dc56d116949a27382c2c766112700e7)  
  
void | [setSelected](class_component_item.html#ad4d5ff7f671032886b62fa777cb2f11f) (bool)  
| Selects or deselects the component item. [More...](class_component_item.html#ad4d5ff7f671032886b62fa777cb2f11f)  
  
string | [getClusterID](class_component_item.html#a6d86c642b76aab09dcf70d1fed478dc7) ()  
| Returns the cluster ID of the component item. [More...](class_component_item.html#a6d86c642b76aab09dcf70d1fed478dc7)  
  
QString | [getThisClusterID](class_component_item.html#a6aba38bd0e000c25f71db80189168b1f) ()  
[ComponentItem](class_component_item.html) | [getParent](class_component_item.html#a9ba8526144e6f530dae1aea0a89a38c3) ()  
| Returns the parent cluster that contains this component item. [More...](class_component_item.html#a9ba8526144e6f530dae1aea0a89a38c3)  
  
bool | [moveOutOfCurrentCluster](class_component_item.html#a50b8c6c229063c4832ad1d07d2e0c291) ()  
| Moves the component item out of the current cluster and returns whether it was successful. [More...](class_component_item.html#a50b8c6c229063c4832ad1d07d2e0c291)  
  
bool | [moveIntoCluster](class_component_item.html#a6a5888f0f58d84fb7745f05ff14a6e0d) (QString)  
| Moves the component item into a cluster in the same level with the specified name and returns whether it was successful. [More...](class_component_item.html#a6a5888f0f58d84fb7745f05ff14a6e0d)  
  
bool | [loadAccessoryImage](class_component_item.html#a1db4af634b9a640a72eca2a60e6f9458) (int, QString)  
| Loads an image for an accessory. [More...](class_component_item.html#a1db4af634b9a640a72eca2a60e6f9458)  
  
void | [removeAccessory](class_component_item.html#af849a4d4c5c408d43a138050d20ff4ed) (int)  
| Removes an accessory. [More...](class_component_item.html#af849a4d4c5c408d43a138050d20ff4ed)  
  
  
## Detailed Description

[ComponentItem](class_component_item.html "ComponentItem handles and manipulates component items, such as devices, on the workspace.") handles and manipulates component items, such as devices, on the workspace. 

## Member Function Documentation

## ◆ device()

[Device](class_device.html) ComponentItem::device  | ( | | ) |   
---|---|---|---|---  
  
Returns the device. 

Returns
    [Device](class_device.html "Device is the base class for all device objects."), the device object. 

## ◆ getClusterID()

string ComponentItem::getClusterID  | ( | | ) |   
---|---|---|---|---  
  
Returns the cluster ID of the component item. 

Returns
    string, the cluster ID of the component item. 

## ◆ getHeight()

int ComponentItem::getHeight  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getName()

QString ComponentItem::getName  | ( | | ) |   
---|---|---|---|---  
  
Returns the name of this component item. 

Returns
    QString, name of the component item. 

## ◆ getParent()

[ComponentItem](class_component_item.html) ComponentItem::getParent  | ( | | ) |   
---|---|---|---|---  
  
Returns the parent cluster that contains this component item. 

Returns
    [ComponentItem](class_component_item.html "ComponentItem handles and manipulates component items, such as devices, on the workspace."), the parent cluster that contains this component item. 

## ◆ getThisClusterID()

QString ComponentItem::getThisClusterID  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getWidth()

int ComponentItem::getWidth  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getXCoordinate()

int ComponentItem::getXCoordinate  | ( | | ) |   
---|---|---|---|---  
  
Returns the x-coordinate of the component item. 

Returns
    int, the x-coordinate of the component item. 

## ◆ getXCoordinateCenter()

int ComponentItem::getXCoordinateCenter  | ( | | ) |   
---|---|---|---|---  
  
Returns the center x-coordinate of the component item. 

Returns
    int, the center x-coordinate of the component item. 

## ◆ getYCoordinate()

int ComponentItem::getYCoordinate  | ( | | ) |   
---|---|---|---|---  
  
Returns the y-coordinate of the component item. 

Returns
    int, the y-coordinate of the component item. 

## ◆ getYCoordinateCenter()

int ComponentItem::getYCoordinateCenter  | ( | | ) |   
---|---|---|---|---  
  
Returns the center y-coordinate of the component item. 

Returns
    int, the center y-coordinate of the component item. 

## ◆ loadAccessoryImage()

bool ComponentItem::loadAccessoryImage  | ( | int  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Loads an image for an accessory. 

Parameters
     slotNum,accessory| slot index.   
---|---  
imagePath,path| to the image to use for the accessory.  
  
Returns
    bool, true if successful, false if not. 

## ◆ moveBy()

void ComponentItem::moveBy  | ( | double  | ,   
---|---|---|---  
|  | double  |   
| ) | |   
  
Moves the component item by the specified x and y values. 

Parameters
     x,the| value to move the component item by on the x-axis.   
---|---  
y,the| value to move the component item by on the y-axis.   
  
## ◆ moveIntoCluster()

bool ComponentItem::moveIntoCluster  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Moves the component item into a cluster in the same level with the specified name and returns whether it was successful. 

Parameters
     name,the| name of the cluster in the same level   
---|---  
  
Returns
    boolean, whether the move was successful. 

## ◆ moveOutOfCurrentCluster()

bool ComponentItem::moveOutOfCurrentCluster  | ( | | ) |   
---|---|---|---|---  
  
Moves the component item out of the current cluster and returns whether it was successful. 

Returns
    boolean, whether the move was successful. 

## ◆ moveTo()

void ComponentItem::moveTo  | ( | double  | ,   
---|---|---|---  
|  | double  |   
| ) | |   
  
Moves the component item to the specified coordinates. 

Parameters
     x,the| value to move the component item to on the x-axis.   
---|---  
y,the| value to move the component item to on the y-axis.   
  
## ◆ removeAccessory()

void ComponentItem::removeAccessory  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Removes an accessory. 

Parameters
     slotNum,index| of the accessory to remove.   
---|---  
  
## ◆ setSelected()

void ComponentItem::setSelected  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Selects or deselects the component item. 

Parameters
     bSelected,true| to select the item, false to deselect it.   
---|---  
  
## ◆ setVelocity()

void ComponentItem::setVelocity  | ( | double  | ,   
---|---|---|---  
|  | double  |   
| ) | |   
  
Sets the x-axis and y-axis velocity of the component item. 

Parameters
     xv,the| x-axis velocity of the component item.   
---|---  
yv,the| y-axis velocity of the component item.   
  
## ◆ setVisible()

void ComponentItem::setVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows or hides the component item. 

Parameters
     bVisible,true| to show the component item, false to hide it.   
---|---  
  
## ◆ setX()

void ComponentItem::setX  | ( | double  | | ) |   
---|---|---|---|---|---  
  
Sets the x-coordinate of the component item. 

Parameters
     x,the| x-coordinate of the component item.   
---|---  
  
## ◆ setXCenter()

void ComponentItem::setXCenter  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the center x-coordinate of the component item. 

Parameters
     x,the| center x-coordinate of the component item.   
---|---  
  
## ◆ setXVelocity()

void ComponentItem::setXVelocity  | ( | double  | | ) |   
---|---|---|---|---|---  
  
Sets the x-axis velocity of the component item. 

Parameters
     xv,the| x-axis velocity of the component item.   
---|---  
  
## ◆ setY()

void ComponentItem::setY  | ( | double  | | ) |   
---|---|---|---|---|---  
  
Sets the y-coordinate of the component item. 

Parameters
     y,the| y-coordinate of the component item.   
---|---  
  
## ◆ setYCenter()

void ComponentItem::setYCenter  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the center y-coordinate of the component item. 

Parameters
     y,the| y-coordinate of the component item.   
---|---  
  
## ◆ setYVelocity()

void ComponentItem::setYVelocity  | ( | double  | | ) |   
---|---|---|---|---|---  
  
Sets the y-axis velocity of the component item. 

Parameters
     yv,the| y-axis velocity of the component item.   
---|---  
  
## ◆ type()

int ComponentItem::type  | ( | | ) |   
---|---|---|---|---  
  
Returns the type of the component item. 

Returns
    int, the type of component. Types: COMPONENT = 1100, CONNECTION = 1101, NOTE = 1102, PACKET = 1103, CLUSTER = 1104, RECTANGLE = 1105, LINE = 1106, ELLIPSE = 1107, MULTIUSERITEM = 1108, QOSPACKET = 1109, RESIZEINDICATOR = 1110, ACCESSORYITEM = 1111, POLYGON = 1112, TEXTPOPUP = 1113 

## ◆ xVelocity()

double ComponentItem::xVelocity  | ( | | ) |   
---|---|---|---|---  
  
Returns the x-axis velocity of the component item. 

Returns
    double, the x-axis velocity of the component item. 

## ◆ yVelocity()

double ComponentItem::yVelocity  | ( | | ) |   
---|---|---|---|---  
  
Returns the y-axis velocity of the component item. 

Returns
    double, the y-axis velocity of the component item. 

* * *

The documentation for this class was generated from the following file:

  * [ComponentItem.pki](_component_item_8pki.html)


