# Cisco Packet Tracer Extensions API: NFCollectorProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_n_f_collector_process.html

---

[NFCollectorProcess](class_n_f_collector_process.html "NFCollectorProcess handles the NetFlow Collector process.") handles the NetFlow Collector process. [More...](class_n_f_collector_process.html#details)

##  Public Member Functions  
  
---  
void | [setEnabled](class_n_f_collector_process.html#a86ea34854d9ae41539112d3fda24084d) (bool)  
| Enables or disables the NetFlow Collector. [More...](class_n_f_collector_process.html#a86ea34854d9ae41539112d3fda24084d)  
  
bool | [isEnabled](class_n_f_collector_process.html#a069a386f270013460eabd5f47d43d9e3) ()  
| Returns true if the NetFlow Collector is enabled, otherwise false. [More...](class_n_f_collector_process.html#a069a386f270013460eabd5f47d43d9e3)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[NFCollectorProcess](class_n_f_collector_process.html "NFCollectorProcess handles the NetFlow Collector process.") handles the NetFlow Collector process. 

## Member Function Documentation

## ◆ isEnabled()

bool NFCollectorProcess::isEnabled  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the NetFlow Collector is enabled, otherwise false. 

Returns
    bool, true if the NetFlow Collector is enabled, otherwise false. 

## ◆ setEnabled()

void NFCollectorProcess::setEnabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables the NetFlow Collector. 

Parameters
     enable,true| to enable the NetFlow Collector, false to disable it.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CNFCollectorProcess.pki](_c_n_f_collector_process_8pki.html)


