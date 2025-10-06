# Cisco Packet Tracer Extensions API: UsbController Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_usb_controller.html

---

[UsbController](class_usb_controller.html "UsbController."). [More...](class_usb_controller.html#details)

##  Public Member Functions  
  
---  
void | [begin](class_usb_controller.html#a8467544850e892ed9a143b665150b2b3) (int)  
| Start the [UsbController](class_usb_controller.html "UsbController."). [More...](class_usb_controller.html#a8467544850e892ed9a143b665150b2b3)  
  
void | [end](class_usb_controller.html#aca41f176808a6324788c48715bf5a7f7) ()  
| End the [UsbController](class_usb_controller.html "UsbController."). [More...](class_usb_controller.html#aca41f176808a6324788c48715bf5a7f7)  
  
int | [available](class_usb_controller.html#af5fdf2a859ca84a91ba2ac72ccb51191) ()  
| Returns number of bytes available in the buffer. [More...](class_usb_controller.html#af5fdf2a859ca84a91ba2ac72ccb51191)  
  
int | [print](class_usb_controller.html#a5dd25db046b2de70ce468378eb96d943) (string)  
| Print string to the console. [More...](class_usb_controller.html#a5dd25db046b2de70ce468378eb96d943)  
  
string | [readLine](class_usb_controller.html#a38235b94d9cf720e393510b924df6558) ()  
| Read the next line in the buffer. [More...](class_usb_controller.html#a38235b94d9cf720e393510b924df6558)  
  
string | [readChar](class_usb_controller.html#af60f80860257239af504c052edb85e20) ()  
| Read the next character in the buffer. [More...](class_usb_controller.html#af60f80860257239af504c052edb85e20)  
  
string | [peekChar](class_usb_controller.html#a639c2d6dc44e2683f99f2a2be804309d) ()  
| Peek the next character in the buffer. [More...](class_usb_controller.html#a639c2d6dc44e2683f99f2a2be804309d)  
  
int | [read](class_usb_controller.html#a076f39100b6bd0b46a6291019a4332ae) ()  
| Read the next character in the buffer - same as [readChar()](class_usb_controller.html#af60f80860257239af504c052edb85e20 "Read the next character in the buffer.") [More...](class_usb_controller.html#a076f39100b6bd0b46a6291019a4332ae)  
  
int | [peek](class_usb_controller.html#aaaedefe6041216df22112a2a4c050858) ()  
| Peek the next character in the buffer - same as [peekChar()](class_usb_controller.html#a639c2d6dc44e2683f99f2a2be804309d "Peek the next character in the buffer.") [More...](class_usb_controller.html#aaaedefe6041216df22112a2a4c050858)  
  
int | [write](class_usb_controller.html#ac9571004d175997c0b5a4fa56d552b31) (int)  
| Write a character to the console. [More...](class_usb_controller.html#ac9571004d175997c0b5a4fa56d552b31)  
  
void | [setSerialMonitoring](class_usb_controller.html#a30c49e6bade655e779adc15c2249f91f) (bool)  
| Set Serial Monitoring on or off. [More...](class_usb_controller.html#a30c49e6bade655e779adc15c2249f91f)  
  
bool | [isSerialMonitoring](class_usb_controller.html#a97b3e1b345ed301d44827919686451a6) ()  
| Check if Serial Monitoring is on or off. [More...](class_usb_controller.html#a97b3e1b345ed301d44827919686451a6)  
  
bool | [deployProjectFromFileSystem](class_usb_controller.html#aa61569129443b51285253d640dca8d5c) (string, string)  
| Deploy project from file system. [More...](class_usb_controller.html#aa61569129443b51285253d640dca8d5c)  
  
bool | [isPortUp](class_usb_controller.html#a5ebe31b36e4899d226ec219ba640b37f) ()  
| Check if port is powered on. [More...](class_usb_controller.html#a5ebe31b36e4899d226ec219ba640b37f)  
  
bool | [isProtocolUp](class_usb_controller.html#a414509089903ad04a4e8342810c81e35) ()  
| Check if port's protocol is up. [More...](class_usb_controller.html#a414509089903ad04a4e8342810c81e35)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[UsbController](class_usb_controller.html "UsbController."). 

## Member Function Documentation

## ◆ available()

int UsbController::available  | ( | | ) |   
---|---|---|---|---  
  
Returns number of bytes available in the buffer. 

Returns
    int, number of bytes 

## ◆ begin()

void UsbController::begin  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Start the [UsbController](class_usb_controller.html "UsbController."). 

Parameters
     speed,the| speed at which the Usb Controller is operating at   
---|---  
  
## ◆ deployProjectFromFileSystem()

bool UsbController::deployProjectFromFileSystem  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Deploy project from file system. 

Parameters
     projectName,name| of the project in string   
---|---  
path,path| of the project in string   
  
Returns
    bool, true if the project was successfully deployed and false if it's not 

## ◆ end()

void UsbController::end  | ( | | ) |   
---|---|---|---|---  
  
End the [UsbController](class_usb_controller.html "UsbController."). 

## ◆ isPortUp()

bool UsbController::isPortUp  | ( | | ) |   
---|---|---|---|---  
  
Check if port is powered on. 

Returns
    bool, true if it's powered on and false if it's not 

## ◆ isProtocolUp()

bool UsbController::isProtocolUp  | ( | | ) |   
---|---|---|---|---  
  
Check if port's protocol is up. 

Returns
    bool, true if port's protocol is up and false if it's not 

## ◆ isSerialMonitoring()

bool UsbController::isSerialMonitoring  | ( | | ) |   
---|---|---|---|---  
  
Check if Serial Monitoring is on or off. 

Returns
    bool, true for on and false for off 

## ◆ peek()

int UsbController::peek  | ( | | ) |   
---|---|---|---|---  
  
Peek the next character in the buffer - same as [peekChar()](class_usb_controller.html#a639c2d6dc44e2683f99f2a2be804309d "Peek the next character in the buffer.")

Returns
    string, the next character in string format 

## ◆ peekChar()

string UsbController::peekChar  | ( | | ) |   
---|---|---|---|---  
  
Peek the next character in the buffer. 

Returns
    string, the next character in string format 

## ◆ print()

int UsbController::print  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Print string to the console. 

Parameters
     value,the| string to be printed   
---|---  
  
Returns
    int, the length of the string 

## ◆ read()

int UsbController::read  | ( | | ) |   
---|---|---|---|---  
  
Read the next character in the buffer - same as [readChar()](class_usb_controller.html#af60f80860257239af504c052edb85e20 "Read the next character in the buffer.")

Returns
    string, the next character in string format 

## ◆ readChar()

string UsbController::readChar  | ( | | ) |   
---|---|---|---|---  
  
Read the next character in the buffer. 

Returns
    string, the next character in string format 

## ◆ readLine()

string UsbController::readLine  | ( | | ) |   
---|---|---|---|---  
  
Read the next line in the buffer. 

Returns
    string, the next line 

## ◆ setSerialMonitoring()

void UsbController::setSerialMonitoring  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Set Serial Monitoring on or off. 

Parameters
     bMonitoring,true| for on and false for off   
---|---  
  
## ◆ write()

int UsbController::write  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Write a character to the console. 

Parameters
     value,ascii| value of the character to be written \   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CUsbController.pki](_c_usb_controller_8pki.html)


