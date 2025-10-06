# Cisco Packet Tracer Extensions API: NFExporter Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_n_f_exporter.html

---

[NFExporter](class_n_f_exporter.html "NFExporter handles and manipulates NetFlow exporters.") handles and manipulates NetFlow exporters. [More...](class_n_f_exporter.html#details)

##  Public Member Functions  
  
---  
[NFTemplate](struct_n_f_template.html) | [getTemplateById](class_n_f_exporter.html#ac197dd6772fa8b99949247840e06c7e4) (int)  
| Returns the NetFlow template with the specified ID. [More...](class_n_f_exporter.html#ac197dd6772fa8b99949247840e06c7e4)  
  
[NFTemplate](struct_n_f_template.html) | [getTemplateByRecordName](class_n_f_exporter.html#aeb5d05938881869dffaf0dbfeb5d9610) (string)  
| Returns the NetFlow template with the specified record name. [More...](class_n_f_exporter.html#aeb5d05938881869dffaf0dbfeb5d9610)  
  
bool | [removeTemplate](class_n_f_exporter.html#ae0a2a8a4a9abf0c325e62102b37d94c8) (int)  
| Removes the NetFlow template with the specified ID. [More...](class_n_f_exporter.html#ae0a2a8a4a9abf0c325e62102b37d94c8)  
  
void | [setExporterName](class_n_f_exporter.html#ae484ba4906c5750903404b39c97f308a) (string)  
| Sets the name for the NetFlow exporter. [More...](class_n_f_exporter.html#ae484ba4906c5750903404b39c97f308a)  
  
string | [getExporterName](class_n_f_exporter.html#a22b68b6577dde9a26e9c60194cf875bd) ()  
| Returns the name of the NetFlow exporter. [More...](class_n_f_exporter.html#a22b68b6577dde9a26e9c60194cf875bd)  
  
void | [setExporterVersion](class_n_f_exporter.html#a44bae95d49b29f41cabab57cb5b8b2cd) (int)  
| Sets the version for the NetFlow exporter. [More...](class_n_f_exporter.html#a44bae95d49b29f41cabab57cb5b8b2cd)  
  
int | [getExporterVersion](class_n_f_exporter.html#add53e7f379ea80945751ebd46f3d752a) ()  
| Returns the version of the NetFlow exporter. [More...](class_n_f_exporter.html#add53e7f379ea80945751ebd46f3d752a)  
  
long | [getDeviceUpTime](class_n_f_exporter.html#a8d1261e760a81d69a60008ce611c48f0) ()  
| Returns the device up time. [More...](class_n_f_exporter.html#a8d1261e760a81d69a60008ce611c48f0)  
  
bool | [isFullyConfigured](class_n_f_exporter.html#ae0eaf2321debcda0a389260077428c29) ()  
| Returns true if the NetFlow exporter is fully configured, otherwise false. [More...](class_n_f_exporter.html#ae0eaf2321debcda0a389260077428c29)  
  
void | [setSrcPort](class_n_f_exporter.html#aa37fbccdf0e777e973e11de9e2bad7f4) (string)  
| Sets the source port. [More...](class_n_f_exporter.html#aa37fbccdf0e777e973e11de9e2bad7f4)  
  
[Port](class_port.html) | [getSrcPort](class_n_f_exporter.html#a424568cc98103496ee50a29f9c5ec6e1) ()  
| Returns the source port. [More...](class_n_f_exporter.html#a424568cc98103496ee50a29f9c5ec6e1)  
  
void | [setDestinationAddr](class_n_f_exporter.html#af7f9dee28f28f7139a4e7d203efbec7b) (ip)  
| Sets the destination IP address. [More...](class_n_f_exporter.html#af7f9dee28f28f7139a4e7d203efbec7b)  
  
ip | [getDestinationAddr](class_n_f_exporter.html#addf33e5a5b63bdaae89981867be95439) ()  
| Returns the destination IP address. [More...](class_n_f_exporter.html#addf33e5a5b63bdaae89981867be95439)  
  
void | [setDestinationUdpPort](class_n_f_exporter.html#a8d32ddb19b60fbb5ed134e9a0f60c4da) (int)  
| Sets the destination UDP port number. [More...](class_n_f_exporter.html#a8d32ddb19b60fbb5ed134e9a0f60c4da)  
  
int | [getDestinationUdpPort](class_n_f_exporter.html#a343e84c94eaaf0150681f3095be61420) ()  
| Returns the destination UDP port number. [More...](class_n_f_exporter.html#a343e84c94eaaf0150681f3095be61420)  
  
void | [addMonitor](class_n_f_exporter.html#a9ef72f2db32b526a1900655265a8114f) (string)  
| Adds a monitor with the specified name. [More...](class_n_f_exporter.html#a9ef72f2db32b526a1900655265a8114f)  
  
void | [removeMontior](class_n_f_exporter.html#a17e5c1495f6bb535a01dc74d3a8c5c17) (string)  
| Removes the monitor with the specified name. [More...](class_n_f_exporter.html#a17e5c1495f6bb535a01dc74d3a8c5c17)  
  
[FrameInstance](class_frame_instance.html) | [createFrameInstance](class_n_f_exporter.html#a07132dd7ac41d617b3b24bb32cef42e1) ()  
| Creates a frame instance. [More...](class_n_f_exporter.html#a07132dd7ac41d617b3b24bb32cef42e1)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[NFExporter](class_n_f_exporter.html "NFExporter handles and manipulates NetFlow exporters.") handles and manipulates NetFlow exporters. 

## Member Function Documentation

## ◆ addMonitor()

void NFExporter::addMonitor  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Adds a monitor with the specified name. 

Parameters
     monitorName,the| name for the monitor.   
---|---  
  
## ◆ createFrameInstance()

[FrameInstance](class_frame_instance.html) NFExporter::createFrameInstance  | ( | | ) |   
---|---|---|---|---  
  
Creates a frame instance. 

Returns
    [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc."), the [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") object of the frame instance. 

## ◆ getDestinationAddr()

ip NFExporter::getDestinationAddr  | ( | | ) |   
---|---|---|---|---  
  
Returns the destination IP address. 

Returns
    ip, the IP address of the destination. 

## ◆ getDestinationUdpPort()

int NFExporter::getDestinationUdpPort  | ( | | ) |   
---|---|---|---|---  
  
Returns the destination UDP port number. 

Returns
    int, the UDP port number of the destination. 

## ◆ getDeviceUpTime()

long NFExporter::getDeviceUpTime  | ( | | ) |   
---|---|---|---|---  
  
Returns the device up time. 

Returns
    int, the device up time. 

## ◆ getExporterName()

string NFExporter::getExporterName  | ( | | ) |   
---|---|---|---|---  
  
Returns the name of the NetFlow exporter. 

Returns
    string, the name of the NetFlow exporter. 

## ◆ getExporterVersion()

int NFExporter::getExporterVersion  | ( | | ) |   
---|---|---|---|---  
  
Returns the version of the NetFlow exporter. 

Returns
    int, the version of the NetFlow exporter. 

## ◆ getSrcPort()

[Port](class_port.html) NFExporter::getSrcPort  | ( | | ) |   
---|---|---|---|---  
  
Returns the source port. 

Returns
    [Port](class_port.html "Port holds and manipulates the ports on devices."), the [Port](class_port.html "Port holds and manipulates the ports on devices.") object of the source port. 

## ◆ getTemplateById()

[NFTemplate](struct_n_f_template.html) NFExporter::getTemplateById  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the NetFlow template with the specified ID. 

Parameters
     id,the| ID of the NetFlow template of interest.  
---|---  
  
Returns
    [NFTemplate](struct_n_f_template.html "NetFlow template flow structure."), the [NFTemplate](struct_n_f_template.html "NetFlow template flow structure.") object with the specified ID. 

## ◆ getTemplateByRecordName()

[NFTemplate](struct_n_f_template.html) NFExporter::getTemplateByRecordName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the NetFlow template with the specified record name. 

Parameters
     recordName,the| record name of the NetFlow template of interest.  
---|---  
  
Returns
    [NFTemplate](struct_n_f_template.html "NetFlow template flow structure."), the [NFTemplate](struct_n_f_template.html "NetFlow template flow structure.") object with the specified record name. 

## ◆ isFullyConfigured()

bool NFExporter::isFullyConfigured  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the NetFlow exporter is fully configured, otherwise false. 

Returns
    bool, true if the NetFlow exporter is fully configured, otherwise false. 

## ◆ removeMontior()

void NFExporter::removeMontior  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes the monitor with the specified name. 

Parameters
     monitorName,the| name of the monitor of interest.   
---|---  
  
## ◆ removeTemplate()

bool NFExporter::removeTemplate  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Removes the NetFlow template with the specified ID. 

Parameters
     templateId,the| ID of the NetFlow template of interest.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ setDestinationAddr()

void NFExporter::setDestinationAddr  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Sets the destination IP address. 

Parameters
     ip_add,the| IP address of the destination.   
---|---  
  
## ◆ setDestinationUdpPort()

void NFExporter::setDestinationUdpPort  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the destination UDP port number. 

Parameters
     port,the| UDP port number for the destination.   
---|---  
  
## ◆ setExporterName()

void NFExporter::setExporterName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the name for the NetFlow exporter. 

Parameters
     name,the| name for the NetFlow exporter.   
---|---  
  
## ◆ setExporterVersion()

void NFExporter::setExporterVersion  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the version for the NetFlow exporter. 

Parameters
     version,the| version for the NetFlow exporter.   
---|---  
  
## ◆ setSrcPort()

void NFExporter::setSrcPort  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the source port. 

Parameters
     port,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CNFExporter.pki](_c_n_f_exporter_8pki.html)


