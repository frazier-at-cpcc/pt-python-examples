# Cisco Packet Tracer Extensions API: Device Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_device.html

---

[Device](class_device.html "Device is the base class for all device objects.") is the base class for all device objects. [More...](class_device.html#details)

##  Public Member Functions  
  
---  
void | [setName](class_device.html#ad1a61e27ed2ba075091b2e4bf2877687) (QString)  
| Sets the display name of this device. [More...](class_device.html#ad1a61e27ed2ba075091b2e4bf2877687)  
  
QString | [getName](class_device.html#ac32b18f070baf5c4e4be84117b911091) ()  
| Returns the display name of this device. [More...](class_device.html#ac32b18f070baf5c4e4be84117b911091)  
  
void | [nameChanged](class_device.html#a37c97a4102953e9e135ff3c96fcc7f68) (QString, QString)  
| [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. [More...](class_device.html#a37c97a4102953e9e135ff3c96fcc7f68)  
  
void | [setPower](class_device.html#ac22b50f49aa8f4420f3841061ae5bc59) (bool)  
| Sets the power on or off. [More...](class_device.html#ac22b50f49aa8f4420f3841061ae5bc59)  
  
void | [addSound](class_device.html#a7f8a2ada38aa06902802736e1461a642) (QString, QString)  
| Adds sound to the device. [More...](class_device.html#a7f8a2ada38aa06902802736e1461a642)  
  
void | [playSound](class_device.html#abf8fa5ddff0e158e2fda6d601aa56b49) (QString, int)  
| Play sound to the device. [More...](class_device.html#abf8fa5ddff0e158e2fda6d601aa56b49)  
  
void | [stopSound](class_device.html#a012184bbbe97c396a75c7209b65a9e60) (QString)  
| Stop playing sound on the device. [More...](class_device.html#a012184bbbe97c396a75c7209b65a9e60)  
  
void | [stopSounds](class_device.html#aa99d030e084a98c868e3afa75dd18701) ()  
| Stops playing all sounds on the device. [More...](class_device.html#aa99d030e084a98c868e3afa75dd18701)  
  
void | [destroySounds](class_device.html#a510cdc8c5f7a909713c6ab93cf871891) ()  
| Destroy all of the sounds on the device. [More...](class_device.html#a510cdc8c5f7a909713c6ab93cf871891)  
  
bool | [getPower](class_device.html#af1387f677c8ece6e7550181370a10228) ()  
| Returns the current power state of this device. [More...](class_device.html#af1387f677c8ece6e7550181370a10228)  
  
double | [getXCoordinate](class_device.html#af54b92f563f8c8cb89bb0d863d22710b) ()  
| Returns the current x-coordinate position in the Logical workspace for this device. [More...](class_device.html#af54b92f563f8c8cb89bb0d863d22710b)  
  
double | [getYCoordinate](class_device.html#a2e595c8932119cc08c2603bd57dd1639) ()  
| Returns the current y-coordinate position in the Logical workspace for this device. [More...](class_device.html#a2e595c8932119cc08c2603bd57dd1639)  
  
double | [getCenterXCoordinate](class_device.html#a672e63c873c863022c4a2d4a76212f3d) ()  
| Returns the current x-coordinate position in the Logical workspace for this device. [More...](class_device.html#a672e63c873c863022c4a2d4a76212f3d)  
  
double | [getCenterYCoordinate](class_device.html#acc49ba1aa60489aa7d67c1582fa26282) ()  
| Returns the current y-coordinate position in the Logical workspace for this device. [More...](class_device.html#acc49ba1aa60489aa7d67c1582fa26282)  
  
double | [getAreaTopY](class_device.html#a2f8518856f142f89f7668219e65f7b04) ()  
| Returns the current topmost y-coordinate position in the for this device. [More...](class_device.html#a2f8518856f142f89f7668219e65f7b04)  
  
double | [getAreaLeftX](class_device.html#ae962fa77e8119ff33ddd047a2919e1f4) ()  
| Returns the current leftmost x-coordinate position in the for this device. [More...](class_device.html#ae962fa77e8119ff33ddd047a2919e1f4)  
  
bool | [moveToLocationCentered](class_device.html#ad4cb2019a5260f4a6ac10e510c14788b) (int, int)  
| Moves this device to the specified location for its center in Logical workspace. [More...](class_device.html#ad4cb2019a5260f4a6ac10e510c14788b)  
  
bool | [moveToLocation](class_device.html#a1741560dedf627e016381bbfbc3a4d70) (int, int)  
| Moves this device to the specified location in Logical workspace. [More...](class_device.html#a1741560dedf627e016381bbfbc3a4d70)  
  
int | [getXPhysicalWS](class_device.html#a93332d7b361053acff1a271521bf7690) ()  
| Returns the current x-coordinate position in the Physical workspace for this device. [More...](class_device.html#a93332d7b361053acff1a271521bf7690)  
  
int | [getYPhysicalWS](class_device.html#ad9a1a0a8abfe6dc34ece1c2f02afe69b) ()  
| Returns the current y-coordinate position in the Physical workspace for this device. [More...](class_device.html#ad9a1a0a8abfe6dc34ece1c2f02afe69b)  
  
double | [getGlobalXPhysicalWS](class_device.html#ad9267533fd02ea842369d91fcb136ad7) ()  
| Returns the current global x-coordinate position in the Physical workspace for this device. [More...](class_device.html#ad9267533fd02ea842369d91fcb136ad7)  
  
double | [getGlobalYPhysicalWS](class_device.html#a7c319e9c2e1c5fb695ea24eb6427025e) ()  
| Returns the current global y-coordinate position in the Physical workspace for this device. [More...](class_device.html#a7c319e9c2e1c5fb695ea24eb6427025e)  
  
bool | [moveToLocInPhysicalWS](class_device.html#abdaea8dc0a84fa32ea9f23925a77033e) (int, int)  
| Moves this device to the specified location in Physical workspace. [More...](class_device.html#abdaea8dc0a84fa32ea9f23925a77033e)  
  
bool | [moveByInPhysicalWS](class_device.html#a3866354e4ba96dab1022fa4a9efd2285) (int, int)  
| Moves this device by the specified amount in Physical workspace. [More...](class_device.html#a3866354e4ba96dab1022fa4a9efd2285)  
  
void | [powerChanged](class_device.html#a0f7f7134629a3311b168144ffcd93fbc) (bool)  
| [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. [More...](class_device.html#a0f7f7134629a3311b168144ffcd93fbc)  
  
void | [poweringOff](class_device.html#ac048c7cba5fe3e8b3329a8c84b762fbe) ()  
| [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. [More...](class_device.html#ac048c7cba5fe3e8b3329a8c84b762fbe)  
  
DeviceType | [getType](class_device.html#ad1889e61913a6816b9783894c3f46bfb) ()  
| Returns the type of this device. [More...](class_device.html#ad1889e61913a6816b9783894c3f46bfb)  
  
string | [getModel](class_device.html#a7d34a33bf93bb56f91f27c8584d3cc4a) ()  
| Returns the model of this device. [More...](class_device.html#a7d34a33bf93bb56f91f27c8584d3cc4a)  
  
[DeviceDescriptor](class_device_descriptor.html) | [getDescriptor](class_device.html#a823ff28b2d392f9d4a17582c981a0893) ()  
| Returns the device descriptor that user can get information on the device like type, model, module supported.. [More...](class_device.html#a823ff28b2d392f9d4a17582c981a0893)  
  
string | [getSerialNumber](class_device.html#a86ab974649f75b9470489da1c9a8b917) ()  
| Returns the device serial number. [More...](class_device.html#a86ab974649f75b9470489da1c9a8b917)  
  
[Port](class_port.html) | [getPort](class_device.html#a94b520de9325b46b65763d39fed990b6) (string)  
| Returns the [Port](class_port.html "Port holds and manipulates the ports on devices.") object with the specified port name. [More...](class_device.html#a94b520de9325b46b65763d39fed990b6)  
  
int | [getPortCount](class_device.html#ad30d1380486468edac167ab1d5ba1092) ()  
| Returns the number of ports in this device. [More...](class_device.html#ad30d1380486468edac167ab1d5ba1092)  
  
[Port](class_port.html) | [getPortAt](class_device.html#a9cf207bdeee5e37bbdf0b90de3144151) (int)  
| Returns the [Port](class_port.html "Port holds and manipulates the ports on devices.") object at the specified index. [More...](class_device.html#a9cf207bdeee5e37bbdf0b90de3144151)  
  
[Process](class_process.html) | [getProcess](class_device.html#a11983d3bf184fe3f93db1619159d79df) (string)  
| Returns the [Process](class_process.html "Process is the base class for all device processes.") object associated the process name. [More...](class_device.html#a11983d3bf184fe3f93db1619159d79df)  
  
int | [getUsbPortCount](class_device.html#aa1c8ba4c0de4270360bbdd328f01825f) ()  
| Return the number of usb port. [More...](class_device.html#aa1c8ba4c0de4270360bbdd328f01825f)  
  
[UsbPort](class_usb_port.html) | [getUsbPortAt](class_device.html#a6f8c5a4bf83ae5cca33333ff0a94205f) (int)  
| Returns the usb port at a specified index. [More...](class_device.html#a6f8c5a4bf83ae5cca33333ff0a94205f)  
  
[Module](class_module.html) | [getRootModule](class_device.html#a89db9006d9bc978f62660f722212749b) ()  
| Returns the root module of the device. [More...](class_device.html#a89db9006d9bc978f62660f722212749b)  
  
bool | [addModule](class_device.html#afd27d5bdcf0543d8cf28246e802c6048) (string, ModuleType, string)  
| Adds a specific module to a particular slot. [More...](class_device.html#afd27d5bdcf0543d8cf28246e802c6048)  
  
bool | [removeModule](class_device.html#afaa8fbb93f721ef20e7d1677857d1852) (string)  
| Removes the module from the slot. [More...](class_device.html#afaa8fbb93f721ef20e7d1677857d1852)  
  
void | [moduleAdded](class_device.html#a229c5694ca916d7b905ee4febba3ef01) (ModuleType, string, string)  
| This event is emitted when a module is added. [More...](class_device.html#a229c5694ca916d7b905ee4febba3ef01)  
  
void | [moduleRemoved](class_device.html#ae3bb5e79149948d47e316002fadcbe02) (ModuleType, string, string)  
| This event is emitted when a module is removed. [More...](class_device.html#ae3bb5e79149948d47e316002fadcbe02)  
  
void | [portAdded](class_device.html#aed6b1fc39defb8711b16b81fbb1b944a) (string)  
| This event is emitted when a port is added. [More...](class_device.html#aed6b1fc39defb8711b16b81fbb1b944a)  
  
void | [portRemoved](class_device.html#a4c852869a6e4c6b4602fd2580e413062) (string)  
| This event is emitted when a port is removed. [More...](class_device.html#a4c852869a6e4c6b4602fd2580e413062)  
  
void | [portRemoving](class_device.html#af8a78cef01f22292cc7e9a62b216901f) (string)  
| This event is emitted when a port is being removed but before it is actually removed. This is useful for script modules to clean up things before the port is removed. [More...](class_device.html#af8a78cef01f22292cc7e9a62b216901f)  
  
[TerminalLine](class_terminal_line.html) | [getCommandLine](class_device.html#aba1bf234b4b3e4f51a8ef2755118bfc8) ()  
| Returns the command line [TerminalLine](class_terminal_line.html "TerminalLine manages the terminal lines, virtual terminal lines, and console lines.") object. [More...](class_device.html#aba1bf234b4b3e4f51a8ef2755118bfc8)  
  
void | [addCustomVar](class_device.html#aa4282996bfa2cda7a0829e536e6dc0f9) (QString, QString)  
| Adds a custom variable. [More...](class_device.html#aa4282996bfa2cda7a0829e536e6dc0f9)  
  
bool | [removeCustomVar](class_device.html#a03a441623bba8e779b8aaadc0eada0e0) (QString)  
| Removes a custom variable. [More...](class_device.html#a03a441623bba8e779b8aaadc0eada0e0)  
  
bool | [hasCustomVar](class_device.html#a554f2833f59f7201251acc58aca2e745) (QString)  
| Returns true if this device has a custom variable with the specified name. [More...](class_device.html#a554f2833f59f7201251acc58aca2e745)  
  
QString | [getCustomVarStr](class_device.html#a03b5d8f42474b78af9da40a826034241) (QString)  
| Returns the value of the variable with the specified name. [More...](class_device.html#a03b5d8f42474b78af9da40a826034241)  
  
int | [getCustomVarsCount](class_device.html#a92f6219f6b7d3ba9439afd3a15baf14e) ()  
| Returns the number of custom variables this device has. [More...](class_device.html#a92f6219f6b7d3ba9439afd3a15baf14e)  
  
QString | [getCustomVarNameAt](class_device.html#a52b937b6bb23f4cb11f5add85522713b) (int)  
| Returns the name of the custom variable at the specified index. [More...](class_device.html#a52b937b6bb23f4cb11f5add85522713b)  
  
QString | [getCustomVarValueStrAt](class_device.html#ad0606af5dbe4a249df3dbdc140aed396) (int)  
| Returns the value of the custom variable at the specified index. [More...](class_device.html#ad0606af5dbe4a249df3dbdc140aed396)  
  
void | [setCustomInterface](class_device.html#aaceb18161acc504ca84b39124b4ef9cb) (QString)  
| Set custom interface to the device. [More...](class_device.html#aaceb18161acc504ca84b39124b4ef9cb)  
  
QString | [getCustomInterface](class_device.html#a1552e1f557cc7f74a781aa46fdc86f91) ()  
| Get custom interface name on the device. [More...](class_device.html#a1552e1f557cc7f74a781aa46fdc86f91)  
  
QString | [serializeToXml](class_device.html#a1c0c3f1c03997d0b0d0b46a0d2508cd7) ()  
| Returns the serialization string of this device. [More...](class_device.html#a1c0c3f1c03997d0b0d0b46a0d2508cd7)  
  
QString | [activityTreeToXml](class_device.html#afdbdc164388c056b65bf3d147ce5cc16) ()  
| Returns the serialization string of this device's activity tree. [More...](class_device.html#afdbdc164388c056b65bf3d147ce5cc16)  
  
[PhysicalObject](class_physical_object.html) | [getPhysicalObject](class_device.html#ada1f60b57f4d6da9ee54d3880d2afec9) ()  
| Get custom interface name on the device. [More...](class_device.html#ada1f60b57f4d6da9ee54d3880d2afec9)  
  
QString | [getCustomLogicalImage](class_device.html#ad0927145729889e8c7aba9da07b0c8f5) ()  
| Get custom logical image path. [More...](class_device.html#ad0927145729889e8c7aba9da07b0c8f5)  
  
void | [setCustomLogicalImage](class_device.html#aff102967fedd0711f7544cad3722448e) (QString)  
| Set custom logical image path. [More...](class_device.html#aff102967fedd0711f7544cad3722448e)  
  
QString | [getCustomPhysicalImage](class_device.html#a251b11e42acd69701c2d9792d63618a5) ()  
| Get custom physical image path. [More...](class_device.html#a251b11e42acd69701c2d9792d63618a5)  
  
void | [setCustomPhysicalImage](class_device.html#ae1d2453c75b0d98ada1090298c15ffe8) (QString)  
| Set custom physical image path. [More...](class_device.html#ae1d2453c75b0d98ada1090298c15ffe8)  
  
vector< string > | [getSupportedModule](class_device.html#aeaddf90364503f0ffa9144f8dc4cd1f5) ()  
| Get a vector of supported modules. [More...](class_device.html#aeaddf90364503f0ffa9144f8dc4cd1f5)  
  
void | [setTime](class_device.html#a9527abd54dfb98372574876043e8e813) (int, int, int, int, int, int)  
| Set time to the device. [More...](class_device.html#a9527abd54dfb98372574876043e8e813)  
  
long | [getUpTime](class_device.html#a3c763a37bcbbe9bf6886f70b9f3899ac) ()  
| Set time to the device. [More...](class_device.html#a3c763a37bcbbe9bf6886f70b9f3899ac)  
  
vector< string > | [getPorts](class_device.html#a06bf83a93610cf41de70daf0b9d680cd) ()  
| Set time to the device. [More...](class_device.html#a06bf83a93610cf41de70daf0b9d680cd)  
  
double | [getDeviceExternalAttributeValue](class_device.html#af8e2a937e87a00cf15b4c7a7e7dc4311) (string)  
| Get device external attribute value. [More...](class_device.html#af8e2a937e87a00cf15b4c7a7e7dc4311)  
  
void | [setDeviceExternalAttributes](class_device.html#ad5e33d5820fcf0773f26e19c98c4d1c0) (QString)  
| Set device external attribute value. [More...](class_device.html#ad5e33d5820fcf0773f26e19c98c4d1c0)  
  
void | [addDeviceExternalAttributes](class_device.html#a772dd5a866625100bff03790c78fd96f) (QString)  
| Add device external attribute value. [More...](class_device.html#a772dd5a866625100bff03790c78fd96f)  
  
void | [subtractDeviceExternalAttributes](class_device.html#af3a40ba772ba2c2b58f788b7fc513e21) (QString)  
| Remove some of the device external attribute value pairs from the current list. [More...](class_device.html#af3a40ba772ba2c2b58f788b7fc513e21)  
  
QString | [getDeviceExternalAttributes](class_device.html#a1615dc3d8f77e4d2da21409b23b5b1c8) ()  
| Returns the list of external attributes and associated values. [More...](class_device.html#a1615dc3d8f77e4d2da21409b23b5b1c8)  
  
void | [clearDeviceExternalAttributes](class_device.html#a08679ec77f5695895cb9ac6cc4fcf80b) ()  
bool | [isOutdated](class_device.html#a0ae5b919f774d9f9c735f7245f747b3b) ()  
bool | [restoreToDefault](class_device.html#a829425f504dc6265e70053b05838814a) (bool, bool)  
void | [updateTemplateCreationTime](class_device.html#afc43a1076698e8f5892354860518836d) ()  
bool | [runProject](class_device.html#a38cdc3dfed044e7501c17fa2eb2aed40) (string, string)  
| Runs a programming project in the mcu. [More...](class_device.html#a38cdc3dfed044e7501c17fa2eb2aed40)  
  
bool | [stopProject](class_device.html#a12e3a648945b0ba0b9be6f0163c0a9ce) (string)  
| Stops a programming project in the mcu. [More...](class_device.html#a12e3a648945b0ba0b9be6f0163c0a9ce)  
  
bool | [isProjectRunning](class_device.html#a8459fab2e7f63d498284ee6af2f45dd2) (string)  
| Checks if a programming project with the given name is running. [More...](class_device.html#a8459fab2e7f63d498284ee6af2f45dd2)  
  
bool | [runCodeInProject](class_device.html#aa33324c24d287542d28b75d1b315ff23) (string, string)  
| Runs additional code in the given project. [More...](class_device.html#aa33324c24d287542d28b75d1b315ff23)  
  
void | [addProgrammingSerialOutputs](class_device.html#af1aef4f4dcd3af174b5ebd03d92fbbc2) (string)  
| Writes to the programming output. Text appears in the programming output dialog. [More...](class_device.html#af1aef4f4dcd3af174b5ebd03d92fbbc2)  
  
string | [getProgrammingSerialOutputs](class_device.html#aae83cbfc9bcf39fc383d0a94aa390d15) ()  
| Gets the programming output. It is the text that appears in the programming output dialog. [More...](class_device.html#aae83cbfc9bcf39fc383d0a94aa390d15)  
  
void | [clearProgrammingSerialOutputs](class_device.html#aab494dd36d98721cf9ad0b95d4df0a41) ()  
| Clears the programming output dialog. [More...](class_device.html#aab494dd36d98721cf9ad0b95d4df0a41)  
  
[UserDesktopAppConfig](class_user_desktop_app_config.html) | [addUserDesktopApp](class_device.html#a23a5a16ed476b7126c10d7b12acc2a8c) (string)  
[UserDesktopAppConfig](class_user_desktop_app_config.html) | [addUserDesktopAppFrom](class_device.html#a873c9ebae08432e9a2b5291292002c99) ([UserDesktopAppConfig](class_user_desktop_app_config.html))  
[UserDesktopAppConfig](class_user_desktop_app_config.html) | [addUserDesktopAppFromGlobal](class_device.html#a783cf257875aa15b3e0b53eee7c47535) (string)  
int | [getUserDesktopAppCount](class_device.html#a5d008e523ceb7410fc51eae41b638c6a) ()  
[UserDesktopAppConfig](class_user_desktop_app_config.html) | [getUserDesktopAppAt](class_device.html#a84f78c0b3b0921958a41d2769dfad904) (int)  
[UserDesktopAppConfig](class_user_desktop_app_config.html) | [getUserDesktopAppByDir](class_device.html#a7189710bb99dda2b5a8db9ea2125995f) (string)  
[UserDesktopAppConfig](class_user_desktop_app_config.html) | [getUserDesktopAppById](class_device.html#ae3e2114932a5430f0a3a46985d668b2a) (string)  
void | [removeUserDesktopApp](class_device.html#a0289ca531f292cfcc03ee857f805cec7) (string)  
void | [relinkUserDesktopApp](class_device.html#a7b215963d15dc74c90f7cc3accb09e2a) (string, string)  
bool | [isDesktopAvailable](class_device.html#acebbc2745d52165fa19246edcfa11269) ()  
  
## Detailed Description

[Device](class_device.html "Device is the base class for all device objects.") is the base class for all device objects. 

## Member Function Documentation

## ◆ activityTreeToXml()

QString Device::activityTreeToXml  | ( | | ) |   
---|---|---|---|---  
  
Returns the serialization string of this device's activity tree. 

Parameters
     QString,the| serialization string of this device activity tree.   
---|---  
  
## ◆ addCustomVar()

void Device::addCustomVar  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Adds a custom variable. 

Parameters
     name,the| name of the variable.   
---|---  
var,the| value of the variable.   
  
## ◆ addDeviceExternalAttributes()

void Device::addDeviceExternalAttributes  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Add device external attribute value. 

Parameters
     attributeValues,QString| attribute value pair in json format   
---|---  
  
## ◆ addModule()

bool Device::addModule  | ( | string  | ,   
---|---|---|---  
|  | ModuleType  | ,   
|  | string  |   
| ) | |   
  
Adds a specific module to a particular slot. 

Parameters
     slot,the| slot to add the module to.   
---|---  
type,the| type of the module. [Module](class_module.html) types: eLineCard = 0, eNetworkModule = 1, eInterfaceCard = 2, ePtRouterModule = 3, ePtSwitchModule = 4, ePtCloudModule = 5, ePtRepeaterModule = 6, ePtHostModule = 7, ePtModemModule = 8, ePtLaptopModule = 9, ePtTVModule = 10, eIpPhonePowerAdapter = 11, ePtTabletPCModule = 12, ePtPdaModule = 13, ePtWirelessEndDeviceModule = 14, ePtWiredEndDeviceModule = 15, eTrs35 = 16, eUsb = 17, eNonRemovableModule = 18, eASAPowerAdapter = 19   
model,the| model name of the module.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ addProgrammingSerialOutputs()

void Device::addProgrammingSerialOutputs  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Writes to the programming output. Text appears in the programming output dialog. 

Parameters
     output,text| to write.   
---|---  
  
## ◆ addSound()

void Device::addSound  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Adds sound to the device. 

Parameters
     soundPath,the| path to the sound file  
---|---  
soundId,the| id to identify the sound from other sounds   
  
## ◆ addUserDesktopApp()

[UserDesktopAppConfig](class_user_desktop_app_config.html) Device::addUserDesktopApp  | ( | string  | | ) |   
---|---|---|---|---|---  
  
## ◆ addUserDesktopAppFrom()

[UserDesktopAppConfig](class_user_desktop_app_config.html) Device::addUserDesktopAppFrom  | ( | [UserDesktopAppConfig](class_user_desktop_app_config.html) | | ) |   
---|---|---|---|---|---  
  
## ◆ addUserDesktopAppFromGlobal()

[UserDesktopAppConfig](class_user_desktop_app_config.html) Device::addUserDesktopAppFromGlobal  | ( | string  | | ) |   
---|---|---|---|---|---  
  
## ◆ clearDeviceExternalAttributes()

void Device::clearDeviceExternalAttributes  | ( | | ) |   
---|---|---|---|---  
  
## ◆ clearProgrammingSerialOutputs()

void Device::clearProgrammingSerialOutputs  | ( | | ) |   
---|---|---|---|---  
  
Clears the programming output dialog. 

## ◆ destroySounds()

void Device::destroySounds  | ( | | ) |   
---|---|---|---|---  
  
Destroy all of the sounds on the device. 

## ◆ getAreaLeftX()

double Device::getAreaLeftX  | ( | | ) |   
---|---|---|---|---  
  
Returns the current leftmost x-coordinate position in the for this device. 

Returns
    double, the current x-coordinate. 

## ◆ getAreaTopY()

double Device::getAreaTopY  | ( | | ) |   
---|---|---|---|---  
  
Returns the current topmost y-coordinate position in the for this device. 

Returns
    double, the current y-coordinate. 

## ◆ getCenterXCoordinate()

double Device::getCenterXCoordinate  | ( | | ) |   
---|---|---|---|---  
  
Returns the current x-coordinate position in the Logical workspace for this device. 

Returns
    double, the current x-coordinate. 

## ◆ getCenterYCoordinate()

double Device::getCenterYCoordinate  | ( | | ) |   
---|---|---|---|---  
  
Returns the current y-coordinate position in the Logical workspace for this device. 

Returns
    double, the current y-coordinate. 

## ◆ getCommandLine()

[TerminalLine](class_terminal_line.html) Device::getCommandLine  | ( | | ) |   
---|---|---|---|---  
  
Returns the command line [TerminalLine](class_terminal_line.html "TerminalLine manages the terminal lines, virtual terminal lines, and console lines.") object. 

Returns
    [TerminalLine](class_terminal_line.html "TerminalLine manages the terminal lines, virtual terminal lines, and console lines."), the [TerminalLine](class_terminal_line.html "TerminalLine manages the terminal lines, virtual terminal lines, and console lines.") object. 

## ◆ getCustomInterface()

QString Device::getCustomInterface  | ( | | ) |   
---|---|---|---|---  
  
Get custom interface name on the device. 

Returns
    QString, the custom interface name 

## ◆ getCustomLogicalImage()

QString Device::getCustomLogicalImage  | ( | | ) |   
---|---|---|---|---  
  
Get custom logical image path. 

Returns
    QString, the custom logical image name 

## ◆ getCustomPhysicalImage()

QString Device::getCustomPhysicalImage  | ( | | ) |   
---|---|---|---|---  
  
Get custom physical image path. 

Returns
    QString, custom physical image name in string 

## ◆ getCustomVarNameAt()

QString Device::getCustomVarNameAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the name of the custom variable at the specified index. 

Parameters
     index,the| index of the variable of interest.  
---|---  
QString,the| name of the custom variable at the specified index.   
  
## ◆ getCustomVarsCount()

int Device::getCustomVarsCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of custom variables this device has. 

Parameters
     QString,the| number of custom variables this device has.   
---|---  
  
## ◆ getCustomVarStr()

QString Device::getCustomVarStr  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the value of the variable with the specified name. 

Parameters
     name,the| name of the variable of interest.  
---|---  
QString,the| value of the custom variable.   
  
## ◆ getCustomVarValueStrAt()

QString Device::getCustomVarValueStrAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the value of the custom variable at the specified index. 

Parameters
     index,the| index of the variable of interest.  
---|---  
QString,the| value of the custom variable at the specified index.   
  
## ◆ getDescriptor()

[DeviceDescriptor](class_device_descriptor.html) Device::getDescriptor  | ( | | ) |   
---|---|---|---|---  
  
Returns the device descriptor that user can get information on the device like type, model, module supported.. 

Returns
    [DeviceDescriptor](class_device_descriptor.html "Descriptor for a device."), [DeviceDescriptor](class_device_descriptor.html "Descriptor for a device.") object 

## ◆ getDeviceExternalAttributes()

QString Device::getDeviceExternalAttributes  | ( | | ) |   
---|---|---|---|---  
  
Returns the list of external attributes and associated values. 

Parameters
     QString,attribute| value pair in json format   
---|---  
  
## ◆ getDeviceExternalAttributeValue()

double Device::getDeviceExternalAttributeValue  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Get device external attribute value. 

Returns
    double, attribute value 

## ◆ getGlobalXPhysicalWS()

double Device::getGlobalXPhysicalWS  | ( | | ) |   
---|---|---|---|---  
  
Returns the current global x-coordinate position in the Physical workspace for this device. 

Returns
    double, the current global x-cordinate. 

## ◆ getGlobalYPhysicalWS()

double Device::getGlobalYPhysicalWS  | ( | | ) |   
---|---|---|---|---  
  
Returns the current global y-coordinate position in the Physical workspace for this device. 

Returns
    double, the current global y-coordinate. 

## ◆ getModel()

string Device::getModel  | ( | | ) |   
---|---|---|---|---  
  
Returns the model of this device. 

Returns
    string, the model of this device. 

## ◆ getName()

QString Device::getName  | ( | | ) |   
---|---|---|---|---  
  
Returns the display name of this device. 

Returns
    QString, the display name of this device. 

## ◆ getPhysicalObject()

[PhysicalObject](class_physical_object.html) Device::getPhysicalObject  | ( | | ) |   
---|---|---|---|---  
  
Get custom interface name on the device. 

Returns
    QString, the custom interface name 

## ◆ getPort()

[Port](class_port.html) Device::getPort  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the [Port](class_port.html "Port holds and manipulates the ports on devices.") object with the specified port name. 

Parameters
     portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
---|---  
  
Returns
    [Port](class_port.html "Port holds and manipulates the ports on devices."), the [Port](class_port.html "Port holds and manipulates the ports on devices.") object associated with the port name. 

## ◆ getPortAt()

[Port](class_port.html) Device::getPortAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the [Port](class_port.html "Port holds and manipulates the ports on devices.") object at the specified index. 

Parameters
     int| index, the index of the port of interest.  
---|---  
  
Returns
    [Port](class_port.html "Port holds and manipulates the ports on devices."), the [Port](class_port.html "Port holds and manipulates the ports on devices.") object at the specified index. 

## ◆ getPortCount()

int Device::getPortCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of ports in this device. 

Returns
    int, the number of ports in this device. 

## ◆ getPorts()

vector< string > Device::getPorts  | ( | | ) |   
---|---|---|---|---  
  
Set time to the device. 

Returns
    vector<string>, vector of port names in string format 

## ◆ getPower()

bool Device::getPower  | ( | | ) |   
---|---|---|---|---  
  
Returns the current power state of this device. 

Returns
    bool, true if the power is on, otherwise false. 

## ◆ getProcess()

[Process](class_process.html) Device::getProcess  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the [Process](class_process.html "Process is the base class for all device processes.") object associated the process name. 

Parameters
     process,the| name of the process. Valid process names. Not all names have an interface to interact with. Only get names for which there are interfaces. The word "Process" is optional and may be appended to the end or ommitted.: Aaa, AcsServer, RadiusClient, RadiusServer, TacacsClient, TacacsServer, [Acl](class_acl.html "Acl holds and manipulates AclStatements."), Aclv6, PingTcp, Settings, AnalogPhoneHandler, AnalogPhone, ArpLookUp, Arp, AsaAcl, AsaAclv6, Firewall, Firewallv6, AsaNat, AsaNatv6, Bgp, [BluetoothManager](class_bluetooth_manager.html "BluetoothManager."), CustomBluetooth, Bridge, [BVIManager](class_b_v_i_manager.html "BVIManager holds and manipulates BVIs on an embedded access point on a router."), CapwapAC, Capwap, [Cbac](class_cbac.html "Cbac holds and manipulates Context-based access control."), Cbacv6, Cdp, CellularClientManager, CellularClient, Cellular, COPapChapAuthenticator, [ParserViewManager](class_parser_view_manager.html "ParserViewManager manages and manipulates the parser view."), [PrivilegeManager](class_privilege_manager.html "PrivilegeManager handles and manipulates privileges on routers and switches."), PortMapped, DhcpClient, DhcpRelayAgent, DhcpServerMain, DhcpServer, DhcpSnoopingBindingDBAgent, DhcpSnooping, Dhcpv6Client, Dhcpv6Main, Dhcpv6ServerMain, Dhcpv6Server, [DnsClient](class_dns_client.html "DnsClient is the process that handles retrieving DNS lookups."), DnsResolver, DnsServer, Dtp, EigrpMain, Eigrp, Eigrpv6Main, Eigrpv6, EtherChannel, EtherChannelDispatcher, EtherChannelManager, Lacp, Pagp, CsmaCd, Dot1QEncap, Dot1QSubIntDispatcher, EthernetEncap, [FileManager](class_file_manager.html "FileManager holds and manipulates the file manager process on routers and switches."), DlciLookUp, FrameRelayMain, FrameRelay, FRSubIntDispatcher, InvArp, [LmiSignaling](class_lmi_signaling.html), FtpClient, [FtpServer](class_ftp_server.html "FtpServer is the process that handles the FTP service."), Gre, TunnelInterface, [Hdlc](class_hdlc.html), Hsrp, Hsrpv6, [HttpBackgroundClient](class_http_background_client.html), [HttpBackgroundClientManager](class_http_background_client_manager.html), [HttpClient](class_http_client.html "HttpClient handles and manipulates the HTTP client on devices."), HttpProxy, [HttpServer](class_http_server.html "HttpServer handles and manipulates the HTTP server on devices."), [HttpsServer](class_https_server.html "HttpsServer handles and manipulates the HTTPS server on devices."), IoxServer, WebSocketClient, Wlc2504HttpsServer, Wlc2504Server, Icmp, Ping, TraceRoute, Icmpv6, [CustomIO](class_custom_i_o.html "CustomIO holds and manipulates the CustomIO on IoE devices."), IoeClient, [IoEComponent](class_io_e_component.html "IoEComponent holds and manipulates the IoEComponent on IoE devices."), [Ioe](class_ioe.html), IoeServer, IoeUserManager, IoxGuestOs, UserApp, UserJsApp, UserPyApp, [HostIp](class_host_ip.html "HostIp handles and manipulates the default gateway on end devices."), IpFragmentation, Ips, [HostIpv6](class_host_ipv6.html), Ipv6Fragmentation, PMTUDiscovery, Ipv6Ip, [IsatapClient](class_isatap_client.html "IsatapClient is the class that handles the ISATAP client."), L2Nat, LinksysRouterEventHandler, Lldp, Loopback, [LoopbackManager](class_loopback_manager.html "LoopbackManager is the process that manages loopback interfaces."), [EmailClient](class_email_client.html "EmailClient is the process that handles the email client."), [EmailServer](class_email_server.html "EmailServer is the process that handles the email server."), Nat, NatV6, Nd, NeighborLookUp, Netflow, Netflowv6, NFCollector, [NFExporter](class_n_f_exporter.html "NFExporter handles and manipulates NetFlow exporters."), NtpClient, NtpServer, OspfMain, Ospf, Ospfv3Main, Ospfv3, [Pop3Client](class_pop3_client.html "Pop3Client handles and manipulates POP3 clients."), [Pop3Server](class_pop3_server.html "Pop3Server handles and manipulates POP3 servers."), InterfaceStatus, PortKeepAlive, Chap, PAP, [PhoneSignaling](class_phone_signaling.html), PppMain, Ppp, DialerInterface, DialerInterfaceManager, [PppoeClient](class_pppoe_client.html "PppoeClient handles and manipulates the PPPoE client."), PppoeClientManager, Pppoe, PppoeServer, VirtualAccessInterface, [VirtualTemplateInterface](class_virtual_template_interface.html "VirtualTemplateInterface handles and manipulates individual virtual template interfaces for PPPoE."), [VirtualTemplateManager](class_virtual_template_manager.html "VirtualTemplateManager manages and manipulates virtual template interfaces for PPPoE."), PTP, Rep, [CableSignaling](class_cable_signaling.html), CloudSwitcher, [DslSignaling](class_dsl_signaling.html), Forwarding, LoopBreaker, PatchWire, Repeater, Rip, Ripv6Main, Ripv6, IpUnnumberDispatcher, PortDispatcher, Routing, [RoutingProtocol](class_routing_protocol.html "RoutingProtocol is the base class for routing protocol processes."), [RoutingProcessv6](class_routing_processv6.html), Security, [SmtpClient](class_smtp_client.html "SmtpClient handles and manipulates the SMTP client."), [SmtpServer](class_smtp_server.html "SmtpServer handles and manipulates the SMTP service."), [SnmpAgent](class_snmp_agent.html "SnmpAgent holds and manipulates the SNMP agent."), SnmpManager, SshClient, SshServer, StpMain, Stp, MacSwitcher, [PortSecurity](class_port_security.html "PortSecurity handles and manipulates port security on switch ports."), SdmManager, Span, SpanDest, SpanDestLocalPort, SpanSource, SpanSourceLocalPort, SpanSourceLocalPortChannel, SpanSourceLocalVlan, [VlanManager](class_vlan_manager.html "VlanManager holds and manipulates VLANs on routers and switches."), WLCMacSwitcher, SyslogClient, [SyslogServer](class_syslog_server.html "SyslogServer handles and manipulates the Syslog service."), CustomTcp, Tcp, TcpUserTraffic, ReverseTelnet, TelnetClient, TelnetServer, TftpClient, [TftpServer](class_tftp_server.html "TftpServer handles and manipulates the TFTP service."), TftpSession, TftpSessionManager, Tv, CustomUdp, Udp, UdpTraceRoute, [UsbController](class_usb_controller.html "UsbController."), CME, H323Client, H323, H323Server, PhoneMedia, Rtp, SccpClient, SccpServer, VoiceSwitcher, Ah, [EasyVpnClient](class_easy_vpn_client.html "EasyVpnClient is the process that handles the Easy VPN client."), EasyVpnServer, Esp, Ike, Ipsec, Vtp, AccessPointSwitcher, CsmaCa, LWAccessPointSwitcher, LWWirelessServer, WEP, WirelessClient, [WirelessCommon](class_wireless_common.html "WirelessCommon handles and manipulates common wireless settings."), WirelessEncap, WirelessServerManager, WirelessServer, WLCServer, WPA, Zfw, Zfwv6  
---|---  
  
Returns
    [Process](class_process.html "Process is the base class for all device processes."), the [Process](class_process.html "Process is the base class for all device processes.") object associated with the process name. 

## ◆ getProgrammingSerialOutputs()

string Device::getProgrammingSerialOutputs  | ( | | ) |   
---|---|---|---|---  
  
Gets the programming output. It is the text that appears in the programming output dialog. 

Returns
    string, value is the text that appears in the programming output dialog. 

## ◆ getRootModule()

[Module](class_module.html) Device::getRootModule  | ( | | ) |   
---|---|---|---|---  
  
Returns the root module of the device. 

Returns
    [Module](class_module.html), The root module object. 

## ◆ getSerialNumber()

string Device::getSerialNumber  | ( | | ) |   
---|---|---|---|---  
  
Returns the device serial number. 

Returns
    string, device serial number in string format 

## ◆ getSupportedModule()

vector< string > Device::getSupportedModule  | ( | | ) |   
---|---|---|---|---  
  
Get a vector of supported modules. 

Returns
    vector<string>, a vector of supported module info with id and image path name in string format 

## ◆ getType()

DeviceType Device::getType  | ( | | ) |   
---|---|---|---|---  
  
Returns the type of this device. 

Returns
    enum<DeviceType>, the type of this device. [Device](class_device.html "Device is the base class for all device objects.") types: eRouter = 0, eSwitch = 1, eCloud = 2, eBridge = 3, eHub = 4, eRepeater = 5, eCoAxialSplitter = 6, eAccessPoint = 7, ePc = 8, eServer = 9, ePrinter = 10, eWirelessRouter = 11, eIpPhone = 12, eDslModem = 13, eCableModem = 14, eRemoteNetwork = 15, eMultiLayerSwitch = 16, eSwitch3650 = 17, eLaptop = 18, eTabletPC = 19, ePda = 20, eWirelessEndDevice = 21, eWiredEndDevice = 22, eTV = 23, eHomeVoip = 24, eAnalogPhone = 25, eMultiUser = 26, eASA = 27, eIoE = 28, eHomeGateway = 29, eWirelessRouterNewGeneration = 30, eCellTower = 31, eCentralOfficeServer = 32, eCiscoAccessPoint = 33, eEmbeddedCiscoAccessPoint = 34, eSniffer = 35, eMCU = 36, eSBC = 37, eThing = 38, eMCUComponent = 39, eEmbeddedServer = 40, eWirelessLanController = 41, eCluster = 42, eGeoIcon = 43, eLightWeightAccessPoint = 44, ePowerDistributionDevice = 45, ePatchPanel = 46, eWallMount = 47, eSecurityAppliance = 48, eMerakiServer = 49 

## ◆ getUpTime()

long Device::getUpTime  | ( | | ) |   
---|---|---|---|---  
  
Set time to the device. 

Returns
    vector<string>, vector of port names in string format 

## ◆ getUsbPortAt()

[UsbPort](class_usb_port.html) Device::getUsbPortAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the usb port at a specified index. 

Returns
    int, index of the usb port 

## ◆ getUsbPortCount()

int Device::getUsbPortCount  | ( | | ) |   
---|---|---|---|---  
  
Return the number of usb port. 

Returns
    int, number of usb port 

## ◆ getUserDesktopAppAt()

[UserDesktopAppConfig](class_user_desktop_app_config.html) Device::getUserDesktopAppAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
## ◆ getUserDesktopAppByDir()

[UserDesktopAppConfig](class_user_desktop_app_config.html) Device::getUserDesktopAppByDir  | ( | string  | | ) |   
---|---|---|---|---|---  
  
## ◆ getUserDesktopAppById()

[UserDesktopAppConfig](class_user_desktop_app_config.html) Device::getUserDesktopAppById  | ( | string  | | ) |   
---|---|---|---|---|---  
  
## ◆ getUserDesktopAppCount()

int Device::getUserDesktopAppCount  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getXCoordinate()

double Device::getXCoordinate  | ( | | ) |   
---|---|---|---|---  
  
Returns the current x-coordinate position in the Logical workspace for this device. 

Returns
    double, the current x-coordinate. 

## ◆ getXPhysicalWS()

int Device::getXPhysicalWS  | ( | | ) |   
---|---|---|---|---  
  
Returns the current x-coordinate position in the Physical workspace for this device. 

Returns
    int, the current x-cordinate. 

## ◆ getYCoordinate()

double Device::getYCoordinate  | ( | | ) |   
---|---|---|---|---  
  
Returns the current y-coordinate position in the Logical workspace for this device. 

Returns
    double, the current y-coordinate. 

## ◆ getYPhysicalWS()

int Device::getYPhysicalWS  | ( | | ) |   
---|---|---|---|---  
  
Returns the current y-coordinate position in the Physical workspace for this device. 

Returns
    int, the current y-coordinate. 

## ◆ hasCustomVar()

bool Device::hasCustomVar  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns true if this device has a custom variable with the specified name. 

Parameters
     name,the| name of the variable of interest.  
---|---  
var,true| if this device has a custom variable with the specified name.   
  
## ◆ isDesktopAvailable()

bool Device::isDesktopAvailable  | ( | | ) |   
---|---|---|---|---  
  
## ◆ isOutdated()

bool Device::isOutdated  | ( | | ) |   
---|---|---|---|---  
  
## ◆ isProjectRunning()

bool Device::isProjectRunning  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Checks if a programming project with the given name is running. 

Parameters
     projectName,The| name of the project to check is running. Something like "Blink (JavaScript)"  
---|---  
  
Returns
    bool, value is true if the project was found running, false if not. 

## ◆ moduleAdded()

void Device::moduleAdded  | ( | ModuleType  | ,   
---|---|---|---  
|  | string  | ,   
|  | string  |   
| ) | |   
  
This event is emitted when a module is added. 

  * type, the type of module. [Module](class_module.html) types: eLineCard = 0, eNetworkModule = 1, eInterfaceCard = 2, ePtRouterModule = 3, ePtSwitchModule = 4, ePtCloudModule = 5, ePtRepeaterModule = 6, ePtHostModule = 7, ePtModemModule = 8, ePtLaptopModule = 9, ePtTVModule = 10, eIpPhonePowerAdapter = 11, ePtTabletPCModule = 12, ePtPdaModule = 13, ePtWirelessEndDeviceModule = 14, ePtWiredEndDeviceModule = 15, eTrs35 = 16, eUsb = 17, eNonRemovableModule = 18, eASAPowerAdapter = 19, eCustomModuleType = 2000 
  * model, the model of the module.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ moduleRemoved()

void Device::moduleRemoved  | ( | ModuleType  | ,   
---|---|---|---  
|  | string  | ,   
|  | string  |   
| ) | |   
  
This event is emitted when a module is removed. 

  * type, the type of module. [Module](class_module.html) types: eLineCard = 0, eNetworkModule = 1, eInterfaceCard = 2, ePtRouterModule = 3, ePtSwitchModule = 4, ePtCloudModule = 5, ePtRepeaterModule = 6, ePtHostModule = 7, ePtModemModule = 8, ePtLaptopModule = 9, ePtTVModule = 10, eIpPhonePowerAdapter = 11, ePtTabletPCModule = 12, ePtPdaModule = 13, ePtWirelessEndDeviceModule = 14, ePtWiredEndDeviceModule = 15, eTrs35 = 16, eUsb = 17, eNonRemovableModule = 18, eASAModule = 19, eASAPowerAdapter = 20   

  * model, the model of the module.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ moveByInPhysicalWS()

bool Device::moveByInPhysicalWS  | ( | int  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Moves this device by the specified amount in Physical workspace. 

Parameters
     x,the| x-amount to move by.   
---|---  
y,the| y-amount to move by.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ moveToLocation()

bool Device::moveToLocation  | ( | int  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Moves this device to the specified location in Logical workspace. 

Parameters
     x,the| new x-coordinate position.   
---|---  
y,the| new y-coordinate position.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ moveToLocationCentered()

bool Device::moveToLocationCentered  | ( | int  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Moves this device to the specified location for its center in Logical workspace. 

Parameters
     x,the| new x-coordinate position.   
---|---  
y,the| new y-coordinate position.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ moveToLocInPhysicalWS()

bool Device::moveToLocInPhysicalWS  | ( | int  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Moves this device to the specified location in Physical workspace. 

Parameters
     x,the| new x-coordinate position.   
---|---  
y,the| new y-coordinate position.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ nameChanged()

void Device::nameChanged  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

This event is emitted when the display name is changed.

  * newName, the new name of this device. 
  * oldName, the old name of this device. 



## ◆ playSound()

void Device::playSound  | ( | QString  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Play sound to the device. 

Parameters
     soundID,the| id of the sounpath to the sound file  
---|---  
numLoop,the| number of times to play the sound   
  
## ◆ portAdded()

void Device::portAdded  | ( | string  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when a port is added. 

Parameters
     portName,the| name of the port that was added.  
---|---  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ portRemoved()

void Device::portRemoved  | ( | string  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when a port is removed. 

Parameters
     portName,the| name of the port that was removed.  
---|---  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ portRemoving()

void Device::portRemoving  | ( | string  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when a port is being removed but before it is actually removed. This is useful for script modules to clean up things before the port is removed. 

Parameters
     portName,the| name of the port that is being removed.  
---|---  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ powerChanged()

void Device::powerChanged  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

This event is emitted when the power is changed.

  * on, the new power state. 



## ◆ poweringOff()

void Device::poweringOff  | ( | | ) |   
---|---|---|---|---  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

This event is emitted when the power is turning off but before all processes are cleared. It is useful for script modules to clean up before everything else. 

## ◆ relinkUserDesktopApp()

void Device::relinkUserDesktopApp  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
## ◆ removeCustomVar()

bool Device::removeCustomVar  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Removes a custom variable. 

Parameters
     name,the| name of the variable.  
---|---  
  
Returns
    bool, true if successful, otherwise, false. 

## ◆ removeModule()

bool Device::removeModule  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes the module from the slot. 

Parameters
     slot,the| slot to remove the module from.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ removeUserDesktopApp()

void Device::removeUserDesktopApp  | ( | string  | | ) |   
---|---|---|---|---|---  
  
## ◆ restoreToDefault()

bool Device::restoreToDefault  | ( | bool  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
## ◆ runCodeInProject()

bool Device::runCodeInProject  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Runs additional code in the given project. 

Parameters
     projectName,The| name of the project to run additional code in. Something like "Blink (JavaScript)"   
---|---  
code,the| code to run. If you were writing javascript you could output text like this. "Serial.println('testing output')"  
  
Returns
    bool, value is true if the project was found and the code was run, false if not. 

## ◆ runProject()

bool Device::runProject  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Runs a programming project in the mcu. 

Parameters
     projectName,The| name of the project to run. Something like "Blink (JavaScript)"   
---|---  
extraCode,does| nothing.  
  
Returns
    bool, value is true if the project existed and was started, false if not. 

## ◆ serializeToXml()

QString Device::serializeToXml  | ( | | ) |   
---|---|---|---|---  
  
Returns the serialization string of this device. 

Parameters
     QString,the| serialization string of this device.   
---|---  
  
## ◆ setCustomInterface()

void Device::setCustomInterface  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Set custom interface to the device. 

Parameters
     QString,the| custom interface name   
---|---  
  
## ◆ setCustomLogicalImage()

void Device::setCustomLogicalImage  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Set custom logical image path. 

Parameters
     strPath,the| path to the custom logical image   
---|---  
  
## ◆ setCustomPhysicalImage()

void Device::setCustomPhysicalImage  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Set custom physical image path. 

Parameters
     strPath,custom| physical image name in string   
---|---  
  
## ◆ setDeviceExternalAttributes()

void Device::setDeviceExternalAttributes  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Set device external attribute value. 

Parameters
     attributeValues,QString| attribute value pair in json format   
---|---  
  
## ◆ setName()

void Device::setName  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Sets the display name of this device. 

Parameters
     name,the| display name string.   
---|---  
  
## ◆ setPower()

void Device::setPower  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Sets the power on or off. 

Parameters
     bOn,true| to set the power on, false to set the power off.   
---|---  
  
## ◆ setTime()

void Device::setTime  | ( | int  | ,   
---|---|---|---  
|  | int  | ,   
|  | int  | ,   
|  | int  | ,   
|  | int  | ,   
|  | int  |   
| ) | |   
  
Set time to the device. 

Parameters
     iuHour,hour| in integer  
---|---  
uiMin,minute| in integer  
uiSec,second| in integer  
uiDay,day| in integer  
uiMonth,month| in integer  
uiYear,year| in integer   
  
## ◆ stopProject()

bool Device::stopProject  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Stops a programming project in the mcu. 

Parameters
     projectName,The| name of the project to stop. Something like "Blink (JavaScript)"  
---|---  
  
Returns
    bool, value is true if the project was found and stopped, false if not. 

## ◆ stopSound()

void Device::stopSound  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Stop playing sound on the device. 

Parameters
     soundID,the| id of the sounpath to the sound file   
---|---  
  
## ◆ stopSounds()

void Device::stopSounds  | ( | | ) |   
---|---|---|---|---  
  
Stops playing all sounds on the device. 

## ◆ subtractDeviceExternalAttributes()

void Device::subtractDeviceExternalAttributes  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Remove some of the device external attribute value pairs from the current list. 

Parameters
     attributeValues,QString| attribute value pair in json format   
---|---  
  
## ◆ updateTemplateCreationTime()

void Device::updateTemplateCreationTime  | ( | | ) |   
---|---|---|---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CDevice.pki](_c_device_8pki.html)


