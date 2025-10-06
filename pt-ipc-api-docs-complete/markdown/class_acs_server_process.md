# Cisco Packet Tracer Extensions API: AcsServerProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_acs_server_process.html

---

[AcsServerProcess](class_acs_server_process.html "AcsServerProcess holds and manipulates the ACS server process.") holds and manipulates the ACS server process. [More...](class_acs_server_process.html#details)

##  Public Member Functions  
  
---  
bool | [addToUserMap](class_acs_server_process.html#a8aa0ef76ba36a504e0692228762b9cde) (string, string, string)  
| Adds a user record with the specified username, description, and password. [More...](class_acs_server_process.html#a8aa0ef76ba36a504e0692228762b9cde)  
  
void | [deleteFromUserMap](class_acs_server_process.html#a70f0f64acfacd5fbd0508240d44320ff) (string)  
| Removes the user record with the specified username, description, and password. [More...](class_acs_server_process.html#a70f0f64acfacd5fbd0508240d44320ff)  
  
bool | [addToClientMap](class_acs_server_process.html#a2e08bc501d775ed71c147f73156f31df) (ip, Aaa::EAcsServerType, string, string)  
| Adds a client with the specified IP address, server type, name, and password. [More...](class_acs_server_process.html#a2e08bc501d775ed71c147f73156f31df)  
  
void | [deleteFromClientMap](class_acs_server_process.html#ae96b3625c8c9a632c549f685150d6c0d) (ip, Aaa::EAcsServerType)  
| Removes the client with the specified username, description, and password. [More...](class_acs_server_process.html#ae96b3625c8c9a632c549f685150d6c0d)  
  
void | [enableACSServerService](class_acs_server_process.html#a12328b2d467c7314399823814e8a0a01) (bool)  
| Removes the client with the specified username, description, and password. [More...](class_acs_server_process.html#a12328b2d467c7314399823814e8a0a01)  
  
bool | [isEnabled](class_acs_server_process.html#a1e15faf5e1e34ea950d1ec80652c0695) ()  
| Returns true if the ACS service is enabled, otherwise false. [More...](class_acs_server_process.html#a1e15faf5e1e34ea950d1ec80652c0695)  
  
vector< string > | [getUserRecordsAsString](class_acs_server_process.html#ae8e197b9b0b92565e7401a4de60487fb) ()  
| Returns a vector of all user records in string format: key:username,password,description. [More...](class_acs_server_process.html#ae8e197b9b0b92565e7401a4de60487fb)  
  
vector< string > | [getClientRecordsAsString](class_acs_server_process.html#a1cbe1f7b0e10018b46d9ccf4da2bb628) ()  
| Returns a vector of all client records in string format: key:username,password,description. [More...](class_acs_server_process.html#a1cbe1f7b0e10018b46d9ccf4da2bb628)  
  
void | [removeAllUserRecords](class_acs_server_process.html#a62afefec66ecadd9297026a160e90f3d) ()  
void | [removeAllClientRecords](class_acs_server_process.html#a423bdbcac2376e74a9e1d15af6e79607) ()  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[AcsServerProcess](class_acs_server_process.html "AcsServerProcess holds and manipulates the ACS server process.") holds and manipulates the ACS server process. 

## Member Function Documentation

## ◆ addToClientMap()

bool AcsServerProcess::addToClientMap  | ( | ip  | ,   
---|---|---|---  
|  | Aaa::EAcsServerType  | ,   
|  | string  | ,   
|  | string  |   
| ) | |   
  
Adds a client with the specified IP address, server type, name, and password. 

Parameters
     hostIp,the| IP address of the client.   
---|---  
serverType,the| type of server. [Server](class_server.html "Server is Server device object with a terminal line.") types: eTacacsServer = 0, eRadiusServer = 1   
name,the| name of the client.   
keyStr,the| secret key for the client.  
  
Returns
    bool, true if client added successfully, otherwise false. 

## ◆ addToUserMap()

bool AcsServerProcess::addToUserMap  | ( | string  | ,   
---|---|---|---  
|  | string  | ,   
|  | string  |   
| ) | |   
  
Adds a user record with the specified username, description, and password. 

Parameters
     userName,the| username of the user record to add.   
---|---  
description,the| description of the user record to add.   
password,the| password of the user record to add.  
  
Returns
    bool, true if user record added successfully, otherwise false. 

## ◆ deleteFromClientMap()

void AcsServerProcess::deleteFromClientMap  | ( | ip  | ,   
---|---|---|---  
|  | Aaa::EAcsServerType  |   
| ) | |   
  
Removes the client with the specified username, description, and password. 

Parameters
     hostIp,the| IP address of the client.   
---|---  
serverType,the| type of server. [Server](class_server.html "Server is Server device object with a terminal line.") types: eTacacsServer = 0, eRadiusServer = 1   
name,the| name of the client.   
keyStr,the| secret key for the client.  
  
Returns
    bool, true if client removed successfully, otherwise false. 

## ◆ deleteFromUserMap()

void AcsServerProcess::deleteFromUserMap  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes the user record with the specified username, description, and password. 

Parameters
     userName,the| username of the user record to remove.   
---|---  
  
## ◆ enableACSServerService()

void AcsServerProcess::enableACSServerService  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Removes the client with the specified username, description, and password. 

Parameters
     status,true| enables the ACS service, false disables it.   
---|---  
  
## ◆ getClientRecordsAsString()

vector< string > AcsServerProcess::getClientRecordsAsString  | ( | | ) |   
---|---|---|---|---  
  
Returns a vector of all client records in string format: key:username,password,description. 

Returns
    Returns a vector of all user records in string format: key:description,server_type_as_integer,hostip,keystring [Server](class_server.html "Server is Server device object with a terminal line.") type = eTacacsServer=0, [Server](class_server.html "Server is Server device object with a terminal line.") type = eRadiusServer=1 

## ◆ getUserRecordsAsString()

vector< string > AcsServerProcess::getUserRecordsAsString  | ( | | ) |   
---|---|---|---|---  
  
Returns a vector of all user records in string format: key:username,password,description. 

Returns
    Returns a vector of all user records in string format: key:username,password,description 

## ◆ isEnabled()

bool AcsServerProcess::isEnabled  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the ACS service is enabled, otherwise false. 

Returns
    bool, true if the ACS service is enabled, otherwise false. 

## ◆ removeAllClientRecords()

void AcsServerProcess::removeAllClientRecords  | ( | | ) |   
---|---|---|---|---  
  
## ◆ removeAllUserRecords()

void AcsServerProcess::removeAllUserRecords  | ( | | ) |   
---|---|---|---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CAcsServerProcess.pki](_c_acs_server_process_8pki.html)


