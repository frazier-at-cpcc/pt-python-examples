# Cisco Packet Tracer Extensions API: CbacProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_cbac_process.html

---

[CbacProcess](class_cbac_process.html "CbacProcess is the process that handles CBAC.") is the process that handles CBAC. [More...](class_cbac_process.html#details)

##  Public Member Functions  
  
---  
int | [getCbacCount](class_cbac_process.html#aff56d3846b04e40d8d342b5ca716147b) ()  
| Returns the number of CBAC access lists. [More...](class_cbac_process.html#aff56d3846b04e40d8d342b5ca716147b)  
  
[Cbac](class_cbac.html) | [getCbacAt](class_cbac_process.html#a81ff2ec1c983ff32c767c0dcdec97da1) (int)  
| Returns the CBAC access list at the specified index. [More...](class_cbac_process.html#a81ff2ec1c983ff32c767c0dcdec97da1)  
  
void | [setGlobalAuditTrail](class_cbac_process.html#ad95b9762a28bdc88d695df9f4eae4ee1) (Bool)  
| Enables or disables global audit trail. [More...](class_cbac_process.html#ad95b9762a28bdc88d695df9f4eae4ee1)  
  
void | [setGlobalAlert](class_cbac_process.html#a37102e1dc394d4d9578eac8c40f54ba3) (Bool)  
| Enables or disables global alert. [More...](class_cbac_process.html#a37102e1dc394d4d9578eac8c40f54ba3)  
  
void | [setTcpSynWaitTime](class_cbac_process.html#a4752a2e8fc18803cb7aeeb9ab30e4536) (int)  
| Sets the value for TCP sync wait. [More...](class_cbac_process.html#a4752a2e8fc18803cb7aeeb9ab30e4536)  
  
void | [setTcpFinWaitTime](class_cbac_process.html#a47fac4c7fca14bed5447475fd3a28ea9) (int)  
| Sets the value for TCP FIN wait. [More...](class_cbac_process.html#a47fac4c7fca14bed5447475fd3a28ea9)  
  
void | [setTcpIdleTime](class_cbac_process.html#a425e99778496c9c0d46b272f9c8547f3) (int)  
| Sets the value for TCP idle time. [More...](class_cbac_process.html#a425e99778496c9c0d46b272f9c8547f3)  
  
void | [setUdpIdleTime](class_cbac_process.html#ad2f814b2724b14a2e081f2905af18e05) (int)  
| Sets the value for UDP idle time. [More...](class_cbac_process.html#ad2f814b2724b14a2e081f2905af18e05)  
  
void | [setDnsTimeout](class_cbac_process.html#a4c6d1bc1946db18853c6b4038e7b8a1e) (int)  
| Sets the value for DNS timeout. [More...](class_cbac_process.html#a4c6d1bc1946db18853c6b4038e7b8a1e)  
  
Bool | [getGlobalAuditTrail](class_cbac_process.html#ad79a7060dd0c997c200d82575c05d5d2) ()  
| Returns the global audit trail value. [More...](class_cbac_process.html#ad79a7060dd0c997c200d82575c05d5d2)  
  
Bool | [getGlobalAlert](class_cbac_process.html#a6cf5dfcd5d9e21e87263823d3e8ec9d0) ()  
| Returns the global alert value. [More...](class_cbac_process.html#a6cf5dfcd5d9e21e87263823d3e8ec9d0)  
  
void | [setMaxIncompleteHigh](class_cbac_process.html#a704b0fd5d685775f221cfbd40689123d) (int)  
| Sets the max-incomplete high value. [More...](class_cbac_process.html#a704b0fd5d685775f221cfbd40689123d)  
  
void | [setMaxIncompleteLow](class_cbac_process.html#a48edcc0fa978d3c6fae2b1c691cd6b94) (int)  
| Sets the max-incomplete low value. [More...](class_cbac_process.html#a48edcc0fa978d3c6fae2b1c691cd6b94)  
  
void | [setOneMinuteHigh](class_cbac_process.html#af2c309283a80c9902c409016f8ae9ee8) (int)  
| Sets the one-minute high value. [More...](class_cbac_process.html#af2c309283a80c9902c409016f8ae9ee8)  
  
void | [setOneMinuteLow](class_cbac_process.html#a46707b5e4260bf9d01ed538682079690) (int)  
| Sets the one-minute low value. [More...](class_cbac_process.html#a46707b5e4260bf9d01ed538682079690)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[CbacProcess](class_cbac_process.html "CbacProcess is the process that handles CBAC.") is the process that handles CBAC. 

## Member Function Documentation

## ◆ getCbacAt()

[Cbac](class_cbac.html) CbacProcess::getCbacAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the CBAC access list at the specified index. 

Parameters
     index,index| to get the access list from  
---|---  
  
Returns
    [Cbac](class_cbac.html "Cbac holds and manipulates Context-based access control."), the CBAC access list at the specified index. 

## ◆ getCbacCount()

int CbacProcess::getCbacCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of CBAC access lists. 

Returns
    int, the number of CBAC access lists. 

## ◆ getGlobalAlert()

Bool CbacProcess::getGlobalAlert  | ( | | ) |   
---|---|---|---|---  
  
Returns the global alert value. 

Returns
    enum<Bool>, values: eDefault = -1, eFalse = 0, eTrue = 1 

## ◆ getGlobalAuditTrail()

Bool CbacProcess::getGlobalAuditTrail  | ( | | ) |   
---|---|---|---|---  
  
Returns the global audit trail value. 

Returns
    enum<Bool>, values: eDefault = -1, eFalse = 0, eTrue = 1 

## ◆ setDnsTimeout()

void CbacProcess::setDnsTimeout  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the value for DNS timeout. 

Parameters
     timeout,the| value for DNS timeout.   
---|---  
  
## ◆ setGlobalAlert()

void CbacProcess::setGlobalAlert  | ( | Bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables global alert. 

Parameters
     val,values| eDefault = -1, eFalse = 0, eTrue = 1   
---|---  
  
## ◆ setGlobalAuditTrail()

void CbacProcess::setGlobalAuditTrail  | ( | Bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables global audit trail. 

Parameters
     val,values| eDefault = -1, eFalse = 0, eTrue = 1   
---|---  
  
## ◆ setMaxIncompleteHigh()

void CbacProcess::setMaxIncompleteHigh  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the max-incomplete high value. 

Parameters
     hinum,the| max-incomplete high value.   
---|---  
  
## ◆ setMaxIncompleteLow()

void CbacProcess::setMaxIncompleteLow  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the max-incomplete low value. 

Parameters
     lonum,the| max-incomplete low value.   
---|---  
  
## ◆ setOneMinuteHigh()

void CbacProcess::setOneMinuteHigh  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the one-minute high value. 

Parameters
     hinum,the| one-minute high value.   
---|---  
  
## ◆ setOneMinuteLow()

void CbacProcess::setOneMinuteLow  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the one-minute low value. 

Parameters
     lonum,the| one-minute low value.   
---|---  
  
## ◆ setTcpFinWaitTime()

void CbacProcess::setTcpFinWaitTime  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the value for TCP FIN wait. 

Parameters
     finwait,the| value for TCP FIN wait.   
---|---  
  
## ◆ setTcpIdleTime()

void CbacProcess::setTcpIdleTime  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the value for TCP idle time. 

Parameters
     idleTime,the| value for TCP idle time.   
---|---  
  
## ◆ setTcpSynWaitTime()

void CbacProcess::setTcpSynWaitTime  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the value for TCP sync wait. 

Parameters
     synTime,the| value for TCP sync wait.   
---|---  
  
## ◆ setUdpIdleTime()

void CbacProcess::setUdpIdleTime  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the value for UDP idle time. 

Parameters
     idleTime,the| value for UDP idle time.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CCbacProcess.pki](_c_cbac_process_8pki.html)


