# Cisco Packet Tracer Extensions API: ProposalPayload Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_proposal_payload.html

---

Proposal payload structure. [More...](struct_proposal_payload.html#details)

##  Public Attributes  
  
---  
byte | [proposalNumber](struct_proposal_payload.html#a7be539d7ab225e670e1be9fe794cfac0)  
byte | [proposalId](struct_proposal_payload.html#a944c8d18c5e43e4b50655d9628da614f)  
vector< [TransformPayload](struct_transform_payload.html) > | [transformList](struct_proposal_payload.html#a90144cd897d7369be330ec291ae32228)  
byte | [spiSize](struct_proposal_payload.html#a0d0a4996fd4d9fd2bc27a18cd276b56c)  
byte | [numTransforms](struct_proposal_payload.html#a84dd7ee7c8648281359195c5ba2921ce)  
int | [spi](struct_proposal_payload.html#a9aa780bc38b1ea72c8f53b320a1944c9)  
int | [inSpi](struct_proposal_payload.html#aedd8e5a60eb804efe29a6e01f815a311)  
Public Attributes inherited from [IkePayload](struct_ike_payload.html)  
short | [length](struct_ike_payload.html#af91b522ca65dd50a8af9b2f184768372)  
byte | [reserved](struct_ike_payload.html#af4c12fe68fea6002842f87efd8b3467d)  
byte | [nextPayloadType](struct_ike_payload.html#aee8173dae0eb91256f1763af6ff74900)  
  
## Detailed Description

Proposal payload structure. 

## Member Data Documentation

## ◆ inSpi

int ProposalPayload::inSpi  
---  
  
## ◆ numTransforms

byte ProposalPayload::numTransforms  
---  
  
## ◆ proposalId

byte ProposalPayload::proposalId  
---  
  
## ◆ proposalNumber

byte ProposalPayload::proposalNumber  
---  
  
## ◆ spi

int ProposalPayload::spi  
---  
  
## ◆ spiSize

byte ProposalPayload::spiSize  
---  
  
## ◆ transformList

vector<[TransformPayload](struct_transform_payload.html)> ProposalPayload::transformList  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [CProposalPayload.pki](_c_proposal_payload_8pki.html)


