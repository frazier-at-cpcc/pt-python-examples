# Cisco Packet Tracer Extensions API: CTelephonyService Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_c_telephony_service.html

---

[CTelephonyService](class_c_telephony_service.html "CTelephonyService handles and manipulates telephony services.") handles and manipulates telephony services. [More...](class_c_telephony_service.html#details)

##  Public Member Functions  
  
---  
void | [setAutoRegistration](class_c_telephony_service.html#aee70316b462952c84698c01379d6579d) (bool)  
| Enables or disables auto registration. [More...](class_c_telephony_service.html#aee70316b462952c84698c01379d6579d)  
  
bool | [isAutoRegEnabled](class_c_telephony_service.html#aa9acf34381393472c94d739f365011e4) ()  
| Returns true if auto registration is enabled, otherwise false. [More...](class_c_telephony_service.html#aa9acf34381393472c94d739f365011e4)  
  
void | [setMaxEphone](class_c_telephony_service.html#a25d8abc3b568502f04531e55afc5b407) (int)  
| Sets the maximum number of ephones. [More...](class_c_telephony_service.html#a25d8abc3b568502f04531e55afc5b407)  
  
int | [getMaxEphoneNumber](class_c_telephony_service.html#aac1584afeb0cc75faf6101a8b6871218) ()  
| Returns the maximum number of ephones. [More...](class_c_telephony_service.html#aac1584afeb0cc75faf6101a8b6871218)  
  
void | [setMaxDnNumber](class_c_telephony_service.html#ad027c2b6d6dbd4e5ee3015d6f76c9eff) (int)  
| Sets the maximum number of directory numbers. [More...](class_c_telephony_service.html#ad027c2b6d6dbd4e5ee3015d6f76c9eff)  
  
int | [getMaxDnNumber](class_c_telephony_service.html#a2984ada176a4965a0c73a95042c50597) ()  
| Returns the maximum number of directory numbers. [More...](class_c_telephony_service.html#a2984ada176a4965a0c73a95042c50597)  
  
void | [setSourcePort](class_c_telephony_service.html#aa8998e584eed48264468e1827bd55f3e) (int)  
| Sets the source port number. [More...](class_c_telephony_service.html#aa8998e584eed48264468e1827bd55f3e)  
  
int | [getSourcePort](class_c_telephony_service.html#a1210d8a551191783cf3b5753415d9095) ()  
| Returns the source port number. [More...](class_c_telephony_service.html#a1210d8a551191783cf3b5753415d9095)  
  
void | [setSystemMessage](class_c_telephony_service.html#aea34e7921bd22ac04095efa2e97d87fc) (string)  
| Sets the system message. [More...](class_c_telephony_service.html#aea34e7921bd22ac04095efa2e97d87fc)  
  
void | [setAutoAssign](class_c_telephony_service.html#a7891302df8416164a165e75f44aefc76) (int, int)  
| Sets the auto assign directory numbers. [More...](class_c_telephony_service.html#a7891302df8416164a165e75f44aefc76)  
  
int | [getAutoAssignCount](class_c_telephony_service.html#af429ae38c87980cc7dba009769e898b6) ()  
| Returns the number of auto assigned directory numbers. [More...](class_c_telephony_service.html#af429ae38c87980cc7dba009769e898b6)  
  
int | [getAutoAssignStartDnAt](class_c_telephony_service.html#ace0c992f9fb2206b2d1cd2df0530cfe0) (int)  
| Returns the auto assigned start directory number at the specified index. [More...](class_c_telephony_service.html#ace0c992f9fb2206b2d1cd2df0530cfe0)  
  
int | [getAutoAssignStopDnAt](class_c_telephony_service.html#a1f5eff3ec5a307ecc46a5ae9bda32b2c) (int)  
| Returns the auto assigned stop directory number at the specified index. [More...](class_c_telephony_service.html#a1f5eff3ec5a307ecc46a5ae9bda32b2c)  
  
  
## Detailed Description

[CTelephonyService](class_c_telephony_service.html "CTelephonyService handles and manipulates telephony services.") handles and manipulates telephony services. 

## Member Function Documentation

## ◆ getAutoAssignCount()

int CTelephonyService::getAutoAssignCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of auto assigned directory numbers. 

Returns
    int, the number of auto assigned directory numbers. 

## ◆ getAutoAssignStartDnAt()

int CTelephonyService::getAutoAssignStartDnAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the auto assigned start directory number at the specified index. 

Parameters
     index,the| index of the auto assigned start directory number of interest.  
---|---  
  
Returns
    int, the auto assigned start directory number at the specified index. 

## ◆ getAutoAssignStopDnAt()

int CTelephonyService::getAutoAssignStopDnAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the auto assigned stop directory number at the specified index. 

Parameters
     index,the| index of the auto assigned stop directory number of interest.  
---|---  
  
Returns
    int, the auto assigned stop directory number at the specified index. 

## ◆ getMaxDnNumber()

int CTelephonyService::getMaxDnNumber  | ( | | ) |   
---|---|---|---|---  
  
Returns the maximum number of directory numbers. 

Returns
    int, the maximum number of directory numbers. 

## ◆ getMaxEphoneNumber()

int CTelephonyService::getMaxEphoneNumber  | ( | | ) |   
---|---|---|---|---  
  
Returns the maximum number of ephones. 

Returns
    int, the maximum number of ephones. 

## ◆ getSourcePort()

int CTelephonyService::getSourcePort  | ( | | ) |   
---|---|---|---|---  
  
Returns the source port number. 

Returns
    int, the source port number. 

## ◆ isAutoRegEnabled()

bool CTelephonyService::isAutoRegEnabled  | ( | | ) |   
---|---|---|---|---  
  
Returns true if auto registration is enabled, otherwise false. 

Returns
    bool, true if auto registration is enabled, otherwise false. 

## ◆ setAutoAssign()

void CTelephonyService::setAutoAssign  | ( | int  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Sets the auto assign directory numbers. 

Parameters
     startTag,the| start directory numbers.   
---|---  
stopTag,the| stop directory numbers.   
  
## ◆ setAutoRegistration()

void CTelephonyService::setAutoRegistration  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables auto registration. 

Parameters
     bVal,true| to enable auto registration.   
---|---  
  
## ◆ setMaxDnNumber()

void CTelephonyService::setMaxDnNumber  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the maximum number of directory numbers. 

Parameters
     maxDnNum,the| maximum number of directory numbers.   
---|---  
  
## ◆ setMaxEphone()

void CTelephonyService::setMaxEphone  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the maximum number of ephones. 

Parameters
     maxEphNum,the| maximum number of ephones.   
---|---  
  
## ◆ setSourcePort()

void CTelephonyService::setSourcePort  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the source port number. 

Parameters
     portNum,the| source port number.   
---|---  
  
## ◆ setSystemMessage()

void CTelephonyService::setSystemMessage  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the system message. 

Parameters
     msg,the| system message.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CTelephonyService.pki](_c_telephony_service_8pki.html)


