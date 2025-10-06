# Cisco Packet Tracer Extensions API: StpMainProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_stp_main_process.html

---

[StpMainProcess](class_stp_main_process.html "StpMainProcess holds and manages the individual STP processes.") holds and manages the individual STP processes. [More...](class_stp_main_process.html#details)

##  Public Member Functions  
  
---  
[StpProcess](class_stp_process.html) | [getStpProcess](class_stp_main_process.html#a77bde61176dd8632f3c53709e0bc09a4) (int)  
| Returns the STP process from the specified VLAN. [More...](class_stp_main_process.html#a77bde61176dd8632f3c53709e0bc09a4)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[StpMainProcess](class_stp_main_process.html "StpMainProcess holds and manages the individual STP processes.") holds and manages the individual STP processes. 

## Member Function Documentation

## ◆ getStpProcess()

[StpProcess](class_stp_process.html) StpMainProcess::getStpProcess  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the STP process from the specified VLAN. 

Parameters
     vlanID,the| VLAN number of interest.  
---|---  
  
Returns
    [StpProcess](class_stp_process.html "StpProcess handles and manipulates STP processes."), the [StpProcess](class_stp_process.html "StpProcess handles and manipulates STP processes.") object from the specified VLAN. 

* * *

The documentation for this class was generated from the following file:

  * [CStpMainProcess.pki](_c_stp_main_process_8pki.html)


