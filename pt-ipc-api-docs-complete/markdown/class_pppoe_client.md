# Cisco Packet Tracer Extensions API: PppoeClient Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_pppoe_client.html

---

[PppoeClient](class_pppoe_client.html "PppoeClient handles and manipulates the PPPoE client.") handles and manipulates the PPPoE client. [More...](class_pppoe_client.html#details)

##  Public Member Functions  
  
---  
void | [setUsername](class_pppoe_client.html#a11f09d1eb36c53c4e1822e68209a1938) (string)  
| Sets the username. [More...](class_pppoe_client.html#a11f09d1eb36c53c4e1822e68209a1938)  
  
void | [setConnectionStatus](class_pppoe_client.html#a2458f8f93951ea1c6403840d1305dc5f) (PppoeConnectionStatus)  
| Sets the status. [More...](class_pppoe_client.html#a2458f8f93951ea1c6403840d1305dc5f)  
  
string | [getUsername](class_pppoe_client.html#a5d6681e76380943fd233af657d11dd23) ()  
| Gets the username. [More...](class_pppoe_client.html#a5d6681e76380943fd233af657d11dd23)  
  
void | [setPassword](class_pppoe_client.html#afe880d44a95ce3c207030dca22b052e6) (string)  
| Sets the password. [More...](class_pppoe_client.html#afe880d44a95ce3c207030dca22b052e6)  
  
string | [getPassword](class_pppoe_client.html#a4c344a8689a014fe9e8dbf006f8e09f6) ()  
| Gets the password. [More...](class_pppoe_client.html#a4c344a8689a014fe9e8dbf006f8e09f6)  
  
void | [setServiceName](class_pppoe_client.html#a49c0ed347a4450fce44251295dea1e0d) (string)  
| Sets the service name. [More...](class_pppoe_client.html#a49c0ed347a4450fce44251295dea1e0d)  
  
string | [getServiceName](class_pppoe_client.html#adfe473df07c2c1df26d356d0f9f8095e) ()  
| Gets the service name. [More...](class_pppoe_client.html#adfe473df07c2c1df26d356d0f9f8095e)  
  
void | [connect](class_pppoe_client.html#a5ff9af7693ebf557a54cc90e575d611c) (string, string)  
| Makes a PPPoE connection with the specified username and password. [More...](class_pppoe_client.html#a5ff9af7693ebf557a54cc90e575d611c)  
  
void | [connectFromPc](class_pppoe_client.html#a6c5b19853474236ecdd4b3a164668a63) (string, string)  
void | [disconnectFromPc](class_pppoe_client.html#a41a19e3038503d3ce9d318c208c8bfec) ()  
void | [disconnect](class_pppoe_client.html#a75e7eb46aeb4512a15726d801ce94973) (int, PppoeConnectionStatus, bool)  
| Disconnects the PPPoE connection. enum EPppoeConnectionStatus { eConnected = 0, eConnecting = 1, ePoolRejected = 2, eDisconnected = 3, eTimeout = 4, eNoKeepAlive = 5, eAuthentcationFailed = 6 };. [More...](class_pppoe_client.html#a75e7eb46aeb4512a15726d801ce94973)  
  
bool | [isConnected](class_pppoe_client.html#a615496dd8334c91b5bd133698c773530) ()  
| Checks if it is connected. [More...](class_pppoe_client.html#a615496dd8334c91b5bd133698c773530)  
  
void | [setConnected](class_pppoe_client.html#a9ba6fa226283f9c4b8add444caf8769f) (bool)  
| Set if it is connected. [More...](class_pppoe_client.html#a9ba6fa226283f9c4b8add444caf8769f)  
  
PppoeConnectionStatus | [getConnectionStatus](class_pppoe_client.html#a54fb1eb3fe61af3cbfbd7933bb25b007) ()  
| Gets the connection status. [More...](class_pppoe_client.html#a54fb1eb3fe61af3cbfbd7933bb25b007)  
  
void | [updatePppoeInfo](class_pppoe_client.html#a22d5eb9bbccabf1df5887f0802fa0029) (QString, QString)  
| This event is emitted when a PPPoE update info event occurs. [More...](class_pppoe_client.html#a22d5eb9bbccabf1df5887f0802fa0029)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[PppoeClient](class_pppoe_client.html "PppoeClient handles and manipulates the PPPoE client.") handles and manipulates the PPPoE client. 

## Member Function Documentation

## ◆ connect()

void PppoeClient::connect  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Makes a PPPoE connection with the specified username and password. 

Parameters
     userName,the| username.   
---|---  
password,the| password.   
  
## ◆ connectFromPc()

void PppoeClient::connectFromPc  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
## ◆ disconnect()

void PppoeClient::disconnect  | ( | int  | ,   
---|---|---|---  
|  | PppoeConnectionStatus  | ,   
|  | bool  |   
| ) | |   
  
Disconnects the PPPoE connection. enum EPppoeConnectionStatus { eConnected = 0, eConnecting = 1, ePoolRejected = 2, eDisconnected = 3, eTimeout = 4, eNoKeepAlive = 5, eAuthentcationFailed = 6 };. 

## ◆ disconnectFromPc()

void PppoeClient::disconnectFromPc  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getConnectionStatus()

PppoeConnectionStatus PppoeClient::getConnectionStatus  | ( | | ) |   
---|---|---|---|---  
  
Gets the connection status. 

Returns
    enum<PppoeConnectionStatus> types: eConnected = 0, eConnecting = 1, ePoolRejected = 2, eDisconnected = 3, eTimeout = 4, eNoKeepAlive = 5, eAuthentcationFailed = 6 

## ◆ getPassword()

string PppoeClient::getPassword  | ( | | ) |   
---|---|---|---|---  
  
Gets the password. 

Returns
    , the password. 

## ◆ getServiceName()

string PppoeClient::getServiceName  | ( | | ) |   
---|---|---|---|---  
  
Gets the service name. 

Returns
    string, the service name to use. 

## ◆ getUsername()

string PppoeClient::getUsername  | ( | | ) |   
---|---|---|---|---  
  
Gets the username. 

Returns
    string, the username. 

## ◆ isConnected()

bool PppoeClient::isConnected  | ( | | ) |   
---|---|---|---|---  
  
Checks if it is connected. 

Returns
    bool, true if connected, false if not. 

## ◆ setConnected()

void PppoeClient::setConnected  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Set if it is connected. 

Parameters
     flag,true| if connected, false if not.   
---|---  
  
## ◆ setConnectionStatus()

void PppoeClient::setConnectionStatus  | ( | PppoeConnectionStatus  | | ) |   
---|---|---|---|---|---  
  
Sets the status. 

Parameters
     status,the| status types: eConnected = 0, eConnecting = 1, ePoolRejected = 2, eDisconnected = 3, eTimeout = 4, eNoKeepAlive = 5, eAuthentcationFailed = 6   
---|---  
  
## ◆ setPassword()

void PppoeClient::setPassword  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the password. 

Parameters
     password,the| password.   
---|---  
  
## ◆ setServiceName()

void PppoeClient::setServiceName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the service name. 

Parameters
     service,the| service name to use.   
---|---  
  
## ◆ setUsername()

void PppoeClient::setUsername  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the username. 

Parameters
     userName,the| username.   
---|---  
  
## ◆ updatePppoeInfo()

void PppoeClient::updatePppoeInfo  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
This event is emitted when a PPPoE update info event occurs. 

  * deviceName, name of hte device this was from. 
  * info, the PPPoE update info.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

* * *

The documentation for this class was generated from the following file:

  * [CPppoeClient.pki](_c_pppoe_client_8pki.html)


