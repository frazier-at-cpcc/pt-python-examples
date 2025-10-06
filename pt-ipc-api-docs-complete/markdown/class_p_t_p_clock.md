# Cisco Packet Tracer Extensions API: PTPClock Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_p_t_p_clock.html

---

This file holds CPTPClock class declaration. [More...](class_p_t_p_clock.html#details)

##  Public Member Functions  
  
---  
void | [setMode](class_p_t_p_clock.html#a37e50d6fc2f56d53cdec8e3253e146f3) (PTPMode)  
| Sets the mode. [More...](class_p_t_p_clock.html#a37e50d6fc2f56d53cdec8e3253e146f3)  
  
PTPMode | [getMode](class_p_t_p_clock.html#a04b9bd8ffef1e8073f6f200852db3f67) ()  
| Returns the mode. [More...](class_p_t_p_clock.html#a04b9bd8ffef1e8073f6f200852db3f67)  
  
string | [getModeStr](class_p_t_p_clock.html#a88518c67e7f9559b796543e770921d3d) ()  
| Returns the mode as a string. [More...](class_p_t_p_clock.html#a88518c67e7f9559b796543e770921d3d)  
  
int | [getNumOfPorts](class_p_t_p_clock.html#a17fb3f271b7c8328530e9e572f795a60) ()  
| Returns the number of ports. [More...](class_p_t_p_clock.html#a17fb3f271b7c8328530e9e572f795a60)  
  
void | [setProfile](class_p_t_p_clock.html#a873bce67ec98f51a9a509423c827e452) (PTPProfile)  
| Sets the profile type. [More...](class_p_t_p_clock.html#a873bce67ec98f51a9a509423c827e452)  
  
PTPProfile | [getProfile](class_p_t_p_clock.html#ac12c7dca395faab870c62a2a0d59bd8e) ()  
| Gets the profile type. [More...](class_p_t_p_clock.html#ac12c7dca395faab870c62a2a0d59bd8e)  
  
string | [getProfileStr](class_p_t_p_clock.html#ae12412ec88f92b99c8eef529ef5664f9) ()  
| Returns the profile as a string. [More...](class_p_t_p_clock.html#ae12412ec88f92b99c8eef529ef5664f9)  
  
void | [setDelayMechanism](class_p_t_p_clock.html#a9a6d4e92736f2188d1e2cb4f0262e92d) (DelayMechanism)  
| Sets the delay mechanism type. [More...](class_p_t_p_clock.html#a9a6d4e92736f2188d1e2cb4f0262e92d)  
  
int | [getDelayMechanism](class_p_t_p_clock.html#a4aaf32df5a5447cdf47a373a13dd9187) ()  
| Gets the profile type. [More...](class_p_t_p_clock.html#a4aaf32df5a5447cdf47a373a13dd9187)  
  
string | [getDelayMechanismStr](class_p_t_p_clock.html#ac4a25950b40db871b576fecd3e9b3142) ()  
| Returns the delay mechanisim as a string. [More...](class_p_t_p_clock.html#ac4a25950b40db871b576fecd3e9b3142)  
  
void | [setPriority1](class_p_t_p_clock.html#a10084fe0101ed22b01ea60b6d8e79892) (int)  
| Sets priority 1 to the given value. [More...](class_p_t_p_clock.html#a10084fe0101ed22b01ea60b6d8e79892)  
  
void | [setPriority2](class_p_t_p_clock.html#a0819135d1b97073a4a3044fa91776de0) (int)  
| Sets priority 2 to the given value. [More...](class_p_t_p_clock.html#a0819135d1b97073a4a3044fa91776de0)  
  
void | [setPtpTime](class_p_t_p_clock.html#a0afc64a4cc0acc06cbbe77156600e061) (string)  
| Sets ptp time to the given value. [More...](class_p_t_p_clock.html#a0afc64a4cc0acc06cbbe77156600e061)  
  
void | [clearConfig](class_p_t_p_clock.html#a0cc494668b3a2b3ebf19a137dc1e1f73) ()  
| Clears the config. [More...](class_p_t_p_clock.html#a0cc494668b3a2b3ebf19a137dc1e1f73)  
  
void | [init](class_p_t_p_clock.html#a5f6e28f5a204c6a08664a16905b782e7) ()  
| Runs the init setup. [More...](class_p_t_p_clock.html#a5f6e28f5a204c6a08664a16905b782e7)  
  
  
## Detailed Description

This file holds CPTPClock class declaration. 

## Member Function Documentation

## ◆ clearConfig()

void PTPClock::clearConfig  | ( | | ) |   
---|---|---|---|---  
  
Clears the config. 

## ◆ getDelayMechanism()

int PTPClock::getDelayMechanism  | ( | | ) |   
---|---|---|---|---  
  
Gets the profile type. 

Returns
    int, the profile type. Timer types: eDefault = 0, ePower = 1 

## ◆ getDelayMechanismStr()

string PTPClock::getDelayMechanismStr  | ( | | ) |   
---|---|---|---|---  
  
Returns the delay mechanisim as a string. 

Returns
    string, profile strings: "End to End", "Peer to Peer" 

## ◆ getMode()

PTPMode PTPClock::getMode  | ( | | ) |   
---|---|---|---|---  
  
Returns the mode. 

Returns
    enum<PTPMode>, the modes. Mode types: eE2etransparent = 0, eBoundary = 1, eForward = 2 

## ◆ getModeStr()

string PTPClock::getModeStr  | ( | | ) |   
---|---|---|---|---  
  
Returns the mode as a string. 

Returns
    string, Mode strings: "e2etransparent", "boundary", "forward" 

## ◆ getNumOfPorts()

int PTPClock::getNumOfPorts  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of ports. 

Returns
    int, the number of ports. 

## ◆ getProfile()

PTPProfile PTPClock::getProfile  | ( | | ) |   
---|---|---|---|---  
  
Gets the profile type. 

Returns
    enum<PTPProfile>, the profile type. Timer types: eDefault = 0, ePower = 1 

## ◆ getProfileStr()

string PTPClock::getProfileStr  | ( | | ) |   
---|---|---|---|---  
  
Returns the profile as a string. 

Returns
    string, profile strings: "Default", "Power" 

## ◆ init()

void PTPClock::init  | ( | | ) |   
---|---|---|---|---  
  
Runs the init setup. 

## ◆ setDelayMechanism()

void PTPClock::setDelayMechanism  | ( | DelayMechanism  | | ) |   
---|---|---|---|---|---  
  
Sets the delay mechanism type. 

Parameters
     delay,the| type of delay. Timer types: eEnd2End = 0, ePeer2Peer = 1   
---|---  
  
## ◆ setMode()

void PTPClock::setMode  | ( | PTPMode  | | ) |   
---|---|---|---|---|---  
  
Sets the mode. 

Parameters
     mode,the| type of timer. Timer types: eE2etransparent = 0, eBoundary = 1, eForward = 2   
---|---  
  
## ◆ setPriority1()

void PTPClock::setPriority1  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets priority 1 to the given value. 

Parameters
     val,value| to use.   
---|---  
  
## ◆ setPriority2()

void PTPClock::setPriority2  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets priority 2 to the given value. 

Parameters
     val,value| to use.   
---|---  
  
## ◆ setProfile()

void PTPClock::setProfile  | ( | PTPProfile  | | ) |   
---|---|---|---|---|---  
  
Sets the profile type. 

Parameters
     profile,the| type of timer. Timer types: eDefault = 0, ePower = 1   
---|---  
  
## ◆ setPtpTime()

void PTPClock::setPtpTime  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets ptp time to the given value. 

Parameters
     time,time| to use.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CPTPClock.pki](_c_p_t_p_clock_8pki.html)


