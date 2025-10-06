# Cisco Packet Tracer Extensions API: SshServerProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_ssh_server_process.html

---

[SshServerProcess](class_ssh_server_process.html "SshServerProcess handles and manipulates the SSH service.") handles and manipulates the SSH service. [More...](class_ssh_server_process.html#details)

##  Public Member Functions  
  
---  
void | [setVersion](class_ssh_server_process.html#ab80b9e52297964465693c79c2d61bc44) (Ssh::SshVersion)  
| Sets the SSH version. [More...](class_ssh_server_process.html#ab80b9e52297964465693c79c2d61bc44)  
  
Ssh::SshVersion | [getVersion](class_ssh_server_process.html#a4077c65f78f28aaac5fd7a5dc15d2e5a) ()  
| Returns the SSH version. [More...](class_ssh_server_process.html#a4077c65f78f28aaac5fd7a5dc15d2e5a)  
  
bool | [isUsernameReceived](class_ssh_server_process.html#a9789b28af36c813549397b7c753c0cd7) ()  
| Returns true if the username is received, otherwise false. [More...](class_ssh_server_process.html#a9789b28af36c813549397b7c753c0cd7)  
  
void | [usernameReceived](class_ssh_server_process.html#abf111ac0c7093a5c679ef80fd032bd99) (bool)  
| Sets the username as received or not received. [More...](class_ssh_server_process.html#abf111ac0c7093a5c679ef80fd032bd99)  
  
void | [setRetryAmount](class_ssh_server_process.html#a2c03edf75e650050614e319ce7d35fe5) (int)  
| Sets the retry amount. [More...](class_ssh_server_process.html#a2c03edf75e650050614e319ce7d35fe5)  
  
int | [getRetryAmount](class_ssh_server_process.html#adfa3e544d35ff7a3862520c81e7ec7e9) ()  
| Returns the retry amount. [More...](class_ssh_server_process.html#adfa3e544d35ff7a3862520c81e7ec7e9)  
  
void | [setAuthTimeout](class_ssh_server_process.html#a9b861cf7a1ebccd8e13da9c571716960) (int)  
| Sets the authentication timeout. [More...](class_ssh_server_process.html#a9b861cf7a1ebccd8e13da9c571716960)  
  
int | [getAuthTimeout](class_ssh_server_process.html#ab50362111a0968b34606d6a5f61ea816) ()  
| Returns the authentication timeout. [More...](class_ssh_server_process.html#ab50362111a0968b34606d6a5f61ea816)  
  
Public Member Functions inherited from [TelnetServerProcess](class_telnet_server_process.html)  
int | [getTelnetClientCount](class_telnet_server_process.html#a60a675fc8503d9ff3bd9c2a1da492785) ()  
| Returns the number of telnet clients connected. [More...](class_telnet_server_process.html#a60a675fc8503d9ff3bd9c2a1da492785)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[SshServerProcess](class_ssh_server_process.html "SshServerProcess handles and manipulates the SSH service.") handles and manipulates the SSH service. 

## Member Function Documentation

## ◆ getAuthTimeout()

int SshServerProcess::getAuthTimeout  | ( | | ) |   
---|---|---|---|---  
  
Returns the authentication timeout. 

Parameters
     int,the| authentication timeout.   
---|---  
  
## ◆ getRetryAmount()

int SshServerProcess::getRetryAmount  | ( | | ) |   
---|---|---|---|---  
  
Returns the retry amount. 

Returns
    int, the retry amount. 

## ◆ getVersion()

Ssh::SshVersion SshServerProcess::getVersion  | ( | | ) |   
---|---|---|---|---  
  
Returns the SSH version. 

Returns
    enum<Ssh::SshVersion>, the SSH version. SSH versions: shVerDefault = 0, sshVerOne = 1, sshVerTwo = 2 

## ◆ isUsernameReceived()

bool SshServerProcess::isUsernameReceived  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the username is received, otherwise false. 

Returns
    bool, true if the username is received, otherwise false. 

## ◆ setAuthTimeout()

void SshServerProcess::setAuthTimeout  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the authentication timeout. 

Parameters
     sec,the| authentication timeout.   
---|---  
  
## ◆ setRetryAmount()

void SshServerProcess::setRetryAmount  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the retry amount. 

Parameters
     amt,the| retry amount.   
---|---  
  
## ◆ setVersion()

void SshServerProcess::setVersion  | ( | Ssh::SshVersion  | | ) |   
---|---|---|---|---|---  
  
Sets the SSH version. 

Parameters
     version,the| SSH version. SSH versions: shVerDefault = 0, sshVerOne = 1, sshVerTwo = 2   
---|---  
  
## ◆ usernameReceived()

void SshServerProcess::usernameReceived  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Sets the username as received or not received. 

Parameters
     usernameReceived,true| for received, false for not received.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CSshServerProcess.pki](_c_ssh_server_process_8pki.html)


