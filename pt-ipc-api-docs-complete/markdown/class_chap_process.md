# Cisco Packet Tracer Extensions API: ChapProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_chap_process.html

---

[ChapProcess](class_chap_process.html "ChapProcess is the process that manipulates the protocol CHAP.") is the process that manipulates the protocol CHAP. [More...](class_chap_process.html#details)

##  Public Member Functions  
  
---  
void | [setPassword](class_chap_process.html#a486a73bc3afb60e7213bb952c1354cd8) (string)  
| Sets the CHAP password. [More...](class_chap_process.html#a486a73bc3afb60e7213bb952c1354cd8)  
  
void | [setUserName](class_chap_process.html#a21f99a5fd85c32f47057b545d63dd511) (string)  
| Sets the CHAP username. [More...](class_chap_process.html#a21f99a5fd85c32f47057b545d63dd511)  
  
string | [getUserName](class_chap_process.html#a89de0507bd626984e8eba25f9fb3310d) ()  
| Returns the CHAP username. [More...](class_chap_process.html#a89de0507bd626984e8eba25f9fb3310d)  
  
string | [getPassword](class_chap_process.html#a0b4549bcc39a0cab30bfa03ba0e524df) ()  
| Returns the CHAP password. [More...](class_chap_process.html#a0b4549bcc39a0cab30bfa03ba0e524df)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[ChapProcess](class_chap_process.html "ChapProcess is the process that manipulates the protocol CHAP.") is the process that manipulates the protocol CHAP. 

## Member Function Documentation

## ◆ getPassword()

string ChapProcess::getPassword  | ( | | ) |   
---|---|---|---|---  
  
Returns the CHAP password. 

Returns
    string, the CHAP password. 

## ◆ getUserName()

string ChapProcess::getUserName  | ( | | ) |   
---|---|---|---|---  
  
Returns the CHAP username. 

Returns
    string, the CHAP username. 

## ◆ setPassword()

void ChapProcess::setPassword  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the CHAP password. 

Parameters
     string,the| CHAP password.   
---|---  
  
## ◆ setUserName()

void ChapProcess::setUserName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the CHAP username. 

Parameters
     string,the| CHAP username.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CChapProcess.pki](_c_chap_process_8pki.html)


