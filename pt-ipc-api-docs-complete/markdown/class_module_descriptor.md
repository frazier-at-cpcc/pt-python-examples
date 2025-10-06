# Cisco Packet Tracer Extensions API: ModuleDescriptor Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_module_descriptor.html

---

Descriptor for modules. Used to create a module based on the stored information. [More...](class_module_descriptor.html#details)

##  Public Member Functions  
  
---  
ModuleType | [getType](class_module_descriptor.html#af0983ecb52f43965083c9140308daeb2) ()  
| Returns the type of the module descriptor. [More...](class_module_descriptor.html#af0983ecb52f43965083c9140308daeb2)  
  
string | [getModel](class_module_descriptor.html#aa0494d49e50d39a3e523dec9eacfa693) ()  
| Returns type name of the module.. [More...](class_module_descriptor.html#aa0494d49e50d39a3e523dec9eacfa693)  
  
void | [setImagePath](class_module_descriptor.html#a44a7e20454846d45721534b166f01fbd) (string)  
| Sets the image path to the image to use for the module. [More...](class_module_descriptor.html#a44a7e20454846d45721534b166f01fbd)  
  
string | [getImagePath](class_module_descriptor.html#a9d55c74c646505933f8bc71824ed609c) ()  
| Gets the image path to the image to use for the module. [More...](class_module_descriptor.html#a9d55c74c646505933f8bc71824ed609c)  
  
void | [setInfo](class_module_descriptor.html#a60b345742646b2af32dcd52065affa36) (QString)  
| Sets the text to display when in module view and the module is selected. [More...](class_module_descriptor.html#a60b345742646b2af32dcd52065affa36)  
  
QString | [getInfo](class_module_descriptor.html#aa8247ac7175b81fad493a525b00c5083) ()  
| Gets the text to display when in module view and the module is selected. [More...](class_module_descriptor.html#aa8247ac7175b81fad493a525b00c5083)  
  
void | [setGroup](class_module_descriptor.html#a3631042a9735a466269791339414d1d2) (QString)  
| Sets the group the module is considered a part of. [More...](class_module_descriptor.html#a3631042a9735a466269791339414d1d2)  
  
QString | [getGroup](class_module_descriptor.html#a5ee6b31fc922f6ee3ce4f171756bd7bf) ()  
| Gets the group the module is considered a part of. [More...](class_module_descriptor.html#a5ee6b31fc922f6ee3ce4f171756bd7bf)  
  
void | [addSlot](class_module_descriptor.html#a107f9e70b53cbf9d2acc5abc98428d52) (ModuleType)  
| Adds the given module type to the module descriptor. Doing this allows the module type to be added to the module created from the descriptor. [More...](class_module_descriptor.html#a107f9e70b53cbf9d2acc5abc98428d52)  
  
int | [getSlotCount](class_module_descriptor.html#a2df10f2f0cb02206fb96323e4fb23d80) ()  
| Returns the number of slots in the descriptor. [More...](class_module_descriptor.html#a2df10f2f0cb02206fb96323e4fb23d80)  
  
ModuleType | [getSlotTypeAt](class_module_descriptor.html#ae80d0e68e7c3e3b15269fc7a004e44ed) (int)  
| Returns the module type of the given slot index. [More...](class_module_descriptor.html#ae80d0e68e7c3e3b15269fc7a004e44ed)  
  
bool | [addModuleAt](class_module_descriptor.html#ac4ac73cc2e96bec4a3ba38e84adc4b53) ([ModuleDescriptor](class_module_descriptor.html), int)  
| Adds the module descriptor to the given slot index, if possible. [More...](class_module_descriptor.html#ac4ac73cc2e96bec4a3ba38e84adc4b53)  
  
void | [removeModuleAt](class_module_descriptor.html#a91775fd2f7c440c03268eb7f8a01c61e) (int)  
| Removes the module descriptor to the given module index. [More...](class_module_descriptor.html#a91775fd2f7c440c03268eb7f8a01c61e)  
  
int | [getModuleCount](class_module_descriptor.html#ac2ad4639c7dbcca383a04aa2b6f5c63f) ()  
| Returns the number of module descriptions stored. [More...](class_module_descriptor.html#ac2ad4639c7dbcca383a04aa2b6f5c63f)  
  
[ModuleDescriptor](class_module_descriptor.html) | [getModuleAt](class_module_descriptor.html#a4da06e5a8220b1e6d89169deb6a3b09c) (int)  
| Returns module description at the given index. [More...](class_module_descriptor.html#a4da06e5a8220b1e6d89169deb6a3b09c)  
  
void | [setHotSwappable](class_module_descriptor.html#afcb43b8d09f1b787691ef1276ac8be52) (bool)  
| Set if the module is hot swappable (able to be removed and added while the device is powered on). [More...](class_module_descriptor.html#afcb43b8d09f1b787691ef1276ac8be52)  
  
bool | [isHotSwappable](class_module_descriptor.html#a2674d6760bbcbf8be0689a5a15e13345) ()  
| Get if the module is hot swappable (able to be removed and added while the device is powered on). [More...](class_module_descriptor.html#a2674d6760bbcbf8be0689a5a15e13345)  
  
[ModulePhysicalView](class_module_physical_view.html) | [addModulePhysicalView](class_module_descriptor.html#aca48c48fb783e19b77cc1e1468a2a738) (int, int, int, int)  
| Add a display area to the descriptor. [More...](class_module_descriptor.html#aca48c48fb783e19b77cc1e1468a2a738)  
  
int | [getModulePhysicalViewCount](class_module_descriptor.html#a0b439eb65343d01ef6843b44416b1891) ()  
| Get the number of display areas in the module. [More...](class_module_descriptor.html#a0b439eb65343d01ef6843b44416b1891)  
  
[ModulePhysicalView](class_module_physical_view.html) | [getModulePhysicalViewAt](class_module_descriptor.html#a9a6e1a5b70bfb0cf967572f7c4af2da5) (int)  
| Get the display area at the given index. [More...](class_module_descriptor.html#a9a6e1a5b70bfb0cf967572f7c4af2da5)  
  
[Module](class_module.html) | [create](class_module_descriptor.html#ac54f73df9fe8376ca811ce4281a1e044) ()  
| Create a module using the descriptor. [More...](class_module_descriptor.html#ac54f73df9fe8376ca811ce4281a1e044)  
  
  
## Detailed Description

Descriptor for modules. Used to create a module based on the stored information. 

## Member Function Documentation

## ◆ addModuleAt()

bool ModuleDescriptor::addModuleAt  | ( | [ModuleDescriptor](class_module_descriptor.html) | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Adds the module descriptor to the given slot index, if possible. 

Parameters
     index,index| to try to store the module descriptor at.  
---|---  
  
Returns
    bool, value is true if the module descriptor was stored, false if not. 

## ◆ addModulePhysicalView()

[ModulePhysicalView](class_module_physical_view.html) ModuleDescriptor::addModulePhysicalView  | ( | int  | ,   
---|---|---|---  
|  | int  | ,   
|  | int  | ,   
|  | int  |   
| ) | |   
  
Add a display area to the descriptor. 

Parameters
     X1,left| x.   
---|---  
X2,right| x.   
Y1,top| y.   
Y2,bottom| y.   
  
  
## ◆ addSlot()

void ModuleDescriptor::addSlot  | ( | ModuleType  | | ) |   
---|---|---|---|---|---  
  
Adds the given module type to the module descriptor. Doing this allows the module type to be added to the module created from the descriptor. 

Parameters
     type,module| type to add.   
---|---  
  
## ◆ create()

[Module](class_module.html) ModuleDescriptor::create  | ( | | ) |   
---|---|---|---|---  
  
Create a module using the descriptor. 

Returns
    [Module](class_module.html), module created using the descriptor. 

## ◆ getGroup()

QString ModuleDescriptor::getGroup  | ( | | ) |   
---|---|---|---|---  
  
Gets the group the module is considered a part of. 

Returns
    QString, Some modules use this and most don't. The ones that do can be "SENSORS" or "ACTUATORS". 

## ◆ getImagePath()

string ModuleDescriptor::getImagePath  | ( | | ) |   
---|---|---|---|---  
  
Gets the image path to the image to use for the module. 

Returns
    string, path of the image to use. Something like "../art/PhysicalView/gModuleNM-4AS.xpm" 

## ◆ getInfo()

QString ModuleDescriptor::getInfo  | ( | | ) |   
---|---|---|---|---  
  
Gets the text to display when in module view and the module is selected. 

Returns
    QString, text that is displayed explaining the module. 

## ◆ getModel()

string ModuleDescriptor::getModel  | ( | | ) |   
---|---|---|---|---  
  
Returns type name of the module.. 

Returns
    string, type name of the model. Something like "NM-2W". 

## ◆ getModuleAt()

[ModuleDescriptor](class_module_descriptor.html) ModuleDescriptor::getModuleAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns module description at the given index. 

Parameters
     index,index| to retrive the description from. Range (0, [getModuleCount()](class_module_descriptor.html#ac2ad4639c7dbcca383a04aa2b6f5c63f "Returns the number of module descriptions stored.")-1).  
---|---  
  
Returns
    [ModuleDescriptor](class_module_descriptor.html "Descriptor for modules. Used to create a module based on the stored information."), the module description at the given index. 

## ◆ getModuleCount()

int ModuleDescriptor::getModuleCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of module descriptions stored. 

Returns
    int, the number of module descriptions stored. 

## ◆ getModulePhysicalViewAt()

[ModulePhysicalView](class_module_physical_view.html) ModuleDescriptor::getModulePhysicalViewAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Get the display area at the given index. 

Parameters
     index,index| of the display area to retrive.  
---|---  
  
return [ModulePhysicalView](class_module_physical_view.html "Physical view for module."), display area at the given index. 

## ◆ getModulePhysicalViewCount()

int ModuleDescriptor::getModulePhysicalViewCount  | ( | | ) |   
---|---|---|---|---  
  
Get the number of display areas in the module. 

Returns
    int, the number of display areas in the module descriptor. 

## ◆ getSlotCount()

int ModuleDescriptor::getSlotCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of slots in the descriptor. 

Returns
    int, the number of slots in the descriptor. 

## ◆ getSlotTypeAt()

ModuleType ModuleDescriptor::getSlotTypeAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the module type of the given slot index. 

Parameters
     index,slot| index to get the module type for.  
---|---  
  
Returns
    ModuleType, the module type of the given slot index. 

## ◆ getType()

ModuleType ModuleDescriptor::getType  | ( | | ) |   
---|---|---|---|---  
  
Returns the type of the module descriptor. 

Returns
    enum<ModuleType>, the number of the module. Types: eLineCard = 0, eNetworkModule = 1, eInterfaceCard = 2, ePtRouterModule = 3, ePtSwitchModule = 4, ePtCloudModule = 5, ePtRepeaterModule = 6, ePtHostModule = 7,   
ePtModemModule = 8, ePtLaptopModule = 9, ePtTVModule = 10, eIpPhonePowerAdapter = 11, ePtTabletPCModule = 12, ePtPdaModule = 13, ePtWirelessEndDeviceModule = 14, ePtWiredEndDeviceModule = 15, eTrs35 = 16, eUsb = 17, eNonRemovableModule = 18, eASAModule = 19, eASAPowerAdapter = 20, ePtCellTowerModule = 21, ePtIoeModule = 22, ePtIoeNetworkModule = 23, ePtIoeAnalogModule = 24, ePtIoeDigitalModule = 25, ePtIoeCustomIOModule = 26, ePtIoePowerAdapter = 27, ePtIoeMcuComponentPowerAdapter = 28, ePtRouterPowerAdapter = 29, eSfpModule = 30, eAccessPointPowerAdaptor = 31, eNonRemovableInterfaceCard = 32, eCustomModuleType = 2000 

## ◆ isHotSwappable()

bool ModuleDescriptor::isHotSwappable  | ( | | ) |   
---|---|---|---|---  
  
Get if the module is hot swappable (able to be removed and added while the device is powered on). 

Returns
    bool, true if the module can be added and removed while the device is powered on, false if not. 

## ◆ removeModuleAt()

void ModuleDescriptor::removeModuleAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Removes the module descriptor to the given module index. 

Parameters
     index,index| to try to remove the module descriptor from. Range (0, [getModuleCount()](class_module_descriptor.html#ac2ad4639c7dbcca383a04aa2b6f5c63f "Returns the number of module descriptions stored.")-1).   
---|---  
  
## ◆ setGroup()

void ModuleDescriptor::setGroup  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Sets the group the module is considered a part of. 

Parameters
     group,Some| modules use this and most don't. The ones that do can be "SENSORS" or "ACTUATORS".   
---|---  
  
## ◆ setHotSwappable()

void ModuleDescriptor::setHotSwappable  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Set if the module is hot swappable (able to be removed and added while the device is powered on). 

Parameters
     bHot,true| if the module can be added and removed while the device is powered on, false if not.   
---|---  
  
## ◆ setImagePath()

void ModuleDescriptor::setImagePath  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the image path to the image to use for the module. 

Parameters
     path,path| of the image to use. Something like "../art/PhysicalView/gModuleNM-4AS.xpm"   
---|---  
  
## ◆ setInfo()

void ModuleDescriptor::setInfo  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Sets the text to display when in module view and the module is selected. 

Parameters
     strInfo,text| to display explaining the module.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CModuleDescriptor.pki](_c_module_descriptor_8pki.html)


