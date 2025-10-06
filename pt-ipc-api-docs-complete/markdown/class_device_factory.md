# Cisco Packet Tracer Extensions API: DeviceFactory Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_device_factory.html

---

The factory of devices. [More...](class_device_factory.html#details)

##  Public Member Functions  
  
---  
[DeviceDescriptor](class_device_descriptor.html) | [getDescriptor](class_device_factory.html#a1f5be4900746ad5cadb8e6313f91127f) (DeviceType, string)  
| Returns the Descriptor of the device. [More...](class_device_factory.html#a1f5be4900746ad5cadb8e6313f91127f)  
  
int | [getAvailableDeviceCount](class_device_factory.html#aa5faa3c22bd40a80f3c052cb39b74126) ()  
| Returns the number of available device type. [More...](class_device_factory.html#aa5faa3c22bd40a80f3c052cb39b74126)  
  
[DeviceDescriptor](class_device_descriptor.html) | [getAvailableDeviceAt](class_device_factory.html#a4bf9ee0a69837cf4cf10deea2fe19989) (int)  
| Returns the available device descriptorat a specified index. [More...](class_device_factory.html#a4bf9ee0a69837cf4cf10deea2fe19989)  
  
int | [getAvailableDeviceForTypeCount](class_device_factory.html#a6045143f2f6fb820be9739dbdcafad29) (DeviceType)  
| Returns the available device model for a specified type. [More...](class_device_factory.html#a6045143f2f6fb820be9739dbdcafad29)  
  
[DeviceDescriptor](class_device_descriptor.html) | [getAvailableDeviceForTypeAt](class_device_factory.html#a948e7af8b4f09075777527c8320bdab4) (DeviceType, int)  
| Returns the available device descriptor of a specified type at a specified index. [More...](class_device_factory.html#a948e7af8b4f09075777527c8320bdab4)  
  
  
## Detailed Description

The factory of devices. 

## Member Function Documentation

## ◆ getAvailableDeviceAt()

[DeviceDescriptor](class_device_descriptor.html) DeviceFactory::getAvailableDeviceAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the available device descriptorat a specified index. 

Parameters
     index,a| specified index  
---|---  
  
Returns
    [DeviceDescriptor](class_device_descriptor.html "Descriptor for a device."), [DeviceDescriptor](class_device_descriptor.html "Descriptor for a device.") object 

## ◆ getAvailableDeviceCount()

int DeviceFactory::getAvailableDeviceCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of available device type. 

Returns
    int, number of available device type 

## ◆ getAvailableDeviceForTypeAt()

[DeviceDescriptor](class_device_descriptor.html) DeviceFactory::getAvailableDeviceForTypeAt  | ( | DeviceType  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Returns the available device descriptor of a specified type at a specified index. 

Parameters
     type,enum<DeviceType>| \- see documentation for function [getDescriptor()](class_device_factory.html#a1f5be4900746ad5cadb8e6313f91127f "Returns the Descriptor of the device.") above  
---|---  
index,a| specified index  
  
Returns
    [DeviceDescriptor](class_device_descriptor.html "Descriptor for a device."), [DeviceDescriptor](class_device_descriptor.html "Descriptor for a device.") object 

## ◆ getAvailableDeviceForTypeCount()

int DeviceFactory::getAvailableDeviceForTypeCount  | ( | DeviceType  | | ) |   
---|---|---|---|---|---  
  
Returns the available device model for a specified type. 

Parameters
     type,enum<DeviceType>| \- see documentation for function [getDescriptor()](class_device_factory.html#a1f5be4900746ad5cadb8e6313f91127f "Returns the Descriptor of the device.") above  
---|---  
  
Returns
    int, the available device model for a specified type 

## ◆ getDescriptor()

[DeviceDescriptor](class_device_descriptor.html) DeviceFactory::getDescriptor  | ( | DeviceType  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Returns the Descriptor of the device. 

Parameters
     type,enum<DeviceType>|   
---|---  
  
Returns
    enum<DeviceType>, the type of this device. [Device](class_device.html "Device is the base class for all device objects.") types: eRouter = 0, eSwitch = 1, eCloud = 2, eBridge = 3, eHub = 4, eRepeater = 5, eCoAxialSplitter = 6, eAccessPoint = 7, ePc = 8, eServer = 9, ePrinter = 10, eWirelessRouter = 11, eIpPhone = 12, eDslModem = 13, eCableModem = 14, eRemoteNetwork = 15, eMultiLayerSwitch = 16, eLaptop = 17, eTabletPC = 18, ePda = 19, eWirelessEndDevice = 20, eWiredEndDevice = 21, eTV = 22, eHomeVoip = 23, eAnalogPhone = 24, eMultiUser = 25, eASA = 26, eIoE = 27, eHomeGateway = 28, eCellTower = 29, eCentralOfficeServer = 30, eWirelessLanController = 31,

Parameters
     model,the| device model in string format   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CDeviceFactory.pki](_c_device_factory_8pki.html)


