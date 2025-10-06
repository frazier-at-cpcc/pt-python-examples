# Cisco Packet Tracer Extensions API: Network Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_network.html

---

[Network](class_network.html "Network is the entry point for all device configurations in the network. It retrieves devices.") is the entry point for all device configurations in the network. It retrieves devices. [More...](class_network.html#details)

##  Public Member Functions  
  
---  
[Device](class_device.html) | [getDevice](class_network.html#a44a86dffbe90ff3daef2580e1e2faa34) (QString)  
| Returns the device with the specified device name. [More...](class_network.html#a44a86dffbe90ff3daef2580e1e2faa34)  
  
[Device](class_device.html) | [getDeviceAt](class_network.html#a479b42140fbecbfe269fdc1198f347a7) (int)  
| Returns the device at the specified index. [More...](class_network.html#a479b42140fbecbfe269fdc1198f347a7)  
  
int | [getDeviceCount](class_network.html#aca7dea2bc81088494ca54dc21e477ef1) ()  
| Returns the number of devices in the network. [More...](class_network.html#aca7dea2bc81088494ca54dc21e477ef1)  
  
int | [getLinkCount](class_network.html#a33883131ecfa52b0b9b65edc162d69da) ()  
[Link](class_link.html) | [getLinkAt](class_network.html#a31a6606aaff73ebb66be31b08ef2af96) (int)  
double | [getTotalDeviceAttributeValue](class_network.html#ad8ea614ac17472d2faea643cc0f27e1e) (string)  
  
## Detailed Description

[Network](class_network.html "Network is the entry point for all device configurations in the network. It retrieves devices.") is the entry point for all device configurations in the network. It retrieves devices. 

## Member Function Documentation

## ◆ getDevice()

[Device](class_device.html) Network::getDevice  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the device with the specified device name. 

Parameters
     deviceName,the| device name of the device of interest.  
---|---  
  
Returns
    [Device](class_device.html "Device is the base class for all device objects."), the [Device](class_device.html "Device is the base class for all device objects.") object with the specified device name. 

## ◆ getDeviceAt()

[Device](class_device.html) Network::getDeviceAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the device at the specified index. 

Parameters
     index,the| index of the device of interest.  
---|---  
  
Returns
    [Device](class_device.html "Device is the base class for all device objects."), the [Device](class_device.html "Device is the base class for all device objects.") object at the specified index. 

## ◆ getDeviceCount()

int Network::getDeviceCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of devices in the network. 

Returns
    int, the number of devices in the network. 

## ◆ getLinkAt()

[Link](class_link.html) Network::getLinkAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
## ◆ getLinkCount()

int Network::getLinkCount  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getTotalDeviceAttributeValue()

double Network::getTotalDeviceAttributeValue  | ( | string  | | ) |   
---|---|---|---|---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CNetwork.pki](_c_network_8pki.html)


