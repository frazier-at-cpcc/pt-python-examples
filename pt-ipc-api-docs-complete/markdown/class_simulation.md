# Cisco Packet Tracer Extensions API: Simulation Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_simulation.html

---

[Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") holds the traffic details like PDUs, ports, etc. [More...](class_simulation.html#details)

##  Public Member Functions  
  
---  
int | [getFrameInstanceCount](class_simulation.html#a07f2a9f2924fd55f1483ef8145e72ca9) ()  
| Returns the number of FrameInstances at present in the simulation. [More...](class_simulation.html#a07f2a9f2924fd55f1483ef8145e72ca9)  
  
[FrameInstance](class_frame_instance.html) | [getFrameInstanceAt](class_simulation.html#a63c096d2687388237c7eda45760bbc12) (int)  
| Returns the [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") at the specified index in the simulation event list. [More...](class_simulation.html#a63c096d2687388237c7eda45760bbc12)  
  
int | [getCurrentFrameInstanceIndex](class_simulation.html#af687565b89dc8c4938593bb5e7942344) ()  
| Returns index of "current" frame instance. [More...](class_simulation.html#af687565b89dc8c4938593bb5e7942344)  
  
void | [resetSimulation](class_simulation.html#a7d5a3b634f8670de6b15f2042e3ae6ce) ()  
| Resets simulation and fires the event. [More...](class_simulation.html#a7d5a3b634f8670de6b15f2042e3ae6ce)  
  
void | [forwardStarted](class_simulation.html#ac9138f5c2717feaa6a6856d9302eb114) ()  
| This event is emitted when simulation playback is started. [More...](class_simulation.html#ac9138f5c2717feaa6a6856d9302eb114)  
  
void | [forwardEnded](class_simulation.html#aa3f1f71ac3375c153e7ec68a724fc1e9) ()  
| This event is emitted when simulation playback is stopped. [More...](class_simulation.html#aa3f1f71ac3375c153e7ec68a724fc1e9)  
  
void | [newFrameInstanceAdded](class_simulation.html#ad74d67fd86baada7f804e54d7270c2d7) (TrafficType, int)  
| This event is emitted when a new frame instance is added. [More...](class_simulation.html#ad74d67fd86baada7f804e54d7270c2d7)  
  
void | [simulationReset](class_simulation.html#a35edf1bdc80dc9604cb9b1174761ba18) ()  
| This event is emitted when the simulation is reset. [More...](class_simulation.html#a35edf1bdc80dc9604cb9b1174761ba18)  
  
void | [simulationBufferFull](class_simulation.html#a7e4d7b92564a28812ff0269c142f6655) ()  
| [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. [More...](class_simulation.html#a7e4d7b92564a28812ff0269c142f6655)  
  
void | [simulationModeChanged](class_simulation.html#a2d5eccf24b50f23597cff961e72a08d4) ()  
| This event is emitted when the Realtime or [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") Mode is changed. [More...](class_simulation.html#a2d5eccf24b50f23597cff961e72a08d4)  
  
bool | [isSimulationMode](class_simulation.html#a693e21cfafe98ef10598eca6e1db08eb) ()  
| Returns true if in [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") Mode, otherwise false. [More...](class_simulation.html#a693e21cfafe98ef10598eca6e1db08eb)  
  
[FrameInstance](class_frame_instance.html) | [createFrameInstance](class_simulation.html#a82ddba7d0b2143a5d281f6680fef3ddf) ([Device](class_device.html), TrafficType, int, QString)  
| Create [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") to be sent from a device. [More...](class_simulation.html#a82ddba7d0b2143a5d281f6680fef3ddf)  
  
[FrameInstance](class_frame_instance.html) | [createFrameInstanceCustomType](class_simulation.html#a7cf69523e1dfdeea71990af766298765) ([Device](class_device.html), QString, int, QString)  
| Create [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") to be sent from a device with a custom traffic type. [More...](class_simulation.html#a7cf69523e1dfdeea71990af766298765)  
  
void | [finalizeFrameInstance](class_simulation.html#aa28dafd32a54849a08fe003f7ca8aea4) ([FrameInstance](class_frame_instance.html))  
| Finalize frame instance. [More...](class_simulation.html#aa28dafd32a54849a08fe003f7ca8aea4)  
  
[SimulationTimer](class_simulation_timer.html) | [createTimer](class_simulation.html#aa0e2948f81cbcf68f1b5f2e97a942eae) (int, bool)  
| Create [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") Timer. [More...](class_simulation.html#aa0e2948f81cbcf68f1b5f2e97a942eae)  
  
uuid | [createTimerUuid](class_simulation.html#a4bff1a18e9289078e89c4491916133f9) (int, bool)  
| Create [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") Timer and return the uuid of the timer object. [More...](class_simulation.html#a4bff1a18e9289078e89c4491916133f9)  
  
[SimulationTimer](class_simulation_timer.html) | [getIpcTimer](class_simulation.html#a6c194350a73fa18043cae0f5ffc59f35) (uuid)  
| Get [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") Timer based on uuid. [More...](class_simulation.html#a6c194350a73fa18043cae0f5ffc59f35)  
  
long | [getCurrentSimTime](class_simulation.html#ac6bf075003e1e619c9eaf67b62377509) ()  
| Get Current [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") Time. [More...](class_simulation.html#ac6bf075003e1e619c9eaf67b62377509)  
  
void | [setSimulationMode](class_simulation.html#ab49893e0816adf7b738eb7b10df5fbc8) (bool)  
| Sets the mode to simulation mode. [More...](class_simulation.html#ab49893e0816adf7b738eb7b10df5fbc8)  
  
void | [forward](class_simulation.html#ab8e2313fdab2150b47d2559ef1f26135) ()  
| Forwards the simulation by 1 step. [More...](class_simulation.html#ab8e2313fdab2150b47d2559ef1f26135)  
  
void | [backward](class_simulation.html#a89553e4676dbfbe6982e702ba13f5bd7) ()  
| Backs the simulation by 1 step. [More...](class_simulation.html#a89553e4676dbfbe6982e702ba13f5bd7)  
  
  
## Detailed Description

[Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") holds the traffic details like PDUs, ports, etc. 

## Member Function Documentation

## ◆ backward()

void Simulation::backward  | ( | | ) |   
---|---|---|---|---  
  
Backs the simulation by 1 step. 

## ◆ createFrameInstance()

[FrameInstance](class_frame_instance.html) Simulation::createFrameInstance  | ( | [Device](class_device.html) | ,   
---|---|---|---  
|  | TrafficType  | ,   
|  | int  | ,   
|  | QString  |   
| ) | |   
  
Create [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") to be sent from a device. 

Parameters
     ownerDevice,the| device for which the frame instance is created  
---|---  
trafficType,the| type of traffic for the frame instance, see documentation for newFrameInstanceAdded event  
color,rbg| color code for the frame  
dstStr,destination| ip address in string format  
  
Returns
    [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc."), [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") object 

## ◆ createFrameInstanceCustomType()

[FrameInstance](class_frame_instance.html) Simulation::createFrameInstanceCustomType  | ( | [Device](class_device.html) | ,   
---|---|---|---  
|  | QString  | ,   
|  | int  | ,   
|  | QString  |   
| ) | |   
  
Create [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") to be sent from a device with a custom traffic type. 

Parameters
     ownerDevice,the| device for which the frame instance is created  
---|---  
customTrafficType,the| type of traffic for the frame instance, see documentation for newFrameInstanceAdded event  
color,rbg| color code for the frame  
dstStr,destination| ip address in string format  
  
Returns
    [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc."), [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") object 

## ◆ createTimer()

[SimulationTimer](class_simulation_timer.html) Simulation::createTimer  | ( | int  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Create [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") Timer. 

Parameters
     delay,delay| time before timer expires  
---|---  
bAddRandom,true| to set the timer to expire at random time and false to not including the random factor  
  
Returns
    [SimulationTimer](class_simulation_timer.html "A simulation timer that expires in simulation time."), [SimulationTimer](class_simulation_timer.html "A simulation timer that expires in simulation time.") object 

## ◆ createTimerUuid()

uuid Simulation::createTimerUuid  | ( | int  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Create [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") Timer and return the uuid of the timer object. 

Parameters
     delay,delay| time before timer expires  
---|---  
bAddRandom,true| to set the timer to expire at random time and false to not including the random factor  
  
Returns
    uuid, [SimulationTimer](class_simulation_timer.html "A simulation timer that expires in simulation time.") object's uuid 

## ◆ finalizeFrameInstance()

void Simulation::finalizeFrameInstance  | ( | [FrameInstance](class_frame_instance.html) | | ) |   
---|---|---|---|---|---  
  
Finalize frame instance. 

Parameters
     frameInstance,[FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.")| object   
---|---  
  
## ◆ forward()

void Simulation::forward  | ( | | ) |   
---|---|---|---|---  
  
Forwards the simulation by 1 step. 

## ◆ forwardEnded()

void Simulation::forwardEnded  | ( | | ) |   
---|---|---|---|---  
  
This event is emitted when simulation playback is stopped. 

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ forwardStarted()

void Simulation::forwardStarted  | ( | | ) |   
---|---|---|---|---  
  
This event is emitted when simulation playback is started. 

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ getCurrentFrameInstanceIndex()

int Simulation::getCurrentFrameInstanceIndex  | ( | | ) |   
---|---|---|---|---  
  
Returns index of "current" frame instance. 

## ◆ getCurrentSimTime()

long Simulation::getCurrentSimTime  | ( | | ) |   
---|---|---|---|---  
  
Get Current [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") Time. 

Returns
    long, Current [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") Time 

## ◆ getFrameInstanceAt()

[FrameInstance](class_frame_instance.html) Simulation::getFrameInstanceAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") at the specified index in the simulation event list. 

Parameters
     nodeIndex,the| index of [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") of interest.  
---|---  
  
Returns
    [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc."), the [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") object at the specified index in the simulation event list. 

## ◆ getFrameInstanceCount()

int Simulation::getFrameInstanceCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of FrameInstances at present in the simulation. 

Returns
    int, the number of FrameInstances at present in the simulation. 

## ◆ getIpcTimer()

[SimulationTimer](class_simulation_timer.html) Simulation::getIpcTimer  | ( | uuid  | | ) |   
---|---|---|---|---|---  
  
Get [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") Timer based on uuid. 

Parameters
     uuid,uuid| of the timer  
---|---  
  
Returns
    [SimulationTimer](class_simulation_timer.html "A simulation timer that expires in simulation time."), [SimulationTimer](class_simulation_timer.html "A simulation timer that expires in simulation time.") object 

## ◆ isSimulationMode()

bool Simulation::isSimulationMode  | ( | | ) |   
---|---|---|---|---  
  
Returns true if in [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") Mode, otherwise false. 

Returns
    bool, true if in [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") Mode, otherwise false. 

## ◆ newFrameInstanceAdded()

void Simulation::newFrameInstanceAdded  | ( | TrafficType  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
This event is emitted when a new frame instance is added. 

  * trafficType, the user traffic type. User traffic types: eTrafficType_Icmp = 0, eTrafficType_Tcp = 1, eTrafficType_Udp = 2, eTrafficType_RipV1 = 3, eTrafficType_RipV2 = 4, eTrafficType_Arp = 5, eTrafficType_Cdp = 6, eTrafficType_Dhcp = 7, eTrafficType_Nat = 8, eTrafficType_Eigrp = 9, eTrafficType_Vtp = 10, eTrafficType_Stp = 11, eTrafficType_Ospf = 12, eTrafficType_Dtp = 13, eTrafficType_Telnet = 14, eTrafficType_Ssh = 15, eTrafficType_Tftp = 16, eTrafficType_Http = 17, eTrafficType_Https = 18, eTrafficType_Dns = 19, eTrafficType_Icmpv6 = 20, eTrafficType_Lacp = 21, eTrafficType_Pagp = 22, eTrafficType_Ipsec = 23, eTrafficType_Ike = 24, eTrafficType_Syslog = 25, eTrafficType_Tacacs = 26, eTrafficType_Radius = 27, eTrafficType_Snmp = 28, eTrafficType_Ntp = 29, eTrafficType_Ftp = 30, eTrafficType_Smtp = 31, eTrafficType_Pop3 = 32, eTrafficType_Sccp = 33, eTrafficType_Rtp = 34, eTrafficType_H323 = 35, eTrafficType_Bgp = 36, eTrafficType_Hsrp = 37, eTrafficType_Hsrpv6 = 38, eTrafficType_Netflow = 39, eTrafficType_Ndv6 = 40, eTrafficType_Ripng = 41, eTrafficType_Dhcpv6 = 42, eTrafficType_Eigrpv6 = 43, eTrafficType_Ospfv6 = 44, eTrafficType_IoE = 45, eTrafficType_Ptp = 46, eTrafficType_Rep = 47, eTrafficType_CapwapUdp = 48, eTrafficType_Lldp = 49, eTrafficType_Span = 50, eTrafficType_IoETcp = 51, eTrafficType_Usb = 52, eTrafficType_Bluetooth = 53, eTrafficType_Custom = 1000 
  * index, the index of the frame instance.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ resetSimulation()

void Simulation::resetSimulation  | ( | | ) |   
---|---|---|---|---  
  
Resets simulation and fires the event. 

## ◆ setSimulationMode()

void Simulation::setSimulationMode  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Sets the mode to simulation mode. 

  * toSimMode, whether to change to simulation mode or not (realtime). 



## ◆ simulationBufferFull()

void Simulation::simulationBufferFull  | ( | | ) |   
---|---|---|---|---  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ simulationModeChanged()

void Simulation::simulationModeChanged  | ( | | ) |   
---|---|---|---|---  
  
This event is emitted when the Realtime or [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") Mode is changed. 

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ simulationReset()

void Simulation::simulationReset  | ( | | ) |   
---|---|---|---|---  
  
This event is emitted when the simulation is reset. 

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

* * *

The documentation for this class was generated from the following file:

  * [CSimulation.pki](_c_simulation_8pki.html)


