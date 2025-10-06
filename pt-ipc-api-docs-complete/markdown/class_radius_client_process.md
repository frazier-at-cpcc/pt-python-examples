# Cisco Packet Tracer Extensions API: RadiusClientProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_radius_client_process.html

---

[RadiusClientProcess](class_radius_client_process.html "RadiusClientProcess holds and manipulates the RADIUS client.") holds and manipulates the RADIUS client. [More...](class_radius_client_process.html#details)

##  Public Member Functions  
  
---  
void | [removeFromServerVect](class_radius_client_process.html#a9153b1e220ad16d2f297628e12034e8f) (ip)  
| Removes the specified client IP address from the ACS server. [More...](class_radius_client_process.html#a9153b1e220ad16d2f297628e12034e8f)  
  
void | [removeFromServerVectByName](class_radius_client_process.html#a1820ccfeaabad095737d09ae37f9e5c3) (string)  
| Removes the specified RADIUS server. [More...](class_radius_client_process.html#a1820ccfeaabad095737d09ae37f9e5c3)  
  
void | [addToServerVect](class_radius_client_process.html#a3e2f668eda99f52bbf60107fe6ccc088) (ip, string, bool, int, string)  
| Adds the specified client IP address to the ACS server. [More...](class_radius_client_process.html#a3e2f668eda99f52bbf60107fe6ccc088)  
  
int | [getServerCount](class_radius_client_process.html#a834c258df05cf45aeef83d27f9a6795a) ()  
| Returns the number of ACS servers. [More...](class_radius_client_process.html#a834c258df05cf45aeef83d27f9a6795a)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[RadiusClientProcess](class_radius_client_process.html "RadiusClientProcess holds and manipulates the RADIUS client.") holds and manipulates the RADIUS client. 

## Member Function Documentation

## ◆ addToServerVect()

void RadiusClientProcess::addToServerVect  | ( | ip  | ,   
---|---|---|---  
|  | string  | ,   
|  | bool  | ,   
|  | int  | ,   
|  | string  |   
| ) | |   
  
Adds the specified client IP address to the ACS server. 

Parameters
     ipAddr,the| client IP address of interest.   
---|---  
keyStr,the| secret key.   
isSingleConnection,true| for single connection, false for multiple connection.   
authPort,the| RADIUS port.   
  
## ◆ getServerCount()

int RadiusClientProcess::getServerCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of ACS servers. 

Returns
    int, the number of ACS servers. 

## ◆ removeFromServerVect()

void RadiusClientProcess::removeFromServerVect  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Removes the specified client IP address from the ACS server. 

Parameters
     ipAddr,the| client IP address of interest.   
---|---  
  
## ◆ removeFromServerVectByName()

void RadiusClientProcess::removeFromServerVectByName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes the specified RADIUS server. 

Parameters
     serverName,the| name of the RADIUS server to remove.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CRadiusClientProcess.pki](_c_radius_client_process_8pki.html)


