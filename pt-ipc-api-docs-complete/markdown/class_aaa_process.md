# Cisco Packet Tracer Extensions API: AaaProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_aaa_process.html

---

[AaaProcess](class_aaa_process.html "AaaProcess holds and manipulates the AAA process.") holds and manipulates the AAA process. [More...](class_aaa_process.html#details)

##  Public Member Functions  
  
---  
Aaa::EAuthMethod | [getAuthMethodAt](class_aaa_process.html#a081113a36b3713183a8f0f5ac14cca87) (string, int)  
| Returns the authentication method at the given index in the list. [More...](class_aaa_process.html#a081113a36b3713183a8f0f5ac14cca87)  
  
void | [remAuthListByName](class_aaa_process.html#a0480e697cd9aacf0c78753150f705885) (string)  
| Removes a configured authentication list from the process. [More...](class_aaa_process.html#a0480e697cd9aacf0c78753150f705885)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[AaaProcess](class_aaa_process.html "AaaProcess holds and manipulates the AAA process.") holds and manipulates the AAA process. 

## Member Function Documentation

## ◆ getAuthMethodAt()

Aaa::EAuthMethod AaaProcess::getAuthMethodAt  | ( | string  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Returns the authentication method at the given index in the list. 

Remarks
    For example, if you configured an authentication list named 'myauth', and you specified to use radius and local, radius would be index 0 and local would be index 1.

Parameters
     listName,the| authentication list name to inquire about ('default' is a built-in list)   
---|---  
methodIndex,the| index into the list.  
  
Returns
    enum<Aaa::EAuthMethod>, the type of authentication in that list. Authentication types: eTacacs = 0, eRadius = 1, eLocal = 2, eNone = 3, eEnable = 4, eNull = 5 

## ◆ remAuthListByName()

void AaaProcess::remAuthListByName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes a configured authentication list from the process. 

Parameters
     name,the| name of the authentication list to remove.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CAaaProcess.pki](_c_aaa_process_8pki.html)


