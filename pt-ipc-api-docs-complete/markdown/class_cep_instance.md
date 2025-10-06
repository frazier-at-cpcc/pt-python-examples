# Cisco Packet Tracer Extensions API: CepInstance Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_cep_instance.html

---

[CepInstance](class_cep_instance.html "CepInstance is the external process \(ExApp and Script Module\) that communicates with Packet Tracer th...") is the external process (ExApp and Script [Module](class_module.html)) that communicates with Packet Tracer through the [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality."). [More...](class_cep_instance.html#details)

##  Public Member Functions  
  
---  
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

[CepInstance](class_cep_instance.html "CepInstance is the external process \(ExApp and Script Module\) that communicates with Packet Tracer th...") is the external process (ExApp and Script [Module](class_module.html)) that communicates with Packet Tracer through the [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality."). 

## Member Function Documentation

## ◆ addExclusivePublisher()

bool CepInstance::addExclusivePublisher  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns true if the exclusive publisher with the specified certificate was added successfully, otherwise false. 

Parameters
     pem,the| PEM base64-encoded DER certificate string.  
---|---  
  
Returns
    bool, true if the exclusive publisher with the specified certificate was added successfully, otherwise false. 

## ◆ clearExclusivePublishers()

void CepInstance::clearExclusivePublishers  | ( | | ) |   
---|---|---|---|---  
  
Clears all exclusive publishers. 

## ◆ getCep()

[Cep](class_cep.html) CepInstance::getCep  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getCommandLineArg()

QString CepInstance::getCommandLineArg  | ( | | ) |   
---|---|---|---|---  
  
Returns the command line argument for this external process (ExApp or Script [Module](class_module.html)) when launching PT. 

Returns
    QString, the command line argument fort his external process 

## ◆ getExclusivePublisherAt()

string CepInstance::getExclusivePublisherAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the exclusive publisher at the specified index. 

Parameters
     index,the| index of the exclusive publisher.  
---|---  
  
Returns
    string, the exclusive publisher at the specified index. 

## ◆ getExclusivePublisherCount()

int CepInstance::getExclusivePublisherCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of exclusive publishers. 

Returns
    int, the number of exclusive publishers. 

## ◆ getInstanceId()

uuid CepInstance::getInstanceId  | ( | | ) |   
---|---|---|---|---  
  
Returns the UUID of this external process. 

Returns
    uuid, the UUID of this external process. 

## ◆ hasExclusivePublisher()

bool CepInstance::hasExclusivePublisher  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns true if the specified certificate is an exclusive publisher, otherwise false. 

Parameters
     pem,the| PEM base64-encoded DER certificate string.  
---|---  
  
Returns
    bool, Returns true if the specified certificate is an exclusive publisher, otherwise false. 

## ◆ messageReceived()

void CepInstance::messageReceived  | ( | string  | ,   
---|---|---|---  
|  | uuid  | ,   
|  | QString  |   
| ) | |   
  
This event is emitted when this external process receives a message from a local external process. 

  * srcCepId, the name of the external process source. 
  * srcCepInstanceId, the UUID of the external process source. 
  * message, the message from the external process source.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ registeredFileOpened()

void CepInstance::registeredFileOpened  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when PT GUI or OS opens a file that is registered to this external process. 

  * filePath, the path of the file opened.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ remoteMessageReceived()

void CepInstance::remoteMessageReceived  | ( | string  | ,   
---|---|---|---  
|  | uuid  | ,   
|  | QString  |   
| ) | |   
  
This event is emitted when this external process receives a message from a remote external process. 

  * srcCepId, the name of the external process source. 
  * srcCepInstanceId, the UUID of the external process source. 
  * message, the message from the external process source.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ removeExclusivePublisher()

bool CepInstance::removeExclusivePublisher  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns true if the exclusive publisher with the specified certificate was removed successfully, otherwise false. 

Parameters
     pem,the| PEM base64-encoded DER certificate string.  
---|---  
  
Returns
    bool, true if the exclusive publisher with the specified certificate was removed successfully, otherwise false. 

## ◆ removeExclusivePublisherAt()

void CepInstance::removeExclusivePublisherAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Removes the exclusive publisher at the specified index. 

Parameters
     index,the| index of the exclusive publisher.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CCepInstance.pki](_c_cep_instance_8pki.html)


