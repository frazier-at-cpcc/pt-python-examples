# Cisco Packet Tracer Extensions API: CCMEProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_c_c_m_e_process.html

---

[CCMEProcess](class_c_c_m_e_process.html "CCMEProcess is the process that handles CME.") is the process that handles CME. [More...](class_c_c_m_e_process.html#details)

##  Public Member Functions  
  
---  
[CEphoneDirectory](class_c_ephone_directory.html) | [getEphoneDirectory](class_c_c_m_e_process.html#aff185c200f9bd8d19642b394654022fb) (int)  
| Returns the [CEphoneDirectory](class_c_ephone_directory.html "CEphoneDirectory holds and manipulates the ephone directory.") object with the specified sequence number. [More...](class_c_c_m_e_process.html#aff185c200f9bd8d19642b394654022fb)  
  
[CEphone](class_c_ephone.html) | [getEphone](class_c_c_m_e_process.html#aa395434c6678fd88e0da9b593f92d8fc) (int)  
| Returns the [CEphone](class_c_ephone.html "CEphone holds and manipulates VOIP ephones.") object with the specified sequence number. [More...](class_c_c_m_e_process.html#aa395434c6678fd88e0da9b593f92d8fc)  
  
[CTelephonyService](class_c_telephony_service.html) | [getTelephonyService](class_c_c_m_e_process.html#a8839105e40f7ed560b1f93d79dea0997) ()  
| Returns the [CTelephonyService](class_c_telephony_service.html "CTelephonyService handles and manipulates telephony services.") object. [More...](class_c_c_m_e_process.html#a8839105e40f7ed560b1f93d79dea0997)  
  
[CDialPeer](class_c_dial_peer.html) | [getDialPeer](class_c_c_m_e_process.html#a54f2754a6d18d94516364592ea3f15f0) (int)  
| Returns the [CDialPeer](class_c_dial_peer.html "CDialPeer holds and manipulates dial peers for VOIP.") object with the specified dial peer tag number. [More...](class_c_c_m_e_process.html#a54f2754a6d18d94516364592ea3f15f0)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[CCMEProcess](class_c_c_m_e_process.html "CCMEProcess is the process that handles CME.") is the process that handles CME. 

## Member Function Documentation

## ◆ getDialPeer()

[CDialPeer](class_c_dial_peer.html) CCMEProcess::getDialPeer  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the [CDialPeer](class_c_dial_peer.html "CDialPeer holds and manipulates dial peers for VOIP.") object with the specified dial peer tag number. 

Parameters
     dialPeerTag,the| tag number of the dial peer.  
---|---  
  
Returns
    [CDialPeer](class_c_dial_peer.html "CDialPeer holds and manipulates dial peers for VOIP."), the [CDialPeer](class_c_dial_peer.html "CDialPeer holds and manipulates dial peers for VOIP.") object with the specified dial peer tag number. 

## ◆ getEphone()

[CEphone](class_c_ephone.html) CCMEProcess::getEphone  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the [CEphone](class_c_ephone.html "CEphone holds and manipulates VOIP ephones.") object with the specified sequence number. 

Parameters
     int| tag, the unique sequence number of the ephone.  
---|---  
  
Returns
    [CEphone](class_c_ephone.html "CEphone holds and manipulates VOIP ephones."), the [CEphone](class_c_ephone.html "CEphone holds and manipulates VOIP ephones.") object with the specified sequence number. 

## ◆ getEphoneDirectory()

[CEphoneDirectory](class_c_ephone_directory.html) CCMEProcess::getEphoneDirectory  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the [CEphoneDirectory](class_c_ephone_directory.html "CEphoneDirectory holds and manipulates the ephone directory.") object with the specified sequence number. 

Parameters
     dnTag,the| unique sequence number of the ephone directory number.  
---|---  
  
Returns
    [CEphoneDirectory](class_c_ephone_directory.html "CEphoneDirectory holds and manipulates the ephone directory."), the [CEphoneDirectory](class_c_ephone_directory.html "CEphoneDirectory holds and manipulates the ephone directory.") object with the specified sequence number. 

## ◆ getTelephonyService()

[CTelephonyService](class_c_telephony_service.html) CCMEProcess::getTelephonyService  | ( | | ) |   
---|---|---|---|---  
  
Returns the [CTelephonyService](class_c_telephony_service.html "CTelephonyService handles and manipulates telephony services.") object. 

Returns
    [CTelephonyService](class_c_telephony_service.html "CTelephonyService handles and manipulates telephony services."), the [CTelephonyService](class_c_telephony_service.html "CTelephonyService handles and manipulates telephony services.") object. 

* * *

The documentation for this class was generated from the following file:

  * [CCMEProcess.pki](_c_c_m_e_process_8pki.html)


