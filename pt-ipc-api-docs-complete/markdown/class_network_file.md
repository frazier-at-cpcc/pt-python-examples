# Cisco Packet Tracer Extensions API: NetworkFile Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_network_file.html

---

[NetworkFile](class_network_file.html "NetworkFile is the main system file for the application. It holds all the configurations for the engi...") is the main system file for the application. It holds all the configurations for the engine as well as the UI. [More...](class_network_file.html#details)

##  Public Member Functions  
  
---  
QString | [getSavedFilename](class_network_file.html#ad39db310fcbe9537acdb83cb2d0cc3a0) ()  
| Returns the filename of the currently opened file. [More...](class_network_file.html#ad39db310fcbe9537acdb83cb2d0cc3a0)  
  
QString | [getVersion](class_network_file.html#add899ff676d13c9cbb68e8e98ce89acd) ()  
| Returns the version the current file was saved in. [More...](class_network_file.html#add899ff676d13c9cbb68e8e98ce89acd)  
  
QString | [getNetworkDescription](class_network_file.html#ac31096b326e652e38fdc21b707ec14d2) ()  
| Returns the network description of the current file. [More...](class_network_file.html#ac31096b326e652e38fdc21b707ec14d2)  
  
void | [setNetworkDescription](class_network_file.html#a6026d74e5a7116cb545647b1c42b36c9) (QString)  
| Sets the network description for the current file. [More...](class_network_file.html#a6026d74e5a7116cb545647b1c42b36c9)  
  
[Options](class_options.html) | [getOptions](class_network_file.html#a926ba5389b2cb60cd95c7286654f47dc) ()  
| Returns the option settings of the current file. [More...](class_network_file.html#a926ba5389b2cb60cd95c7286654f47dc)  
  
[Network](class_network.html) | [getMainNetwork](class_network_file.html#a46ac622d2a6d64602a46b3e31e987f30) ()  
| Returns the network of the current file. [More...](class_network_file.html#a46ac622d2a6d64602a46b3e31e987f30)  
  
[UserProfile](class_user_profile.html) | [getUserProfile](class_network_file.html#a38c546e9debf684bdc2c953f9f7bdf9a) ()  
| Returns the user profile of the current file. [More...](class_network_file.html#a38c546e9debf684bdc2c953f9f7bdf9a)  
  
[Simulation](class_simulation.html) | [getMainSimulation](class_network_file.html#aa26979829f2dc835543ab93535c9fe67) ()  
| Returns the simulation of the current file. [More...](class_network_file.html#aa26979829f2dc835543ab93535c9fe67)  
  
[Workspace](class_workspace.html) | [getWorkspace](class_network_file.html#a10b424fdf82d159ab8f19d3330df9ae0) ()  
| Returns the workspace of the current file. [More...](class_network_file.html#a10b424fdf82d159ab8f19d3330df9ae0)  
  
[ActivityScriptEngine](class_activity_script_engine.html) | [getActivityScriptEngine](class_network_file.html#ae73eb5b0e7ec7e1bf702da7db6b9c4c0) ()  
| Returns the activity script engine of the current file. [More...](class_network_file.html#ae73eb5b0e7ec7e1bf702da7db6b9c4c0)  
  
[ActivityScriptEngine](class_activity_script_engine.html) | [getScriptEngine](class_network_file.html#a4b33c57dda5d441fd05f326601a1b427) ()  
| Returns the script engine of the current file. [More...](class_network_file.html#a4b33c57dda5d441fd05f326601a1b427)  
  
void | [resetScriptEngine](class_network_file.html#ab297523cea8744d42abfc1621dfcc568) ()  
| Removes the current activity script engine and creates a new one. [More...](class_network_file.html#ab297523cea8744d42abfc1621dfcc568)  
  
bool | [addScript](class_network_file.html#a54de70849c764976e7a84f45e8e801e6) (QString, QString)  
| Adds a script to the activity file. [More...](class_network_file.html#a54de70849c764976e7a84f45e8e801e6)  
  
bool | [addScriptFile](class_network_file.html#ae585096d5a909b477c81d2279569dce1) (QString, QString)  
| Adds the script contents to the activity file from a file path. [More...](class_network_file.html#ae585096d5a909b477c81d2279569dce1)  
  
void | [addDefaultScripts](class_network_file.html#a429ac3bcafa3fca82506b111198e66ac) ()  
| Resets the scripts to the default scripts. [More...](class_network_file.html#a429ac3bcafa3fca82506b111198e66ac)  
  
bool | [removeScript](class_network_file.html#aed9b12765b9fd44fc69d0144405f829f) (QString)  
| Removes the specified script from the activity file hash. [More...](class_network_file.html#aed9b12765b9fd44fc69d0144405f829f)  
  
QString | [getScript](class_network_file.html#ae5988d3f64efe5c4601c2b00d8773648) (QString)  
| Returns the content of the script with the specified ID. [More...](class_network_file.html#ae5988d3f64efe5c4601c2b00d8773648)  
  
vector< QString > | [getScriptIDs](class_network_file.html#a0060962a0f0f49c59e945c4a59b86a65) ()  
| Returns the list of IDs currently in the system. [More...](class_network_file.html#a0060962a0f0f49c59e945c4a59b86a65)  
  
bool | [addScriptDataStore](class_network_file.html#aa576377ab63aa1dc39e31041a7b4581b) (QString, QString)  
| Adds script data store for persistent storage (e.g. constants, options, settings). [More...](class_network_file.html#aa576377ab63aa1dc39e31041a7b4581b)  
  
bool | [removeScriptDataStore](class_network_file.html#a30e07d8196c8573d63f672def5570d35) (QString)  
| Removes the specified script data store for persistent storage (e.g. constants, options, settings). [More...](class_network_file.html#a30e07d8196c8573d63f672def5570d35)  
  
QString | [getScriptDataStore](class_network_file.html#ad280660efe843f30dee566c867920877) (QString)  
| Returns the content of the specified script data store. [More...](class_network_file.html#ad280660efe843f30dee566c867920877)  
  
vector< QString > | [getScriptDataStoreIDs](class_network_file.html#a0f1b26d4c4784eda8b34052546924cfb) ()  
| Returns the list of IDs of script data stores. [More...](class_network_file.html#a0f1b26d4c4784eda8b34052546924cfb)  
  
[FilterSet](class_filter_set.html) | [getFilterSet](class_network_file.html#ad9d6a773f3a77bbeda36f2728e14873d) ()  
| Returns the engine filter set for simulation packets, what is filtered out. [More...](class_network_file.html#ad9d6a773f3a77bbeda36f2728e14873d)  
  
bool | [addCustomTrafficType](class_network_file.html#a30bba52fe1d6fa46ed97742e85007140) (QString)  
| Adds a custom traffic type. Returns true if successful, false otherwise. [More...](class_network_file.html#a30bba52fe1d6fa46ed97742e85007140)  
  
bool | [hasCustomTrafficType](class_network_file.html#a2dc37057bed1c3443f381db1c2eb3dab) (QString)  
| Returns whether a custom traffic type is already added. [More...](class_network_file.html#a2dc37057bed1c3443f381db1c2eb3dab)  
  
bool | [addCustomPduType](class_network_file.html#a04659f37526b157b807ef4a32f979315) (QString, QString)  
| Adds a custom PDU type. Returns true if successful, false otherwise. [More...](class_network_file.html#a04659f37526b157b807ef4a32f979315)  
  
bool | [hasCustomPduType](class_network_file.html#a1a9a50d9b3a26348ed9285de70ec86d8) (QString)  
| Returns whether a custom PDU type is already added. [More...](class_network_file.html#a1a9a50d9b3a26348ed9285de70ec86d8)  
  
void | [duplicateDevice](class_network_file.html#a7faa39e73d4472750e6f46263d61474b) ([Device](class_device.html))  
| Creates and stores a copy of the given device. [More...](class_network_file.html#a7faa39e73d4472750e6f46263d61474b)  
  
bool | [isActivityFile](class_network_file.html#a6eb32fb45be25823b7bb0850dd5c7aaa) ()  
| Returns whether this file is an activity file or regular network file. [More...](class_network_file.html#a6eb32fb45be25823b7bb0850dd5c7aaa)  
  
  
## Detailed Description

[NetworkFile](class_network_file.html "NetworkFile is the main system file for the application. It holds all the configurations for the engi...") is the main system file for the application. It holds all the configurations for the engine as well as the UI. 

## Member Function Documentation

## ◆ addCustomPduType()

bool NetworkFile::addCustomPduType  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Adds a custom PDU type. Returns true if successful, false otherwise. 

Parameters
     customPduType,the| custom PDU type name.   
---|---  
jsonDefinition,a| JSON string representing the definition of the PDU in the following format and must include the following: { "title": "My Protocol PDU", "units": "Bits", "unit_marks": [16], "width": 32, "fields": [{"value": "TYPE: {type}","size": 32}, {"value": "data: {data}","size": 32}]  
  
Returns
    bool, true if successfully added the custom PDU type, otherwise false. 

## ◆ addCustomTrafficType()

bool NetworkFile::addCustomTrafficType  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Adds a custom traffic type. Returns true if successful, false otherwise. 

Returns
    bool, true if successfully added the custom traffic type, otherwise false. 

## ◆ addDefaultScripts()

void NetworkFile::addDefaultScripts  | ( | | ) |   
---|---|---|---|---  
  
Resets the scripts to the default scripts. 

Remarks
    Missing script files will be addded, existing scripts of the same name will be overwritten. 

## ◆ addScript()

bool NetworkFile::addScript  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Adds a script to the activity file. 

Parameters
     id,the| ID (e.g. filename) of the the script.   
---|---  
contents,the| content of the script.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ addScriptDataStore()

bool NetworkFile::addScriptDataStore  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Adds script data store for persistent storage (e.g. constants, options, settings). 

Parameters
     id,the| ID (e.g. name) of the data store.   
---|---  
contents,the| content of the data store.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ addScriptFile()

bool NetworkFile::addScriptFile  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Adds the script contents to the activity file from a file path. 

Parameters
     id,the| ID (e.g. filename) of the the script.   
---|---  
filename,the| path including the filename of the script.  
  
Remarks
    The script is not evaluated immediately.

Returns
    bool, true if the script was successfully added, false if not. 

## ◆ duplicateDevice()

void NetworkFile::duplicateDevice  | ( | [Device](class_device.html) | | ) |   
---|---|---|---|---|---  
  
Creates and stores a copy of the given device. 

Parameters
     device,device| to duplicate.   
---|---  
  
## ◆ getActivityScriptEngine()

[ActivityScriptEngine](class_activity_script_engine.html) NetworkFile::getActivityScriptEngine  | ( | | ) |   
---|---|---|---|---  
  
Returns the activity script engine of the current file. 

Returns
    [ActivityScriptEngine](class_activity_script_engine.html "This class provides access to activity related scripting functions."), the [ActivityScriptEngine](class_activity_script_engine.html "This class provides access to activity related scripting functions.") object of the current file. 

## ◆ getFilterSet()

[FilterSet](class_filter_set.html) NetworkFile::getFilterSet  | ( | | ) |   
---|---|---|---|---  
  
Returns the engine filter set for simulation packets, what is filtered out. 

Returns
    [FilterSet](class_filter_set.html), the filter set. 

## ◆ getMainNetwork()

[Network](class_network.html) NetworkFile::getMainNetwork  | ( | | ) |   
---|---|---|---|---  
  
Returns the network of the current file. 

Returns
    [Network](class_network.html "Network is the entry point for all device configurations in the network. It retrieves devices."), the [Network](class_network.html "Network is the entry point for all device configurations in the network. It retrieves devices.") object of the current file. 

## ◆ getMainSimulation()

[Simulation](class_simulation.html) NetworkFile::getMainSimulation  | ( | | ) |   
---|---|---|---|---  
  
Returns the simulation of the current file. 

Returns
    [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc."), the [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") object of the current file. 

## ◆ getNetworkDescription()

QString NetworkFile::getNetworkDescription  | ( | | ) |   
---|---|---|---|---  
  
Returns the network description of the current file. 

Returns
    QString, the network description. 

## ◆ getOptions()

[Options](class_options.html) NetworkFile::getOptions  | ( | | ) |   
---|---|---|---|---  
  
Returns the option settings of the current file. 

Returns
    [Options](class_options.html "Options contains the current running options for the application."), the [Options](class_options.html "Options contains the current running options for the application.") object of the current file. 

## ◆ getSavedFilename()

QString NetworkFile::getSavedFilename  | ( | | ) |   
---|---|---|---|---  
  
Returns the filename of the currently opened file. 

Returns
    QString, the filename of the currently opened file. 

## ◆ getScript()

QString NetworkFile::getScript  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the content of the script with the specified ID. 

Parameters
     id,the| ID (e.g. filename) of the script.  
---|---  
  
Returns
    QString, the content of the script with the specified ID. 

## ◆ getScriptDataStore()

QString NetworkFile::getScriptDataStore  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the content of the specified script data store. 

Parameters
     id,the| ID (e.g. name) of the data store of interest.  
---|---  
  
Returns
    QString, the content of the specified script data store. 

## ◆ getScriptDataStoreIDs()

vector< QString > NetworkFile::getScriptDataStoreIDs  | ( | | ) |   
---|---|---|---|---  
  
Returns the list of IDs of script data stores. 

Returns
    vector<QString>, the list of IDs of script data stores. 

## ◆ getScriptEngine()

[ActivityScriptEngine](class_activity_script_engine.html) NetworkFile::getScriptEngine  | ( | | ) |   
---|---|---|---|---  
  
Returns the script engine of the current file. 

Returns
    [ActivityScriptEngine](class_activity_script_engine.html "This class provides access to activity related scripting functions."), the [ActivityScriptEngine](class_activity_script_engine.html "This class provides access to activity related scripting functions.") object of the current file. 

## ◆ getScriptIDs()

vector< QString > NetworkFile::getScriptIDs  | ( | | ) |   
---|---|---|---|---  
  
Returns the list of IDs currently in the system. 

Returns
    vector<QString>, the list of IDs currently in the system. 

## ◆ getUserProfile()

[UserProfile](class_user_profile.html) NetworkFile::getUserProfile  | ( | | ) |   
---|---|---|---|---  
  
Returns the user profile of the current file. 

Returns
    [UserProfile](class_user_profile.html "UserProfile allows manipulation of the User Profile dialog."), the [UserProfile](class_user_profile.html "UserProfile allows manipulation of the User Profile dialog.") object of the current file. 

## ◆ getVersion()

QString NetworkFile::getVersion  | ( | | ) |   
---|---|---|---|---  
  
Returns the version the current file was saved in. 

Returns
    QString, the version the current file was saved in. 

## ◆ getWorkspace()

[Workspace](class_workspace.html) NetworkFile::getWorkspace  | ( | | ) |   
---|---|---|---|---  
  
Returns the workspace of the current file. 

Returns
    [Workspace](class_workspace.html "Workspace is the base class for Logical and Physical workspace related objects."), the [Workspace](class_workspace.html "Workspace is the base class for Logical and Physical workspace related objects.") object of the current file. 

## ◆ hasCustomPduType()

bool NetworkFile::hasCustomPduType  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns whether a custom PDU type is already added. 

Returns
    bool, true the custom traffic PDU is already added, otherwise false. 

## ◆ hasCustomTrafficType()

bool NetworkFile::hasCustomTrafficType  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns whether a custom traffic type is already added. 

Returns
    bool, true the custom traffic type is already added, otherwise false. 

## ◆ isActivityFile()

bool NetworkFile::isActivityFile  | ( | | ) |   
---|---|---|---|---  
  
Returns whether this file is an activity file or regular network file. 

## ◆ removeScript()

bool NetworkFile::removeScript  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Removes the specified script from the activity file hash. 

Parameters
     id,the| ID (e.g. filename) of the script.  
---|---  
  
Returns
    bool, true if successful, otherwise false.

Remarks
    This will not remove the script contents from memory. However, upon the next [resetScriptEngine()](class_network_file.html#ab297523cea8744d42abfc1621dfcc568 "Removes the current activity script engine and creates a new one."), the removed script will not be loaded. 

## ◆ removeScriptDataStore()

bool NetworkFile::removeScriptDataStore  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Removes the specified script data store for persistent storage (e.g. constants, options, settings). 

Parameters
     id,the| ID (e.g. name) of the data store of interest.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ resetScriptEngine()

void NetworkFile::resetScriptEngine  | ( | | ) |   
---|---|---|---|---  
  
Removes the current activity script engine and creates a new one. 

Remarks
    All loaded script results will be lost. 

## ◆ setNetworkDescription()

void NetworkFile::setNetworkDescription  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Sets the network description for the current file. 

Parameters
     description,the| network description for the current file.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [NetworkFile.pki](_network_file_8pki.html)


