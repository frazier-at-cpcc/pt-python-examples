# Cisco Packet Tracer Extensions API: LoopbackManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_loopback_manager.html

---

[LoopbackManager](class_loopback_manager.html "LoopbackManager is the process that manages loopback interfaces.") is the process that manages loopback interfaces. [More...](class_loopback_manager.html#details)

##  Public Member Functions  
  
---  
[RouterPort](class_router_port.html) | [getLoopback](class_loopback_manager.html#afad2fb731d0919988763af10de8d56b0) (int)  
| Returns the loopback interface at the specified loopback interface number. [More...](class_loopback_manager.html#afad2fb731d0919988763af10de8d56b0)  
  
[RouterPort](class_router_port.html) | [getLoopbackAt](class_loopback_manager.html#a8a8d91c005c25fe33db496d840a7a048) (int)  
| Returns the loopback interface at the specified index. [More...](class_loopback_manager.html#a8a8d91c005c25fe33db496d840a7a048)  
  
bool | [addLoopback](class_loopback_manager.html#a431c8caa993a90e43dc4966cc606d3c0) (int)  
| Adds a loopback interface with the specified loopback interface number. [More...](class_loopback_manager.html#a431c8caa993a90e43dc4966cc606d3c0)  
  
bool | [removeLoopback](class_loopback_manager.html#a8fc0b1693b7abf2a637651fc7bd814ac) (int)  
| Removes the loopback interface with the specified loopback interface number. [More...](class_loopback_manager.html#a8fc0b1693b7abf2a637651fc7bd814ac)  
  
int | [getLoopbackCount](class_loopback_manager.html#a59d14659199412034ba31b7c57335248) ()  
| Returns the number of loopback interfaces. [More...](class_loopback_manager.html#a59d14659199412034ba31b7c57335248)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[LoopbackManager](class_loopback_manager.html "LoopbackManager is the process that manages loopback interfaces.") is the process that manages loopback interfaces. 

## Member Function Documentation

## ◆ addLoopback()

bool LoopbackManager::addLoopback  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Adds a loopback interface with the specified loopback interface number. 

Parameters
     loopbackNumber,the| loopback interface number.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ getLoopback()

[RouterPort](class_router_port.html) LoopbackManager::getLoopback  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the loopback interface at the specified loopback interface number. 

Parameters
     loopbackNumber,the| loopback interface number of interest.  
---|---  
  
Returns
    [RouterPort](class_router_port.html "RouterPort handles and manipulates the router port."), the [RouterPort](class_router_port.html "RouterPort handles and manipulates the router port.") object at the specified loopback interface number. 

## ◆ getLoopbackAt()

[RouterPort](class_router_port.html) LoopbackManager::getLoopbackAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the loopback interface at the specified index. 

Parameters
     index,the| index of the loopback interface of interest.  
---|---  
  
Returns
    [RouterPort](class_router_port.html "RouterPort handles and manipulates the router port."), the [RouterPort](class_router_port.html "RouterPort handles and manipulates the router port.") object at the specified index. 

## ◆ getLoopbackCount()

int LoopbackManager::getLoopbackCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of loopback interfaces. 

Returns
    int, the number of loopback interfaces. 

## ◆ removeLoopback()

bool LoopbackManager::removeLoopback  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Removes the loopback interface with the specified loopback interface number. 

Parameters
     loopbackNumber,the| loopback interface number of interest.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

* * *

The documentation for this class was generated from the following file:

  * [CLoopbackManager.pki](_c_loopback_manager_8pki.html)


