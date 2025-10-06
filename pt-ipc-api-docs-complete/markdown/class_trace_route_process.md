# Cisco Packet Tracer Extensions API: TraceRouteProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_trace_route_process.html

---

[TraceRouteProcess](class_trace_route_process.html "TraceRouteProcess handles and manipulates the traceroute process.") handles and manipulates the traceroute process. [More...](class_trace_route_process.html#details)

##  Public Member Functions  
  
---  
void | [start](class_trace_route_process.html#a1d39a32b6a988ee5b92e4f8b2602eb56) ()  
| Starts the traceroute process. [More...](class_trace_route_process.html#a1d39a32b6a988ee5b92e4f8b2602eb56)  
  
void | [cancel](class_trace_route_process.html#af33d07c54bb0c9bf1cb10ef85851b051) ()  
| Cancels the traceroute process. [More...](class_trace_route_process.html#af33d07c54bb0c9bf1cb10ef85851b051)  
  
short | [getId](class_trace_route_process.html#a0bb3da4759a9f625a0bc1426ec176935) ()  
| Returns the traceroute process ID. [More...](class_trace_route_process.html#a0bb3da4759a9f625a0bc1426ec176935)  
  
ip | [getLastIP](class_trace_route_process.html#a7e9e2d41e5a3ec5d010a88c4630b5e7f) ()  
| Returns the last IP address. [More...](class_trace_route_process.html#a7e9e2d41e5a3ec5d010a88c4630b5e7f)  
  
int | [getSentCount](class_trace_route_process.html#a5b2498974f0bfa3f6e51db9f88e8ae1b) ()  
| Returns the number of packets sent. [More...](class_trace_route_process.html#a5b2498974f0bfa3f6e51db9f88e8ae1b)  
  
int | [getTimeout](class_trace_route_process.html#ae0c7452d99f7bf0916a227514913814e) ()  
| Returns the timeout value. [More...](class_trace_route_process.html#ae0c7452d99f7bf0916a227514913814e)  
  
int | [getLastDelay](class_trace_route_process.html#a1bd0a6526a83a4e7278c2f0c3e64ca28) ()  
| Returns the last delay value. [More...](class_trace_route_process.html#a1bd0a6526a83a4e7278c2f0c3e64ca28)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[TraceRouteProcess](class_trace_route_process.html "TraceRouteProcess handles and manipulates the traceroute process.") handles and manipulates the traceroute process. 

## Member Function Documentation

## ◆ cancel()

void TraceRouteProcess::cancel  | ( | | ) |   
---|---|---|---|---  
  
Cancels the traceroute process. 

## ◆ getId()

short TraceRouteProcess::getId  | ( | | ) |   
---|---|---|---|---  
  
Returns the traceroute process ID. 

Returns
    short, the traceroute process ID. 

## ◆ getLastDelay()

int TraceRouteProcess::getLastDelay  | ( | | ) |   
---|---|---|---|---  
  
Returns the last delay value. 

Returns
    int, the last delay value. 

## ◆ getLastIP()

ip TraceRouteProcess::getLastIP  | ( | | ) |   
---|---|---|---|---  
  
Returns the last IP address. 

Returns
    ip, the last IP address. 

## ◆ getSentCount()

int TraceRouteProcess::getSentCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of packets sent. 

Returns
    int, the number of packets sent. 

## ◆ getTimeout()

int TraceRouteProcess::getTimeout  | ( | | ) |   
---|---|---|---|---  
  
Returns the timeout value. 

Returns
    int, the timeout value. 

## ◆ start()

void TraceRouteProcess::start  | ( | | ) |   
---|---|---|---|---  
  
Starts the traceroute process. 

* * *

The documentation for this class was generated from the following file:

  * [CTraceRouteProcess.pki](_c_trace_route_process_8pki.html)


