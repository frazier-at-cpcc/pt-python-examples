# Cisco Packet Tracer Extensions API: CryptoMapSet Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_crypto_map_set.html

---

[CryptoMapSet](class_crypto_map_set.html "CryptoMapSet holds and manipulates crypto map sets.") holds and manipulates crypto map sets. [More...](class_crypto_map_set.html#details)

##  Public Member Functions  
  
---  
void | [setCryptoSetName](class_crypto_map_set.html#aa193f6b03ef04c04a5e34ac93f29ed80) (string)  
| Sets the name of this crypto map set. [More...](class_crypto_map_set.html#aa193f6b03ef04c04a5e34ac93f29ed80)  
  
string | [getCryptoSetName](class_crypto_map_set.html#a25ec187e001fd0e8cc52026cd7f8a823) ()  
| Returns the name of this crypto map set. [More...](class_crypto_map_set.html#a25ec187e001fd0e8cc52026cd7f8a823)  
  
void | [addCryptoMapSeqByNum](class_crypto_map_set.html#a4e6b6d88c6708443fbf6837476ff23cd) (int)  
| Adds a crypto map to this crypto map set with the specified sequence number. [More...](class_crypto_map_set.html#a4e6b6d88c6708443fbf6837476ff23cd)  
  
void | [removeCryptoMapSeqByNum](class_crypto_map_set.html#ad3564cd601faefaf4db1f180d13e2e99) (int)  
| Removes the crypto map from this crypto map set with the associated sequence number. [More...](class_crypto_map_set.html#ad3564cd601faefaf4db1f180d13e2e99)  
  
[CryptoMapSeq](class_crypto_map_seq.html) | [getCryptoMapSeqAt](class_crypto_map_set.html#a0045c5d62ba5030be856cf61518ee8d7) (int)  
| Returns the crypto map from this crypto map set at the specified index. [More...](class_crypto_map_set.html#a0045c5d62ba5030be856cf61518ee8d7)  
  
[CryptoMapSeq](class_crypto_map_seq.html) | [getCryptoSeqByNum](class_crypto_map_set.html#ad5318544b8e1e0253b7e91488babf2db) (int)  
| Returns the crypto map from this crypto map set with the associated sequence number. [More...](class_crypto_map_set.html#ad5318544b8e1e0253b7e91488babf2db)  
  
int | [getCryptoSeqCount](class_crypto_map_set.html#a8b761500749670c717b7a3c5e7bb6c98) ()  
| Returns the number of crypto maps in this crypto map set. [More...](class_crypto_map_set.html#a8b761500749670c717b7a3c5e7bb6c98)  
  
bool | [isSeqExisted](class_crypto_map_set.html#a57335dd60910e5686e1fb033514efcfd) (int)  
| Returns true if the crypto map with the associated sequence number exists in this crypto map, otherwise false. [More...](class_crypto_map_set.html#a57335dd60910e5686e1fb033514efcfd)  
  
int | [getFlowTableCount](class_crypto_map_set.html#a0fbb792d9ea3896f73efe7d4281c11ac) ()  
| Returns the number of flow tables in this crypto map set. [More...](class_crypto_map_set.html#a0fbb792d9ea3896f73efe7d4281c11ac)  
  
[FlowTable](class_flow_table.html) | [getTableAtIndex](class_crypto_map_set.html#a0a114133f71bf18ee51df2ed207617a2) (int)  
| Returns the flow table at the specified index. [More...](class_crypto_map_set.html#a0a114133f71bf18ee51df2ed207617a2)  
  
  
## Detailed Description

[CryptoMapSet](class_crypto_map_set.html "CryptoMapSet holds and manipulates crypto map sets.") holds and manipulates crypto map sets. 

## Member Function Documentation

## ◆ addCryptoMapSeqByNum()

void CryptoMapSet::addCryptoMapSeqByNum  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Adds a crypto map to this crypto map set with the specified sequence number. 

Parameters
     num,the| specified sequence number for the crypto map.   
---|---  
  
## ◆ getCryptoMapSeqAt()

[CryptoMapSeq](class_crypto_map_seq.html) CryptoMapSet::getCryptoMapSeqAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the crypto map from this crypto map set at the specified index. 

Parameters
     index,the| index of the crypto map of interest.  
---|---  
  
Returns
    [CryptoMapSeq](class_crypto_map_seq.html "CryptoMapSeq holds and manipulates crypto maps in a crypto map set."), the [CryptoMapSeq](class_crypto_map_seq.html "CryptoMapSeq holds and manipulates crypto maps in a crypto map set.") object at the specified index. 

## ◆ getCryptoSeqByNum()

[CryptoMapSeq](class_crypto_map_seq.html) CryptoMapSet::getCryptoSeqByNum  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the crypto map from this crypto map set with the associated sequence number. 

Parameters
     seqNum,the| sequence number of the crypto map of interest.  
---|---  
  
Returns
    [CryptoMapSeq](class_crypto_map_seq.html "CryptoMapSeq holds and manipulates crypto maps in a crypto map set."), the [CryptoMapSeq](class_crypto_map_seq.html "CryptoMapSeq holds and manipulates crypto maps in a crypto map set.") object with the associated sequence number. 

## ◆ getCryptoSeqCount()

int CryptoMapSet::getCryptoSeqCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of crypto maps in this crypto map set. 

Returns
    int, the number of crypto maps in this crypto map set. 

## ◆ getCryptoSetName()

string CryptoMapSet::getCryptoSetName  | ( | | ) |   
---|---|---|---|---  
  
Returns the name of this crypto map set. 

Returns
    string, the name of this crypto map set. 

## ◆ getFlowTableCount()

int CryptoMapSet::getFlowTableCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of flow tables in this crypto map set. 

Returns
    int, the number of flow tables in this crypto map set. 

## ◆ getTableAtIndex()

[FlowTable](class_flow_table.html) CryptoMapSet::getTableAtIndex  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the flow table at the specified index. 

Parameters
     index,the| index of the flow table of interest.  
---|---  
  
Returns
    [FlowTable](class_flow_table.html "FlowTable holds and manipulates the flow table."), the [FlowTable](class_flow_table.html "FlowTable holds and manipulates the flow table.") object at the specified index. 

## ◆ isSeqExisted()

bool CryptoMapSet::isSeqExisted  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns true if the crypto map with the associated sequence number exists in this crypto map, otherwise false. 

Parameters
     seqNum,the| sequence number of the crypto map of interest.  
---|---  
  
Returns
    bool, true if the crypto map with the associated sequence number exists in this crypto map, otherwise false. 

## ◆ removeCryptoMapSeqByNum()

void CryptoMapSet::removeCryptoMapSeqByNum  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Removes the crypto map from this crypto map set with the associated sequence number. 

Parameters
     num,the| associated sequence number of the crypto map.   
---|---  
  
## ◆ setCryptoSetName()

void CryptoMapSet::setCryptoSetName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the name of this crypto map set. 

Parameters
     string,the| name to set on this crypto map set.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CCryptoMapSet.pki](_c_crypto_map_set_8pki.html)


