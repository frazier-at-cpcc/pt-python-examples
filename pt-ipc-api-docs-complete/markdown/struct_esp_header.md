# Cisco Packet Tracer Extensions API: EspHeader Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_esp_header.html

---

ESP header structure. [More...](struct_esp_header.html#details)

##  Public Attributes  
  
---  
int | [nextHeader](struct_esp_header.html#a60df5971847afcca9ca4ee1820d7cf2b)  
int | [paddingLength](struct_esp_header.html#a1501dd823775c4fbacb9ec2b720406fa)  
int | [spi](struct_esp_header.html#a8aee87ab29813f3c26663f9616f641d4)  
int | [sequenceNumber](struct_esp_header.html#a202549ca3a6856c13e12c3c9330052c9)  
int | [padding](struct_esp_header.html#a5eb705887ec4d589c00ca53ada11a62b)  
string | [encryptionData](struct_esp_header.html#ad6f3909259ec574a6d5b48093f45d359)  
string | [authenticationData](struct_esp_header.html#a810fd116d8397365f44336a1ebe74b2e)  
EspEncryption | [espEncryption](struct_esp_header.html#a753170fdd6e57aa2cafe87e66226b50a)  
EspAuth | [espAuthentication](struct_esp_header.html#a7cfa3980a65fb497c4a6592c1ef6ad2c)  
Public Attributes inherited from [Header](struct_header.html)  
[Pdu](struct_pdu.html) | [payload](struct_header.html#a07ee8693faef1e16c65765b5bcdc366d)  
  
## Detailed Description

ESP header structure. 

## Member Data Documentation

## ◆ authenticationData

string EspHeader::authenticationData  
---  
  
## ◆ encryptionData

string EspHeader::encryptionData  
---  
  
## ◆ espAuthentication

EspAuth EspHeader::espAuthentication  
---  
  
## ◆ espEncryption

EspEncryption EspHeader::espEncryption  
---  
  
## ◆ nextHeader

int EspHeader::nextHeader  
---  
  
## ◆ padding

int EspHeader::padding  
---  
  
## ◆ paddingLength

int EspHeader::paddingLength  
---  
  
## ◆ sequenceNumber

int EspHeader::sequenceNumber  
---  
  
## ◆ spi

int EspHeader::spi  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [CEspHeader.pki](_c_esp_header_8pki.html)


