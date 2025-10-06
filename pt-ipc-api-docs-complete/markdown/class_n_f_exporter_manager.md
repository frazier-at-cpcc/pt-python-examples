# Cisco Packet Tracer Extensions API: NFExporterManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_n_f_exporter_manager.html

---

[NFExporterManager](class_n_f_exporter_manager.html "NFExporterManager manages different NetFlow exporters configured on routers.") manages different NetFlow exporters configured on routers. [More...](class_n_f_exporter_manager.html#details)

##  Public Member Functions  
  
---  
[NFExporter](class_n_f_exporter.html) | [createNFExporter](class_n_f_exporter_manager.html#a811a308cef5f59b502a8dabe547a84ab) (string)  
| Creates a NetFlow exporter with the specified name. [More...](class_n_f_exporter_manager.html#a811a308cef5f59b502a8dabe547a84ab)  
  
void | [removeNFExporter](class_n_f_exporter_manager.html#a4197876f426ef369e4600c7971d99d3d) (string)  
| Removes the NetFlow exporter with the specified name. [More...](class_n_f_exporter_manager.html#a4197876f426ef369e4600c7971d99d3d)  
  
[NFExporter](class_n_f_exporter.html) | [getNFExporterAt](class_n_f_exporter_manager.html#a351c80e713f7d2c2dd3b7cf3edb3802f) (int)  
| Returns the NetFlow exporter at the specified index. [More...](class_n_f_exporter_manager.html#a351c80e713f7d2c2dd3b7cf3edb3802f)  
  
[NFExporter](class_n_f_exporter.html) | [getNFExporterByName](class_n_f_exporter_manager.html#aa1c250b22b79f6ae0a12e183e30a00e8) (string)  
| Returns the NetFlow exporter with the specified name. [More...](class_n_f_exporter_manager.html#aa1c250b22b79f6ae0a12e183e30a00e8)  
  
[NFExporter](class_n_f_exporter.html) | [getNFExporterByIpAndPort](class_n_f_exporter_manager.html#a3264495b536f97a9f5da5a2e9aec9c85) (ip, int)  
| Returns the NetFlow exporter with the specified IP address and UDP port number. [More...](class_n_f_exporter_manager.html#a3264495b536f97a9f5da5a2e9aec9c85)  
  
void | [removeNFExporterAt](class_n_f_exporter_manager.html#aaf0add90e78f6699ae4118afb3b37633) (int)  
| Removes the NetFlow exporter at the specified index. [More...](class_n_f_exporter_manager.html#aaf0add90e78f6699ae4118afb3b37633)  
  
int | [getNFExporterCount](class_n_f_exporter_manager.html#a72e26ac56c59b6f3799984a577c45336) ()  
| Returns the number of NetFlow exporters. [More...](class_n_f_exporter_manager.html#a72e26ac56c59b6f3799984a577c45336)  
  
  
## Detailed Description

[NFExporterManager](class_n_f_exporter_manager.html "NFExporterManager manages different NetFlow exporters configured on routers.") manages different NetFlow exporters configured on routers. 

## Member Function Documentation

## ◆ createNFExporter()

[NFExporter](class_n_f_exporter.html) NFExporterManager::createNFExporter  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Creates a NetFlow exporter with the specified name. 

Parameters
     exporterName,the| name for the NetFlow exporter.  
---|---  
  
Returns
    [NFExporter](class_n_f_exporter.html "NFExporter handles and manipulates NetFlow exporters."), the [NFExporter](class_n_f_exporter.html "NFExporter handles and manipulates NetFlow exporters.") object of the created NetFlow exporter. 

## ◆ getNFExporterAt()

[NFExporter](class_n_f_exporter.html) NFExporterManager::getNFExporterAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the NetFlow exporter at the specified index. 

Parameters
     index,the| index of the NetFlow exporter of interest.  
---|---  
  
Returns
    [NFExporter](class_n_f_exporter.html "NFExporter handles and manipulates NetFlow exporters."), the [NFExporter](class_n_f_exporter.html "NFExporter handles and manipulates NetFlow exporters.") object at the specified index. 

## ◆ getNFExporterByIpAndPort()

[NFExporter](class_n_f_exporter.html) NFExporterManager::getNFExporterByIpAndPort  | ( | ip  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Returns the NetFlow exporter with the specified IP address and UDP port number. 

Parameters
     ipAddr,the| IP address of the NetFlow exporter of interest.   
---|---  
udpPort,the| UDP port number of the NetFlow exporter of interest.  
  
Returns
    [NFExporter](class_n_f_exporter.html "NFExporter handles and manipulates NetFlow exporters."), the [NFExporter](class_n_f_exporter.html "NFExporter handles and manipulates NetFlow exporters.") object with the specified name. 

## ◆ getNFExporterByName()

[NFExporter](class_n_f_exporter.html) NFExporterManager::getNFExporterByName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the NetFlow exporter with the specified name. 

Parameters
     name,the| name of the NetFlow exporter of interest.  
---|---  
  
Returns
    [NFExporter](class_n_f_exporter.html "NFExporter handles and manipulates NetFlow exporters."), the [NFExporter](class_n_f_exporter.html "NFExporter handles and manipulates NetFlow exporters.") object with the specified name. 

## ◆ getNFExporterCount()

int NFExporterManager::getNFExporterCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of NetFlow exporters. 

Returns
    int, the number of NetFlow exporters. 

## ◆ removeNFExporter()

void NFExporterManager::removeNFExporter  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes the NetFlow exporter with the specified name. 

Parameters
     exporterName,the| name of the NetFlow exporter of interest.   
---|---  
  
## ◆ removeNFExporterAt()

void NFExporterManager::removeNFExporterAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Removes the NetFlow exporter at the specified index. 

Parameters
     index,the| index of the NetFlow exporter of interest.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CNFExporterManager.pki](_c_n_f_exporter_manager_8pki.html)


