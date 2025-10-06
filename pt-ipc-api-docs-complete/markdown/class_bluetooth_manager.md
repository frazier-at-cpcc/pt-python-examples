# Cisco Packet Tracer Extensions API: BluetoothManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_bluetooth_manager.html

---

[BluetoothManager](class_bluetooth_manager.html "BluetoothManager."). [More...](class_bluetooth_manager.html#details)

##  Public Member Functions  
  
---  
void | [setDiscoverable](class_bluetooth_manager.html#a8e27c1ed639661c83dfdefe5f42af516) (bool)  
bool | [isDiscoverable](class_bluetooth_manager.html#ac42bee7b6ff7b86170fa3d1b5548e75b) ()  
void | [discover](class_bluetooth_manager.html#a65a3cbe31f2747b40869785452a3b29e) ()  
void | [deviceDiscovered](class_bluetooth_manager.html#ab4b14d99b3abc33d4d5ed8be648ebcf1) (mac, QString)  
| [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. [More...](class_bluetooth_manager.html#ab4b14d99b3abc33d4d5ed8be648ebcf1)  
  
void | [pair](class_bluetooth_manager.html#af6cd8718221a2e33d98380ec130c6f99) (mac)  
void | [acceptPairRequest](class_bluetooth_manager.html#a71073acf4d392e671ab61ee8a31ba963) (mac, QString)  
void | [unpair](class_bluetooth_manager.html#a658331ae80b399dca0ffb2f6c88e54ae) (mac)  
bool | [processPairRequest](class_bluetooth_manager.html#a6fd3bf4a0712dc0dbb4a80a9c0307fd6) (mac, QString)  
void | [devicePaired](class_bluetooth_manager.html#a7f1b4ad0c68ec9dbc4ed91b9b37ea852) (mac)  
| [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. [More...](class_bluetooth_manager.html#a7f1b4ad0c68ec9dbc4ed91b9b37ea852)  
  
void | [deviceUnpaired](class_bluetooth_manager.html#a06e27ad97207db6234c4406a920a6016) (mac)  
| [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. [More...](class_bluetooth_manager.html#a06e27ad97207db6234c4406a920a6016)  
  
void | [deviceConnected](class_bluetooth_manager.html#aa872f8386ec717ef36a744412f311176) (mac)  
| [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. [More...](class_bluetooth_manager.html#aa872f8386ec717ef36a744412f311176)  
  
void | [deviceDisconnected](class_bluetooth_manager.html#a170d38a059b9b7fcb85e875ef0cce9e5) (mac)  
| [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. [More...](class_bluetooth_manager.html#a170d38a059b9b7fcb85e875ef0cce9e5)  
  
int | [getDeviceCount](class_bluetooth_manager.html#a7f9b2ee40e40de5f564420a9a3151c59) ()  
[BluetoothDevice](struct_bluetooth_device.html) | [getDeviceAt](class_bluetooth_manager.html#aa719a730e0c060c84ab0a07904ec1a6c) (int)  
[BluetoothDevice](struct_bluetooth_device.html) | [getDevice](class_bluetooth_manager.html#a15cdd4369660dba1c00127362445b45a) (mac)  
[BluetoothDevice](struct_bluetooth_device.html) | [getDeviceByName](class_bluetooth_manager.html#ad99a58af93a5098d8de45edf80f3a034) (QString)  
void | [enableBroadcast](class_bluetooth_manager.html#a154bad99badf4228cae0bf7fbcfb993e) (bool)  
bool | [isBroadcastEnabled](class_bluetooth_manager.html#ad4f58a8251cf13a93dbaa2da977b0a69) ()  
void | [setBeaconBroadcasting](class_bluetooth_manager.html#a4c5eeaf474b4b1372825ee4fb6b60cca) (bool)  
bool | [isBeaconBroadcasting](class_bluetooth_manager.html#aea0505ef43e0eb678542970a8ff8370d) ()  
void | [setBeaconFrequency](class_bluetooth_manager.html#ad7dc8026fff34a71deba83e190ed4157) (int)  
int | [getBeaconFrequency](class_bluetooth_manager.html#a4ab27d6e50cbc86a9b397ef33fbe8742) ()  
void | [setBeaconUuid](class_bluetooth_manager.html#a22575936e9ddbe412135403ba45e1d0c) (uuid)  
uuid | [getBeaconUuid](class_bluetooth_manager.html#a6fb927dc6e85472d810dce3bff0329af) ()  
void | [setBeaconData](class_bluetooth_manager.html#afa980d1e5cdeab399aba73d1060bc52d) (QString)  
QString | [getBeaconData](class_bluetooth_manager.html#ab274a2457f871bca7c7b1fa60af6dec8) ()  
bool | [broadcastBeacon](class_bluetooth_manager.html#a013a037942206799efd9364936b1d654) (uuid, QString)  
[CustomBluetoothProcess](class_custom_bluetooth_process.html) | [createCustomProcess](class_bluetooth_manager.html#a29bdad336d82bd350118fb4a5ae6faaa) ()  
void | [deleteCustomProcess](class_bluetooth_manager.html#a03ddc5ee8c431babe31f408c2bf663ef) ([CustomBluetoothProcess](class_custom_bluetooth_process.html))  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[BluetoothManager](class_bluetooth_manager.html "BluetoothManager."). 

## Member Function Documentation

## ◆ acceptPairRequest()

void BluetoothManager::acceptPairRequest  | ( | mac  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
## ◆ broadcastBeacon()

bool BluetoothManager::broadcastBeacon  | ( | uuid  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
## ◆ createCustomProcess()

[CustomBluetoothProcess](class_custom_bluetooth_process.html) BluetoothManager::createCustomProcess  | ( | | ) |   
---|---|---|---|---  
  
## ◆ deleteCustomProcess()

void BluetoothManager::deleteCustomProcess  | ( | [CustomBluetoothProcess](class_custom_bluetooth_process.html) | | ) |   
---|---|---|---|---|---  
  
## ◆ deviceConnected()

void BluetoothManager::deviceConnected  | ( | mac  | | ) |   
---|---|---|---|---|---  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ deviceDisconnected()

void BluetoothManager::deviceDisconnected  | ( | mac  | | ) |   
---|---|---|---|---|---  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ deviceDiscovered()

void BluetoothManager::deviceDiscovered  | ( | mac  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ devicePaired()

void BluetoothManager::devicePaired  | ( | mac  | | ) |   
---|---|---|---|---|---  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ deviceUnpaired()

void BluetoothManager::deviceUnpaired  | ( | mac  | | ) |   
---|---|---|---|---|---  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ discover()

void BluetoothManager::discover  | ( | | ) |   
---|---|---|---|---  
  
## ◆ enableBroadcast()

void BluetoothManager::enableBroadcast  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
## ◆ getBeaconData()

QString BluetoothManager::getBeaconData  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getBeaconFrequency()

int BluetoothManager::getBeaconFrequency  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getBeaconUuid()

uuid BluetoothManager::getBeaconUuid  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getDevice()

[BluetoothDevice](struct_bluetooth_device.html) BluetoothManager::getDevice  | ( | mac  | | ) |   
---|---|---|---|---|---  
  
## ◆ getDeviceAt()

[BluetoothDevice](struct_bluetooth_device.html) BluetoothManager::getDeviceAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
## ◆ getDeviceByName()

[BluetoothDevice](struct_bluetooth_device.html) BluetoothManager::getDeviceByName  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
## ◆ getDeviceCount()

int BluetoothManager::getDeviceCount  | ( | | ) |   
---|---|---|---|---  
  
## ◆ isBeaconBroadcasting()

bool BluetoothManager::isBeaconBroadcasting  | ( | | ) |   
---|---|---|---|---  
  
## ◆ isBroadcastEnabled()

bool BluetoothManager::isBroadcastEnabled  | ( | | ) |   
---|---|---|---|---  
  
## ◆ isDiscoverable()

bool BluetoothManager::isDiscoverable  | ( | | ) |   
---|---|---|---|---  
  
## ◆ pair()

void BluetoothManager::pair  | ( | mac  | | ) |   
---|---|---|---|---|---  
  
## ◆ processPairRequest()

bool BluetoothManager::processPairRequest  | ( | mac  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
## ◆ setBeaconBroadcasting()

void BluetoothManager::setBeaconBroadcasting  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
## ◆ setBeaconData()

void BluetoothManager::setBeaconData  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
## ◆ setBeaconFrequency()

void BluetoothManager::setBeaconFrequency  | ( | int  | | ) |   
---|---|---|---|---|---  
  
## ◆ setBeaconUuid()

void BluetoothManager::setBeaconUuid  | ( | uuid  | | ) |   
---|---|---|---|---|---  
  
## ◆ setDiscoverable()

void BluetoothManager::setDiscoverable  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
## ◆ unpair()

void BluetoothManager::unpair  | ( | mac  | | ) |   
---|---|---|---|---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CBluetoothManager.pki](_c_bluetooth_manager_8pki.html)


