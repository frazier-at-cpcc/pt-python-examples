# Cisco Packet Tracer Extensions API: Workspace Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_workspace.html

---

[Workspace](class_workspace.html "Workspace is the base class for Logical and Physical workspace related objects.") is the base class for Logical and Physical workspace related objects. [More...](class_workspace.html#details)

##  Public Member Functions  
  
---  
bool | [isLogicalView](class_workspace.html#a107586b8d04b8d0b1d656a26ab2568f0) ()  
| Returns true if the Logical workspace is currently visible, otherwise false. [More...](class_workspace.html#a107586b8d04b8d0b1d656a26ab2568f0)  
  
bool | [isGeoView](class_workspace.html#a592dcd7034cf19b891330811089a7ad8) ()  
| Returns true if the Physical workspace is currently visible, otherwise false. [More...](class_workspace.html#a592dcd7034cf19b891330811089a7ad8)  
  
bool | [isRackView](class_workspace.html#a73d9268175e28c534292dc028fdffa94) ()  
| Returns true if the wiring closet is currently visible, otherwise false. [More...](class_workspace.html#a73d9268175e28c534292dc028fdffa94)  
  
[LogicalWorkspace](class_logical_workspace.html) | [getLogicalWorkspace](class_workspace.html#a09843580557412583206e374453b3735) ()  
| Returns the Logical workspace. [More...](class_workspace.html#a09843580557412583206e374453b3735)  
  
[GeoView](class_geo_view.html) | [getGeoView](class_workspace.html#af74af78dba8ffdd62fd5b95e9db70ffd) ()  
| Returns the Physical workspace. [More...](class_workspace.html#af74af78dba8ffdd62fd5b95e9db70ffd)  
  
[RackView](class_rack_view.html) | [getRackView](class_workspace.html#a1feebeee5428d386d8a54ffe2fed1044) ()  
| Returns the wiring closet. [More...](class_workspace.html#a1feebeee5428d386d8a54ffe2fed1044)  
  
[PhysicalObject](class_physical_object.html) | [getRootPhysicalObject](class_workspace.html#a85937e9088aa20fb47ebe0fe7068f691) ()  
[PhysicalObject](class_physical_object.html) | [getCurrentPhysicalObject](class_workspace.html#abfc6037c77801375094d2efe9b3e93dd) ()  
| Returns the current physical location. [More...](class_workspace.html#abfc6037c77801375094d2efe9b3e93dd)  
  
bool | [switchToPhysicalObject](class_workspace.html#ab6c0d86ee196aee1ab822f0023009c8c) ([PhysicalObject](class_physical_object.html))  
| Switch to the new physical location. [More...](class_workspace.html#ab6c0d86ee196aee1ab822f0023009c8c)  
  
void | [physicalObjectAdded](class_workspace.html#afb43cb3aa05718dcea7c914e87f67a78) ([PhysicalObject](class_physical_object.html))  
| This event is emitted when a new Physical object(container, building, closet...) is added. [More...](class_workspace.html#afb43cb3aa05718dcea7c914e87f67a78)  
  
void | [physicalObjectRemoved](class_workspace.html#af464a880cc394d70067cd6cce2fcf386) (uuid)  
| This event is emitted when a Physical object(container, building, closet...) is removed. [More...](class_workspace.html#af464a880cc394d70067cd6cce2fcf386)  
  
void | [physicalObjectMoved](class_workspace.html#af45c49b4b7e042409f3304da0e5da655) ([PhysicalObject](class_physical_object.html), uuid, [PhysicalObject](class_physical_object.html))  
| This event is emitted when a Physical object(container, building, closet...) is moved. [More...](class_workspace.html#af45c49b4b7e042409f3304da0e5da655)  
  
void | [currentPhysicalObjectChanged](class_workspace.html#a8f64ea539072a33e9dd0920a999fcb5f) ([PhysicalObject](class_physical_object.html), [PhysicalObject](class_physical_object.html))  
| This event is emitted when a Physical object(container, building, closet...) is changed. [More...](class_workspace.html#a8f64ea539072a33e9dd0920a999fcb5f)  
  
void | [setLogicalBackgroundPath](class_workspace.html#a83a2901fb8970f4f8f5cecea64c5743b) (QString, bool)  
| Sets the background image of the logical workspace. [More...](class_workspace.html#a83a2901fb8970f4f8f5cecea64c5743b)  
  
vector< QString > | [devicesAt](class_workspace.html#accd3ddccbbe6d92e6a218191dd03174f) (int, int, int, int, bool)  
| Returns a list of devices within a rectangle with specified with and height right of the specified location. [More...](class_workspace.html#accd3ddccbbe6d92e6a218191dd03174f)  
  
void | [setComponentOpacity](class_workspace.html#a663ac70784dfc8323e6344fb0124c7c9) (QString, QString, double)  
| Set the opacity for a component. [More...](class_workspace.html#a663ac70784dfc8323e6344fb0124c7c9)  
  
void | [fillColor](class_workspace.html#ae06f435becd5c736944be915f1c85841) (QString, QString, int, int, int)  
| Fill the component with a specified color. [More...](class_workspace.html#ae06f435becd5c736944be915f1c85841)  
  
void | [setComponentRotation](class_workspace.html#a3d3f8900f6782f921fe5b9181e82643c) (QString, QString, double)  
| Set the rotation for a component. [More...](class_workspace.html#a3d3f8900f6782f921fe5b9181e82643c)  
  
void | [setThingRotation](class_workspace.html#abc4cefcc090b95d2b2a0a44e3ff34f9e) (QString, double)  
| Set the rotation for a thing. [More...](class_workspace.html#abc4cefcc090b95d2b2a0a44e3ff34f9e)  
  
void | [setThingCustomText](class_workspace.html#ad30e58a40b21afbec31f0b980f595526) (QString, int, int, int, int, QString)  
| Set the custom text for Thing at a location. [More...](class_workspace.html#ad30e58a40b21afbec31f0b980f595526)  
  
bool | [hasProperty](class_workspace.html#a93a8462e63d1b2adbd1f856524891b30) (QString)  
| Check if the a property is defined. [More...](class_workspace.html#a93a8462e63d1b2adbd1f856524891b30)  
  
QString | [getProperty](class_workspace.html#ad4265d9f6834f7ea663c31c55daab14b) (QString)  
| Return the property value. [More...](class_workspace.html#ad4265d9f6834f7ea663c31c55daab14b)  
  
void | [setProperty](class_workspace.html#af19a287644b8246b8213b4cd270f7fb0) (QString, QString)  
| Set the property value. [More...](class_workspace.html#af19a287644b8246b8213b4cd270f7fb0)  
  
vector< QString > | [getProperties](class_workspace.html#a9065bfe3e46f1b4cdd19826871483c35) ()  
| Return a list of properties defined. [More...](class_workspace.html#a9065bfe3e46f1b4cdd19826871483c35)  
  
void | [pauseEnvironmentTime](class_workspace.html#a15b4e86ec6614d4543f12fb15f7ad594) ()  
| Pause the Environemnt time. [More...](class_workspace.html#a15b4e86ec6614d4543f12fb15f7ad594)  
  
void | [resumeEnvironmentTime](class_workspace.html#a21cb96ad1003d131750d7698fc4b6093) ()  
| Resume the Environemnt time. [More...](class_workspace.html#a21cb96ad1003d131750d7698fc4b6093)  
  
int | [getEnvironmentTimeInSeconds](class_workspace.html#a3d2bf6ca419f356f06736d189ed8a25c) ()  
| Get [Environment](class_environment.html "An object in the Physical Workspace.") time in seconds. [More...](class_workspace.html#a3d2bf6ca419f356f06736d189ed8a25c)  
  
void | [resetEnvironment](class_workspace.html#a1665d6ae50eb688f80855f158c99c489) ()  
| Reset the Environemnt time. [More...](class_workspace.html#a1665d6ae50eb688f80855f158c99c489)  
  
void | [setParentGraphicFromComponent](class_workspace.html#afc35999adb2b36bcba7a392731f39b33) (QString, QString, int, bool, bool)  
| Set parent graphic from component. [More...](class_workspace.html#afc35999adb2b36bcba7a392731f39b33)  
  
bool | [moveItemInWorkspace](class_workspace.html#a4777892cd437f27e2bd41ed7f2bf8355) (QString, int, int)  
| Move item in workspace to a new location. [More...](class_workspace.html#a4777892cd437f27e2bd41ed7f2bf8355)  
  
void | [setBaseZLevel](class_workspace.html#ad44e38e5f4a93cfeb646532f7fab2e7e) (QString, float)  
| Sets the base z level, which is the current z level plus the base level. [More...](class_workspace.html#ad44e38e5f4a93cfeb646532f7fab2e7e)  
  
float | [getZLevel](class_workspace.html#a1da99a577815a74792e3aa198d5585b2) (QString)  
| Returns the current z level. [More...](class_workspace.html#a1da99a577815a74792e3aa198d5585b2)  
  
void | [setVisible](class_workspace.html#a9deb627eb95e0e6a38f4cc71a21d2b42) (bool)  
void | [zoomIn](class_workspace.html#acc6d001ee427873466d48f136e151905) ()  
| Zooms into the workspace. [More...](class_workspace.html#acc6d001ee427873466d48f136e151905)  
  
void | [zoomOut](class_workspace.html#a014b841eca5b154fe874bcb4a600e814) ()  
| Zooms out of the workspace. [More...](class_workspace.html#a014b841eca5b154fe874bcb4a600e814)  
  
void | [zoomReset](class_workspace.html#ac232b2724dd1686a8cca79e085c57415) ()  
| Resets the zoom scale of the workspace. [More...](class_workspace.html#ac232b2724dd1686a8cca79e085c57415)  
  
void | [deviceTypeSelected](class_workspace.html#a5bcad4e9c83d5a37aae91dd8bfb24bfb) (QString, [DeviceDescriptor](class_device_descriptor.html), bool)  
| This event is emitted when a device or cable is selected from the network component box or cable pegboard. [More...](class_workspace.html#a5bcad4e9c83d5a37aae91dd8bfb24bfb)  
  
void | [deviceTypeDeselected](class_workspace.html#aeba530350a4bf29813af41e2fe324ead) ()  
| This event is emitted when a device or cable is deselected from the network component box (via clicking on the cancel button) or when a cable is deselected from a cable pegboard. [More...](class_workspace.html#aeba530350a4bf29813af41e2fe324ead)  
  
  
## Detailed Description

[Workspace](class_workspace.html "Workspace is the base class for Logical and Physical workspace related objects.") is the base class for Logical and Physical workspace related objects. 

## Member Function Documentation

## ◆ currentPhysicalObjectChanged()

void Workspace::currentPhysicalObjectChanged  | ( | [PhysicalObject](class_physical_object.html) | ,   
---|---|---|---  
|  | [PhysicalObject](class_physical_object.html) |   
| ) | |   
  
This event is emitted when a Physical object(container, building, closet...) is changed. 

  * oldObject, the orginal [PhysicalObject](class_physical_object.html "An object in the Physical Workspace.") object


  * newObject, the new Physical object



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ devicesAt()

vector< QString > Workspace::devicesAt  | ( | int  | ,   
---|---|---|---  
|  | int  | ,   
|  | int  | ,   
|  | int  | ,   
|  | bool  |   
| ) | |   
  
Returns a list of devices within a rectangle with specified with and height right of the specified location. 

Parameters
     x,x| coordinate of the specified location  
---|---  
y,y| coordinate of the specified location  
w,width| of the rectangle that contains the devices to be included  
h,height| of the rectangle that contains the devices to be included  
includeClusters,true| if including devices inside the cluster and false if not including  
  
Returns
    vector<QString> of device names 

## ◆ deviceTypeDeselected()

void Workspace::deviceTypeDeselected  | ( | | ) |   
---|---|---|---|---  
  
This event is emitted when a device or cable is deselected from the network component box (via clicking on the cancel button) or when a cable is deselected from a cable pegboard. 

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ deviceTypeSelected()

void Workspace::deviceTypeSelected  | ( | QString  | ,   
---|---|---|---  
|  | [DeviceDescriptor](class_device_descriptor.html) | ,   
|  | bool  |   
| ) | |   
  
This event is emitted when a device or cable is selected from the network component box or cable pegboard. 

  * str, represents the device type or cable type


  * dd, the [DeviceDescriptor](class_device_descriptor.html "Descriptor for a device.") object


  * bType, true if the state of the workspace is sAddDevices, false if the state is sAddDevice



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ fillColor()

void Workspace::fillColor  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | int  | ,   
|  | int  | ,   
|  | int  |   
| ) | |   
  
Fill the component with a specified color. 

Parameters
     deviceName,device| name  
---|---  
componentName,component| name  
red,the| rbg red value  
green,the| rbg green value  
blue,the| rbg blue value  
  
Returns
    none 

## ◆ getCurrentPhysicalObject()

[PhysicalObject](class_physical_object.html) Workspace::getCurrentPhysicalObject  | ( | | ) |   
---|---|---|---|---  
  
Returns the current physical location. 

Returns
    [PhysicalObject](class_physical_object.html "An object in the Physical Workspace."), the [PhysicalObject](class_physical_object.html "An object in the Physical Workspace.") object. 

## ◆ getEnvironmentTimeInSeconds()

int Workspace::getEnvironmentTimeInSeconds  | ( | | ) |   
---|---|---|---|---  
  
Get [Environment](class_environment.html "An object in the Physical Workspace.") time in seconds. 

Returns
    int, time in seconds 

## ◆ getGeoView()

[GeoView](class_geo_view.html) Workspace::getGeoView  | ( | | ) |   
---|---|---|---|---  
  
Returns the Physical workspace. 

Returns
    [GeoView](class_geo_view.html "GeoView handles and manipulates the Physical Workspace excluding the wiring closet."), the [GeoView](class_geo_view.html "GeoView handles and manipulates the Physical Workspace excluding the wiring closet.") object. 

## ◆ getLogicalWorkspace()

[LogicalWorkspace](class_logical_workspace.html) Workspace::getLogicalWorkspace  | ( | | ) |   
---|---|---|---|---  
  
Returns the Logical workspace. 

Returns
    [LogicalWorkspace](class_logical_workspace.html "LogicalWorkspace is a graphics view. Network design using logical topology icons happens in this spac..."), the Logical object. 

## ◆ getProperties()

vector< QString > Workspace::getProperties  | ( | | ) |   
---|---|---|---|---  
  
Return a list of properties defined. 

Returns
    vector<QString>, list of property names 

## ◆ getProperty()

QString Workspace::getProperty  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Return the property value. 

Parameters
     prop,property| name  
---|---  
  
Returns
    QString, property value 

## ◆ getRackView()

[RackView](class_rack_view.html) Workspace::getRackView  | ( | | ) |   
---|---|---|---|---  
  
Returns the wiring closet. 

Returns
    [RackView](class_rack_view.html "RackView allows for UI manipulation of the RackView \(wiring closet\)."), the [RackView](class_rack_view.html "RackView allows for UI manipulation of the RackView \(wiring closet\).") object. 

## ◆ getRootPhysicalObject()

[PhysicalObject](class_physical_object.html) Workspace::getRootPhysicalObject  | ( | | ) |   
---|---|---|---|---  
  
Returns the root/top item in the physical workspace location tree 

## ◆ getZLevel()

float Workspace::getZLevel  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the current z level. 

Returns
    none 

## ◆ hasProperty()

bool Workspace::hasProperty  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Check if the a property is defined. 

Parameters
     prop,property| name  
---|---  
  
Returns
    bool, true if it contains the property and false if not 

## ◆ isGeoView()

bool Workspace::isGeoView  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the Physical workspace is currently visible, otherwise false. 

Returns
    bool, true if the Physical workspace is currently visible, otherwise false. 

## ◆ isLogicalView()

bool Workspace::isLogicalView  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the Logical workspace is currently visible, otherwise false. 

Returns
    bool, true if the Logical workspace is currently visible, otherwise false. 

## ◆ isRackView()

bool Workspace::isRackView  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the wiring closet is currently visible, otherwise false. 

Returns
    bool, true if the wiring closet is currently visible, otherwise false. 

## ◆ moveItemInWorkspace()

bool Workspace::moveItemInWorkspace  | ( | QString  | ,   
---|---|---|---  
|  | int  | ,   
|  | int  |   
| ) | |   
  
Move item in workspace to a new location. 

Parameters
     itemName,item| name   
---|---  
x,the| x coordinate   
y,the| y coordinate   
  
Returns
    none 

## ◆ pauseEnvironmentTime()

void Workspace::pauseEnvironmentTime  | ( | | ) |   
---|---|---|---|---  
  
Pause the Environemnt time. 

Returns
    none 

## ◆ physicalObjectAdded()

void Workspace::physicalObjectAdded  | ( | [PhysicalObject](class_physical_object.html) | | ) |   
---|---|---|---|---|---  
  
This event is emitted when a new Physical object(container, building, closet...) is added. 

  * object, the [PhysicalObject](class_physical_object.html "An object in the Physical Workspace.") object that was added



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ physicalObjectMoved()

void Workspace::physicalObjectMoved  | ( | [PhysicalObject](class_physical_object.html) | ,   
---|---|---|---  
|  | uuid  | ,   
|  | [PhysicalObject](class_physical_object.html) |   
| ) | |   
  
This event is emitted when a Physical object(container, building, closet...) is moved. 

  * object, the [PhysicalObject](class_physical_object.html "An object in the Physical Workspace.") object that was moved


  * oldParentUuid, the uuid of the parent container


  * newParent, the new parent Physical object that the current object was moved to



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ physicalObjectRemoved()

void Workspace::physicalObjectRemoved  | ( | uuid  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when a Physical object(container, building, closet...) is removed. 

  * objectUuid, the uuid of the physical object that was removed



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ resetEnvironment()

void Workspace::resetEnvironment  | ( | | ) |   
---|---|---|---|---  
  
Reset the Environemnt time. 

Returns
    none 

## ◆ resumeEnvironmentTime()

void Workspace::resumeEnvironmentTime  | ( | | ) |   
---|---|---|---|---  
  
Resume the Environemnt time. 

Returns
    none 

## ◆ setBaseZLevel()

void Workspace::setBaseZLevel  | ( | QString  | ,   
---|---|---|---  
|  | float  |   
| ) | |   
  
Sets the base z level, which is the current z level plus the base level. 

Parameters
     deviceName,item| name   
---|---  
baseZLevel,the| base level   
  
Returns
    none 

## ◆ setComponentOpacity()

void Workspace::setComponentOpacity  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | double  |   
| ) | |   
  
Set the opacity for a component. 

Parameters
     deviceName,device| name  
---|---  
componentName,component| name  
value,the| opacity value  
  
Returns
    none 

## ◆ setComponentRotation()

void Workspace::setComponentRotation  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | double  |   
| ) | |   
  
Set the rotation for a component. 

Parameters
     deviceName,device| name  
---|---  
componentName,component| name  
value,the| rotation value  
  
Returns
    none 

## ◆ setLogicalBackgroundPath()

void Workspace::setLogicalBackgroundPath  | ( | QString  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Sets the background image of the logical workspace. 

Parameters
     tiled,true| if the image will be used as tiled layout and false if not  
---|---  
  
Returns
    none 

## ◆ setParentGraphicFromComponent()

void Workspace::setParentGraphicFromComponent  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | int  | ,   
|  | bool  | ,   
|  | bool  |   
| ) | |   
  
Set parent graphic from component. 

Parameters
     deviceName,device| name   
---|---  
componentName,component| name   
index,the| image index to be used   
bOnLogical,if| true, set parent graphic in logical workspace   
bOnPhysical,if| true, set parent graphic in physical workspace   
  
Returns
    none 

## ◆ setProperty()

void Workspace::setProperty  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Set the property value. 

Parameters
     prop,property| name  
---|---  
value,property| value  
  
Returns
    none 

## ◆ setThingCustomText()

void Workspace::setThingCustomText  | ( | QString  | ,   
---|---|---|---  
|  | int  | ,   
|  | int  | ,   
|  | int  | ,   
|  | int  | ,   
|  | QString  |   
| ) | |   
  
Set the custom text for Thing at a location. 

Parameters
     deviceName,device| name  
---|---  
x,the| x coordinate of where the text will show up  
y,the| y coordinate of where the text will show up  
width,the| width the text  
height,the| height of the text  
text,the| string to show up  
  
Returns
    none 

## ◆ setThingRotation()

void Workspace::setThingRotation  | ( | QString  | ,   
---|---|---|---  
|  | double  |   
| ) | |   
  
Set the rotation for a thing. 

Parameters
     deviceName,device| name  
---|---  
value,the| rotation value  
  
Returns
    none 

## ◆ setVisible()

void Workspace::setVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
## ◆ switchToPhysicalObject()

bool Workspace::switchToPhysicalObject  | ( | [PhysicalObject](class_physical_object.html) | | ) |   
---|---|---|---|---|---  
  
Switch to the new physical location. 

Parameters
     object,[PhysicalObject](class_physical_object.html "An object in the Physical Workspace.")| object  
---|---  
  
Returns
    bool, return true if the switching is successful and false if not. 

## ◆ zoomIn()

void Workspace::zoomIn  | ( | | ) |   
---|---|---|---|---  
  
Zooms into the workspace. 

Returns
    none 

## ◆ zoomOut()

void Workspace::zoomOut  | ( | | ) |   
---|---|---|---|---  
  
Zooms out of the workspace. 

Returns
    none 

## ◆ zoomReset()

void Workspace::zoomReset  | ( | | ) |   
---|---|---|---|---  
  
Resets the zoom scale of the workspace. 

Returns
    none 

* * *

The documentation for this class was generated from the following file:

  * [Workspace.pki](_workspace_8pki.html)


