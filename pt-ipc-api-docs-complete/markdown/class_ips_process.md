# Cisco Packet Tracer Extensions API: IpsProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_ips_process.html

---

[IpsProcess](class_ips_process.html "IpsProcess is the process that handles intrusion prevention.") is the process that handles intrusion prevention. [More...](class_ips_process.html#details)

##  Public Member Functions  
  
---  
void | [setConfigLocation](class_ips_process.html#ad337db92ab952a137d8047e10856143f) (string)  
| Sets the directory location. [More...](class_ips_process.html#ad337db92ab952a137d8047e10856143f)  
  
string | [getConfigLocation](class_ips_process.html#a91d35067255e19bfde3f8b99de5de963) ()  
| Returns the config location directory for IPS. [More...](class_ips_process.html#a91d35067255e19bfde3f8b99de5de963)  
  
string | [getIpsAt](class_ips_process.html#a8e07184489e0bdfdebae0ebab7edd7e0) (int)  
| Returns the IPS at the specified index. [More...](class_ips_process.html#a8e07184489e0bdfdebae0ebab7edd7e0)  
  
string | [getAclForIps](class_ips_process.html#a70caf202cf68b239a906899301e4f666) (string)  
| Returns the ACL for the IPS with the specified name. [More...](class_ips_process.html#a70caf202cf68b239a906899301e4f666)  
  
void | [addIps](class_ips_process.html#a689d4180ba8fe381bb71774f4200825d) (string, string)  
| Adds an IPS with the specified name and ACL. [More...](class_ips_process.html#a689d4180ba8fe381bb71774f4200825d)  
  
bool | [deleteIps](class_ips_process.html#af8b77e1010a182b6721ce6b5921ed4c7) (string)  
| Removes the IPS from the list. [More...](class_ips_process.html#af8b77e1010a182b6721ce6b5921ed4c7)  
  
int | [getIpsListSize](class_ips_process.html#a26c94a8e42458f3f0bc765317f74a49d) ()  
| Returns the number of IPS configured. [More...](class_ips_process.html#a26c94a8e42458f3f0bc765317f74a49d)  
  
[SignatureCategory](class_signature_category.html) | [getRootSigCategory](class_ips_process.html#a2654fc2db2906c5f631d4316916cf20e) ()  
| Returns the root signature category category. [More...](class_ips_process.html#a2654fc2db2906c5f631d4316916cf20e)  
  
[Category](class_category.html) | [getSubCategoryAt](class_ips_process.html#a5dec74f1e7e6ccfceba7412f26c108e0) (int)  
| Returns the subcategory at the specified index. [More...](class_ips_process.html#a5dec74f1e7e6ccfceba7412f26c108e0)  
  
int | [getSubCategorySize](class_ips_process.html#aa5506a9e6be3b8e02b80ef92076d49f0) ()  
| Returns the subcategory size. [More...](class_ips_process.html#aa5506a9e6be3b8e02b80ef92076d49f0)  
  
[IcmpSignature](class_icmp_signature.html) | [getIcmpSignature](class_ips_process.html#a59876ddef0d3dd9145b4344bcf58034d) ()  
| Returns the ICMP signature. [More...](class_ips_process.html#a59876ddef0d3dd9145b4344bcf58034d)  
  
void | [setRetryCount](class_ips_process.html#ac4772163aec03b9fcc258a39d2c4d279) (int)  
| Sets the retry count. [More...](class_ips_process.html#ac4772163aec03b9fcc258a39d2c4d279)  
  
int | [getRetryCount](class_ips_process.html#a905de894c38f1f2324f2519a180a0367) ()  
| Returns the retry count. [More...](class_ips_process.html#a905de894c38f1f2324f2519a180a0367)  
  
void | [setNotifyLog](class_ips_process.html#a1e8f892aaab306fdd0c3330efcfea167) (bool)  
| Sets the syslog notification. [More...](class_ips_process.html#a1e8f892aaab306fdd0c3330efcfea167)  
  
bool | [isSysLogEnabled](class_ips_process.html#a6d34f2c280e186769fd6b1c0fc96b3d9) ()  
| Returns true if syslog is enabled, otherwise false. [More...](class_ips_process.html#a6d34f2c280e186769fd6b1c0fc96b3d9)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[IpsProcess](class_ips_process.html "IpsProcess is the process that handles intrusion prevention.") is the process that handles intrusion prevention. 

## Member Function Documentation

## ◆ addIps()

void IpsProcess::addIps  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Adds an IPS with the specified name and ACL. 

Parameters
     ipsName,the| name of this IPS.   
---|---  
aclName,the| name of the ACL for this IPS.   
  
  
## ◆ deleteIps()

bool IpsProcess::deleteIps  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes the IPS from the list. 

Parameters
     ipsName,the| name of the IPS of interest.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ getAclForIps()

string IpsProcess::getAclForIps  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the ACL for the IPS with the specified name. 

Parameters
     ipsName,the| name of the IPS of interest.  
---|---  
  
Returns
    string, the ACL for the IPS with the specified name. 

## ◆ getConfigLocation()

string IpsProcess::getConfigLocation  | ( | | ) |   
---|---|---|---|---  
  
Returns the config location directory for IPS. 

Returns
    string, the config location directory for IPS. 

## ◆ getIcmpSignature()

[IcmpSignature](class_icmp_signature.html) IpsProcess::getIcmpSignature  | ( | | ) |   
---|---|---|---|---  
  
Returns the ICMP signature. 

Returns
    [IcmpSignature](class_icmp_signature.html "IcmpSignature handles and manipulates ICMP signatures."), the [IcmpSignature](class_icmp_signature.html "IcmpSignature handles and manipulates ICMP signatures.") object. 

## ◆ getIpsAt()

string IpsProcess::getIpsAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the IPS at the specified index. 

Parameters
     index,the| index of the IPS of interest.  
---|---  
  
Returns
    string, the IPS at the specified index. 

## ◆ getIpsListSize()

int IpsProcess::getIpsListSize  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of IPS configured. 

Returns
    int, the number of IPS configured. 

## ◆ getRetryCount()

int IpsProcess::getRetryCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the retry count. 

Returns
    int, the retry count. 

## ◆ getRootSigCategory()

[SignatureCategory](class_signature_category.html) IpsProcess::getRootSigCategory  | ( | | ) |   
---|---|---|---|---  
  
Returns the root signature category category. 

Returns
    [SignatureCategory](class_signature_category.html "SignatureCategory handles and manipulates signature categories."), the [SignatureCategory](class_signature_category.html "SignatureCategory handles and manipulates signature categories.") object. 

## ◆ getSubCategoryAt()

[Category](class_category.html) IpsProcess::getSubCategoryAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the subcategory at the specified index. 

Parameters
     index,the| index of the subcategory of interest.  
---|---  
  
Returns
    [Category](class_category.html "Category is the class for signature subcategories."), the [Category](class_category.html "Category is the class for signature subcategories.") object at the specified index. 

## ◆ getSubCategorySize()

int IpsProcess::getSubCategorySize  | ( | | ) |   
---|---|---|---|---  
  
Returns the subcategory size. 

Returns
    int, the subcategory size. 

## ◆ isSysLogEnabled()

bool IpsProcess::isSysLogEnabled  | ( | | ) |   
---|---|---|---|---  
  
Returns true if syslog is enabled, otherwise false. 

Returns
    bool, true if syslog is enabled, otherwise false. 

## ◆ setConfigLocation()

void IpsProcess::setConfigLocation  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the directory location. 

Parameters
     name,the| directory location.   
---|---  
  
## ◆ setNotifyLog()

void IpsProcess::setNotifyLog  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Sets the syslog notification. 

Parameters
     val,true| to enable syslog, false to disable it.   
---|---  
  
## ◆ setRetryCount()

void IpsProcess::setRetryCount  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the retry count. 

Parameters
     count,the| retry count.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CIpsProcess.pki](_c_ips_process_8pki.html)


