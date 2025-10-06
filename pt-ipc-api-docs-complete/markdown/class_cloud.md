# Cisco Packet Tracer Extensions API: Cloud Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_cloud.html

---

[Cloud](class_cloud.html "Cloud is a cloud device.") is a cloud device. [More...](class_cloud.html#details)

##  Public Member Functions  
  
---  
bool | [addPhoneConnection](class_cloud.html#a9843ff13ba839d2f4952d52d15bc0226) (string, string)  
| Associates a phone number to a port. [More...](class_cloud.html#a9843ff13ba839d2f4952d52d15bc0226)  
  
void | [removePhoneConnection](class_cloud.html#acd5da8935aefabdd4de11b2b0e090491) (string)  
| Removes the phone number from the port. [More...](class_cloud.html#acd5da8935aefabdd4de11b2b0e090491)  
  
bool | [addSubLinkConnection](class_cloud.html#acd732270fdb26a206caa7eca98805de7) (string, string, string, string)  
| Adds a sublink connection between the two specified ports. [More...](class_cloud.html#acd732270fdb26a206caa7eca98805de7)  
  
bool | [removeSubLinkConnection](class_cloud.html#ae52f696bda4e21f4451e27fa88f4d5a3) (string, string)  
| Removes the sublink connection. [More...](class_cloud.html#ae52f696bda4e21f4451e27fa88f4d5a3)  
  
bool | [addPortConnection](class_cloud.html#adeb451dc8fe4865bb62500d94dc9e275) (string, string)  
| Adds the port connection. [More...](class_cloud.html#adeb451dc8fe4865bb62500d94dc9e275)  
  
bool | [removePortConnection](class_cloud.html#a1c71360939573e571a15de02b8738f4b) (string)  
| Removes the port connection. [More...](class_cloud.html#a1c71360939573e571a15de02b8738f4b)  
  
bool | [removeAllPortConnection](class_cloud.html#ae11b961ed860f41237ae48fde4661dff) (string)  
| Removes all port connections. [More...](class_cloud.html#ae11b961ed860f41237ae48fde4661dff)  
  
bool | [setDslConnection](class_cloud.html#a745c73b4c106b83f9aaeed72f2153983) (string, bool)  
| Sets the DSL or cable connection. [More...](class_cloud.html#a745c73b4c106b83f9aaeed72f2153983)  
  
int | [getSubLinkConnectionCount](class_cloud.html#a35f6ce087e9b5e1920118b88cd23a6a9) ()  
| Return the number of sublink connection. [More...](class_cloud.html#a35f6ce087e9b5e1920118b88cd23a6a9)  
  
pair< [CloudSubLink](struct_cloud_sub_link.html), [CloudSubLink](struct_cloud_sub_link.html) > | [getSubLinkConnectionAt](class_cloud.html#a8e9424ab779f63dafb22b34351e28143) (int)  
| Return the Sublink Connection at an index. [More...](class_cloud.html#a8e9424ab779f63dafb22b34351e28143)  
  
int | [getPortConnectionCount](class_cloud.html#a253bc3b4022474e72e6413f07bed8342) ()  
| Return the number of port connections. [More...](class_cloud.html#a253bc3b4022474e72e6413f07bed8342)  
  
vector< string > | [getPortStrConnections](class_cloud.html#a231236c82c9151901e76a0cf287ef7ac) ()  
| Return a list of connection with port names. [More...](class_cloud.html#a231236c82c9151901e76a0cf287ef7ac)  
  
bool | [isDslConnection](class_cloud.html#a07dd7367f65ac12652147905319c4d4b) (string)  
| Check if the port is used in a Dsl Connection. [More...](class_cloud.html#a07dd7367f65ac12652147905319c4d4b)  
  
void | [removeSubLinkConnectionAt](class_cloud.html#a1490f28e8b7f5fcab9f8246f5286decf) (int)  
| Remove sublink connection at an index. [More...](class_cloud.html#a1490f28e8b7f5fcab9f8246f5286decf)  
  
vector< string > | [getSubLinkConnectionInfo](class_cloud.html#af71c5f190fb3282f3217881be3ef87c0) ()  
| Get Sublink Connection Info (from port, from sublink, to port, to sublink) [More...](class_cloud.html#af71c5f190fb3282f3217881be3ef87c0)  
  
int | [getHardwareQueueCount](class_cloud.html#a57f5c71ed9f09a44d2fa605bf80899ad) ()  
| Get the number of hardware queue. [More...](class_cloud.html#a57f5c71ed9f09a44d2fa605bf80899ad)  
  
[HardwareQueue](class_hardware_queue.html) | [getHardwareQueueAt](class_cloud.html#a6270e97379f8e068690441902c544a6c) (int)  
| Remove hardware queue at an index. [More...](class_cloud.html#a6270e97379f8e068690441902c544a6c)  
  
Public Member Functions inherited from [Device](class_device.html)  
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

[Cloud](class_cloud.html "Cloud is a cloud device.") is a cloud device. 

## Member Function Documentation

## ◆ addPhoneConnection()

bool Cloud::addPhoneConnection  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Associates a phone number to a port. 

Parameters
     number,the| telephone number. The format is 5551239999.   
---|---  
portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ addPortConnection()

bool Cloud::addPortConnection  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Adds the port connection. 

Parameters
     portName1,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0   
---|---  
portName2,see| portName1 description.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ addSubLinkConnection()

bool Cloud::addSubLinkConnection  | ( | string  | ,   
---|---|---|---  
|  | string  | ,   
|  | string  | ,   
|  | string  |   
| ) | |   
  
Adds a sublink connection between the two specified ports. 

Parameters
     portName1,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0   
---|---  
subLinkName1,the| name of the sublink associated to portName1.   
portName2,see| portName1 description.   
subLinkName1,the| name of the sublink associated to portName2.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ getHardwareQueueAt()

[HardwareQueue](class_hardware_queue.html) Cloud::getHardwareQueueAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Remove hardware queue at an index. 

Parameters
     index,the| index at which the hardware queue is at  
---|---  
  
Returns
    [HardwareQueue](class_hardware_queue.html), [HardwareQueue](class_hardware_queue.html) object 

## ◆ getHardwareQueueCount()

int Cloud::getHardwareQueueCount  | ( | | ) |   
---|---|---|---|---  
  
Get the number of hardware queue. 

Returns
    int, number of hardware queue 

## ◆ getPortConnectionCount()

int Cloud::getPortConnectionCount  | ( | | ) |   
---|---|---|---|---  
  
Return the number of port connections. 

Returns
    int, number of port connection 

## ◆ getPortStrConnections()

vector< string > Cloud::getPortStrConnections  | ( | | ) |   
---|---|---|---|---  
  
Return a list of connection with port names. 

Returns
    vector<string>, list of connection with port names 

## ◆ getSubLinkConnectionAt()

pair< [CloudSubLink](struct_cloud_sub_link.html), [CloudSubLink](struct_cloud_sub_link.html) > Cloud::getSubLinkConnectionAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Return the Sublink Connection at an index. 

Parameters
     index,the| index location in the queue of the desired sublink connection  
---|---  
  
Returns
    pair<CloudSubLink, CloudSubLink>, from and to sublink pair 

## ◆ getSubLinkConnectionCount()

int Cloud::getSubLinkConnectionCount  | ( | | ) |   
---|---|---|---|---  
  
Return the number of sublink connection. 

Returns
    int, number of sublink connection 

## ◆ getSubLinkConnectionInfo()

vector< string > Cloud::getSubLinkConnectionInfo  | ( | | ) |   
---|---|---|---|---  
  
Get Sublink Connection Info (from port, from sublink, to port, to sublink) 

Returns
    vector<string>, list of sublink connection info in string format 

## ◆ isDslConnection()

bool Cloud::isDslConnection  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Check if the port is used in a Dsl Connection. 

Returns
    vector<string>, list of connection with port names 

## ◆ removeAllPortConnection()

bool Cloud::removeAllPortConnection  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes all port connections. 

Parameters
     portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ removePhoneConnection()

void Cloud::removePhoneConnection  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes the phone number from the port. 

Parameters
     number,the| telephone number to remove.   
---|---  
  
## ◆ removePortConnection()

bool Cloud::removePortConnection  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes the port connection. 

Parameters
     portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ removeSubLinkConnection()

bool Cloud::removeSubLinkConnection  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Removes the sublink connection. 

Parameters
     portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0   
---|---  
subLinkName,the| name of the sublink associated to portName.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ removeSubLinkConnectionAt()

void Cloud::removeSubLinkConnectionAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Remove sublink connection at an index. 

Parameters
     index,the| index at which the sublink connection should be removed  
---|---  
  
Returns
    none 

## ◆ setDslConnection()

bool Cloud::setDslConnection  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Sets the DSL or cable connection. 

Parameters
     portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0   
---|---  
bDsl,true| for DSL connection, false for cable connection.  
  
Returns
    bool, true if successful, otherwise false. 

* * *

The documentation for this class was generated from the following file:

  * [CCloud.pki](_c_cloud_8pki.html)


