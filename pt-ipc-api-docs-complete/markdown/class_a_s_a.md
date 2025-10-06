# Cisco Packet Tracer Extensions API: ASA Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_a_s_a.html

---

[ASA](class_a_s_a.html "ASA is the base class for all ASA devices.") is the base class for all [ASA](class_a_s_a.html "ASA is the base class for all ASA devices.") devices. [More...](class_a_s_a.html#details)

##  Public Member Functions  
  
---  
[AsaWebvpnUserManager](class_asa_webvpn_user_manager.html) | [getWebvpnUserManager](class_a_s_a.html#aef674507994c447e3004c8590fdd1514) ()  
| Returns the [ASA](class_a_s_a.html "ASA is the base class for all ASA devices.") Web VPN User Manager object. [More...](class_a_s_a.html#aef674507994c447e3004c8590fdd1514)  
  
bool | [addBookmark](class_a_s_a.html#afb7e1cf1b696be415289e8b33a5367d5) (string, string)  
| Returns true if the bookmark with the specified title and URL was added successfully, otherwise false. [More...](class_a_s_a.html#afb7e1cf1b696be415289e8b33a5367d5)  
  
bool | [removeBookmark](class_a_s_a.html#a7995662630beed06c7f2825865a4dd95) (string)  
| Returns true if the bookmark with the specified title was removed successfully, otherwise false. [More...](class_a_s_a.html#a7995662630beed06c7f2825865a4dd95)  
  
int | [getBookmarkCount](class_a_s_a.html#a0f3ae5b6e5db9807152bb28dd1cb4b04) ()  
| Returns the number of bookmarks. [More...](class_a_s_a.html#a0f3ae5b6e5db9807152bb28dd1cb4b04)  
  
string | [getBookmarkList](class_a_s_a.html#aa687ba3492b7608bbad6de145c93820a) ()  
| Returns a comma-separated list of bookmarks. [More...](class_a_s_a.html#aa687ba3492b7608bbad6de145c93820a)  
  
string | [getBookmarkUrl](class_a_s_a.html#adc22a27d4b3f3c73191ad9cee62d69a8) (string)  
| Returns the URL of the specified bookmark. [More...](class_a_s_a.html#adc22a27d4b3f3c73191ad9cee62d69a8)  
  
Public Member Functions inherited from [CiscoDevice](class_cisco_device.html)  
void | [setHostName](class_cisco_device.html#a4667368ed5e5255d92576174e718e60c) (string)  
| Sets the hostname of this device with the specified string. [More...](class_cisco_device.html#a4667368ed5e5255d92576174e718e60c)  
  
string | [getHostName](class_cisco_device.html#ab9bee21aa39105170881ea936f49f9f2) ()  
| Returns the hostname of this device. [More...](class_cisco_device.html#ab9bee21aa39105170881ea936f49f9f2)  
  
void | [setEnableSecret](class_cisco_device.html#afe9516c637aeb658332ff5a59e1f35b0) (string)  
| Sets the encrypted enable secret password with the specified string. [More...](class_cisco_device.html#afe9516c637aeb658332ff5a59e1f35b0)  
  
string | [getEnableSecret](class_cisco_device.html#a47ad8815ab1e3c0146839a2553632d33) ()  
| Returns the encrypted enable secret string. [More...](class_cisco_device.html#a47ad8815ab1e3c0146839a2553632d33)  
  
void | [setEnablePassword](class_cisco_device.html#ab81d776d046173cca8d78e85e1215775) (string, int)  
| Sets the enable password. [More...](class_cisco_device.html#ab81d776d046173cca8d78e85e1215775)  
  
string | [getEnablePassword](class_cisco_device.html#ae1766f3118ea6359b6169ad7e43422f2) ()  
| Returns the enable password. [More...](class_cisco_device.html#ae1766f3118ea6359b6169ad7e43422f2)  
  
void | [setStartupFile](class_cisco_device.html#add7b3257a1c4b4c8bc7b064a1a4771f3) (string)  
| Sets the startup file to the specified file. [More...](class_cisco_device.html#add7b3257a1c4b4c8bc7b064a1a4771f3)  
  
vector< string > | [getStartupFile](class_cisco_device.html#a4ce47dda936794018b7a2ac90b0b0f04) ()  
| Returns the contents of the current startup file. [More...](class_cisco_device.html#a4ce47dda936794018b7a2ac90b0b0f04)  
  
bool | [addBootSystem](class_cisco_device.html#a36706d1f6bcfc4373bd8124def6315db) (string)  
| Modifies the system parameters to add a particular boot system image. [More...](class_cisco_device.html#a36706d1f6bcfc4373bd8124def6315db)  
  
bool | [removeBootSystem](class_cisco_device.html#acd6b36e174e2a945fef3043d60b3df2a) (string)  
| Removes the specified boot system from this device. [More...](class_cisco_device.html#acd6b36e174e2a945fef3043d60b3df2a)  
  
void | [removeAllBootSystem](class_cisco_device.html#a290f1774f3025c3c41be5ca66d14d987) ()  
| Removes all boot system images from this device. [More...](class_cisco_device.html#a290f1774f3025c3c41be5ca66d14d987)  
  
vector< [BootSystemEntry](struct_boot_system_entry.html) > | [getBootSystems](class_cisco_device.html#a71e0fe74401b62d296c13a243462d0c6) ()  
| Returns the list of current boot system images. [More...](class_cisco_device.html#a71e0fe74401b62d296c13a243462d0c6)  
  
short | [getConfigRegister](class_cisco_device.html#a8637609432f5f1e875603c7e9884d58d) ()  
| Returns the current config register. [More...](class_cisco_device.html#a8637609432f5f1e875603c7e9884d58d)  
  
void | [setNextConfigRegister](class_cisco_device.html#a40445eaec281630772cc2063a097cc57) (short)  
| Sets the next config register. [More...](class_cisco_device.html#a40445eaec281630772cc2063a097cc57)  
  
short | [getNextConfigRegister](class_cisco_device.html#a37ae0099c98b6f464fb070c7dde404c7) ()  
| Returns the next config register. [More...](class_cisco_device.html#a37ae0099c98b6f464fb070c7dde404c7)  
  
void | [setBannerMotd](class_cisco_device.html#a3ad50e1d6bc6fcbfe71f09ec591fef30) (string)  
| Sets the message of the day banner when the device boots. [More...](class_cisco_device.html#a3ad50e1d6bc6fcbfe71f09ec591fef30)  
  
string | [getBannerMotd](class_cisco_device.html#a922d0da8141577d347944b71cc09eef3) ()  
| Returns the message of the day banner. [More...](class_cisco_device.html#a922d0da8141577d347944b71cc09eef3)  
  
void | [setTimeZone](class_cisco_device.html#a9a103186140a69d0a21e22367f6aedea) (string, short, short)  
| Sets the timezone for this device. [More...](class_cisco_device.html#a9a103186140a69d0a21e22367f6aedea)  
  
string | [getTimeZone](class_cisco_device.html#a0eec6f6d5dcf8199bb5c73c851dd2814) ()  
| Returns the timezone of this device. [More...](class_cisco_device.html#a0eec6f6d5dcf8199bb5c73c851dd2814)  
  
mac | [getBia](class_cisco_device.html#abd73b440a3ae0cffcb4ba34538253589) ()  
| Returns the burned-in address of this device. [More...](class_cisco_device.html#abd73b440a3ae0cffcb4ba34538253589)  
  
void | [setServicePasswordEncryption](class_cisco_device.html#aaedbbdded3153e48a21524572317beea) (bool)  
| Enables or disables service password encryption. [More...](class_cisco_device.html#aaedbbdded3153e48a21524572317beea)  
  
bool | [getServicePasswordEncryption](class_cisco_device.html#a0b264c1a9923fc257963191455dce56a) ()  
| Returns true if service password encryption is enabled, otherwise false. [More...](class_cisco_device.html#a0b264c1a9923fc257963191455dce56a)  
  
[Port](class_port.html) | [getConsole](class_cisco_device.html#a1be645264890a6400c85a5774429dac1) ()  
| Returns the console port of this device. [More...](class_cisco_device.html#a1be645264890a6400c85a5774429dac1)  
  
[TerminalLine](class_terminal_line.html) | [getConsoleLine](class_cisco_device.html#a906e2abc08dba7c28acf0084faf0021a) ()  
| Returns the console line of this device. [More...](class_cisco_device.html#a906e2abc08dba7c28acf0084faf0021a)  
  
[TerminalLine](class_terminal_line.html) | [getVtyLine](class_cisco_device.html#a86c1d3c5865776d6dd45b723e2719728) (int)  
| Returns the vty line specified by num. [More...](class_cisco_device.html#a86c1d3c5865776d6dd45b723e2719728)  
  
[TerminalLine](class_terminal_line.html) | [getLine](class_cisco_device.html#ab46d6fe3f36af50cace98edebcf2515d) (int)  
| Returns the line specified by num. [More...](class_cisco_device.html#ab46d6fe3f36af50cace98edebcf2515d)  
  
[TerminalLine](class_terminal_line.html) | [getIpcTerminalLine](class_cisco_device.html#ae5635a05465b7890be7a98b6a86fbdab) ()  
| Returns the [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") terminal line of this device. [More...](class_cisco_device.html#ae5635a05465b7890be7a98b6a86fbdab)  
  
pair< CommandStatus, string > | [enterCommand](class_cisco_device.html#a9ce1efd82618dd3d34aeec01906e633b) (string, string)  
| Enters the specified command in the specified mode to the terminal. [More...](class_cisco_device.html#a9ce1efd82618dd3d34aeec01906e633b)  
  
bool | [isBooting](class_cisco_device.html#afac16dd6a53645aff8579afaf26bcbc4) ()  
| Checks whether the device is currently booting. [More...](class_cisco_device.html#afac16dd6a53645aff8579afaf26bcbc4)  
  
void | [skipBoot](class_cisco_device.html#a6e658e4ed501ce6ae6e06399d8374bc5) ()  
| Skips the booting process. [More...](class_cisco_device.html#a6e658e4ed501ce6ae6e06399d8374bc5)  
  
void | [doneBooting](class_cisco_device.html#a0ba90431b159a77c4c63de66b1fffe7f) ()  
| This event is emitted when the device is done booting. [More...](class_cisco_device.html#a0ba90431b159a77c4c63de66b1fffe7f)  
  
void | [setFtpUsername](class_cisco_device.html#a9cb80e4f7477434f05cdb342f0343fdf) (string)  
| Sets the FTP username for the device. [More...](class_cisco_device.html#a9cb80e4f7477434f05cdb342f0343fdf)  
  
void | [setFtpPasswd](class_cisco_device.html#aa99ad1c7b35d76ac4d8ea3e1092b665b) (string, int)  
| Sets the FTP password for the device. [More...](class_cisco_device.html#aa99ad1c7b35d76ac4d8ea3e1092b665b)  
  
string | [getFtpUsername](class_cisco_device.html#ad4b7edccb272dbd2646d5ed03b5e52ac) ()  
| Returns the FTP username for the device. [More...](class_cisco_device.html#ad4b7edccb272dbd2646d5ed03b5e52ac)  
  
string | [getFtpPasswd](class_cisco_device.html#a91bba05b1820b812f0c8d1014a4d994f) ()  
| Returns the FTP password for the device. [More...](class_cisco_device.html#a91bba05b1820b812f0c8d1014a4d994f)  
  
void | [clearFtpUsername](class_cisco_device.html#a1865debaf39265bda24f1fcad8062f4d) ()  
| Clears the current FTP username. [More...](class_cisco_device.html#a1865debaf39265bda24f1fcad8062f4d)  
  
void | [clearFtpPasswd](class_cisco_device.html#a83a2b4c9896aa0e9d73b3d775b5f48d9) ()  
| Clears the current FTP password. [More...](class_cisco_device.html#a83a2b4c9896aa0e9d73b3d775b5f48d9)  
  
int | [getUserPassCount](class_cisco_device.html#a4969d7ef38de33e5c2b7d2ba97e3380b) ()  
| Returns the number of authenticated users. [More...](class_cisco_device.html#a4969d7ef38de33e5c2b7d2ba97e3380b)  
  
void | [addUserPassEntry](class_cisco_device.html#aa12fb9d2a3cec9dad8f9b4195042e96d) (string, string, int)  
| Adds an authenticated user with the specified username, password, and type. [More...](class_cisco_device.html#aa12fb9d2a3cec9dad8f9b4195042e96d)  
  
void | [removeUserPassEntry](class_cisco_device.html#a232e5d5e4fe71a03815c0cdbbaaf45de) (string)  
| Removes the authenticated user with the specified username. [More...](class_cisco_device.html#a232e5d5e4fe71a03815c0cdbbaaf45de)  
  
string | [getUserEntryAt](class_cisco_device.html#ac647ffe4ed7ec0bc33b202ade968ea2c) (int)  
| Returns the username of the authenticated user at the specified index. [More...](class_cisco_device.html#ac647ffe4ed7ec0bc33b202ade968ea2c)  
  
void | [removeUserPassAt](class_cisco_device.html#a6c9b9b102115fde4c748d5746858222a) (int)  
| Removes the username of the authenticated user at the specified index. [More...](class_cisco_device.html#a6c9b9b102115fde4c748d5746858222a)  
  
bool | [isUserExist](class_cisco_device.html#a38f54e7e64378344e5d3a68c233ed4e4) (string)  
| Returns true if the specified authenticated user exists, otherwise false. [More...](class_cisco_device.html#a38f54e7e64378344e5d3a68c233ed4e4)  
  
void | [lineConnected](class_cisco_device.html#a74be9caef8e425f9701fd602d6eb3d29) (int, ip, short, LoginMethod)  
| This event is emitted when a terminal line has connected. [More...](class_cisco_device.html#a74be9caef8e425f9701fd602d6eb3d29)  
  
void | [lineDisconnected](class_cisco_device.html#a90a2b854b27b3532d6ebac82c8f7b4fa) (int)  
| This event is emitted when a terminal line has disconnected. [More...](class_cisco_device.html#a90a2b854b27b3532d6ebac82c8f7b4fa)  
  
void | [lineAuthenticationStarted](class_cisco_device.html#adf1e3d0fd7b27f135cc4378da39b8971) (int, ip, short, LoginMethod)  
| This event is emitted when a terminal line has started authentication. [More...](class_cisco_device.html#adf1e3d0fd7b27f135cc4378da39b8971)  
  
void | [lineAuthenticationFailed](class_cisco_device.html#a2a4b654ac0c3d37766e72a834fd186fb) (int)  
| This event is emitted when a terminal line failed authentication. [More...](class_cisco_device.html#a2a4b654ac0c3d37766e72a834fd186fb)  
  
void | [lineAuthenticationFinished](class_cisco_device.html#aaf5e11762ba332699d22a84ac4162b68) (int, bool)  
| This event is emitted when a terminal line finished authentication. [More...](class_cisco_device.html#aaf5e11762ba332699d22a84ac4162b68)  
  
void | [closeTableEvent](class_cisco_device.html#aecd73ebef2ba385426fa3e790296ae6d) ()  
| [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. [More...](class_cisco_device.html#aecd73ebef2ba385426fa3e790296ae6d)  
  
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

[ASA](class_a_s_a.html "ASA is the base class for all ASA devices.") is the base class for all [ASA](class_a_s_a.html "ASA is the base class for all ASA devices.") devices. 

## Member Function Documentation

## ◆ addBookmark()

bool ASA::addBookmark  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Returns true if the bookmark with the specified title and URL was added successfully, otherwise false. 

/param title, the title for the bookmark. /param url, the URL for the bookmark.

Returns
    bool, true if the bookmark with the specified title and URL was added successfully, otherwise false. 

## ◆ getBookmarkCount()

int ASA::getBookmarkCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of bookmarks. 

Returns
    int, the number of bookmarks. 

## ◆ getBookmarkList()

string ASA::getBookmarkList  | ( | | ) |   
---|---|---|---|---  
  
Returns a comma-separated list of bookmarks. 

Returns
    string, a comma-separated list of bookmarks. 

## ◆ getBookmarkUrl()

string ASA::getBookmarkUrl  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the URL of the specified bookmark. 

Returns
    string, the URL of the specified bookmark. 

## ◆ getWebvpnUserManager()

[AsaWebvpnUserManager](class_asa_webvpn_user_manager.html) ASA::getWebvpnUserManager  | ( | | ) |   
---|---|---|---|---  
  
Returns the [ASA](class_a_s_a.html "ASA is the base class for all ASA devices.") Web VPN User Manager object. 

Returns
    [AsaWebvpnUserManager](class_asa_webvpn_user_manager.html "AsaWebvpnUserManager manages clientless VPN users on ASA devices."), the [AsaWebvpnUserManager](class_asa_webvpn_user_manager.html "AsaWebvpnUserManager manages clientless VPN users on ASA devices.") object. 

## ◆ removeBookmark()

bool ASA::removeBookmark  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns true if the bookmark with the specified title was removed successfully, otherwise false. 

/param title, the title for the bookmark.

Returns
    bool, true if the bookmark with the specified title was removed successfully, otherwise false. 

* * *

The documentation for this class was generated from the following file:

  * [CASA.pki](_c_a_s_a_8pki.html)


