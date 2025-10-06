# Cisco Packet Tracer Extensions API: DeviceDescriptor Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_device_descriptor.html

---

Descriptor for a device. [More...](class_device_descriptor.html#details)

##  Public Member Functions  
  
---  
DeviceType | [getType](class_device_descriptor.html#a9b2554fa8538c06fd7bffccc621ede31) ()  
| Return device type. [More...](class_device_descriptor.html#a9b2554fa8538c06fd7bffccc621ede31)  
  
string | [getModel](class_device_descriptor.html#aee7d08ba4b4446b67eb92b9819eecfab) ()  
| Get device model. [More...](class_device_descriptor.html#aee7d08ba4b4446b67eb92b9819eecfab)  
  
void | [addSupportedModuleType](class_device_descriptor.html#aae0c2e505314e84fce4c47f6154a69fc) (ModuleType)  
| Add supported module type to device descriptor. [More...](class_device_descriptor.html#aae0c2e505314e84fce4c47f6154a69fc)  
  
void | [removeSupportedModuleType](class_device_descriptor.html#a1dc0b0348a4e6dda76858eb1ffa974de) (ModuleType)  
| Remove supported module type to device descriptor. [More...](class_device_descriptor.html#a1dc0b0348a4e6dda76858eb1ffa974de)  
  
bool | [isModuleTypeSupported](class_device_descriptor.html#a8292b4054647c85fd25b6fc819953f50) (ModuleType)  
| Check if module type is supported. [More...](class_device_descriptor.html#a8292b4054647c85fd25b6fc819953f50)  
  
int | [getSupportedModuleTypeCount](class_device_descriptor.html#a338e6ad80521b051cbdb9ff6df5b3315) ()  
| Get the number of module type. [More...](class_device_descriptor.html#a338e6ad80521b051cbdb9ff6df5b3315)  
  
ModuleType | [getSupportedModuleTypeAt](class_device_descriptor.html#a01a23bd17d3200a51e236f3e51140a9c) (int)  
| Get the supported module type at a specified index. [More...](class_device_descriptor.html#a01a23bd17d3200a51e236f3e51140a9c)  
  
[ModuleDescriptor](class_module_descriptor.html) | [getRootModule](class_device_descriptor.html#a00373cd10c44e4364ea474ae32b631c5) ()  
| Get the root module descriptor. [More...](class_device_descriptor.html#a00373cd10c44e4364ea474ae32b631c5)  
  
bool | [isModelSupported](class_device_descriptor.html#af22eefbc73c16e586220ad3507b4d3d7) ()  
| Check if the descriptor is model supported. [More...](class_device_descriptor.html#af22eefbc73c16e586220ad3507b4d3d7)  
  
int | [getSpecifiedModelCount](class_device_descriptor.html#a342c4f8c18598da22e447a1c0297fd52) ()  
| Get specified model count. [More...](class_device_descriptor.html#a342c4f8c18598da22e447a1c0297fd52)  
  
string | [getSpecifiedModelAt](class_device_descriptor.html#a2f5a49c4c3dd9b0109d9592afa4a6248) (int)  
| Get specified model at a specified index. [More...](class_device_descriptor.html#a2f5a49c4c3dd9b0109d9592afa4a6248)  
  
bool | [isExistSpecifiedModel](class_device_descriptor.html#a44db948aef6bec9ba48c03f531da6734) (string)  
| Check if the model exist. [More...](class_device_descriptor.html#a44db948aef6bec9ba48c03f531da6734)  
  
void | [addSpecifiedModel](class_device_descriptor.html#a1547df31dba7c83fda58e3a3bb484791) (string)  
| Add module model to support. [More...](class_device_descriptor.html#a1547df31dba7c83fda58e3a3bb484791)  
  
void | [removeSpecifiedModel](class_device_descriptor.html#a37f855d7fe6500cbeb1462e170243e0f) (string)  
| Remove model model to support. [More...](class_device_descriptor.html#a37f855d7fe6500cbeb1462e170243e0f)  
  
void | [setModelSupportedFlag](class_device_descriptor.html#a31eedd1578defdf256e3c9fc994fb9e5) (bool)  
| Set supported flag to the device descriptor. [More...](class_device_descriptor.html#a31eedd1578defdf256e3c9fc994fb9e5)  
  
void | [addRequiredScriptModule](class_device_descriptor.html#a5e8113cf04db9669f8b50a30b8c0dd76) (string)  
| Add required script module. [More...](class_device_descriptor.html#a5e8113cf04db9669f8b50a30b8c0dd76)  
  
void | [removeRequiredScriptModule](class_device_descriptor.html#ad0599779c4efa01f9929b4aa148de2f1) (string)  
| Removed required script module. [More...](class_device_descriptor.html#ad0599779c4efa01f9929b4aa148de2f1)  
  
int | [getRequiredScriptModuleCount](class_device_descriptor.html#ac70e67e80dc401d5c1e316235cd58269) ()  
| Get the number of required script module. [More...](class_device_descriptor.html#ac70e67e80dc401d5c1e316235cd58269)  
  
string | [getRequiredScriptModuleAt](class_device_descriptor.html#a4636916eeeb63f3cc69dad7b9200fb7e) (int)  
| Get the name of the required script module at a specified index. [More...](class_device_descriptor.html#a4636916eeeb63f3cc69dad7b9200fb7e)  
  
  
## Detailed Description

Descriptor for a device. 

## Member Function Documentation

## ◆ addRequiredScriptModule()

void DeviceDescriptor::addRequiredScriptModule  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Add required script module. 

Parameters
     smId,script| module id  
---|---  
  
Returns
    none 

## ◆ addSpecifiedModel()

void DeviceDescriptor::addSpecifiedModel  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Add module model to support. 

Parameters
     model,specified| model   
---|---  
  
## ◆ addSupportedModuleType()

void DeviceDescriptor::addSupportedModuleType  | ( | ModuleType  | | ) |   
---|---|---|---|---|---  
  
Add supported module type to device descriptor. 

Parameters
     type,module| type enum<ModuleType>, start with 0 and add 1 to subsequent module type eLineCard=0, // Line card eNetworkModule, // [Network](class_network.html "Network is the entry point for all device configurations in the network. It retrieves devices.") module eInterfaceCard, // Interface card ePtRouterModule, // Packet Tracer router module ePtSwitchModule, // Packet Tracer switch module ePtCloudModule, // Packet Tracer cloud module ePtRepeaterModule, // Packet Tracer repeater module ePtHostModule, // Packet Tracer host module ePtModemModule, ePtLaptopModule, ePtTVModule, eIpPhonePowerAdapter, ePtTabletPCModule, ePtPdaModule, ePtWirelessEndDeviceModule, ePtWiredEndDeviceModule, eTrs35, eUsb, eNonRemovableModule, // Non-removable module eASAModule, eASAPowerAdapter, ePtCellTowerModule, ePtIoeModule, ePtIoeNetworkModule, ePtIoeAnalogModule, ePtIoeDigitalModule, ePtIoeCustomIOModule, ePtIoePowerAdapter, ePtIoeMcuComponentPowerAdapter, ePtRouterPowerAdapter, eSfpModule, eAccessPointPowerAdaptor, eNonRemovableInterfaceCard, eCustomModuleType = 2000   
---|---  
  
## ◆ getModel()

string DeviceDescriptor::getModel  | ( | | ) |   
---|---|---|---|---  
  
Get device model. 

Returns
    string, device model in string format 

## ◆ getRequiredScriptModuleAt()

string DeviceDescriptor::getRequiredScriptModuleAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Get the name of the required script module at a specified index. 

Parameters
     index,specified| index  
---|---  
  
Returns
    string, script module name 

## ◆ getRequiredScriptModuleCount()

int DeviceDescriptor::getRequiredScriptModuleCount  | ( | | ) |   
---|---|---|---|---  
  
Get the number of required script module. 

Returns
    int, number of required script module 

## ◆ getRootModule()

[ModuleDescriptor](class_module_descriptor.html) DeviceDescriptor::getRootModule  | ( | | ) |   
---|---|---|---|---  
  
Get the root module descriptor. 

Returns
    [ModuleDescriptor](class_module_descriptor.html "Descriptor for modules. Used to create a module based on the stored information."), root module descriptor 

## ◆ getSpecifiedModelAt()

string DeviceDescriptor::getSpecifiedModelAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Get specified model at a specified index. 

Parameters
     index,specified| index  
---|---  
  
Returns
    string, the specified model name in string format 

## ◆ getSpecifiedModelCount()

int DeviceDescriptor::getSpecifiedModelCount  | ( | | ) |   
---|---|---|---|---  
  
Get specified model count. 

Returns
    int, the number of specified model 

## ◆ getSupportedModuleTypeAt()

ModuleType DeviceDescriptor::getSupportedModuleTypeAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Get the supported module type at a specified index. 

Parameters
     index,the| specified index  
---|---  
  
Returns
    enum<ModuleType>, see different types documented in [addSupportedModuleType()](class_device_descriptor.html#aae0c2e505314e84fce4c47f6154a69fc "Add supported module type to device descriptor.") function 

## ◆ getSupportedModuleTypeCount()

int DeviceDescriptor::getSupportedModuleTypeCount  | ( | | ) |   
---|---|---|---|---  
  
Get the number of module type. 

Returns
    int, number of module type 

## ◆ getType()

DeviceType DeviceDescriptor::getType  | ( | | ) |   
---|---|---|---|---  
  
Return device type. 

Returns
    enum<DeviceType> start with 0 and add 1 for subsequent type eRouter = 0, eSwitch, eCloud, eBridge, eHub, eRepeater, eCoAxialSplitter, eAccessPoint, ePc, eServer, ePrinter, eWirelessRouter, eIpPhone, eDslModem, eCableModem, eRemoteNetwork, eMultiLayerSwitch, eLaptop, eTabletPC, ePda, eWirelessEndDevice, eWiredEndDevice, eTV, eHomeVoip, eAnalogPhone, eMultiUser, eASA, eIoE, eHomeGateway, eCellTower, eCentralOfficeServer, eCiscoAccessPoint, eEmbeddedCiscoAccessPoint, eSniffer, eMCU, eSBC, eThing, eMCUComponent, eEmbeddedServer, eWirelessLanController, eCluster, eGeoIcon 

## ◆ isExistSpecifiedModel()

bool DeviceDescriptor::isExistSpecifiedModel  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Check if the model exist. 

Parameters
     model,specified| model  
---|---  
  
Returns
    bool, true if the model exist and false if it does not 

## ◆ isModelSupported()

bool DeviceDescriptor::isModelSupported  | ( | | ) |   
---|---|---|---|---  
  
Check if the descriptor is model supported. 

Returns
    bool, true if model supported and false if not 

## ◆ isModuleTypeSupported()

bool DeviceDescriptor::isModuleTypeSupported  | ( | ModuleType  | | ) |   
---|---|---|---|---|---  
  
Check if module type is supported. 

Parameters
     type,enum<ModuleType>|   
---|---  
type,module| type enum<ModuleType>, start with 0 and add 1 to subsequent module type eLineCard=0, // Line card eNetworkModule, // [Network](class_network.html "Network is the entry point for all device configurations in the network. It retrieves devices.") module eInterfaceCard, // Interface card ePtRouterModule, // Packet Tracer router module ePtSwitchModule, // Packet Tracer switch module ePtCloudModule, // Packet Tracer cloud module ePtRepeaterModule, // Packet Tracer repeater module ePtHostModule, // Packet Tracer host module ePtModemModule, ePtLaptopModule, ePtTVModule, eIpPhonePowerAdapter, ePtTabletPCModule, ePtPdaModule, ePtWirelessEndDeviceModule, ePtWiredEndDeviceModule, eTrs35, eUsb, eNonRemovableModule, // Non-removable module eASAModule, eASAPowerAdapter, ePtCellTowerModule, ePtIoeModule, ePtIoeNetworkModule, ePtIoeAnalogModule, ePtIoeDigitalModule, ePtIoeCustomIOModule, ePtIoePowerAdapter, ePtIoeMcuComponentPowerAdapter, ePtRouterPowerAdapter, eSfpModule, eAccessPointPowerAdaptor, eNonRemovableInterfaceCard, eCustomModuleType = 2000  
  
Returns
    bool, true if the module type is supported and false if not 

## ◆ removeRequiredScriptModule()

void DeviceDescriptor::removeRequiredScriptModule  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removed required script module. 

Parameters
     smId,script| module id  
---|---  
  
Returns
    none 

## ◆ removeSpecifiedModel()

void DeviceDescriptor::removeSpecifiedModel  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Remove model model to support. 

Parameters
     model,specified| model   
---|---  
  
## ◆ removeSupportedModuleType()

void DeviceDescriptor::removeSupportedModuleType  | ( | ModuleType  | | ) |   
---|---|---|---|---|---  
  
Remove supported module type to device descriptor. 

Parameters
     type,module| type enum<ModuleType>, same type as param for [addSupportedModuleType()](class_device_descriptor.html#aae0c2e505314e84fce4c47f6154a69fc "Add supported module type to device descriptor.").   
---|---  
  
## ◆ setModelSupportedFlag()

void DeviceDescriptor::setModelSupportedFlag  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Set supported flag to the device descriptor. 

Parameters
     isSupported,true| if supported and false if not  
---|---  
  
Returns
    none 

* * *

The documentation for this class was generated from the following file:

  * [CDeviceDescriptor.pki](_c_device_descriptor_8pki.html)


