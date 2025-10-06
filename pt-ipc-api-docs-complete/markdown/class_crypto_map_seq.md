# Cisco Packet Tracer Extensions API: CryptoMapSeq Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_crypto_map_seq.html

---

[CryptoMapSeq](class_crypto_map_seq.html "CryptoMapSeq holds and manipulates crypto maps in a crypto map set.") holds and manipulates crypto maps in a crypto map set. [More...](class_crypto_map_seq.html#details)

##  Public Member Functions  
  
---  
int | [getSeqNum](class_crypto_map_seq.html#a9f50a42defa94ec6d645c94ec42fb0a9) ()  
| Returns the sequence number of this crypto map. [More...](class_crypto_map_seq.html#a9f50a42defa94ec6d645c94ec42fb0a9)  
  
bool | [isIncomplete](class_crypto_map_seq.html#afba1fba2f08e8cfb2f02cbf278aa94b4) ()  
| Returns true if this crypto map is incomplete, otherwise false. [More...](class_crypto_map_seq.html#afba1fba2f08e8cfb2f02cbf278aa94b4)  
  
void | [setMatchAdd](class_crypto_map_seq.html#a64a481983adcf935542ba31eac5222ef) (string)  
| Sets the match for this crypto map. [More...](class_crypto_map_seq.html#a64a481983adcf935542ba31eac5222ef)  
  
string | [getMatchAdd](class_crypto_map_seq.html#ab9ec1dafa00308600bd662c3e2723a37) ()  
| Returns the match for this crypto map. [More...](class_crypto_map_seq.html#ab9ec1dafa00308600bd662c3e2723a37)  
  
void | [setSaLifeTime](class_crypto_map_seq.html#ae31eae4166d57cb3b798640ed8d98387) (int)  
| Sets the IPSec SA lifetime. [More...](class_crypto_map_seq.html#ae31eae4166d57cb3b798640ed8d98387)  
  
int | [getSaLifeTime](class_crypto_map_seq.html#a342ebe5af3a1236b25521b08e0b7605e) ()  
| Returns the IPSec SA lifetime. [More...](class_crypto_map_seq.html#a342ebe5af3a1236b25521b08e0b7605e)  
  
  
## Detailed Description

[CryptoMapSeq](class_crypto_map_seq.html "CryptoMapSeq holds and manipulates crypto maps in a crypto map set.") holds and manipulates crypto maps in a crypto map set. 

## Member Function Documentation

## ◆ getMatchAdd()

string CryptoMapSeq::getMatchAdd  | ( | | ) |   
---|---|---|---|---  
  
Returns the match for this crypto map. 

Returns
    string, the match for this crypto map. 

## ◆ getSaLifeTime()

int CryptoMapSeq::getSaLifeTime  | ( | | ) |   
---|---|---|---|---  
  
Returns the IPSec SA lifetime. 

Returns
    int, the IPSec SA lifetime. 

## ◆ getSeqNum()

int CryptoMapSeq::getSeqNum  | ( | | ) |   
---|---|---|---|---  
  
Returns the sequence number of this crypto map. 

Returns
    int, the sequence number of this crypto map. 

## ◆ isIncomplete()

bool CryptoMapSeq::isIncomplete  | ( | | ) |   
---|---|---|---|---  
  
Returns true if this crypto map is incomplete, otherwise false. 

Returns
    bool, true if this crypto map is incomplete, otherwise false. 

## ◆ setMatchAdd()

void CryptoMapSeq::setMatchAdd  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the match for this crypto map. 

Parameters
     string,the| match to set for this crypto map.   
---|---  
  
## ◆ setSaLifeTime()

void CryptoMapSeq::setSaLifeTime  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the IPSec SA lifetime. 

Parameters
     int,the| IPSec SA lifetime to set.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CCryptoMapSeq.pki](_c_crypto_map_seq_8pki.html)


