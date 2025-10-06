# Cisco Packet Tracer Extensions API: IpcManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_ipc_manager.html

---

[IpcManager](class_ipc_manager.html "IpcManager serves as the entry point for the IPC and manages ExApps and Script Modules.") serves as the entry point for the [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") and manages ExApps and Script Modules. [More...](class_ipc_manager.html#details)

##  Public Member Functions  
  
---  
int | [getListeningPort](class_ipc_manager.html#a1a667b1ed7bf5ae53ff062cf72c9351f) ()  
| Returns the listening port for [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality."). [More...](class_ipc_manager.html#a1a667b1ed7bf5ae53ff062cf72c9351f)  
  
bool | [launchCep](class_ipc_manager.html#adab026b3662b75ffcae93225c5f36a3c) (string)  
| Launches the ExApp with the specified ID. [More...](class_ipc_manager.html#adab026b3662b75ffcae93225c5f36a3c)  
  
bool | [setExclusive](class_ipc_manager.html#ab216200b8705c18c2c194b4135d119f2) (bool)  
| Disconnects all other external processes and locks new connections to this external process' ID only. [More...](class_ipc_manager.html#ab216200b8705c18c2c194b4135d119f2)  
  
bool | [putSaveData](class_ipc_manager.html#ab585d3674390b3ca95e7e3439895d137) (uuid, QString)  
| Saves data with the specified UUID. [More...](class_ipc_manager.html#ab585d3674390b3ca95e7e3439895d137)  
  
QString | [getOpenData](class_ipc_manager.html#ac93dddfa6008e652d43d5858c50a9355) (uuid)  
| Returns the save data with the specified UUID. [More...](class_ipc_manager.html#ac93dddfa6008e652d43d5858c50a9355)  
  
[CepInstance](class_cep_instance.html) | [thisInstance](class_ipc_manager.html#a23c12f55cd82a0c74dc285ac1cacbcad) ()  
| Returns the [CepInstance](class_cep_instance.html "CepInstance is the external process \(ExApp and Script Module\) that communicates with Packet Tracer th...") object for this instance. [More...](class_ipc_manager.html#a23c12f55cd82a0c74dc285ac1cacbcad)  
  
bool | [sendMessageTo](class_ipc_manager.html#af8d3479dea1ad007378e0c972536a6a9) (string, QString)  
| Sends a message to the local instance with the specified ID. [More...](class_ipc_manager.html#af8d3479dea1ad007378e0c972536a6a9)  
  
bool | [sendMessageToInstance](class_ipc_manager.html#a7c15fe44434a4f05df93771469808d88) (uuid, QString)  
| Sends a message to the local instance with the specified UUID. [More...](class_ipc_manager.html#a7c15fe44434a4f05df93771469808d88)  
  
bool | [sendMessageToAll](class_ipc_manager.html#a4f7297487d76ab454a579dca2d43c3dc) (QString)  
| Sends a message to all instances. [More...](class_ipc_manager.html#a4f7297487d76ab454a579dca2d43c3dc)  
  
bool | [sendMessageToRemote](class_ipc_manager.html#acc6aee89aa72f9adf64ffe8c0d363870) (string, QString)  
| Sends a message to the remote instance with the specified ID. [More...](class_ipc_manager.html#acc6aee89aa72f9adf64ffe8c0d363870)  
  
bool | [sendMessageToRemoteInstance](class_ipc_manager.html#aa9ac6fb8d1cbb8a8c85eb5cae84c6643) (uuid, QString)  
| Sends a message to the remote instance with the specified UUID. [More...](class_ipc_manager.html#aa9ac6fb8d1cbb8a8c85eb5cae84c6643)  
  
void | [onSave](class_ipc_manager.html#ac3988f3a3ab61d616d584e67731a1b72) (uuid)  
| This event is emitted when data is saved. [More...](class_ipc_manager.html#ac3988f3a3ab61d616d584e67731a1b72)  
  
void | [onOpen](class_ipc_manager.html#a004501b45af445ce1604806eaae8ebf8) (uuid, QString)  
| This event is emitted when data is opened. [More...](class_ipc_manager.html#a004501b45af445ce1604806eaae8ebf8)  
  
void | [onOpening](class_ipc_manager.html#a0e9268cb7856d53810b660655ed9ea2f) (uuid, QString)  
| This event is emitted when file is being opened. The ExApp or script module has access to the data at this point but should wait til the onOpen event for the file to be opened completely. [More...](class_ipc_manager.html#a0e9268cb7856d53810b660655ed9ea2f)  
  
bool | [registerOpenFileType](class_ipc_manager.html#aa7eb84093a3ea2bbbf1d41bc5efad2a9) (QString)  
| Register a file extension to be opened by this CEP instance if the file is opened from PT GUI or OS. [More...](class_ipc_manager.html#aa7eb84093a3ea2bbbf1d41bc5efad2a9)  
  
bool | [unregisterOpenFileType](class_ipc_manager.html#ae837c154ba7cf509c2c2d00f96bbc2a9) (QString)  
| Unregister a file extension to be opened by this CEP instance if the file is opened from PT GUI or OS. [More...](class_ipc_manager.html#ae837c154ba7cf509c2c2d00f96bbc2a9)  
  
  
## Detailed Description

[IpcManager](class_ipc_manager.html "IpcManager serves as the entry point for the IPC and manages ExApps and Script Modules.") serves as the entry point for the [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") and manages ExApps and Script Modules. 

## Member Function Documentation

## ◆ getListeningPort()

int IpcManager::getListeningPort  | ( | | ) |   
---|---|---|---|---  
  
Returns the listening port for [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality."). 

Returns
    int, the listening port for [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality."). 

## ◆ getOpenData()

QString IpcManager::getOpenData  | ( | uuid  | | ) |   
---|---|---|---|---|---  
  
Returns the save data with the specified UUID. 

Parameters
     openId,the| UUID of the save data.  
---|---  
  
Returns
    QString, the save data with the specified UUID. 

## ◆ launchCep()

bool IpcManager::launchCep  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Launches the ExApp with the specified ID. 

Parameters
     cepId,the| ID of the external process.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ onOpen()

void IpcManager::onOpen  | ( | uuid  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
This event is emitted when data is opened. 

  * openId, the UUID of the data. 
  * openData, the data.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ onOpening()

void IpcManager::onOpening  | ( | uuid  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
This event is emitted when file is being opened. The ExApp or script module has access to the data at this point but should wait til the onOpen event for the file to be opened completely. 

  * openId, the UUID of the data. 
  * openData, the data.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ onSave()

void IpcManager::onSave  | ( | uuid  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when data is saved. 

  * saveId, the UUID of the data.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ putSaveData()

bool IpcManager::putSaveData  | ( | uuid  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Saves data with the specified UUID. 

Parameters
     saveId,the| UUID of the save data.   
---|---  
saveData,the| data to save.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ registerOpenFileType()

bool IpcManager::registerOpenFileType  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Register a file extension to be opened by this CEP instance if the file is opened from PT GUI or OS. 

  * fileExtension, the extenstion to register



Returns
    bool, true if successful, otherwise false. 

## ◆ sendMessageTo()

bool IpcManager::sendMessageTo  | ( | string  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Sends a message to the local instance with the specified ID. 

\paran cepId, the ID of the local instance. \paran msg, the message to send.

Returns
    bool, true if successful, otherwise false. 

## ◆ sendMessageToAll()

bool IpcManager::sendMessageToAll  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Sends a message to all instances. 

\paran msg, the message to send.

Returns
    bool, true if successful, otherwise false. 

## ◆ sendMessageToInstance()

bool IpcManager::sendMessageToInstance  | ( | uuid  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Sends a message to the local instance with the specified UUID. 

\paran cepInstanceId, the UUID of the local instance. \paran msg, the message to send.

Returns
    bool, true if successful, otherwise false. 

## ◆ sendMessageToRemote()

bool IpcManager::sendMessageToRemote  | ( | string  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Sends a message to the remote instance with the specified ID. 

Parameters
     cepId,the| ID of the remote instance. \paran msg, the message to send.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ sendMessageToRemoteInstance()

bool IpcManager::sendMessageToRemoteInstance  | ( | uuid  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Sends a message to the remote instance with the specified UUID. 

Parameters
     cepInstanceId,the| UUID of the remote instance. \paran msg, the message to send.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ setExclusive()

bool IpcManager::setExclusive  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Disconnects all other external processes and locks new connections to this external process' ID only. 

Parameters
     exclusive,true| to disconnect all external processes of different IDs, false to allow new connections from other external processes.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ thisInstance()

[CepInstance](class_cep_instance.html) IpcManager::thisInstance  | ( | | ) |   
---|---|---|---|---  
  
Returns the [CepInstance](class_cep_instance.html "CepInstance is the external process \(ExApp and Script Module\) that communicates with Packet Tracer th...") object for this instance. 

Returns
    [CepInstance](class_cep_instance.html "CepInstance is the external process \(ExApp and Script Module\) that communicates with Packet Tracer th..."), the [CepInstance](class_cep_instance.html "CepInstance is the external process \(ExApp and Script Module\) that communicates with Packet Tracer th...") object for this instance. 

## ◆ unregisterOpenFileType()

bool IpcManager::unregisterOpenFileType  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Unregister a file extension to be opened by this CEP instance if the file is opened from PT GUI or OS. 

  * fileExtension, the extenstion to unregister



Returns
    bool, true if successful, otherwise false. 

* * *

The documentation for this class was generated from the following file:

  * [CIpcManager.pki](_c_ipc_manager_8pki.html)


