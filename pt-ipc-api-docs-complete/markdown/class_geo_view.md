# Cisco Packet Tracer Extensions API: GeoView Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_geo_view.html

---

[GeoView](class_geo_view.html "GeoView handles and manipulates the Physical Workspace excluding the wiring closet.") handles and manipulates the Physical [Workspace](class_workspace.html "Workspace is the base class for Logical and Physical workspace related objects.") excluding the wiring closet. [More...](class_geo_view.html#details)

##  Public Member Functions  
  
---  
void | [setVisible](class_geo_view.html#a21ff847ce96a780d6b62a95e686ae869) (bool)  
| Shows or hides this widget from view. [More...](class_geo_view.html#a21ff847ce96a780d6b62a95e686ae869)  
  
[GeoIcon](class_geo_icon.html) | [findGeoIconByDeviceName](class_geo_view.html#a080f2d6b44e7a139c4eb4a50668da541) (QString)  
[GeoIcon](class_geo_icon.html) | [findGeoIconContainerInCurrentViewByDeviceName](class_geo_view.html#a6fdd0406721b12c030b558ae4c913596) (QString)  
[GeoIcon](class_geo_icon.html) | [findGeoIconByPhysicalObjectName](class_geo_view.html#a0e08237cf668963f4723654e626a1ca3) (QString)  
[GeoIcon](class_geo_icon.html) | [getGeoIconByName](class_geo_view.html#afedd01f8503afcdc319013ace4b695a2) (QString)  
[PhysicalObject](class_physical_object.html) | [getPhyObjForDevName](class_geo_view.html#a51ab1602e205bd12f9e906dda1a51a87) (QString)  
void | [centerOn](class_geo_view.html#ad83a89e4a7661925f8fbfb69ffe3659b) (double, double)  
void | [centerOnGeoIconByName](class_geo_view.html#a916d44d5596fa84c87c2577619186274) (QString)  
void | [linkStarted](class_geo_view.html#aa358e6dd89fb4f8fac88ddd8bd961cc1) (QString, string, CONNECT_TYPES)  
| This event is emitted when a link starts (i.e. user connects the first end of a link) [More...](class_geo_view.html#aa358e6dd89fb4f8fac88ddd8bd961cc1)  
  
void | [linkCreated](class_geo_view.html#a1a136cae90d12633f42a968a6341cd0a) (QString, string, QString, string, CONNECT_TYPES)  
| This event is emitted when a link starts (i.e. user connects the first end of a link) [More...](class_geo_view.html#a1a136cae90d12633f42a968a6341cd0a)  
  
  
## Detailed Description

[GeoView](class_geo_view.html "GeoView handles and manipulates the Physical Workspace excluding the wiring closet.") handles and manipulates the Physical [Workspace](class_workspace.html "Workspace is the base class for Logical and Physical workspace related objects.") excluding the wiring closet. 

## Member Function Documentation

## ◆ centerOn()

void GeoView::centerOn  | ( | double  | ,   
---|---|---|---  
|  | double  |   
| ) | |   
  
## ◆ centerOnGeoIconByName()

void GeoView::centerOnGeoIconByName  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
## ◆ findGeoIconByDeviceName()

[GeoIcon](class_geo_icon.html) GeoView::findGeoIconByDeviceName  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
## ◆ findGeoIconByPhysicalObjectName()

[GeoIcon](class_geo_icon.html) GeoView::findGeoIconByPhysicalObjectName  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
## ◆ findGeoIconContainerInCurrentViewByDeviceName()

[GeoIcon](class_geo_icon.html) GeoView::findGeoIconContainerInCurrentViewByDeviceName  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
## ◆ getGeoIconByName()

[GeoIcon](class_geo_icon.html) GeoView::getGeoIconByName  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
## ◆ getPhyObjForDevName()

[PhysicalObject](class_physical_object.html) GeoView::getPhyObjForDevName  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
## ◆ linkCreated()

void GeoView::linkCreated  | ( | QString  | ,   
---|---|---|---  
|  | string  | ,   
|  | QString  | ,   
|  | string  | ,   
|  | CONNECT_TYPES  |   
| ) | |   
  
This event is emitted when a link starts (i.e. user connects the first end of a link) 

  * deviceName1, the name of the first device. 
  * portName1, portName can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0 
  * deviceName2, the name of the second device. 
  * portName2, portName can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0 
  * connType, the connection type. Connection types: ETHERNET_STRAIGHT = 8100, ETHERNET_CROSS = 8101, ETHERNET_ROLL = 8102, FIBER = 8103, PHONE = 8104, CABLE = 8105, SERIAL = 8106, AUTO = 8107, CONSOLE = 8108, WIRELESS = 8109, COAXIAL = 8110, OCTAL = 8111, CELLULAR = 8112, USB = 8113, CUSTOM_IO = 8114,   




[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ linkStarted()

void GeoView::linkStarted  | ( | QString  | ,   
---|---|---|---  
|  | string  | ,   
|  | CONNECT_TYPES  |   
| ) | |   
  
This event is emitted when a link starts (i.e. user connects the first end of a link) 

  * deviceName1, the name of the first device. 
  * portName1, portName can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0 
  * connType, the connection type. Connection types: ETHERNET_STRAIGHT = 8100, ETHERNET_CROSS = 8101, ETHERNET_ROLL = 8102, FIBER = 8103, PHONE = 8104, CABLE = 8105, SERIAL = 8106, AUTO = 8107, CONSOLE = 8108, WIRELESS = 8109, COAXIAL = 8110, OCTAL = 8111, CELLULAR = 8112, USB = 8113, CUSTOM_IO = 8114,   




[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ setVisible()

void GeoView::setVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows or hides this widget from view. 

Parameters
     bVisible,true| to show this widget, false to hide it.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [GeoView.pki](_geo_view_8pki.html)


