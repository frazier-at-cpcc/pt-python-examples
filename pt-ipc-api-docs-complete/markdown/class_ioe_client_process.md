# Cisco Packet Tracer Extensions API: IoeClientProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_ioe_client_process.html

---

[IoeClientProcess](class_ioe_client_process.html "IoeClientProcess handles and manipulates the IoE client process for IoE devices.") handles and manipulates the IoE client process for IoE devices. [More...](class_ioe_client_process.html#details)

##  Public Member Functions  
  
---  
bool | [setupRemoteApi](class_ioe_client_process.html#a4c066fd8d661e60a8c7648966b8dd44a) (QString)  
| setup the API call in remote server, returns true if successful, false otherwise. [More...](class_ioe_client_process.html#a4c066fd8d661e60a8c7648966b8dd44a)  
  
void | [reportStates](class_ioe_client_process.html#aba7800a3720db237646f557b80a0fc73) (QString)  
| send the state of the IoE client to server. [More...](class_ioe_client_process.html#aba7800a3720db237646f557b80a0fc73)  
  
void | [inputReceived](class_ioe_client_process.html#af14c573f95acf969558e46d3657cea7b) (QString)  
| This event is emitted when data coming from IoE client. [More...](class_ioe_client_process.html#af14c573f95acf969558e46d3657cea7b)  
  
void | [stateSet](class_ioe_client_process.html#a17a495717961252694b8c09bc822907c) (string, QString)  
| This event is emitted new state is set in the IoE client. [More...](class_ioe_client_process.html#a17a495717961252694b8c09bc822907c)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[IoeClientProcess](class_ioe_client_process.html "IoeClientProcess handles and manipulates the IoE client process for IoE devices.") handles and manipulates the IoE client process for IoE devices. 

## Member Function Documentation

## ◆ inputReceived()

void IoeClientProcess::inputReceived  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when data coming from IoE client. 

  * states, the string of the data get send to server.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ reportStates()

void IoeClientProcess::reportStates  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
send the state of the IoE client to server. 

Parameters
     states,the| state of the IoE client.   
---|---  
  
## ◆ setupRemoteApi()

bool IoeClientProcess::setupRemoteApi  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
setup the API call in remote server, returns true if successful, false otherwise. 

Parameters
     json,the| API call to server in json format.  
---|---  
  
Returns
    bool, true if successful, false otherwise. 

## ◆ stateSet()

void IoeClientProcess::stateSet  | ( | string  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
This event is emitted new state is set in the IoE client. 

  * stateName, the name of the state. 
  * value, the value of the state.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

* * *

The documentation for this class was generated from the following file:

  * [CIoeClientProcess.pki](_c_ioe_client_process_8pki.html)


