# Cisco Packet Tracer Extensions API: MultiUserManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_multi_user_manager.html

---

[MultiUserManager](class_multi_user_manager.html "MultiUserManager is the entry point to all Multiuser functionalities.") is the entry point to all Multiuser functionalities. [More...](class_multi_user_manager.html#details)

##  Public Member Functions  
  
---  
bool | [startServer](class_multi_user_manager.html#a58f530349fd07508db1bb7c361b88422) (int, QString)  
| Starts the Multiuser server with the specified port number and password. [More...](class_multi_user_manager.html#a58f530349fd07508db1bb7c361b88422)  
  
bool | [stopServer](class_multi_user_manager.html#a9651abe7af9671cbccf5c6b82ab7350a) ()  
| Stops the Multiuser server. [More...](class_multi_user_manager.html#a9651abe7af9671cbccf5c6b82ab7350a)  
  
bool | [isServerStarted](class_multi_user_manager.html#a4741f23b17f22d1c6b1d6fb6ab6001ce) ()  
| Returns true if the Multiuser server is started, otherwise false. [More...](class_multi_user_manager.html#a4741f23b17f22d1c6b1d6fb6ab6001ce)  
  
int | [getPortNumber](class_multi_user_manager.html#ae0100627ed59d6d8b270ac1d6c03be18) ()  
| Returns the port number the Multiuser server is listening on. [More...](class_multi_user_manager.html#ae0100627ed59d6d8b270ac1d6c03be18)  
  
void | [setPassword](class_multi_user_manager.html#ad604a554732338dd1fa2902fda77c8ae) (QString)  
| Sets the password for the Multiuser server. [More...](class_multi_user_manager.html#ad604a554732338dd1fa2902fda77c8ae)  
  
QString | [getPassword](class_multi_user_manager.html#a02eae7e901c5bdd3c9a8eb6580c3b26b) ()  
| Returns the password for the Multiuser server. [More...](class_multi_user_manager.html#a02eae7e901c5bdd3c9a8eb6580c3b26b)  
  
void | [setAcceptMode](class_multi_user_manager.html#ace757466a8fedebf7332b8ee36903294) (AcceptMode)  
| Sets the existing remote networks accept mode. [More...](class_multi_user_manager.html#ace757466a8fedebf7332b8ee36903294)  
  
AcceptMode | [getAcceptMode](class_multi_user_manager.html#a6122fb17227afbdbf16c480b2e3fa137) ()  
| Returns the existing remote networks accept mode. [More...](class_multi_user_manager.html#a6122fb17227afbdbf16c480b2e3fa137)  
  
void | [setNewRNetAcceptMode](class_multi_user_manager.html#a0dd6d632c699fc8bdbf3f69d11806ce5) (AcceptMode)  
| Sets the new remote networks accept mode. [More...](class_multi_user_manager.html#a0dd6d632c699fc8bdbf3f69d11806ce5)  
  
AcceptMode | [getNewRNetAcceptMode](class_multi_user_manager.html#ac2fd9ff7d8d3d5395d45d7a2ac087e67) ()  
| Returns the new remote networks accept mode. [More...](class_multi_user_manager.html#ac2fd9ff7d8d3d5395d45d7a2ac087e67)  
  
int | [getRemoteNetworkCount](class_multi_user_manager.html#afc4003c1d805e54760785a22c41cce0d) ()  
| Returns the number of remote networks on the workspace. [More...](class_multi_user_manager.html#afc4003c1d805e54760785a22c41cce0d)  
  
[RemoteNetwork](class_remote_network.html) | [getRemoteNetworkAt](class_multi_user_manager.html#a718ff32de3ebd3535a147938f2b731ef) (int)  
| Returns the remote network at the specified index. [More...](class_multi_user_manager.html#a718ff32de3ebd3535a147938f2b731ef)  
  
[RemoteNetwork](class_remote_network.html) | [getRemoteNetworkByName](class_multi_user_manager.html#aa7300eb23cb3f38c7f98edb474a83d5b) (QString)  
| Returns the remote network with the specified name. [More...](class_multi_user_manager.html#aa7300eb23cb3f38c7f98edb474a83d5b)  
  
QString | [getListeningAddresses](class_multi_user_manager.html#a64a8b4b7107329a2280bdb1c2afec583) ()  
| Returns the IP addresses the Multiuser server is listening on. [More...](class_multi_user_manager.html#a64a8b4b7107329a2280bdb1c2afec583)  
  
void | [writeUdpDatagram](class_multi_user_manager.html#ae8da4bcff8185e785b4d74d21492e8bb) ()  
| Sends a UDP datagram over the Multiuser connection. [More...](class_multi_user_manager.html#ae8da4bcff8185e785b4d74d21492e8bb)  
  
QString | [getMulticastSenderIp](class_multi_user_manager.html#a33f35971cf040b5b417398a6ff6671e3) ()  
| Returns the source IP address of the multicast datagram. [More...](class_multi_user_manager.html#a33f35971cf040b5b417398a6ff6671e3)  
  
  
## Detailed Description

[MultiUserManager](class_multi_user_manager.html "MultiUserManager is the entry point to all Multiuser functionalities.") is the entry point to all Multiuser functionalities. 

## Member Function Documentation

## ◆ getAcceptMode()

AcceptMode MultiUserManager::getAcceptMode  | ( | | ) |   
---|---|---|---|---  
  
Returns the existing remote networks accept mode. 

Returns
    enum<AcceptMode>, the accept mode. Modes: eAlwaysAccept = 0, eAlwaysDeny = 1, ePrompt = 2 

## ◆ getListeningAddresses()

QString MultiUserManager::getListeningAddresses  | ( | | ) |   
---|---|---|---|---  
  
Returns the IP addresses the Multiuser server is listening on. 

Returns
    QString, the IP addresses the Multiuser server is listening on. 

## ◆ getMulticastSenderIp()

QString MultiUserManager::getMulticastSenderIp  | ( | | ) |   
---|---|---|---|---  
  
Returns the source IP address of the multicast datagram. 

Returns
    QString, the source IP address of the multicast datagram. 

## ◆ getNewRNetAcceptMode()

AcceptMode MultiUserManager::getNewRNetAcceptMode  | ( | | ) |   
---|---|---|---|---  
  
Returns the new remote networks accept mode. 

Returns
    enum<AcceptMode>, the accept mode. Modes: eAlwaysAccept = 0, eAlwaysDeny = 1, ePrompt = 2 

## ◆ getPassword()

QString MultiUserManager::getPassword  | ( | | ) |   
---|---|---|---|---  
  
Returns the password for the Multiuser server. 

Returns
    QString, the password for the Multiuser server. 

## ◆ getPortNumber()

int MultiUserManager::getPortNumber  | ( | | ) |   
---|---|---|---|---  
  
Returns the port number the Multiuser server is listening on. 

Returns
    int, the port number the Multiuser server is listening on. 

## ◆ getRemoteNetworkAt()

[RemoteNetwork](class_remote_network.html) MultiUserManager::getRemoteNetworkAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the remote network at the specified index. 

Parameters
     index,the| index of the remote network of interest.  
---|---  
  
Returns
    [RemoteNetwork](class_remote_network.html "RemoteNetwork handles and manipulates Multiuser remote networks."), the [RemoteNetwork](class_remote_network.html "RemoteNetwork handles and manipulates Multiuser remote networks.") object at the specified index. 

## ◆ getRemoteNetworkByName()

[RemoteNetwork](class_remote_network.html) MultiUserManager::getRemoteNetworkByName  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the remote network with the specified name. 

Parameters
     name,the| name of the remote network of interest.  
---|---  
  
Returns
    [RemoteNetwork](class_remote_network.html "RemoteNetwork handles and manipulates Multiuser remote networks."), the [RemoteNetwork](class_remote_network.html "RemoteNetwork handles and manipulates Multiuser remote networks.") object with the specified name. 

## ◆ getRemoteNetworkCount()

int MultiUserManager::getRemoteNetworkCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of remote networks on the workspace. 

Returns
    int, the number of remote networks on the workspace. 

## ◆ isServerStarted()

bool MultiUserManager::isServerStarted  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the Multiuser server is started, otherwise false. 

Returns
    bool, true if the Multiuser server is started, otherwise false. 

## ◆ setAcceptMode()

void MultiUserManager::setAcceptMode  | ( | AcceptMode  | | ) |   
---|---|---|---|---|---  
  
Sets the existing remote networks accept mode. 

Parameters
     acceptMode,the| accept mode. Modes: eAlwaysAccept = 0, eAlwaysDeny = 1, ePrompt = 2   
---|---  
  
## ◆ setNewRNetAcceptMode()

void MultiUserManager::setNewRNetAcceptMode  | ( | AcceptMode  | | ) |   
---|---|---|---|---|---  
  
Sets the new remote networks accept mode. 

Parameters
     acceptMode,the| accept mode. Modes: eAlwaysAccept = 0, eAlwaysDeny = 1, ePrompt = 2   
---|---  
  
## ◆ setPassword()

void MultiUserManager::setPassword  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Sets the password for the Multiuser server. 

Parameters
     password,the| password for Multiuser server.   
---|---  
  
## ◆ startServer()

bool MultiUserManager::startServer  | ( | int  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Starts the Multiuser server with the specified port number and password. 

Parameters
     portNumber,the| port number to listen on.   
---|---  
password,password.|   
  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ stopServer()

bool MultiUserManager::stopServer  | ( | | ) |   
---|---|---|---|---  
  
Stops the Multiuser server. 

Returns
    bool, true if successful, otherwise false. 

## ◆ writeUdpDatagram()

void MultiUserManager::writeUdpDatagram  | ( | | ) |   
---|---|---|---|---  
  
Sends a UDP datagram over the Multiuser connection. 

* * *

The documentation for this class was generated from the following file:

  * [CMUManager.pki](_c_m_u_manager_8pki.html)


