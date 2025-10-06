# Cisco Packet Tracer Extensions API: IPC Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_i_p_c.html

---

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") is the main entry point for all [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") functionality. [More...](class_i_p_c.html#details)

##  Public Member Functions  
  
---  
[Network](class_network.html) | [network](class_i_p_c.html#a4a270952bc9162bb549059945bdc3c6c) ()  
| Returns the [Network](class_network.html "Network is the entry point for all device configurations in the network. It retrieves devices.") object. [More...](class_i_p_c.html#a4a270952bc9162bb549059945bdc3c6c)  
  
[AppWindow](class_app_window.html) | [appWindow](class_i_p_c.html#a8645f44c04897853c25fc9bb9fede240) ()  
| Returns the [AppWindow](class_app_window.html "AppWindow serves as the entry point to all GUI objects.") object. [More...](class_i_p_c.html#a8645f44c04897853c25fc9bb9fede240)  
  
[MultiUserManager](class_multi_user_manager.html) | [multiUserManager](class_i_p_c.html#a8647fd9d22c81415e5ee35a1267bba30) ()  
| Returns the [MultiUserManager](class_multi_user_manager.html "MultiUserManager is the entry point to all Multiuser functionalities.") object. [More...](class_i_p_c.html#a8647fd9d22c81415e5ee35a1267bba30)  
  
[IpcManager](class_ipc_manager.html) | [ipcManager](class_i_p_c.html#a650b2bd4f6861b4749941cdbaa4b3465) ()  
| Returns the [IpcManager](class_ipc_manager.html "IpcManager serves as the entry point for the IPC and manages ExApps and Script Modules.") object. [More...](class_i_p_c.html#a650b2bd4f6861b4749941cdbaa4b3465)  
  
[UserAppManager](class_user_app_manager.html) | [userAppManager](class_i_p_c.html#abec74c02a35bb9711e78851cd90ef3d7) ()  
| Returns the [UserAppManager](class_user_app_manager.html "User App Manager.") object. [More...](class_i_p_c.html#abec74c02a35bb9711e78851cd90ef3d7)  
  
[CommandLog](class_command_log.html) | [commandLog](class_i_p_c.html#aad69a47cdb667ec98934daaed981596b) ()  
| Returns the [CommandLog](class_command_log.html "CommandLog serves as the entry point to all command log objects.") object. [More...](class_i_p_c.html#aad69a47cdb667ec98934daaed981596b)  
  
[Simulation](class_simulation.html) | [simulation](class_i_p_c.html#aa3fa88a64835b67f1b1fed68cded5571) ()  
| Returns the [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") object. [More...](class_i_p_c.html#aa3fa88a64835b67f1b1fed68cded5571)  
  
[HardwareFactory](class_hardware_factory.html) | [hardwareFactory](class_i_p_c.html#ab115955f5b389154e5171eb39d3e916e) ()  
| Returns the Hardware Factory object. [More...](class_i_p_c.html#ab115955f5b389154e5171eb39d3e916e)  
  
Parser | [getObjectByUuid](class_i_p_c.html#ac99e8169ea6158e39748c73d9e29042e) (string)  
| Returns the [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") Parser object. [More...](class_i_p_c.html#ac99e8169ea6158e39748c73d9e29042e)  
  
[Options](class_options.html) | [options](class_i_p_c.html#ab70dac64d0bf0c8ebac0eefc0868e0b4) ()  
| options for the parsor. [More...](class_i_p_c.html#ab70dac64d0bf0c8ebac0eefc0868e0b4)  
  
[SystemFileManager](class_system_file_manager.html) | [systemFileManager](class_i_p_c.html#a21a6788c55bd7435f4db0e5031fa4568) ()  
| Returns the System [File](class_file.html "File holds and manipulates files on file systems.") Manager object for providing file IO. [More...](class_i_p_c.html#a21a6788c55bd7435f4db0e5031fa4568)  
  
  
## Detailed Description

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") is the main entry point for all [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") functionality. 

## Member Function Documentation

## ◆ appWindow()

[AppWindow](class_app_window.html) IPC::appWindow  | ( | | ) |   
---|---|---|---|---  
  
Returns the [AppWindow](class_app_window.html "AppWindow serves as the entry point to all GUI objects.") object. 

Returns
    [AppWindow](class_app_window.html "AppWindow serves as the entry point to all GUI objects."), the [AppWindow](class_app_window.html "AppWindow serves as the entry point to all GUI objects.") object. 

## ◆ commandLog()

[CommandLog](class_command_log.html) IPC::commandLog  | ( | | ) |   
---|---|---|---|---  
  
Returns the [CommandLog](class_command_log.html "CommandLog serves as the entry point to all command log objects.") object. 

Returns
    [CommandLog](class_command_log.html "CommandLog serves as the entry point to all command log objects."), the [CommandLog](class_command_log.html "CommandLog serves as the entry point to all command log objects.") object. 

## ◆ getObjectByUuid()

Parser IPC::getObjectByUuid  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") Parser object. 

Parameters
     uuid,the| UUID of the parser of interest.  
---|---  
  
Returns
    Parser, the Parser object. 

## ◆ hardwareFactory()

[HardwareFactory](class_hardware_factory.html) IPC::hardwareFactory  | ( | | ) |   
---|---|---|---|---  
  
Returns the Hardware Factory object. 

Returns
    [HardwareFactory](class_hardware_factory.html "Factory for all hardwares."), the Hardware Factory object. 

## ◆ ipcManager()

[IpcManager](class_ipc_manager.html) IPC::ipcManager  | ( | | ) |   
---|---|---|---|---  
  
Returns the [IpcManager](class_ipc_manager.html "IpcManager serves as the entry point for the IPC and manages ExApps and Script Modules.") object. 

Returns
    [IpcManager](class_ipc_manager.html "IpcManager serves as the entry point for the IPC and manages ExApps and Script Modules."), the [IpcManager](class_ipc_manager.html "IpcManager serves as the entry point for the IPC and manages ExApps and Script Modules.") object. 

## ◆ multiUserManager()

[MultiUserManager](class_multi_user_manager.html) IPC::multiUserManager  | ( | | ) |   
---|---|---|---|---  
  
Returns the [MultiUserManager](class_multi_user_manager.html "MultiUserManager is the entry point to all Multiuser functionalities.") object. 

Returns
    [MultiUserManager](class_multi_user_manager.html "MultiUserManager is the entry point to all Multiuser functionalities."), the [MultiUserManager](class_multi_user_manager.html "MultiUserManager is the entry point to all Multiuser functionalities.") object. 

## ◆ network()

[Network](class_network.html) IPC::network  | ( | | ) |   
---|---|---|---|---  
  
Returns the [Network](class_network.html "Network is the entry point for all device configurations in the network. It retrieves devices.") object. 

Returns
    [Network](class_network.html "Network is the entry point for all device configurations in the network. It retrieves devices."), the [Network](class_network.html "Network is the entry point for all device configurations in the network. It retrieves devices.") object. 

## ◆ options()

[Options](class_options.html) IPC::options  | ( | | ) |   
---|---|---|---|---  
  
options for the parsor. 

Parameters
     uuid,the| UUID of the parser of interest.  
---|---  
  
Returns
    [Options](class_options.html "Options contains the current running options for the application."), the parsor options object. 

## ◆ simulation()

[Simulation](class_simulation.html) IPC::simulation  | ( | | ) |   
---|---|---|---|---  
  
Returns the [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") object. 

Returns
    [CommandLog](class_command_log.html "CommandLog serves as the entry point to all command log objects."), the [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") object. 

## ◆ systemFileManager()

[SystemFileManager](class_system_file_manager.html) IPC::systemFileManager  | ( | | ) |   
---|---|---|---|---  
  
Returns the System [File](class_file.html "File holds and manipulates files on file systems.") Manager object for providing file IO. 

Returns
    [SystemFileManager](class_system_file_manager.html "SystemFileManager provides file IO to the local system."), the System [File](class_file.html "File holds and manipulates files on file systems.") Manager object. 

## ◆ userAppManager()

[UserAppManager](class_user_app_manager.html) IPC::userAppManager  | ( | | ) |   
---|---|---|---|---  
  
Returns the [UserAppManager](class_user_app_manager.html "User App Manager.") object. 

Returns
    [UserAppManager](class_user_app_manager.html "User App Manager."), the [UserAppManager](class_user_app_manager.html "User App Manager.") object. 

* * *

The documentation for this class was generated from the following file:

  * [CMainParser.pki](_c_main_parser_8pki.html)


