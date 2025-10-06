# Cisco Packet Tracer Extensions API: PhysicalObject Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_physical_object.html

---

An object in the Physical [Workspace](class_workspace.html "Workspace is the base class for Logical and Physical workspace related objects."). [More...](class_physical_object.html#details)

##  Public Member Functions  
  
---  
QString | [getName](class_physical_object.html#ac7597b2b28e42062cd8b4c7e2ff5fee4) ()  
| Returns the name of this physical object. [More...](class_physical_object.html#ac7597b2b28e42062cd8b4c7e2ff5fee4)  
  
PhysicalObjectType | [getType](class_physical_object.html#acc32231c0bb1b4746afec078d129e319) ()  
| Returns the type of physical object. INTER_CITY = 0, CITY = 1, BUILDING = 2, WIRING_CLOSET = 3, RACK = 4, TABLE = 5, DEVICE = 6 MULTIUSER = 7, GENERIC_CONTAINER = 8,   
[More...](class_physical_object.html#acc32231c0bb1b4746afec078d129e319)  
  
int | [getX](class_physical_object.html#a8b76344a0d243cc0a9bbf4314b3b4097) ()  
| Returns X coordinate. [More...](class_physical_object.html#a8b76344a0d243cc0a9bbf4314b3b4097)  
  
int | [getY](class_physical_object.html#a44c8d8671cf1d54d8b2240e48a8a6a6d) ()  
| Returns Y coordinate. [More...](class_physical_object.html#a44c8d8671cf1d54d8b2240e48a8a6a6d)  
  
int | [getCenterX](class_physical_object.html#a9dc95be658d4b4ad7daac0aaede222d5) ()  
| Returns center X coordinate. [More...](class_physical_object.html#a9dc95be658d4b4ad7daac0aaede222d5)  
  
int | [getCenterY](class_physical_object.html#acc0b7d66d3f5f57327f8062327b64619) ()  
| Returns center Y coordinate. [More...](class_physical_object.html#acc0b7d66d3f5f57327f8062327b64619)  
  
double | [getGlobalX](class_physical_object.html#acb9deb5d2f5f5d28677270218a948e2d) ()  
| Returns global X coordinate. [More...](class_physical_object.html#acb9deb5d2f5f5d28677270218a948e2d)  
  
double | [getGlobalY](class_physical_object.html#a2454022350ca039964594fc96a1ecfa3) ()  
| Returns global Y coordinate. [More...](class_physical_object.html#a2454022350ca039964594fc96a1ecfa3)  
  
[Device](class_device.html) | [getDevice](class_physical_object.html#abc5806f09786648ccb1d5e7d1623b746) ()  
| Returns the device if the type is DEVICE. [More...](class_physical_object.html#abc5806f09786648ccb1d5e7d1623b746)  
  
[PhysicalObject](class_physical_object.html) | [getParent](class_physical_object.html#a2ad0bd983bf6014fe2ce53e2fdfee0cb) ()  
| Returns the parent that contains the physical object. [More...](class_physical_object.html#a2ad0bd983bf6014fe2ce53e2fdfee0cb)  
  
bool | [moveOutOfCurrentObject](class_physical_object.html#a72128997c43a9c35472756f169e7cab4) ()  
| Moves the physical object out of the current parent object and returns whether it was successful. [More...](class_physical_object.html#a72128997c43a9c35472756f169e7cab4)  
  
bool | [moveIntoObject](class_physical_object.html#a48df1104b99bc8fa091906488b261030) (QString)  
| Moves the physical object into an object in the same level with the specified name and returns whether it was successful. [More...](class_physical_object.html#a48df1104b99bc8fa091906488b261030)  
  
int | [getChildCount](class_physical_object.html#a32675a51f2b2e180e842cf602d9f88f8) ()  
| Returns the number of children the physical object has. [More...](class_physical_object.html#a32675a51f2b2e180e842cf602d9f88f8)  
  
[PhysicalObject](class_physical_object.html) | [getChildAt](class_physical_object.html#a8a174325d4aec6e9c976f7b055e9bcae) (int)  
| Returns the child at the given index in the physical object. [More...](class_physical_object.html#a8a174325d4aec6e9c976f7b055e9bcae)  
  
[PhysicalObject](class_physical_object.html) | [getChild](class_physical_object.html#aea3956860b66e928c112b35a93624297) (QString)  
| Returns the child with the specified name in the physical object. [More...](class_physical_object.html#aea3956860b66e928c112b35a93624297)  
  
[PhysicalObject](class_physical_object.html) | [getChildByPath](class_physical_object.html#a4607e252063b95f23b324856318ffe9d) (QString)  
| Returns the child recursively with the specified path separated by comma (,) in the physical object. [More...](class_physical_object.html#a4607e252063b95f23b324856318ffe9d)  
  
void | [setBackground](class_physical_object.html#aaba07da9450e83f3af231d9f87ecf24e) (QString, bool)  
| Sets the background image path to use when inside the physical object. [More...](class_physical_object.html#aaba07da9450e83f3af231d9f87ecf24e)  
  
QString | [getBackground](class_physical_object.html#a0df9d93f690beaa1d2b4c79c644ae0b0) ()  
| Sets the background image path to use when inside the physical object. [More...](class_physical_object.html#a0df9d93f690beaa1d2b4c79c644ae0b0)  
  
[Environment](class_environment.html) | [getEnvironment](class_physical_object.html#a45088ebe7a666e7e16e59e4f756589fc) ()  
| Gets the environment for the physical object. [More...](class_physical_object.html#a45088ebe7a666e7e16e59e4f756589fc)  
  
void | [deviceMoved](class_physical_object.html#acc3e6aaafba4ac0c469d41d14b6cdb3e) ([Device](class_device.html), [PhysicalObject](class_physical_object.html), [PhysicalObject](class_physical_object.html))  
| [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. [More...](class_physical_object.html#acc3e6aaafba4ac0c469d41d14b6cdb3e)  
  
void | [setX](class_physical_object.html#a0f71fd7a5cf15da8b9a27f61a6b66b9a) (int)  
void | [setY](class_physical_object.html#af417d461a729e90d62188328b9588359) (int)  
| Sets the y-coordinate of the component item. [More...](class_physical_object.html#af417d461a729e90d62188328b9588359)  
  
void | [moveBy](class_physical_object.html#a8645498a80b77c06584365cc33f95be7) (int, int)  
| Moves the component item by the specified x and y values. [More...](class_physical_object.html#a8645498a80b77c06584365cc33f95be7)  
  
void | [moveTo](class_physical_object.html#a40e7455d68f922dcbab4746af03ca41e) (int, int)  
| Moves the component item to the specified coordinates. [More...](class_physical_object.html#a40e7455d68f922dcbab4746af03ca41e)  
  
double | [getXScale](class_physical_object.html#aa671d69c935842a52377d67549634f14) ()  
double | [getYScale](class_physical_object.html#a22a861b313f308f2ac5dfa55b0317fab) ()  
double | [getWidth](class_physical_object.html#a50dd885d9921c156823dd452d5795894) ()  
double | [getHeight](class_physical_object.html#a413a855693a4e717ac9d220dde7ddd50) ()  
void | [setXVelocity](class_physical_object.html#aad23efc18d6d2d943f5dca219a6d7456) (double)  
| Sets the x-axis velocity of the component item. [More...](class_physical_object.html#aad23efc18d6d2d943f5dca219a6d7456)  
  
void | [setYVelocity](class_physical_object.html#ae6571a9ddbb4e861555ceebae4a93d14) (double)  
| Sets the y-axis velocity of the component item. [More...](class_physical_object.html#ae6571a9ddbb4e861555ceebae4a93d14)  
  
void | [setVelocity](class_physical_object.html#a6d2cf3dc91b67eb7070c07637730b2bb) (double, double)  
| Sets the x-axis and y-axis velocity of the component item. [More...](class_physical_object.html#a6d2cf3dc91b67eb7070c07637730b2bb)  
  
double | [xVelocity](class_physical_object.html#a69c9326fdcfdd74a9dc1130736be1041) ()  
| Returns the x-axis velocity of the component item. [More...](class_physical_object.html#a69c9326fdcfdd74a9dc1130736be1041)  
  
double | [yVelocity](class_physical_object.html#a01c50ccd8311a3b06e2297e717b9f13d) ()  
| Returns the y-axis velocity of the component item. [More...](class_physical_object.html#a01c50ccd8311a3b06e2297e717b9f13d)  
  
QString | [getPathUuid](class_physical_object.html#ab2cfbb70ea1a896206e7c13be097689f) ()  
| Returns the UUID of the physical object. [More...](class_physical_object.html#ab2cfbb70ea1a896206e7c13be097689f)  
  
QString | [nameToUuidPath](class_physical_object.html#a0888bf7022d990d305cd4157d186c469) (QString)  
| Returns the comma-separated UUID path of the physical object from the given comma-separated physical location name path. [More...](class_physical_object.html#a0888bf7022d990d305cd4157d186c469)  
  
QString | [uuidToNamePath](class_physical_object.html#af1a6ef4805e6d757cb5cb688225b090a) (QString)  
| Returns the comma-separated name path of the physical object from the given comma-separated physical location UUID path. [More...](class_physical_object.html#af1a6ef4805e6d757cb5cb688225b090a)  
  
  
## Detailed Description

An object in the Physical [Workspace](class_workspace.html "Workspace is the base class for Logical and Physical workspace related objects."). 

## Member Function Documentation

## ◆ deviceMoved()

void PhysicalObject::deviceMoved  | ( | [Device](class_device.html) | ,   
---|---|---|---  
|  | [PhysicalObject](class_physical_object.html) | ,   
|  | [PhysicalObject](class_physical_object.html) |   
| ) | |   
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

This event is emitted when the device is moved from one physical object to another.

  * dev, the device 
  * from, from container. 
  * to, to container. 



## ◆ getBackground()

QString PhysicalObject::getBackground  | ( | | ) |   
---|---|---|---|---  
  
Sets the background image path to use when inside the physical object. 

Returns
    QString, the background image path. 

## ◆ getCenterX()

int PhysicalObject::getCenterX  | ( | | ) |   
---|---|---|---|---  
  
Returns center X coordinate. 

Returns
    int, center x coordinate. 

## ◆ getCenterY()

int PhysicalObject::getCenterY  | ( | | ) |   
---|---|---|---|---  
  
Returns center Y coordinate. 

Returns
    int, center Y coordinate. 

## ◆ getChild()

[PhysicalObject](class_physical_object.html) PhysicalObject::getChild  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the child with the specified name in the physical object. 

Parameters
     name,name| of the child.  
---|---  
  
Returns
    [PhysicalObject](class_physical_object.html "An object in the Physical Workspace."), the child with the specified name, if any. 

## ◆ getChildAt()

[PhysicalObject](class_physical_object.html) PhysicalObject::getChildAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the child at the given index in the physical object. 

Parameters
     index,index| to get a child from.  
---|---  
  
Returns
    [PhysicalObject](class_physical_object.html "An object in the Physical Workspace."), the child at the given index, if any. 

## ◆ getChildByPath()

[PhysicalObject](class_physical_object.html) PhysicalObject::getChildByPath  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the child recursively with the specified path separated by comma (,) in the physical object. 

Parameters
     path,path| of the child separated by comma (,).  
---|---  
  
Returns
    [PhysicalObject](class_physical_object.html "An object in the Physical Workspace."), the child with the specified path, if any. 

## ◆ getChildCount()

int PhysicalObject::getChildCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of children the physical object has. 

Returns
    int, the number of children the physical object has. 

## ◆ getDevice()

[Device](class_device.html) PhysicalObject::getDevice  | ( | | ) |   
---|---|---|---|---  
  
Returns the device if the type is DEVICE. 

Returns
    [Device](class_device.html "Device is the base class for all device objects."), the device in the object type is DEVICE. 

## ◆ getEnvironment()

[Environment](class_environment.html) PhysicalObject::getEnvironment  | ( | | ) |   
---|---|---|---|---  
  
Gets the environment for the physical object. 

Returns
    [Environment](class_environment.html "An object in the Physical Workspace."), the environment for the physical object. 

## ◆ getGlobalX()

double PhysicalObject::getGlobalX  | ( | | ) |   
---|---|---|---|---  
  
Returns global X coordinate. 

Returns
    double, global x coordinate. 

## ◆ getGlobalY()

double PhysicalObject::getGlobalY  | ( | | ) |   
---|---|---|---|---  
  
Returns global Y coordinate. 

Returns
    double, global Y coordinate. 

## ◆ getHeight()

double PhysicalObject::getHeight  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getName()

QString PhysicalObject::getName  | ( | | ) |   
---|---|---|---|---  
  
Returns the name of this physical object. 

Returns
    QString, name of the object. 

## ◆ getParent()

[PhysicalObject](class_physical_object.html) PhysicalObject::getParent  | ( | | ) |   
---|---|---|---|---  
  
Returns the parent that contains the physical object. 

Returns
    [PhysicalObject](class_physical_object.html "An object in the Physical Workspace."), the parent that contains the physical object. 

## ◆ getPathUuid()

QString PhysicalObject::getPathUuid  | ( | | ) |   
---|---|---|---|---  
  
Returns the UUID of the physical object. 

Returns
    QString, the UUID of the physical object 

## ◆ getType()

PhysicalObjectType PhysicalObject::getType  | ( | | ) |   
---|---|---|---|---  
  
Returns the type of physical object. INTER_CITY = 0, CITY = 1, BUILDING = 2, WIRING_CLOSET = 3, RACK = 4, TABLE = 5, DEVICE = 6 MULTIUSER = 7, GENERIC_CONTAINER = 8,   


Returns
    PhysicalObjectType 

## ◆ getWidth()

double PhysicalObject::getWidth  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getX()

int PhysicalObject::getX  | ( | | ) |   
---|---|---|---|---  
  
Returns X coordinate. 

Returns
    int, x coordinate. 

## ◆ getXScale()

double PhysicalObject::getXScale  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getY()

int PhysicalObject::getY  | ( | | ) |   
---|---|---|---|---  
  
Returns Y coordinate. 

Returns
    int, y coordinate. 

## ◆ getYScale()

double PhysicalObject::getYScale  | ( | | ) |   
---|---|---|---|---  
  
## ◆ moveBy()

void PhysicalObject::moveBy  | ( | int  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Moves the component item by the specified x and y values. 

Parameters
     x,the| value to move the component item by on the x-axis.   
---|---  
y,the| value to move the component item by on the y-axis.   
  
## ◆ moveIntoObject()

bool PhysicalObject::moveIntoObject  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Moves the physical object into an object in the same level with the specified name and returns whether it was successful. 

Parameters
     name,the| name of the object in the same level   
---|---  
  
Returns
    boolean, whether the move was successful. 

## ◆ moveOutOfCurrentObject()

bool PhysicalObject::moveOutOfCurrentObject  | ( | | ) |   
---|---|---|---|---  
  
Moves the physical object out of the current parent object and returns whether it was successful. 

Returns
    boolean, whether the move was successful. 

## ◆ moveTo()

void PhysicalObject::moveTo  | ( | int  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Moves the component item to the specified coordinates. 

Parameters
     x,the| value to move the component item to on the x-axis.   
---|---  
y,the| value to move the component item to on the y-axis.   
  
## ◆ nameToUuidPath()

QString PhysicalObject::nameToUuidPath  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the comma-separated UUID path of the physical object from the given comma-separated physical location name path. 

Returns
    QString, the comma-separated UUID path of the physical object from the given comma-separated physical location name path 

## ◆ setBackground()

void PhysicalObject::setBackground  | ( | QString  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Sets the background image path to use when inside the physical object. 

Parameters
     path,path| to the image to use.   
---|---  
tiled,true| to tile the background false to just show one image.   
  
## ◆ setVelocity()

void PhysicalObject::setVelocity  | ( | double  | ,   
---|---|---|---  
|  | double  |   
| ) | |   
  
Sets the x-axis and y-axis velocity of the component item. 

Parameters
     xv,the| x-axis velocity of the component item.   
---|---  
yv,the| y-axis velocity of the component item.   
  
## ◆ setX()

void PhysicalObject::setX  | ( | int  | | ) |   
---|---|---|---|---|---  
  
## ◆ setXVelocity()

void PhysicalObject::setXVelocity  | ( | double  | | ) |   
---|---|---|---|---|---  
  
Sets the x-axis velocity of the component item. 

Parameters
     xv,the| x-axis velocity of the component item.   
---|---  
  
## ◆ setY()

void PhysicalObject::setY  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the y-coordinate of the component item. 

Parameters
     y,the| y-coordinate of the component item.   
---|---  
  
## ◆ setYVelocity()

void PhysicalObject::setYVelocity  | ( | double  | | ) |   
---|---|---|---|---|---  
  
Sets the y-axis velocity of the component item. 

Parameters
     yv,the| y-axis velocity of the component item.   
---|---  
  
## ◆ uuidToNamePath()

QString PhysicalObject::uuidToNamePath  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the comma-separated name path of the physical object from the given comma-separated physical location UUID path. 

Returns
    QString, the comma-separated name path of the physical object from the given comma-separated physical location UUID path 

## ◆ xVelocity()

double PhysicalObject::xVelocity  | ( | | ) |   
---|---|---|---|---  
  
Returns the x-axis velocity of the component item. 

Returns
    double, the x-axis velocity of the component item. 

## ◆ yVelocity()

double PhysicalObject::yVelocity  | ( | | ) |   
---|---|---|---|---  
  
Returns the y-axis velocity of the component item. 

Returns
    double, the y-axis velocity of the component item. 

* * *

The documentation for this class was generated from the following file:

  * [PhysicalObject.pki](_physical_object_8pki.html)


