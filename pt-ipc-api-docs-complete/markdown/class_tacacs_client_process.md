# Cisco Packet Tracer Extensions API: TacacsClientProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_tacacs_client_process.html

---

[TacacsClientProcess](class_tacacs_client_process.html "TacacsClientProcess holds and manipulates TACACS client.") holds and manipulates TACACS client. [More...](class_tacacs_client_process.html#details)

##  Public Member Functions  
  
---  
void | [removeFromServerVect](class_tacacs_client_process.html#acf1235d4e9153cbdb417726a3c55ae36) (ip)  
| Removes the specified client IP address from the ACS server. [More...](class_tacacs_client_process.html#acf1235d4e9153cbdb417726a3c55ae36)  
  
void | [addToServerVect](class_tacacs_client_process.html#a02a4f21063b719083b9d7479bcfdfa19) (ip, string, bool)  
| Adds the specified client IP address to the ACS server. [More...](class_tacacs_client_process.html#a02a4f21063b719083b9d7479bcfdfa19)  
  
int | [getServerCount](class_tacacs_client_process.html#ae52559ded86034820d4d60caeae09a06) ()  
| Returns the number of ACS servers. [More...](class_tacacs_client_process.html#ae52559ded86034820d4d60caeae09a06)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[TacacsClientProcess](class_tacacs_client_process.html "TacacsClientProcess holds and manipulates TACACS client.") holds and manipulates TACACS client. 

## Member Function Documentation

## ◆ addToServerVect()

void TacacsClientProcess::addToServerVect  | ( | ip  | ,   
---|---|---|---  
|  | string  | ,   
|  | bool  |   
| ) | |   
  
Adds the specified client IP address to the ACS server. 

Parameters
     ipAddr,the| client IP address of interest.   
---|---  
keyStr,the| secret key.   
isSingleConnection,true| for single connection, false for multiple connection.   
  
## ◆ getServerCount()

int TacacsClientProcess::getServerCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of ACS servers. 

Returns
    int, the number of ACS servers. 

## ◆ removeFromServerVect()

void TacacsClientProcess::removeFromServerVect  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Removes the specified client IP address from the ACS server. 

Parameters
     ipAddr,the| client IP address of interest.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CTacacsClientProcess.pki](_c_tacacs_client_process_8pki.html)


