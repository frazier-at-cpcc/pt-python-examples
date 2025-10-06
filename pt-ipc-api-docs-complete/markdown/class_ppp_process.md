# Cisco Packet Tracer Extensions API: PppProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_ppp_process.html

---

[PppProcess](class_ppp_process.html "PppProcess handles and manipulates the PPP encapsulation process.") handles and manipulates the PPP encapsulation process. [More...](class_ppp_process.html#details)

##  Public Member Functions  
  
---  
void | [setAuthenType](class_ppp_process.html#a21739de7429b159956bfcbc5827956f3) (PppAuthenType)  
| Sets the authentication type. [More...](class_ppp_process.html#a21739de7429b159956bfcbc5827956f3)  
  
PppAuthenType | [getAuthenType](class_ppp_process.html#a76617003a37010438f3d9bd469f26bba) ()  
| Returns the authentication type. [More...](class_ppp_process.html#a76617003a37010438f3d9bd469f26bba)  
  
[PAPProcess](class_p_a_p_process.html) | [getPapProcess](class_ppp_process.html#a59a32f64094f4b95470df9e2a0aa69ab) ()  
| Returns the PAP process. [More...](class_ppp_process.html#a59a32f64094f4b95470df9e2a0aa69ab)  
  
[ChapProcess](class_chap_process.html) | [getChapProcess](class_ppp_process.html#a29866e048651c881af9ef4c7dd677c7b) ()  
| Returns the CHAP process. [More...](class_ppp_process.html#a29866e048651c881af9ef4c7dd677c7b)  
  
Public Member Functions inherited from [PortKeepAliveProcess](class_port_keep_alive_process.html)  
void | [setKeepAliveOn](class_port_keep_alive_process.html#a35bfb062718b7507ec3f1fd71c62d4f1) (bool)  
bool | [isKeepAliveOn](class_port_keep_alive_process.html#aa9fe1c119e9f3365c4dec1cb65b13752) ()  
| Returns true if keepalive is enabled, otherwise false. [More...](class_port_keep_alive_process.html#aa9fe1c119e9f3365c4dec1cb65b13752)  
  
void | [setKeepAliveInterval](class_port_keep_alive_process.html#a2e003c5aa950a4a7c1548fcee456e667) (int)  
| Sets the keepalive interval. [More...](class_port_keep_alive_process.html#a2e003c5aa950a4a7c1548fcee456e667)  
  
int | [getKeepAliveInterval](class_port_keep_alive_process.html#adb100ad4b49d7678a1dd4059552f9ee1) ()  
| Returns the keepalive interval. [More...](class_port_keep_alive_process.html#adb100ad4b49d7678a1dd4059552f9ee1)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[PppProcess](class_ppp_process.html "PppProcess handles and manipulates the PPP encapsulation process.") handles and manipulates the PPP encapsulation process. 

## Member Function Documentation

## ◆ getAuthenType()

PppAuthenType PppProcess::getAuthenType  | ( | | ) |   
---|---|---|---|---  
  
Returns the authentication type. 

Returns
    enum<PppAuthenType>, the authentication type. Authentication types: eNoAuthentication = 0, eChap = 1, ePap = 2, ePapChap = 3, eChapPap = 4 

## ◆ getChapProcess()

[ChapProcess](class_chap_process.html) PppProcess::getChapProcess  | ( | | ) |   
---|---|---|---|---  
  
Returns the CHAP process. 

Returns
    [ChapProcess](class_chap_process.html "ChapProcess is the process that manipulates the protocol CHAP."), the [ChapProcess](class_chap_process.html "ChapProcess is the process that manipulates the protocol CHAP.") object. 

## ◆ getPapProcess()

[PAPProcess](class_p_a_p_process.html) PppProcess::getPapProcess  | ( | | ) |   
---|---|---|---|---  
  
Returns the PAP process. 

Returns
    [PAPProcess](class_p_a_p_process.html "PAPProcess handles and manipulates the PAP process."), the [PAPProcess](class_p_a_p_process.html "PAPProcess handles and manipulates the PAP process.") object. 

## ◆ setAuthenType()

void PppProcess::setAuthenType  | ( | PppAuthenType  | | ) |   
---|---|---|---|---|---  
  
Sets the authentication type. 

Parameters
     type,the| authentication type. Authentication types: eNoAuthentication = 0, eChap = 1, ePap = 2, ePapChap = 3, eChapPap = 4   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CPppProcess.pki](_c_ppp_process_8pki.html)


