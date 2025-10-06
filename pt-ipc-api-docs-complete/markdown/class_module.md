# Cisco Packet Tracer Extensions API: Module Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_module.html

---

##  Public Member Functions  
  
---  
int | [getModuleNumber](class_module.html#a06b289ce08c6a589deca6f9b59245263) ()  
| Returns the number of the module. [More...](class_module.html#a06b289ce08c6a589deca6f9b59245263)  
  
string | [getModuleNameAsString](class_module.html#a071bbb44e365eb1f3734d0427fae7404) ()  
| Returns the number of the module. [More...](class_module.html#a071bbb44e365eb1f3734d0427fae7404)  
  
string | [getSlotPath](class_module.html#a99befa3e2c09faf22e423a4d5ad37372) ()  
| Returns slot path. [More...](class_module.html#a99befa3e2c09faf22e423a4d5ad37372)  
  
ModuleType | [getModuleType](class_module.html#acf2d3da3463cd5c0df54c5f57bc576d9) ()  
| Returns the module type. [More...](class_module.html#acf2d3da3463cd5c0df54c5f57bc576d9)  
  
int | [getPortCount](class_module.html#a9b2e91e07d8748f5684b9fe14b71a00e) ()  
| Returns the port count. [More...](class_module.html#a9b2e91e07d8748f5684b9fe14b71a00e)  
  
[Port](class_port.html) | [getPortAt](class_module.html#ae1663f823cbf048421ca4522eb2c6bf8) (int)  
| Returns the port at the given index. [More...](class_module.html#ae1663f823cbf048421ca4522eb2c6bf8)  
  
void | [addSlot](class_module.html#af81055ca830a69192f4071d02b68a2c6) (ModuleType)  
| Adds a slot of the given type. [More...](class_module.html#af81055ca830a69192f4071d02b68a2c6)  
  
int | [getSlotCount](class_module.html#addc26ef0fa3377e3ffff228b40ea9021) ()  
| Returns the total slot count. [More...](class_module.html#addc26ef0fa3377e3ffff228b40ea9021)  
  
ModuleType | [getSlotTypeAt](class_module.html#a5ebf6ca22c18bab467e7edcd68101542) (int)  
| Returns the type of the module at the given index. [More...](class_module.html#a5ebf6ca22c18bab467e7edcd68101542)  
  
void | [removeModuleAt](class_module.html#a7120bba5ac2923218e0f74fe98d3061a) (int)  
| Removes the module at the given index. [More...](class_module.html#a7120bba5ac2923218e0f74fe98d3061a)  
  
int | [getModuleCount](class_module.html#ad01ef3ef48eb78e95d6fc6659bf3a2b1) ()  
| Returns the number modules. [More...](class_module.html#ad01ef3ef48eb78e95d6fc6659bf3a2b1)  
  
[Module](class_module.html) | [getModuleAt](class_module.html#a650ab2a2d789e57945d9f2c617f7ede9) (int)  
| Returns the module at the given index. [More...](class_module.html#a650ab2a2d789e57945d9f2c617f7ede9)  
  
[Device](class_device.html) | [getOwnerDevice](class_module.html#a2784c6ca2352a30e3a9ef9cd171ac3e3) ()  
| Returns owner device of the module. [More...](class_module.html#a2784c6ca2352a30e3a9ef9cd171ac3e3)  
  
[ModuleDescriptor](class_module_descriptor.html) | [getDescriptor](class_module.html#a4da7cef3cf7a91a8be2894b45994aad3) () const  
| Returns the descriptor of the module. Descriptor contains device model, position, etc. [More...](class_module.html#a4da7cef3cf7a91a8be2894b45994aad3)  
  
bool | [addModuleAt](class_module.html#a2505e955df9dadbb99c596143687efdd) (string, int)  
| Adds a module at the specified location. [More...](class_module.html#a2505e955df9dadbb99c596143687efdd)  
  
  
## Member Function Documentation

## ◆ addModuleAt()

bool Module::addModuleAt  | ( | string  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Adds a module at the specified location. 

Parameters
     moduleId,module| type to add. Something like "NM-2W".   
---|---  
index,index| to add at.  
  
Returns
    bool, true if the module was added, false if not. 

## ◆ addSlot()

void Module::addSlot  | ( | ModuleType  | | ) |   
---|---|---|---|---|---  
  
Adds a slot of the given type. 

Parameters
     type,Slot| type to add. Types: eLineCard = 0, eNetworkModule = 1, eInterfaceCard = 2, ePtRouterModule = 3, ePtSwitchModule = 4, ePtCloudModule = 5, ePtRepeaterModule = 6, ePtHostModule = 7,   
ePtModemModule = 8, ePtLaptopModule = 9, ePtTVModule = 10, eIpPhonePowerAdapter = 11, ePtTabletPCModule = 12, ePtPdaModule = 13, ePtWirelessEndDeviceModule = 14, ePtWiredEndDeviceModule = 15, eTrs35 = 16, eUsb = 17, eNonRemovableModule = 18, eASAModule = 19, eASAPowerAdapter = 20, ePtCellTowerModule = 21, ePtIoeModule = 22, ePtIoeNetworkModule = 23, ePtIoeAnalogModule = 24, ePtIoeDigitalModule = 25, ePtIoeCustomIOModule = 26, ePtIoePowerAdapter = 27, ePtIoeMcuComponentPowerAdapter = 28, ePtRouterPowerAdapter = 29, eSfpModule = 30, eAccessPointPowerAdaptor = 31, eNonRemovableInterfaceCard = 32, eCustomModuleType = 2000   
---|---  
  
## ◆ getDescriptor()

[ModuleDescriptor](class_module_descriptor.html) Module::getDescriptor  | ( | | ) |  const  
---|---|---|---|---  
  
Returns the descriptor of the module. Descriptor contains device model, position, etc. 

Returns
    [ModuleDescriptor](class_module_descriptor.html "Descriptor for modules. Used to create a module based on the stored information."), the module descriptor. 

## ◆ getModuleAt()

[Module](class_module.html) Module::getModuleAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the module at the given index. 

Parameters
     index,index| of the module to get. Range (0, getModuleCount - 1).  
---|---  
  
Returns
    [Module](class_module.html), the module found at the given index. 

## ◆ getModuleCount()

int Module::getModuleCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number modules. 

Returns
    int, the number of modules. 

## ◆ getModuleNameAsString()

string Module::getModuleNameAsString  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of the module. 

Returns
    string, the module name as a string. Seems to always be "None". 

## ◆ getModuleNumber()

int Module::getModuleNumber  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of the module. 

Returns
    int, the number of the module. 

## ◆ getModuleType()

ModuleType Module::getModuleType  | ( | | ) |   
---|---|---|---|---  
  
Returns the module type. 

Returns
    enum<ModuleType>, the number of the module. Types: eLineCard = 0, eNetworkModule = 1, eInterfaceCard = 2, ePtRouterModule = 3, ePtSwitchModule = 4, ePtCloudModule = 5, ePtRepeaterModule = 6, ePtHostModule = 7,   
ePtModemModule = 8, ePtLaptopModule = 9, ePtTVModule = 10, eIpPhonePowerAdapter = 11, ePtTabletPCModule = 12, ePtPdaModule = 13, ePtWirelessEndDeviceModule = 14, ePtWiredEndDeviceModule = 15, eTrs35 = 16, eUsb = 17, eNonRemovableModule = 18, eASAModule = 19, eASAPowerAdapter = 20, ePtCellTowerModule = 21, ePtIoeModule = 22, ePtIoeNetworkModule = 23, ePtIoeAnalogModule = 24, ePtIoeDigitalModule = 25, ePtIoeCustomIOModule = 26, ePtIoePowerAdapter = 27, ePtIoeMcuComponentPowerAdapter = 28, ePtRouterPowerAdapter = 29, eSfpModule = 30, eAccessPointPowerAdaptor = 31, eNonRemovableInterfaceCard = 32, eCustomModuleType = 2000 

## ◆ getOwnerDevice()

[Device](class_device.html) Module::getOwnerDevice  | ( | | ) |   
---|---|---|---|---  
  
Returns owner device of the module. 

Returns
    [Device](class_device.html "Device is the base class for all device objects."), the device that owns the module. 

## ◆ getPortAt()

[Port](class_port.html) Module::getPortAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the port at the given index. 

Parameters
     index,index| of the port to retrive.   
  
---|---  
  
Returns
    [Port](class_port.html "Port holds and manipulates the ports on devices."), port at the given index. 

## ◆ getPortCount()

int Module::getPortCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the port count. 

Returns
    int, the number of ports. 

## ◆ getSlotCount()

int Module::getSlotCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the total slot count. 

Returns
    int, the total slot count. 

## ◆ getSlotPath()

string Module::getSlotPath  | ( | | ) |   
---|---|---|---|---  
  
Returns slot path. 

Returns
    string, the slot path. For example, "0/0" or "0/1". 

## ◆ getSlotTypeAt()

ModuleType Module::getSlotTypeAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the type of the module at the given index. 

Parameters
     index,index| of the module to find the type for.  
---|---  
  
Returns
    enum<ModuleType>, the type of the module. 

## ◆ removeModuleAt()

void Module::removeModuleAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Removes the module at the given index. 

Parameters
     index,index| of the module to remove. Range (0, getModuleCount - 1).   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CModule.pki](_c_module_8pki.html)


