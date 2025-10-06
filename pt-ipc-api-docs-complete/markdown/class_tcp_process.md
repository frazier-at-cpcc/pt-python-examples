# Cisco Packet Tracer Extensions API: TcpProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_tcp_process.html

---

[TcpProcess](class_tcp_process.html "TcpProcess handles and manipulates the TCP process.") handles and manipulates the TCP process. [More...](class_tcp_process.html#details)

##  Public Member Functions  
  
---  
short | [getUserDefinedMSS](class_tcp_process.html#a6b7ef642e82043c955954a4c80e453f8) ()  
| Returns the maximum segment size value. [More...](class_tcp_process.html#a6b7ef642e82043c955954a4c80e453f8)  
  
void | [setUserDefinedMSS](class_tcp_process.html#a282f4a5d8ddadc67ca07c5e7d876736a) (short)  
| Sets the maximum segment size value. [More...](class_tcp_process.html#a282f4a5d8ddadc67ca07c5e7d876736a)  
  
int | [getUserDefinedWindowSize](class_tcp_process.html#a10a0b7a6b95c9c7bb8894cdea5b1535a) ()  
| Returns the window size. [More...](class_tcp_process.html#a10a0b7a6b95c9c7bb8894cdea5b1535a)  
  
bool | [isNagleEnabled](class_tcp_process.html#a460ed7a9c909952e646139fc7e7facbe) ()  
| Returns true if Nagle's algorithm is enabled, otherwise false. [More...](class_tcp_process.html#a460ed7a9c909952e646139fc7e7facbe)  
  
void | [setNagleEnabled](class_tcp_process.html#a65056ab42428898ede1d264772fa6974) (bool)  
| Enables or disables Nagle's algorithm. [More...](class_tcp_process.html#a65056ab42428898ede1d264772fa6974)  
  
int | [getNagleWaitingInterval](class_tcp_process.html#a627009589ce1d0f85a8e2a4fe86e82de) ()  
| Returns Nagle's algorithm waiting interval. [More...](class_tcp_process.html#a627009589ce1d0f85a8e2a4fe86e82de)  
  
void | [setNagleWaitingInterval](class_tcp_process.html#a72b56ed1773e677bf8942a25f7a15cd4) (int)  
| Sets Nagle's algorithm waiting interval. [More...](class_tcp_process.html#a72b56ed1773e677bf8942a25f7a15cd4)  
  
[CustomTcpProcess](class_custom_tcp_process.html) | [listen](class_tcp_process.html#a2f8cef4a617c7eff19b0e9b8fafb3c57) (int, bool)  
| Start a tcp connection that listens. [More...](class_tcp_process.html#a2f8cef4a617c7eff19b0e9b8fafb3c57)  
  
[CustomTcpProcess](class_custom_tcp_process.html) | [connect](class_tcp_process.html#aeacd6324db8899cdc3c62054003d0879) (ip, int, int, int, [FrameInstance](class_frame_instance.html))  
| Start a tcp connection for connecting. [More...](class_tcp_process.html#aeacd6324db8899cdc3c62054003d0879)  
  
void | [deleteCustomProcess](class_tcp_process.html#a6d8820bcdb744ac4b372ecfaa4692e35) ([CustomTcpProcess](class_custom_tcp_process.html))  
| Delete a custom tcp process created for listening or connecting. [More...](class_tcp_process.html#a6d8820bcdb744ac4b372ecfaa4692e35)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[TcpProcess](class_tcp_process.html "TcpProcess handles and manipulates the TCP process.") handles and manipulates the TCP process. 

## Member Function Documentation

## ◆ connect()

[CustomTcpProcess](class_custom_tcp_process.html) TcpProcess::connect  | ( | ip  | ,   
---|---|---|---  
|  | int  | ,   
|  | int  | ,   
|  | int  | ,   
|  | [FrameInstance](class_frame_instance.html) |   
| ) | |   
  
Start a tcp connection for connecting. 

Parameters
     destinationIp,destination| ip address at which the tcp connection will connect to   
---|---  
destinationPort,destination| port number at which the tcp connection will connect to   
sourcePort,source| port number at which the tcp connection is from   
timeout,the| time out value at which the tcp connection will stop trying to connect   
frameInstance,frameInstance| object   
  
Returns
    [CustomTcpProcess](class_custom_tcp_process.html "CustomTcpProcess is the process that manipulates the custom TCP process."), [CustomTcpProcess](class_custom_tcp_process.html "CustomTcpProcess is the process that manipulates the custom TCP process.") object 

## ◆ deleteCustomProcess()

void TcpProcess::deleteCustomProcess  | ( | [CustomTcpProcess](class_custom_tcp_process.html) | | ) |   
---|---|---|---|---|---  
  
Delete a custom tcp process created for listening or connecting. 

Parameters
     process,[CustomTcpProcess](class_custom_tcp_process.html "CustomTcpProcess is the process that manipulates the custom TCP process.")| object   
---|---  
  
## ◆ getNagleWaitingInterval()

int TcpProcess::getNagleWaitingInterval  | ( | | ) |   
---|---|---|---|---  
  
Returns Nagle's algorithm waiting interval. 

Returns
    int, Nagle's algorithm waiting interval. 

## ◆ getUserDefinedMSS()

short TcpProcess::getUserDefinedMSS  | ( | | ) |   
---|---|---|---|---  
  
Returns the maximum segment size value. 

Returns
    short, the maximum segment size value. 

## ◆ getUserDefinedWindowSize()

int TcpProcess::getUserDefinedWindowSize  | ( | | ) |   
---|---|---|---|---  
  
Returns the window size. 

Returns
    int, the window size. 

## ◆ isNagleEnabled()

bool TcpProcess::isNagleEnabled  | ( | | ) |   
---|---|---|---|---  
  
Returns true if Nagle's algorithm is enabled, otherwise false. 

Returns
    bool, true if Nagle's algorithm is enabled, otherwise false. 

## ◆ listen()

[CustomTcpProcess](class_custom_tcp_process.html) TcpProcess::listen  | ( | int  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Start a tcp connection that listens. 

Parameters
     port,port| number at which the tcp connection listens at   
---|---  
requestNotify,true| if a notify is requested or false if it's not   
  
Returns
    [CustomTcpProcess](class_custom_tcp_process.html "CustomTcpProcess is the process that manipulates the custom TCP process."), [CustomTcpProcess](class_custom_tcp_process.html "CustomTcpProcess is the process that manipulates the custom TCP process.") object 

## ◆ setNagleEnabled()

void TcpProcess::setNagleEnabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables Nagle's algorithm. 

Parameters
     val,true| to enable Nagle's algorithm, false to disable it.   
---|---  
  
## ◆ setNagleWaitingInterval()

void TcpProcess::setNagleWaitingInterval  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets Nagle's algorithm waiting interval. 

Parameters
     interval,Nagle's| algorithm waiting interval.   
---|---  
  
## ◆ setUserDefinedMSS()

void TcpProcess::setUserDefinedMSS  | ( | short  | | ) |   
---|---|---|---|---|---  
  
Sets the maximum segment size value. 

Parameters
     short,the| maximum segment size value.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CTcpProcess.pki](_c_tcp_process_8pki.html)


