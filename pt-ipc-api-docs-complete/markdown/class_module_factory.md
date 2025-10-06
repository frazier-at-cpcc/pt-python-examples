# Cisco Packet Tracer Extensions API: ModuleFactory Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_module_factory.html

---

Factory for modules. [More...](class_module_factory.html#details)

##  Public Member Functions  
  
---  
[ModuleDescriptor](class_module_descriptor.html) | [getDescriptor](class_module_factory.html#ae73263ef8085f137411e03582d068329) (ModuleType, string)  
| Gets the module descriptor that matches the given types. [More...](class_module_factory.html#ae73263ef8085f137411e03582d068329)  
  
int | [getAvailableModuleCount](class_module_factory.html#a7a1407117f033b76f56c7798dfa1e0fd) ()  
| Gets the number of module descriptors stored in the factory. [More...](class_module_factory.html#a7a1407117f033b76f56c7798dfa1e0fd)  
  
[ModuleDescriptor](class_module_descriptor.html) | [getAvailableModuleAt](class_module_factory.html#aef89c39820bfe385ddf50f7649a1fe89) (int)  
| Gets the module descriptor at the given index. [More...](class_module_factory.html#aef89c39820bfe385ddf50f7649a1fe89)  
  
int | [getAvailableModuleForTypeCount](class_module_factory.html#a97c460ba1929475ba90ed65c691840ec) (ModuleType)  
| Gets the number of module descriptors stored in the factory of the given type. [More...](class_module_factory.html#a97c460ba1929475ba90ed65c691840ec)  
  
[ModuleDescriptor](class_module_descriptor.html) | [getAvailableModuleForTypeAt](class_module_factory.html#a3d9a2d0f9cc4c92763f23cf326456125) (ModuleType, int)  
| Gets the module descriptor stored for the given type and index. [More...](class_module_factory.html#a3d9a2d0f9cc4c92763f23cf326456125)  
  
[ModuleDescriptor](class_module_descriptor.html) | [addModuleModel](class_module_factory.html#a36ec4ae4987a409226a9a30119e53abe) (ModuleType, string)  
| Adds a module descriptor of the given types. [More...](class_module_factory.html#a36ec4ae4987a409226a9a30119e53abe)  
  
  
## Detailed Description

Factory for modules. 

## Member Function Documentation

## ◆ addModuleModel()

[ModuleDescriptor](class_module_descriptor.html) ModuleFactory::addModuleModel  | ( | ModuleType  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Adds a module descriptor of the given types. 

Parameters
     type,module| type to add.   
---|---  
model,the| string type of for the module. Something like "PT-ROUTER-NM-1CFE".  
  
Returns
    [ModuleDescriptor](class_module_descriptor.html "Descriptor for modules. Used to create a module based on the stored information."), the module descriptor added. 

## ◆ getAvailableModuleAt()

[ModuleDescriptor](class_module_descriptor.html) ModuleFactory::getAvailableModuleAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Gets the module descriptor at the given index. 

Parameters
     int,index| to get the descriptor from. Range (0, [getAvailableModuleCount()](class_module_factory.html#a7a1407117f033b76f56c7798dfa1e0fd "Gets the number of module descriptors stored in the factory.")-1)  
---|---  
  
Returns
    [ModuleDescriptor](class_module_descriptor.html "Descriptor for modules. Used to create a module based on the stored information."), the descriptor at the given index. 

## ◆ getAvailableModuleCount()

int ModuleFactory::getAvailableModuleCount  | ( | | ) |   
---|---|---|---|---  
  
Gets the number of module descriptors stored in the factory. 

Returns
    int, the number of module descriptors stored in the factory. 

## ◆ getAvailableModuleForTypeAt()

[ModuleDescriptor](class_module_descriptor.html) ModuleFactory::getAvailableModuleForTypeAt  | ( | ModuleType  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Gets the module descriptor stored for the given type and index. 

Parameters
     type,module| type to check for.   
---|---  
index,index| in they type to get the descriptor for.  
  
Returns
    [ModuleDescriptor](class_module_descriptor.html "Descriptor for modules. Used to create a module based on the stored information."), the module descriptor stored for the given type and index. 

## ◆ getAvailableModuleForTypeCount()

int ModuleFactory::getAvailableModuleForTypeCount  | ( | ModuleType  | | ) |   
---|---|---|---|---|---  
  
Gets the number of module descriptors stored in the factory of the given type. 

Parameters
     type,module| type to check for.  
---|---  
  
Returns
    int, the number of module descriptors stored in the factory of the given type. 

## ◆ getDescriptor()

[ModuleDescriptor](class_module_descriptor.html) ModuleFactory::getDescriptor  | ( | ModuleType  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Gets the module descriptor that matches the given types. 

Parameters
     moduleType| enum<ModuleType>, the number of the module. Types: eLineCard = 0, eNetworkModule = 1, eInterfaceCard = 2, ePtRouterModule = 3, ePtSwitchModule = 4, ePtCloudModule = 5, ePtRepeaterModule = 6, ePtHostModule = 7,   
ePtModemModule = 8, ePtLaptopModule = 9, ePtTVModule = 10, eIpPhonePowerAdapter = 11, ePtTabletPCModule = 12, ePtPdaModule = 13, ePtWirelessEndDeviceModule = 14, ePtWiredEndDeviceModule = 15, eTrs35 = 16, eUsb = 17, eNonRemovableModule = 18, eASAModule = 19, eASAPowerAdapter = 20, ePtCellTowerModule = 21, ePtIoeModule = 22, ePtIoeNetworkModule = 23, ePtIoeAnalogModule = 24, ePtIoeDigitalModule = 25, ePtIoeCustomIOModule = 26, ePtIoePowerAdapter = 27, ePtIoeMcuComponentPowerAdapter = 28, ePtRouterPowerAdapter = 29, eSfpModule = 30, eAccessPointPowerAdaptor = 31, eNonRemovableInterfaceCard = 32, eCustomModuleType = 2000   
---|---  
model,model| name. Something like "PT-ROUTER-NM-1CFE".   
  
  
Returns
    [ModuleDescriptor](class_module_descriptor.html "Descriptor for modules. Used to create a module based on the stored information."), the descriptor that matches the given types.   


* * *

The documentation for this class was generated from the following file:

  * [CModuleFactory.pki](_c_module_factory_8pki.html)


