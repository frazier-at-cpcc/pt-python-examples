# Cisco Packet Tracer Extensions API: NtpPTProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_ntp_p_t_process.html

---

##  Public Member Functions  
  
---  
void | [setEnabled](class_ntp_p_t_process.html#a7e252cab5193d45148feb6c1088740e7) (bool)  
| Enables or disables the NTP server. [More...](class_ntp_p_t_process.html#a7e252cab5193d45148feb6c1088740e7)  
  
bool | [isEnabled](class_ntp_p_t_process.html#a2a60447d67b807d9d85fa7de31b5ba1a) ()  
| Returns true if the NTP server is enabled, otherwise false. [More...](class_ntp_p_t_process.html#a2a60447d67b807d9d85fa7de31b5ba1a)  
  
void | [setKeyID](class_ntp_p_t_process.html#ae34d818fec49fa2537fbeabcd9f2c9f5) (int)  
| Sets the NTP authentication key to the specified value. [More...](class_ntp_p_t_process.html#ae34d818fec49fa2537fbeabcd9f2c9f5)  
  
int | [getKeyId](class_ntp_p_t_process.html#aa42ca242e6aa2c642904e8fe249da60a) ()  
| Returns the NTP authentication key. [More...](class_ntp_p_t_process.html#aa42ca242e6aa2c642904e8fe249da60a)  
  
string | [getServerMd5Str](class_ntp_p_t_process.html#a2c3563417b058cf1d9de9828436b32e6) ()  
| Returns the NTP authentication password. [More...](class_ntp_p_t_process.html#a2c3563417b058cf1d9de9828436b32e6)  
  
void | [setServerMd5Str](class_ntp_p_t_process.html#a3b2028ec748686f3444ae0197505194c) (string)  
| Sets the NTP authentication password. [More...](class_ntp_p_t_process.html#a3b2028ec748686f3444ae0197505194c)  
  
bool | [getNtpServerAuthentication](class_ntp_p_t_process.html#a0cc130316e9d1e46fb866900d2988fb5) ()  
| Get if the server is set to authenticate. [More...](class_ntp_p_t_process.html#a0cc130316e9d1e46fb866900d2988fb5)  
  
void | [setNtpServerAuthentication](class_ntp_p_t_process.html#ac8acf737f2c6df87fbda5dfcd512118f) (bool)  
| Set if the server is supposed to authenticate. [More...](class_ntp_p_t_process.html#ac8acf737f2c6df87fbda5dfcd512118f)  
  
void | [setRefClockTime](class_ntp_p_t_process.html#aca9c2afc4b056b8115805c80b47da5b7) (string)  
| Set the ref clock time. [More...](class_ntp_p_t_process.html#aca9c2afc4b056b8115805c80b47da5b7)  
  
string | [getRefClockTime](class_ntp_p_t_process.html#ae9606de5956ceede811088e89929d74f) ()  
| Gets the ref clock time. [More...](class_ntp_p_t_process.html#ae9606de5956ceede811088e89929d74f)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Member Function Documentation

## ◆ getKeyId()

int NtpPTProcess::getKeyId  | ( | | ) |   
---|---|---|---|---  
  
Returns the NTP authentication key. 

Returns
    long, the value of the NTP authentication key. 

## ◆ getNtpServerAuthentication()

bool NtpPTProcess::getNtpServerAuthentication  | ( | | ) |   
---|---|---|---|---  
  
Get if the server is set to authenticate. 

Returns
    bool, true if it is set to authenticate, false if not. 

## ◆ getRefClockTime()

string NtpPTProcess::getRefClockTime  | ( | | ) |   
---|---|---|---|---  
  
Gets the ref clock time. 

Returns
    string, ref clock time. Example time: "Tue May 24 2016 10:21:27.929 UTC". 

## ◆ getServerMd5Str()

string NtpPTProcess::getServerMd5Str  | ( | | ) |   
---|---|---|---|---  
  
Returns the NTP authentication password. 

Returns
    string, the NTP authentication password. 

## ◆ isEnabled()

bool NtpPTProcess::isEnabled  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the NTP server is enabled, otherwise false. 

Returns
    bool, true if the NTP server is enabled, otherwise false. 

## ◆ setEnabled()

void NtpPTProcess::setEnabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables the NTP server. 

Parameters
     enable,true| to enable the NTP server, false to disable it.   
---|---  
  
## ◆ setKeyID()

void NtpPTProcess::setKeyID  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the NTP authentication key to the specified value. 

Parameters
     key,the| NTP authentication key value.   
---|---  
  
## ◆ setNtpServerAuthentication()

void NtpPTProcess::setNtpServerAuthentication  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Set if the server is supposed to authenticate. 

Parameters
     yes,true| if it should be set to authenticate, false if not.   
---|---  
  
## ◆ setRefClockTime()

void NtpPTProcess::setRefClockTime  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Set the ref clock time. 

Parameters
     time,time| to set the clock to. Example time: "Tue May 24 2016 10:21:27.929 UTC".   
---|---  
  
## ◆ setServerMd5Str()

void NtpPTProcess::setServerMd5Str  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the NTP authentication password. 

Parameters
     md5,the| NTP authentication password.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CNtpPTProcess.pki](_c_ntp_p_t_process_8pki.html)


