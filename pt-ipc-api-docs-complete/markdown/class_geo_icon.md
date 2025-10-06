# Cisco Packet Tracer Extensions API: GeoIcon Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_geo_icon.html

---

[GeoIcon](class_geo_icon.html "GeoIcon handles and manipulates component items, such as devices, on the workspace.") handles and manipulates component items, such as devices, on the workspace. [More...](class_geo_icon.html#details)

##  Public Member Functions  
  
---  
void | [setVisible](class_geo_icon.html#ae0d760fe33a82fdb314a82415097ceb1) (bool)  
| Shows or hides the component item. [More...](class_geo_icon.html#ae0d760fe33a82fdb314a82415097ceb1)  
  
int | [type](class_geo_icon.html#a9f4148750f4ad1bee67fad0b32122f01) ()  
| Returns the type of the component item. [More...](class_geo_icon.html#a9f4148750f4ad1bee67fad0b32122f01)  
  
void | [moveBy](class_geo_icon.html#a733e97bd53f401a219fdae6c4f6f01d2) (double, double)  
| Moves the component item by the specified x and y values. [More...](class_geo_icon.html#a733e97bd53f401a219fdae6c4f6f01d2)  
  
void | [moveTo](class_geo_icon.html#a049e676b32650a1887473822be60406a) (double, double)  
| Moves the component item to the specified coordinates. [More...](class_geo_icon.html#a049e676b32650a1887473822be60406a)  
  
[PhysicalObject](class_physical_object.html) | [getPhysicalObject](class_geo_icon.html#a613f7dc51a634c115a31ff47ad1aebad) ()  
| Returns the device. [More...](class_geo_icon.html#a613f7dc51a634c115a31ff47ad1aebad)  
  
  
## Detailed Description

[GeoIcon](class_geo_icon.html "GeoIcon handles and manipulates component items, such as devices, on the workspace.") handles and manipulates component items, such as devices, on the workspace. 

## Member Function Documentation

## ◆ getPhysicalObject()

[PhysicalObject](class_physical_object.html) GeoIcon::getPhysicalObject  | ( | | ) |   
---|---|---|---|---  
  
Returns the device. 

Returns
    [Device](class_device.html "Device is the base class for all device objects."), the device object. 

## ◆ moveBy()

void GeoIcon::moveBy  | ( | double  | ,   
---|---|---|---  
|  | double  |   
| ) | |   
  
Moves the component item by the specified x and y values. 

Parameters
     x,the| value to move the component item by on the x-axis.   
---|---  
y,the| value to move the component item by on the y-axis.   
  
## ◆ moveTo()

void GeoIcon::moveTo  | ( | double  | ,   
---|---|---|---  
|  | double  |   
| ) | |   
  
Moves the component item to the specified coordinates. 

Parameters
     x,the| value to move the component item to on the x-axis.   
---|---  
y,the| value to move the component item to on the y-axis.   
  
## ◆ setVisible()

void GeoIcon::setVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows or hides the component item. 

Parameters
     bVisible,true| to show the component item, false to hide it.   
---|---  
  
## ◆ type()

int GeoIcon::type  | ( | | ) |   
---|---|---|---|---  
  
Returns the type of the component item. 

Returns
    int, the type of component. Types: COMPONENT = 1100, CONNECTION = 1101, NOTE = 1102, PACKET = 1103, CLUSTER = 1104, RECTANGLE = 1105, LINE = 1106, ELLIPSE = 1107, MULTIUSERITEM = 1108, QOSPACKET = 1109, RESIZEINDICATOR = 1110, ACCESSORYITEM = 1111, POLYGON = 1112, TEXTPOPUP = 1113 

* * *

The documentation for this class was generated from the following file:

  * [GeoIcon.pki](_geo_icon_8pki.html)


