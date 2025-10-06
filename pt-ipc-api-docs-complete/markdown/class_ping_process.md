# Cisco Packet Tracer Extensions API: PingProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_ping_process.html

---

[PingProcess](class_ping_process.html "PingProcess handles and manipulates ping processes.") handles and manipulates ping processes. [More...](class_ping_process.html#details)

##  Public Member Functions  
  
---  
void | [start](class_ping_process.html#a4aceb535ee46218f2f8f0c7cbe7206f0) ()  
| Starts the ping process. [More...](class_ping_process.html#a4aceb535ee46218f2f8f0c7cbe7206f0)  
  
void | [cancel](class_ping_process.html#a9243eebaf5c355ece27f4d658bfb7966) ()  
| Cancels the ping process. [More...](class_ping_process.html#a9243eebaf5c355ece27f4d658bfb7966)  
  
short | [getId](class_ping_process.html#addac0c0e3bb80b33a881050013cdc6fd) ()  
| Returns the ping process ID. [More...](class_ping_process.html#addac0c0e3bb80b33a881050013cdc6fd)  
  
ip | [getDestinationIP](class_ping_process.html#a104e1e7df5be0dab9be48edf8723ce42) ()  
| Returns the destination IP address. [More...](class_ping_process.html#a104e1e7df5be0dab9be48edf8723ce42)  
  
ip | [getSourceIP](class_ping_process.html#a345f83b12fc98cde39bd1f09b29291ab) ()  
| Returns the source IP address. [More...](class_ping_process.html#a345f83b12fc98cde39bd1f09b29291ab)  
  
ip | [getLastIP](class_ping_process.html#a803f4e85635124a6ee4e110ea37e5265) ()  
| Returns the last IP address in the ping process. [More...](class_ping_process.html#a803f4e85635124a6ee4e110ea37e5265)  
  
bool | [isBroadcast](class_ping_process.html#a42d825924719e3fdcf001658f586adbc) ()  
| Returns true if the ping process is broadcasted, otherwise false. [More...](class_ping_process.html#a42d825924719e3fdcf001658f586adbc)  
  
int | [getTotalCount](class_ping_process.html#ac4969d15086a98f3e45de4c22fd99c04) ()  
| Returns the total number of pings. [More...](class_ping_process.html#ac4969d15086a98f3e45de4c22fd99c04)  
  
int | [getSentCount](class_ping_process.html#aa9a9d17ae4a6b8b07422d2c6b58c03eb) ()  
| Returns the number of echo requests sent. [More...](class_ping_process.html#aa9a9d17ae4a6b8b07422d2c6b58c03eb)  
  
int | [getReceivedCount](class_ping_process.html#a632b0b5036498f3a2d33e68110ec50f5) ()  
| Returns the number of echo replies received. [More...](class_ping_process.html#a632b0b5036498f3a2d33e68110ec50f5)  
  
int | [getTimeout](class_ping_process.html#a5ffd5472af5406e516cb3262555a3ed9) ()  
| Returns the timeout value. [More...](class_ping_process.html#a5ffd5472af5406e516cb3262555a3ed9)  
  
int | [getMinDelay](class_ping_process.html#a9c6c19865ab3c4c49a73185f7f3f4da8) ()  
| Returns the minimum delay value. [More...](class_ping_process.html#a9c6c19865ab3c4c49a73185f7f3f4da8)  
  
int | [getMaxDelay](class_ping_process.html#ac82a518ed052676a14fa133ca2c3f635) ()  
| Returns the maximum delay value. [More...](class_ping_process.html#ac82a518ed052676a14fa133ca2c3f635)  
  
int | [getLastDelay](class_ping_process.html#aa869d37e490e0865ae7d6640e8a10d35) ()  
| Returns the last delay value. [More...](class_ping_process.html#aa869d37e490e0865ae7d6640e8a10d35)  
  
int | [getTotalDelay](class_ping_process.html#ae9acfc8718121841c28e2d34d3459d89) ()  
| Returns the total delay value. [More...](class_ping_process.html#ae9acfc8718121841c28e2d34d3459d89)  
  
int | [getLastTtl](class_ping_process.html#a79170240c5e09dd78646b80884177294) ()  
| Returns the last TTL value. [More...](class_ping_process.html#a79170240c5e09dd78646b80884177294)  
  
void | [donePing](class_ping_process.html#abd2428d7418d66217ae328583dc70ca0) (int, int)  
| This event is emitted when the ping is done. [More...](class_ping_process.html#abd2428d7418d66217ae328583dc70ca0)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[PingProcess](class_ping_process.html "PingProcess handles and manipulates ping processes.") handles and manipulates ping processes. 

## Member Function Documentation

## ◆ cancel()

void PingProcess::cancel  | ( | | ) |   
---|---|---|---|---  
  
Cancels the ping process. 

## ◆ donePing()

void PingProcess::donePing  | ( | int  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
This event is emitted when the ping is done. 

  * receiveCount, the number of echo replies received. 
  * totalDelay, the total delay value.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ getDestinationIP()

ip PingProcess::getDestinationIP  | ( | | ) |   
---|---|---|---|---  
  
Returns the destination IP address. 

Returns
    ip, the destination IP address. 

## ◆ getId()

short PingProcess::getId  | ( | | ) |   
---|---|---|---|---  
  
Returns the ping process ID. 

Returns
    short, the ping process ID. 

## ◆ getLastDelay()

int PingProcess::getLastDelay  | ( | | ) |   
---|---|---|---|---  
  
Returns the last delay value. 

Returns
    int, the last delay value. 

## ◆ getLastIP()

ip PingProcess::getLastIP  | ( | | ) |   
---|---|---|---|---  
  
Returns the last IP address in the ping process. 

Returns
    ip, the last IP address in the ping process. 

## ◆ getLastTtl()

int PingProcess::getLastTtl  | ( | | ) |   
---|---|---|---|---  
  
Returns the last TTL value. 

Returns
    int, the last TTL value. 

## ◆ getMaxDelay()

int PingProcess::getMaxDelay  | ( | | ) |   
---|---|---|---|---  
  
Returns the maximum delay value. 

Returns
    int, the maximum delay value. 

## ◆ getMinDelay()

int PingProcess::getMinDelay  | ( | | ) |   
---|---|---|---|---  
  
Returns the minimum delay value. 

Returns
    int, the minimum delay value. 

## ◆ getReceivedCount()

int PingProcess::getReceivedCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of echo replies received. 

Returns
    int, the number of echo replies received. 

## ◆ getSentCount()

int PingProcess::getSentCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of echo requests sent. 

Returns
    int, the number of echo requests sent. 

## ◆ getSourceIP()

ip PingProcess::getSourceIP  | ( | | ) |   
---|---|---|---|---  
  
Returns the source IP address. 

Returns
    ip, the source IP address. 

## ◆ getTimeout()

int PingProcess::getTimeout  | ( | | ) |   
---|---|---|---|---  
  
Returns the timeout value. 

Returns
    int, the timeout value. 

## ◆ getTotalCount()

int PingProcess::getTotalCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the total number of pings. 

Returns
    int, the total number of pings. 

## ◆ getTotalDelay()

int PingProcess::getTotalDelay  | ( | | ) |   
---|---|---|---|---  
  
Returns the total delay value. 

Returns
    int, the total delay value. 

## ◆ isBroadcast()

bool PingProcess::isBroadcast  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the ping process is broadcasted, otherwise false. 

Returns
    bool, true if the ping process is broadcasted, otherwise false. 

## ◆ start()

void PingProcess::start  | ( | | ) |   
---|---|---|---|---  
  
Starts the ping process. 

* * *

The documentation for this class was generated from the following file:

  * [CPingProcess.pki](_c_ping_process_8pki.html)


