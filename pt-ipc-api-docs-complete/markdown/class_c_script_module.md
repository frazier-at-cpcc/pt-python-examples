# Cisco Packet Tracer Extensions API: CScriptModule Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_c_script_module.html

---

[CScriptModule](class_c_script_module.html "CScriptModule access from itself.") access from itself. [More...](class_c_script_module.html#details)

##  Public Member Functions  
  
---  
bool | [stop](class_c_script_module.html#ad3a799947fa9aec6904d20410e73e974) ()  
| Stop Script [Module](class_module.html). [More...](class_c_script_module.html#ad3a799947fa9aec6904d20410e73e974)  
  
QString | [getScriptCode](class_c_script_module.html#a4462ff8461185e6d66ed51cf307b7a03) (QString)  
| Get Script Code based on script id. [More...](class_c_script_module.html#a4462ff8461185e6d66ed51cf307b7a03)  
  
QString | [getScript](class_c_script_module.html#a69cf47ce50dd465aa2848750f6608d00) (QString)  
| Get Script Code based on script id and processes translations on the code, if exists. [More...](class_c_script_module.html#a69cf47ce50dd465aa2848750f6608d00)  
  
bool | [hasScript](class_c_script_module.html#a95a8c1303c5ffc1813cec05de5606fe7) (QString)  
| Check if the script exists using script id. [More...](class_c_script_module.html#a95a8c1303c5ffc1813cec05de5606fe7)  
  
QString | [getInterfaceCode](class_c_script_module.html#abe8199e685a0c564e42d0cf4d14bb722) (QString)  
| Get Interface Code based on Interface id.. [More...](class_c_script_module.html#abe8199e685a0c564e42d0cf4d14bb722)  
  
QString | [getInterface](class_c_script_module.html#a9feaac193b3cbdc467a7d6c2b92689cd) (QString)  
| Get Interface Code based on Interface id and processes translations on the code, if exists. [More...](class_c_script_module.html#a9feaac193b3cbdc467a7d6c2b92689cd)  
  
bool | [hasInterface](class_c_script_module.html#a874967f44e63401bb2434cdb44d96da3) (QString)  
| Check if the Interface exists using Interface id. [More...](class_c_script_module.html#a874967f44e63401bb2434cdb44d96da3)  
  
QString | [getScriptDataStore](class_c_script_module.html#ae144accfffbb01660c8b9bafc4ba1079) (QString)  
bool | [shouldPromptExternalNetworkAccess](class_c_script_module.html#a20d611211eed16d41c23a195fe664804) ()  
| This delegate determines if script module should prompt for external network access. [More...](class_c_script_module.html#a20d611211eed16d41c23a195fe664804)  
  
bool | [shouldPromptExternalServerOperation](class_c_script_module.html#a139dd922c2e8d068c65eb791d35783b5) (QString, int)  
| This delegate determines if script module should prompt for external server operation. [More...](class_c_script_module.html#a139dd922c2e8d068c65eb791d35783b5)  
  
Public Member Functions inherited from [CepInstance](class_cep_instance.html)  
uuid | [getInstanceId](class_cep_instance.html#a817430f3774ade62b2df8ae9db190908) ()  
| Returns the UUID of this external process. [More...](class_cep_instance.html#a817430f3774ade62b2df8ae9db190908)  
  
[Cep](class_cep.html) | [getCep](class_cep_instance.html#aa3dd8ef831263e55e74f8744ac697f69) ()  
bool | [addExclusivePublisher](class_cep_instance.html#afffbb0364889671a52ef638461af4d9b) (string)  
| Returns true if the exclusive publisher with the specified certificate was added successfully, otherwise false. [More...](class_cep_instance.html#afffbb0364889671a52ef638461af4d9b)  
  
void | [clearExclusivePublishers](class_cep_instance.html#a7c9396b4a030e750b2032923ffecff41) ()  
| Clears all exclusive publishers. [More...](class_cep_instance.html#a7c9396b4a030e750b2032923ffecff41)  
  
bool | [removeExclusivePublisher](class_cep_instance.html#af8b87b7f35ac3884cb75a335c4111fa6) (string)  
| Returns true if the exclusive publisher with the specified certificate was removed successfully, otherwise false. [More...](class_cep_instance.html#af8b87b7f35ac3884cb75a335c4111fa6)  
  
void | [removeExclusivePublisherAt](class_cep_instance.html#ac3b31134593faf3e0c96b0c704087602) (int)  
| Removes the exclusive publisher at the specified index. [More...](class_cep_instance.html#ac3b31134593faf3e0c96b0c704087602)  
  
int | [getExclusivePublisherCount](class_cep_instance.html#a46fbceb4c8674357026c8542466da1b1) ()  
| Returns the number of exclusive publishers. [More...](class_cep_instance.html#a46fbceb4c8674357026c8542466da1b1)  
  
string | [getExclusivePublisherAt](class_cep_instance.html#a03ce553dd1c16936945d942c924d77bc) (int)  
| Returns the exclusive publisher at the specified index. [More...](class_cep_instance.html#a03ce553dd1c16936945d942c924d77bc)  
  
bool | [hasExclusivePublisher](class_cep_instance.html#a02cdfb61694e65ffdf5c53415ed78ddb) (string)  
| Returns true if the specified certificate is an exclusive publisher, otherwise false. [More...](class_cep_instance.html#a02cdfb61694e65ffdf5c53415ed78ddb)  
  
QString | [getCommandLineArg](class_cep_instance.html#afe9e1b11bffa924b713949ad20c611e8) ()  
| Returns the command line argument for this external process (ExApp or Script [Module](class_module.html)) when launching PT. [More...](class_cep_instance.html#afe9e1b11bffa924b713949ad20c611e8)  
  
void | [messageReceived](class_cep_instance.html#ac4771cc7f7f1f9b967b1c6f95f41044e) (string, uuid, QString)  
| This event is emitted when this external process receives a message from a local external process. [More...](class_cep_instance.html#ac4771cc7f7f1f9b967b1c6f95f41044e)  
  
void | [remoteMessageReceived](class_cep_instance.html#a175e52c6d05d083d4066507d63564dc3) (string, uuid, QString)  
| This event is emitted when this external process receives a message from a remote external process. [More...](class_cep_instance.html#a175e52c6d05d083d4066507d63564dc3)  
  
void | [registeredFileOpened](class_cep_instance.html#ae9f7e444afd3eae8aa7bb2baa1fb3887) (QString)  
| This event is emitted when PT GUI or OS opens a file that is registered to this external process. [More...](class_cep_instance.html#ae9f7e444afd3eae8aa7bb2baa1fb3887)  
  
  
## Detailed Description

[CScriptModule](class_c_script_module.html "CScriptModule access from itself.") access from itself. 

## Member Function Documentation

## ◆ getInterface()

QString CScriptModule::getInterface  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Get Interface Code based on Interface id and processes translations on the code, if exists. 

Parameters
     id,Interface| id  
---|---  
  
Returns
    QString, processed Interface code 

## ◆ getInterfaceCode()

QString CScriptModule::getInterfaceCode  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Get Interface Code based on Interface id.. 

Parameters
     id,Interface| id  
---|---  
  
Returns
    QString, Interface code 

## ◆ getScript()

QString CScriptModule::getScript  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Get Script Code based on script id and processes translations on the code, if exists. 

Parameters
     id,script| id  
---|---  
  
Returns
    QString, processed Script code 

## ◆ getScriptCode()

QString CScriptModule::getScriptCode  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Get Script Code based on script id. 

Parameters
     id,script| id  
---|---  
  
Returns
    QString, Script code 

## ◆ getScriptDataStore()

QString CScriptModule::getScriptDataStore  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
## ◆ hasInterface()

bool CScriptModule::hasInterface  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Check if the Interface exists using Interface id. 

Parameters
     id,Interface| id  
---|---  
  
Returns
    bool, true if it exists and false otherwise 

## ◆ hasScript()

bool CScriptModule::hasScript  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Check if the script exists using script id. 

Parameters
     id,script| id  
---|---  
  
Returns
    bool, true if it exists and false otherwise 

## ◆ shouldPromptExternalNetworkAccess()

bool CScriptModule::shouldPromptExternalNetworkAccess  | ( | | ) |   
---|---|---|---|---  
  
This delegate determines if script module should prompt for external network access. 

Returns
    bool, true if script module should prompt, otherwise false. 

## ◆ shouldPromptExternalServerOperation()

bool CScriptModule::shouldPromptExternalServerOperation  | ( | QString  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
This delegate determines if script module should prompt for external server operation. 

Parameters
     protocol,HTTP| or TCP   
---|---  
port,the| port to listen on  
  
Returns
    bool, true if script module should prompt, otherwise false. 

## ◆ stop()

bool CScriptModule::stop  | ( | | ) |   
---|---|---|---|---  
  
Stop Script [Module](class_module.html). 

Returns
    bool, true if it has been stopped and false if otherwise 

* * *

The documentation for this class was generated from the following file:

  * [CScriptModule.pki](_c_script_module_8pki.html)


