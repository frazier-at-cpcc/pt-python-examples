# Cisco Packet Tracer Extensions API: IcmpProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_icmp_process.html

---

[IcmpProcess](class_icmp_process.html "IcmpProcess is the process that handles and manipulates ICMP.") is the process that handles and manipulates ICMP. [More...](class_icmp_process.html#details)

##  Public Member Functions  
  
---  
short | [startPing](class_icmp_process.html#a4a51fef42ffb6f1c8a64de05d4913679) (ip, int, int, int, string)  
| Starts a ping to the specified destination and returns the ping process ID. [More...](class_icmp_process.html#a4a51fef42ffb6f1c8a64de05d4913679)  
  
short | [createPingProcess](class_icmp_process.html#aaf14cb57b480cd47dc90d18a87579a11) (ip, int, int, int, string)  
| Creates a ping process and returns the ping process ID. [More...](class_icmp_process.html#aaf14cb57b480cd47dc90d18a87579a11)  
  
[PingProcess](class_ping_process.html) | [getPingProcess](class_icmp_process.html#adadde986fd49cca3f6ca4eeb0b582de4) (short)  
| Returns the [PingProcess](class_ping_process.html "PingProcess handles and manipulates ping processes.") object associated with specified ping process ID. [More...](class_icmp_process.html#adadde986fd49cca3f6ca4eeb0b582de4)  
  
short | [startTraceRoute](class_icmp_process.html#a9a68d5d57b6eba339c8cd87c25d7e223) (ip, int, int, int, int, int, string)  
| Starts a traceroute to the specified destination and returns the traceroute process ID. [More...](class_icmp_process.html#a9a68d5d57b6eba339c8cd87c25d7e223)  
  
short | [createTraceRouteProcess](class_icmp_process.html#abb3296b03352d7a309413db907547cc1) (ip, int, int, int, int, int, string)  
| Creates a trace route process and returns the traceroute process ID. [More...](class_icmp_process.html#abb3296b03352d7a309413db907547cc1)  
  
[TraceRouteProcess](class_trace_route_process.html) | [getTraceRouteProcess](class_icmp_process.html#a9796f632f372f9a7087342717509d30b) (short)  
| Returns the [TraceRouteProcess](class_trace_route_process.html "TraceRouteProcess handles and manipulates the traceroute process.") object associated with specified traceroute process ID. [More...](class_icmp_process.html#a9796f632f372f9a7087342717509d30b)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[IcmpProcess](class_icmp_process.html "IcmpProcess is the process that handles and manipulates ICMP.") is the process that handles and manipulates ICMP. 

## Member Function Documentation

## ◆ createPingProcess()

short IcmpProcess::createPingProcess  | ( | ip  | ,   
---|---|---|---  
|  | int  | ,   
|  | int  | ,   
|  | int  | ,   
|  | string  |   
| ) | |   
  
Creates a ping process and returns the ping process ID. 

Parameters
     dstIpAddress,the| destination IP address.   
---|---  
repeatTime,the| repeat time value.   
timeout,the| timeout value.   
waitTime,the| wait time value.   
portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
  
Returns
    short, the ping process ID. 

## ◆ createTraceRouteProcess()

short IcmpProcess::createTraceRouteProcess  | ( | ip  | ,   
---|---|---|---  
|  | int  | ,   
|  | int  | ,   
|  | int  | ,   
|  | int  | ,   
|  | int  | ,   
|  | string  |   
| ) | |   
  
Creates a trace route process and returns the traceroute process ID. 

Parameters
     dstIpAddress,the| destination IP address.   
---|---  
probeCount,the| number of probes to send.   
minTTL,the| minimum TTL value.   
maxTTL,the| maximum TTL value.   
timeout,the| timeout value.   
waitTime,the| wait time value.   
portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
  
Returns
    short, the traceroute process ID. 

## ◆ getPingProcess()

[PingProcess](class_ping_process.html) IcmpProcess::getPingProcess  | ( | short  | | ) |   
---|---|---|---|---|---  
  
Returns the [PingProcess](class_ping_process.html "PingProcess handles and manipulates ping processes.") object associated with specified ping process ID. 

Parameters
     id,the| ID of the ping process of interest.  
---|---  
  
Returns
    [PingProcess](class_ping_process.html "PingProcess handles and manipulates ping processes."), the [PingProcess](class_ping_process.html "PingProcess handles and manipulates ping processes.") object associated with specified ping process ID. 

## ◆ getTraceRouteProcess()

[TraceRouteProcess](class_trace_route_process.html) IcmpProcess::getTraceRouteProcess  | ( | short  | | ) |   
---|---|---|---|---|---  
  
Returns the [TraceRouteProcess](class_trace_route_process.html "TraceRouteProcess handles and manipulates the traceroute process.") object associated with specified traceroute process ID. 

Parameters
     id,the| ID of the traceroute process of interest.  
---|---  
  
Returns
    [TraceRouteProcess](class_trace_route_process.html "TraceRouteProcess handles and manipulates the traceroute process."), the [TraceRouteProcess](class_trace_route_process.html "TraceRouteProcess handles and manipulates the traceroute process.") object associated with specified traceroute process ID. 

## ◆ startPing()

short IcmpProcess::startPing  | ( | ip  | ,   
---|---|---|---  
|  | int  | ,   
|  | int  | ,   
|  | int  | ,   
|  | string  |   
| ) | |   
  
Starts a ping to the specified destination and returns the ping process ID. 

Parameters
     dstIpAddress,the| destination IP address.   
---|---  
repeatTime,the| repeat time value.   
timeout,the| timeout value.   
waitTime,the| wait time value.   
portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
  
Returns
    short, the ping process ID. 

## ◆ startTraceRoute()

short IcmpProcess::startTraceRoute  | ( | ip  | ,   
---|---|---|---  
|  | int  | ,   
|  | int  | ,   
|  | int  | ,   
|  | int  | ,   
|  | int  | ,   
|  | string  |   
| ) | |   
  
Starts a traceroute to the specified destination and returns the traceroute process ID. 

Parameters
     dstIpAddress,the| destination IP address.   
---|---  
probeCount,the| number of probes to send.   
minTTL,the| minimum TTL value.   
maxTTL,the| maximum TTL value.   
timeout,the| timeout value.   
waitTime,the| wait time value.   
portName,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
  
Returns
    short, the traceroute process ID. 

* * *

The documentation for this class was generated from the following file:

  * [CIcmpProcess.pki](_c_icmp_process_8pki.html)


