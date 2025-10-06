# Cisco Packet Tracer Extensions API: PTPPortData Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_p_t_p_port_data.html

---

This file holds CPTPPortData class declaration. [More...](class_p_t_p_port_data.html#details)

##  Public Member Functions  
  
---  
void | [setPtpVersion](class_p_t_p_port_data.html#a827ff044019e9f117a72cf4d94da4e7b) (int)  
| Sets ptp version. [More...](class_p_t_p_port_data.html#a827ff044019e9f117a72cf4d94da4e7b)  
  
int | [getPtpVersion](class_p_t_p_port_data.html#ac6481b4bc5b2441026a814fc68362514) ()  
| Gets ptp version. [More...](class_p_t_p_port_data.html#ac6481b4bc5b2441026a814fc68362514)  
  
void | [setPortState](class_p_t_p_port_data.html#ab8aab26ca1e672591318db7e3d930404) (PortState)  
| Sets the profile type. [More...](class_p_t_p_port_data.html#ab8aab26ca1e672591318db7e3d930404)  
  
PortState | [getPortState](class_p_t_p_port_data.html#a2b50b01ad6129338072b58c75c451cfd) ()  
| Gets the port state. [More...](class_p_t_p_port_data.html#a2b50b01ad6129338072b58c75c451cfd)  
  
string | [getPortStateStr](class_p_t_p_port_data.html#ac68fbf337d7d4b18f1db0f1c786bf704) ()  
| Returns the profile as a string. [More...](class_p_t_p_port_data.html#ac68fbf337d7d4b18f1db0f1c786bf704)  
  
void | [setRecommendedPortState](class_p_t_p_port_data.html#ae5314c0df5b17bdbae9fbf7596fb7616) (PortState)  
| Sets the recommended port state. [More...](class_p_t_p_port_data.html#ae5314c0df5b17bdbae9fbf7596fb7616)  
  
PortState | [getRecommendedPortState](class_p_t_p_port_data.html#af19773fc336c75dad7c25de33417dbc0) ()  
| Gets the recommended port state. [More...](class_p_t_p_port_data.html#af19773fc336c75dad7c25de33417dbc0)  
  
void | [setDelayRequestInterval](class_p_t_p_port_data.html#a307fdf9ff6803121ade07b908ed00117) (int)  
| Sets the delay request interval. [More...](class_p_t_p_port_data.html#a307fdf9ff6803121ade07b908ed00117)  
  
int | [getDelayRequestInterval](class_p_t_p_port_data.html#ac4b4a797e06628e5ddfd415ee08a49ab) ()  
| Gets the delay request interval. [More...](class_p_t_p_port_data.html#ac4b4a797e06628e5ddfd415ee08a49ab)  
  
void | [setAnnounceReceiptTimeout](class_p_t_p_port_data.html#aa264f463d371104a9f98b9f7761f6b0c) (int)  
| Sets the announcement receipt timout time. [More...](class_p_t_p_port_data.html#aa264f463d371104a9f98b9f7761f6b0c)  
  
int | [getAnnounceReceiptTimeout](class_p_t_p_port_data.html#a14ef95da267e22c3200d781f4fd0bbd7) ()  
| Gets the announcement receipt timout time. [More...](class_p_t_p_port_data.html#a14ef95da267e22c3200d781f4fd0bbd7)  
  
void | [setAnnounceInterval](class_p_t_p_port_data.html#aa4e3185fdaf6a5c133a87e78fc506a79) (int)  
| Sets the announcement interval time. [More...](class_p_t_p_port_data.html#aa4e3185fdaf6a5c133a87e78fc506a79)  
  
int | [getAnnounceInterval](class_p_t_p_port_data.html#a6fa446772fa82f99c322857bc30e0650) ()  
| Gets the announcement interval time. [More...](class_p_t_p_port_data.html#a6fa446772fa82f99c322857bc30e0650)  
  
void | [setSyncInterval](class_p_t_p_port_data.html#ad4dcf10f9c85347fc966a1637161f8f4) (int)  
| Sets the sync interval time. [More...](class_p_t_p_port_data.html#ad4dcf10f9c85347fc966a1637161f8f4)  
  
int | [getSyncInterval](class_p_t_p_port_data.html#ac6ec760560cc4c390406860002ae51ec) ()  
| Gets the sync interval time. [More...](class_p_t_p_port_data.html#ac6ec760560cc4c390406860002ae51ec)  
  
void | [setSyncWaitLimit](class_p_t_p_port_data.html#aa02b9c05522908344d42ee63e854f0e9) (long)  
| Sets the sync interval wait limit. [More...](class_p_t_p_port_data.html#aa02b9c05522908344d42ee63e854f0e9)  
  
int | [getSyncWaitLimit](class_p_t_p_port_data.html#a8715c531103c9b0917a1c7922fbf12a4) ()  
| Gets the sync interval wait limit. [More...](class_p_t_p_port_data.html#a8715c531103c9b0917a1c7922fbf12a4)  
  
void | [setSyncMsgCounter](class_p_t_p_port_data.html#a59c60e0139864e07f43a5abba14bd66e) (int)  
| Sets the sync message counter. [More...](class_p_t_p_port_data.html#a59c60e0139864e07f43a5abba14bd66e)  
  
void | [incrementSyncMsgCounter](class_p_t_p_port_data.html#a32f208d01e061a16379ebe338cc7c91a) ()  
| Increments the sync message counter. [More...](class_p_t_p_port_data.html#a32f208d01e061a16379ebe338cc7c91a)  
  
int | [getSyncMsgCounter](class_p_t_p_port_data.html#ac0ac5fc6aa59d0dd8ff8adaab7baf5ac) ()  
| Gets the sync message counter. [More...](class_p_t_p_port_data.html#ac0ac5fc6aa59d0dd8ff8adaab7baf5ac)  
  
void | [setDelayReqCounter](class_p_t_p_port_data.html#a322aec3c6f16fef7782daeaf597830ae) (int)  
| Sets the delay request counter. [More...](class_p_t_p_port_data.html#a322aec3c6f16fef7782daeaf597830ae)  
  
void | [incrementDelayReqCounter](class_p_t_p_port_data.html#a1ca64c599932c0228fa4a22f0ec696a5) ()  
| Increments the delay request counter. [More...](class_p_t_p_port_data.html#a1ca64c599932c0228fa4a22f0ec696a5)  
  
int | [getDelayReqCounter](class_p_t_p_port_data.html#a178ed9487606f40b7f99efabdef7d59e) ()  
| Gets delay request count. [More...](class_p_t_p_port_data.html#a178ed9487606f40b7f99efabdef7d59e)  
  
void | [setAnnounceSeqNum](class_p_t_p_port_data.html#a87b56d57014743ccb5f8bc2775394109) (double)  
| Sets the announce sequence number counter. [More...](class_p_t_p_port_data.html#a87b56d57014743ccb5f8bc2775394109)  
  
double | [getAnnounceSeqNum](class_p_t_p_port_data.html#aa117c99e9c1af1e83e2dc596411af913) ()  
| Gets the announce sequence number. [More...](class_p_t_p_port_data.html#aa117c99e9c1af1e83e2dc596411af913)  
  
void | [setSyncSeqNum](class_p_t_p_port_data.html#ad8dbd5f0794c1bbe70f49b52856e757c) (double)  
| Sets the sync sequence number. [More...](class_p_t_p_port_data.html#ad8dbd5f0794c1bbe70f49b52856e757c)  
  
double | [getSyncSeqNum](class_p_t_p_port_data.html#ad9781a89c7b9fc7f255d7e033d5bcf76) ()  
| Gets the sync sequence number. [More...](class_p_t_p_port_data.html#ad9781a89c7b9fc7f255d7e033d5bcf76)  
  
void | [setDecisionCode](class_p_t_p_port_data.html#a145a85c0b1558268bfcc41b49933feef) (DecisionCode)  
| Sets the decision code. [More...](class_p_t_p_port_data.html#a145a85c0b1558268bfcc41b49933feef)  
  
DecisionCode | [getDecisionCode](class_p_t_p_port_data.html#aae4ee8256e5946093f0113260615d1fb) ()  
| Gets the recommended port state. [More...](class_p_t_p_port_data.html#aae4ee8256e5946093f0113260615d1fb)  
  
void | [setLastSyncSeqNum](class_p_t_p_port_data.html#a3e239d15d317fc03d015df57a896b821) (double)  
| Sets the last sync sequence number. [More...](class_p_t_p_port_data.html#a3e239d15d317fc03d015df57a896b821)  
  
double | [getLastSyncSeqNum](class_p_t_p_port_data.html#a68ed31561b2367c9bae59ed4e8d0f47c) ()  
| Gets the last sync sequence number. [More...](class_p_t_p_port_data.html#a68ed31561b2367c9bae59ed4e8d0f47c)  
  
void | [setLastGeneralEventSeqNum](class_p_t_p_port_data.html#a27c77dc8bb2da2456ae830fc9373d8bf) (double)  
| Sets the last known general event sequence number. [More...](class_p_t_p_port_data.html#a27c77dc8bb2da2456ae830fc9373d8bf)  
  
double | [getLastGeneralEventSeqNum](class_p_t_p_port_data.html#a1aa0eb8bf8f278fc025ae1813a8c87b9) ()  
| Gets the last general event sequence number. [More...](class_p_t_p_port_data.html#a1aa0eb8bf8f278fc025ae1813a8c87b9)  
  
void | [setBustEnabled](class_p_t_p_port_data.html#a9a7105e5071829d1d11108e2a4731106) (bool)  
| Sets bust to be enabled or disabled. [More...](class_p_t_p_port_data.html#a9a7105e5071829d1d11108e2a4731106)  
  
bool | [isBustEnabled](class_p_t_p_port_data.html#a93561611a0794d4c136357c7486cd947) ()  
| Gets bust enabled state. [More...](class_p_t_p_port_data.html#a93561611a0794d4c136357c7486cd947)  
  
bool | [removeForeignMasterBySrcPortId](class_p_t_p_port_data.html#a6f8fee0b2edc2bfc1e99c4d5a2959b9f) (string, int)  
| Removes a foreign master by port. [More...](class_p_t_p_port_data.html#a6f8fee0b2edc2bfc1e99c4d5a2959b9f)  
  
void | [clearForeignMasterList](class_p_t_p_port_data.html#ad4e108c95fcc40a419438ad63aeb92f0) ()  
| Removes all the foreign masters. [More...](class_p_t_p_port_data.html#ad4e108c95fcc40a419438ad63aeb92f0)  
  
void | [setEBestSrc](class_p_t_p_port_data.html#ab4c6965b72207ba4acd5a107fcfb7734) (bool)  
| Sets the port data to be or not to be the best source for grandmaster clock. [More...](class_p_t_p_port_data.html#ab4c6965b72207ba4acd5a107fcfb7734)  
  
bool | [isEBestSrc](class_p_t_p_port_data.html#a08ecfdd7097231246b24451a4cafa9b3) ()  
| Check if this port data is the best source for grandmaster clock. [More...](class_p_t_p_port_data.html#a08ecfdd7097231246b24451a4cafa9b3)  
  
void | [resetDatasetToDefault](class_p_t_p_port_data.html#a7a6e66a19ba5e2aa5caa54b6f1804630) ()  
| Resets the data set to default. [More...](class_p_t_p_port_data.html#a7a6e66a19ba5e2aa5caa54b6f1804630)  
  
void | [cancelTimer](class_p_t_p_port_data.html#ab217e069882971e96ef29e6f777ec824) ()  
| Cancels the timer. [More...](class_p_t_p_port_data.html#ab217e069882971e96ef29e6f777ec824)  
  
void | [clearConfig](class_p_t_p_port_data.html#a06e4f39eb51fa79cc18235674a8af045) ()  
| Clears the config. [More...](class_p_t_p_port_data.html#a06e4f39eb51fa79cc18235674a8af045)  
  
  
## Detailed Description

This file holds CPTPPortData class declaration. 

## Member Function Documentation

## ◆ cancelTimer()

void PTPPortData::cancelTimer  | ( | | ) |   
---|---|---|---|---  
  
Cancels the timer. 

## ◆ clearConfig()

void PTPPortData::clearConfig  | ( | | ) |   
---|---|---|---|---  
  
Clears the config. 

## ◆ clearForeignMasterList()

void PTPPortData::clearForeignMasterList  | ( | | ) |   
---|---|---|---|---  
  
Removes all the foreign masters. 

## ◆ getAnnounceInterval()

int PTPPortData::getAnnounceInterval  | ( | | ) |   
---|---|---|---|---  
  
Gets the announcement interval time. 

Returns
    int, the announcement interval time. 

## ◆ getAnnounceReceiptTimeout()

int PTPPortData::getAnnounceReceiptTimeout  | ( | | ) |   
---|---|---|---|---  
  
Gets the announcement receipt timout time. 

Returns
    int, the announcement receipt timout time. 

## ◆ getAnnounceSeqNum()

double PTPPortData::getAnnounceSeqNum  | ( | | ) |   
---|---|---|---|---  
  
Gets the announce sequence number. 

Returns
    double, value is the announce sequence number. 

## ◆ getDecisionCode()

DecisionCode PTPPortData::getDecisionCode  | ( | | ) |   
---|---|---|---|---  
  
Gets the recommended port state. 

Returns
    enum<DecisionCode>, the profile type. Decision codes: None = 0, M1 = 1, M2 = 2, M3 = 3, P1 = 4, P2 = 5, S1 = 6 

## ◆ getDelayReqCounter()

int PTPPortData::getDelayReqCounter  | ( | | ) |   
---|---|---|---|---  
  
Gets delay request count. 

Returns
    int, the delay request count. 

## ◆ getDelayRequestInterval()

int PTPPortData::getDelayRequestInterval  | ( | | ) |   
---|---|---|---|---  
  
Gets the delay request interval. 

Returns
    int, the delay request interval time in seconds. 

## ◆ getLastGeneralEventSeqNum()

double PTPPortData::getLastGeneralEventSeqNum  | ( | | ) |   
---|---|---|---|---  
  
Gets the last general event sequence number. 

Returns
    double, value is the last sync sequence number. 

## ◆ getLastSyncSeqNum()

double PTPPortData::getLastSyncSeqNum  | ( | | ) |   
---|---|---|---|---  
  
Gets the last sync sequence number. 

Returns
    double, value is the last sync sequence number. 

## ◆ getPortState()

PortState PTPPortData::getPortState  | ( | | ) |   
---|---|---|---|---  
  
Gets the port state. 

Returns
    enum<PortState>, the profile type. [Port](class_port.html "Port holds and manipulates the ports on devices.") states: eFaulty = 0, eInit = 1, eDisabled = 2, eListening = 3, eUncalibrated = 4, ePreMaster = 5, eSlave = 6, eMaster = 7, ePassive = 8 

## ◆ getPortStateStr()

string PTPPortData::getPortStateStr  | ( | | ) |   
---|---|---|---|---  
  
Returns the profile as a string. 

Returns
    string, profile strings: "FAULTY", "INITIALIZING", "DISABLED", "LISTENING", "UNCALIBRATED", "PRE_MASTER", "SLAVE", "MASTER", "PASSIVE" 

## ◆ getPtpVersion()

int PTPPortData::getPtpVersion  | ( | | ) |   
---|---|---|---|---  
  
Gets ptp version. 

Returns
    int, version number. 

## ◆ getRecommendedPortState()

PortState PTPPortData::getRecommendedPortState  | ( | | ) |   
---|---|---|---|---  
  
Gets the recommended port state. 

Returns
    enum<PortState>, the profile type. [Port](class_port.html "Port holds and manipulates the ports on devices.") states: eFaulty = 0, eInit = 1, eDisabled = 2, eListening = 3, eUncalibrated = 4, ePreMaster = 5, eSlave = 6, eMaster = 7, ePassive = 8 

## ◆ getSyncInterval()

int PTPPortData::getSyncInterval  | ( | | ) |   
---|---|---|---|---  
  
Gets the sync interval time. 

Returns
    int, the sync interval time. 

## ◆ getSyncMsgCounter()

int PTPPortData::getSyncMsgCounter  | ( | | ) |   
---|---|---|---|---  
  
Gets the sync message counter. 

Returns
    int, value is the sync message count. 

## ◆ getSyncSeqNum()

double PTPPortData::getSyncSeqNum  | ( | | ) |   
---|---|---|---|---  
  
Gets the sync sequence number. 

Returns
    double, value is the sync message count. 

## ◆ getSyncWaitLimit()

int PTPPortData::getSyncWaitLimit  | ( | | ) |   
---|---|---|---|---  
  
Gets the sync interval wait limit. 

Returns
    int, the sync interval wait limit. 

## ◆ incrementDelayReqCounter()

void PTPPortData::incrementDelayReqCounter  | ( | | ) |   
---|---|---|---|---  
  
Increments the delay request counter. 

## ◆ incrementSyncMsgCounter()

void PTPPortData::incrementSyncMsgCounter  | ( | | ) |   
---|---|---|---|---  
  
Increments the sync message counter. 

## ◆ isBustEnabled()

bool PTPPortData::isBustEnabled  | ( | | ) |   
---|---|---|---|---  
  
Gets bust enabled state. 

Returns
    bool, returns true if bust is enabled, false if not. 

## ◆ isEBestSrc()

bool PTPPortData::isEBestSrc  | ( | | ) |   
---|---|---|---|---  
  
Check if this port data is the best source for grandmaster clock. 

Returns
    value, true if it is and false otherwise. 

## ◆ removeForeignMasterBySrcPortId()

bool PTPPortData::removeForeignMasterBySrcPortId  | ( | string  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Removes a foreign master by port. 

Parameters
     uuid,uuid| to find for.   
---|---  
portNum,port| to find for.  
  
Returns
    bool, value is true if the foreign master as removed, false if not. 

## ◆ resetDatasetToDefault()

void PTPPortData::resetDatasetToDefault  | ( | | ) |   
---|---|---|---|---  
  
Resets the data set to default. 

## ◆ setAnnounceInterval()

void PTPPortData::setAnnounceInterval  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the announcement interval time. 

Parameters
     num,the| time.   
---|---  
  
## ◆ setAnnounceReceiptTimeout()

void PTPPortData::setAnnounceReceiptTimeout  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the announcement receipt timout time. 

Parameters
     num,the| time.   
---|---  
  
## ◆ setAnnounceSeqNum()

void PTPPortData::setAnnounceSeqNum  | ( | double  | | ) |   
---|---|---|---|---|---  
  
Sets the announce sequence number counter. 

Parameters
     num,value| to use.   
---|---  
  
## ◆ setBustEnabled()

void PTPPortData::setBustEnabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Sets bust to be enabled or disabled. 

Parameters
     enable,true| to enable, false to disable.   
---|---  
  
## ◆ setDecisionCode()

void PTPPortData::setDecisionCode  | ( | DecisionCode  | | ) |   
---|---|---|---|---|---  
  
Sets the decision code. 

Parameters
     code,the| code to use. codes: None = 0, M1 = 1, M2 = 2, M3 = 3, P1 = 4, P2 = 5, S1 = 6   
---|---  
  
## ◆ setDelayReqCounter()

void PTPPortData::setDelayReqCounter  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the delay request counter. 

Parameters
     num,value| to use.   
---|---  
  
## ◆ setDelayRequestInterval()

void PTPPortData::setDelayRequestInterval  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the delay request interval. 

Parameters
     num,the| delay time in seconds   
---|---  
  
## ◆ setEBestSrc()

void PTPPortData::setEBestSrc  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Sets the port data to be or not to be the best source for grandmaster clock. 

Parameters
     value,true| if the port data is the best source for grandmaster clock and false otherwise.   
---|---  
  
## ◆ setLastGeneralEventSeqNum()

void PTPPortData::setLastGeneralEventSeqNum  | ( | double  | | ) |   
---|---|---|---|---|---  
  
Sets the last known general event sequence number. 

Parameters
     num,value| to use.   
---|---  
  
## ◆ setLastSyncSeqNum()

void PTPPortData::setLastSyncSeqNum  | ( | double  | | ) |   
---|---|---|---|---|---  
  
Sets the last sync sequence number. 

Parameters
     num,value| to use.   
---|---  
  
## ◆ setPortState()

void PTPPortData::setPortState  | ( | PortState  | | ) |   
---|---|---|---|---|---  
  
Sets the profile type. 

Parameters
     state,the| port state to use. states: eFaulty = 0, eInit = 1, eDisabled = 2, eListening = 3, eUncalibrated = 4, ePreMaster = 5, eSlave = 6, eMaster = 7, ePassive = 8   
---|---  
  
## ◆ setPtpVersion()

void PTPPortData::setPtpVersion  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets ptp version. 

Parameters
     num,version| number to use.   
---|---  
  
## ◆ setRecommendedPortState()

void PTPPortData::setRecommendedPortState  | ( | PortState  | | ) |   
---|---|---|---|---|---  
  
Sets the recommended port state. 

Parameters
     state,the| port state to use. states: eFaulty = 0, eInit = 1, eDisabled = 2, eListening = 3, eUncalibrated = 4, ePreMaster = 5, eSlave = 6, eMaster = 7, ePassive = 8   
---|---  
  
## ◆ setSyncInterval()

void PTPPortData::setSyncInterval  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the sync interval time. 

Parameters
     num,the| time.   
---|---  
  
## ◆ setSyncMsgCounter()

void PTPPortData::setSyncMsgCounter  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the sync message counter. 

Parameters
     value,value| to use.   
---|---  
  
## ◆ setSyncSeqNum()

void PTPPortData::setSyncSeqNum  | ( | double  | | ) |   
---|---|---|---|---|---  
  
Sets the sync sequence number. 

Parameters
     num,value| to use.   
---|---  
  
## ◆ setSyncWaitLimit()

void PTPPortData::setSyncWaitLimit  | ( | long  | | ) |   
---|---|---|---|---|---  
  
Sets the sync interval wait limit. 

Parameters
     num,the| wait.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CPTPPortData.pki](_c_p_t_p_port_data_8pki.html)


