# Cisco Packet Tracer Extensions API: PtpProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_ptp_process.html

---

##  Public Member Functions  
  
---  
long | [getT1](class_ptp_process.html#a652577256e224bec96b7b53637ffe920) ()  
| Returns the T1 value. [More...](class_ptp_process.html#a652577256e224bec96b7b53637ffe920)  
  
long | [getT2](class_ptp_process.html#a4dfc5c8f20b9692f9fbe29ac6acad38c) ()  
| Returns the T2 value. [More...](class_ptp_process.html#a4dfc5c8f20b9692f9fbe29ac6acad38c)  
  
long | [getT3](class_ptp_process.html#a481c6a775cd99a7aad4ab67421b6b799) ()  
| Returns the T3 value. [More...](class_ptp_process.html#a481c6a775cd99a7aad4ab67421b6b799)  
  
long | [getT4](class_ptp_process.html#ad7a0acfc604d68a4970c31ab6d04519b) ()  
| Returns the T4 value. [More...](class_ptp_process.html#ad7a0acfc604d68a4970c31ab6d04519b)  
  
void | [setT1](class_ptp_process.html#a1aa4e325ab7a5be97d7057c1c14cf5bb) (long)  
| Sets the T1 value. [More...](class_ptp_process.html#a1aa4e325ab7a5be97d7057c1c14cf5bb)  
  
void | [setT2](class_ptp_process.html#a767cbc9260751f682ce9a63f858e32a2) (long)  
| Sets the T2 value. [More...](class_ptp_process.html#a767cbc9260751f682ce9a63f858e32a2)  
  
void | [setT3](class_ptp_process.html#a0ef8ec197ccb59553c3a07187e6ba231) (long)  
| Sets the T3 value. [More...](class_ptp_process.html#a0ef8ec197ccb59553c3a07187e6ba231)  
  
void | [setT4](class_ptp_process.html#aa8a85ebb7f2fcf694d1443f0362667f8) (long)  
| Sets the T4 value. [More...](class_ptp_process.html#aa8a85ebb7f2fcf694d1443f0362667f8)  
  
void | [setPtpDebugEventFlag](class_ptp_process.html#a332a31cbfd175825a5934b4f56dcc54c) (bool)  
| Sets debug event flag for ptp. [More...](class_ptp_process.html#a332a31cbfd175825a5934b4f56dcc54c)  
  
bool | [getPtpDebugEventFlag](class_ptp_process.html#a3c96f7d429c43b7a6b550701809ed85e) ()  
| Gets debug event flag for ptp. [More...](class_ptp_process.html#a3c96f7d429c43b7a6b550701809ed85e)  
  
void | [setPtpDebugMsgFlag](class_ptp_process.html#ac2774b7b3cec7142f897b6deb34a2a39) (bool)  
| Sets debug message flag for ptp. [More...](class_ptp_process.html#ac2774b7b3cec7142f897b6deb34a2a39)  
  
bool | [getPtpDebugMsgFlag](class_ptp_process.html#a596385bc83ecbd18c789ae197af7b4a5) ()  
| Gets debug message flag for ptp. [More...](class_ptp_process.html#a596385bc83ecbd18c789ae197af7b4a5)  
  
void | [syncToCurrentTime](class_ptp_process.html#a75ac95a5c4cc4d1ee97ff6811445ae3c) ()  
| Syncs the time to the current time. [More...](class_ptp_process.html#a75ac95a5c4cc4d1ee97ff6811445ae3c)  
  
void | [runBMC](class_ptp_process.html#a31a7b7f88a74c90f563070f9b5a74641) ()  
| Runs BMC (best master clock). [More...](class_ptp_process.html#a31a7b7f88a74c90f563070f9b5a74641)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Member Function Documentation

## ◆ getPtpDebugEventFlag()

bool PtpProcess::getPtpDebugEventFlag  | ( | | ) |   
---|---|---|---|---  
  
Gets debug event flag for ptp. 

Returns
    bool, true if debug enabled, false if disabled. 

## ◆ getPtpDebugMsgFlag()

bool PtpProcess::getPtpDebugMsgFlag  | ( | | ) |   
---|---|---|---|---  
  
Gets debug message flag for ptp. 

Parameters
     return,value| is the flag value.   
---|---  
  
## ◆ getT1()

long PtpProcess::getT1  | ( | | ) |   
---|---|---|---|---  
  
Returns the T1 value. 

Returns
    long, the T1 value. 

## ◆ getT2()

long PtpProcess::getT2  | ( | | ) |   
---|---|---|---|---  
  
Returns the T2 value. 

Returns
    long, the T2 value. 

## ◆ getT3()

long PtpProcess::getT3  | ( | | ) |   
---|---|---|---|---  
  
Returns the T3 value. 

Returns
    long, the T3 value. 

## ◆ getT4()

long PtpProcess::getT4  | ( | | ) |   
---|---|---|---|---  
  
Returns the T4 value. 

Returns
    long, the T4 value. 

## ◆ runBMC()

void PtpProcess::runBMC  | ( | | ) |   
---|---|---|---|---  
  
Runs BMC (best master clock). 

## ◆ setPtpDebugEventFlag()

void PtpProcess::setPtpDebugEventFlag  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Sets debug event flag for ptp. 

Parameters
     flag,true| to enable debug, false to disable.   
---|---  
  
## ◆ setPtpDebugMsgFlag()

void PtpProcess::setPtpDebugMsgFlag  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Sets debug message flag for ptp. 

Parameters
     flag,value| to use for the flag.   
---|---  
  
## ◆ setT1()

void PtpProcess::setT1  | ( | long  | | ) |   
---|---|---|---|---|---  
  
Sets the T1 value. 

Parameters
     t,the| T1 value to use.   
---|---  
  
## ◆ setT2()

void PtpProcess::setT2  | ( | long  | | ) |   
---|---|---|---|---|---  
  
Sets the T2 value. 

Parameters
     t,the| T2 value to use.   
---|---  
  
## ◆ setT3()

void PtpProcess::setT3  | ( | long  | | ) |   
---|---|---|---|---|---  
  
Sets the T3 value. 

Parameters
     t,the| T3 value to use.   
---|---  
  
## ◆ setT4()

void PtpProcess::setT4  | ( | long  | | ) |   
---|---|---|---|---|---  
  
Sets the T4 value. 

Parameters
     t,the| T4 value to use.   
---|---  
  
## ◆ syncToCurrentTime()

void PtpProcess::syncToCurrentTime  | ( | | ) |   
---|---|---|---|---  
  
Syncs the time to the current time. 

* * *

The documentation for this class was generated from the following file:

  * [CPTPProcess.pki](_c_p_t_p_process_8pki.html)


