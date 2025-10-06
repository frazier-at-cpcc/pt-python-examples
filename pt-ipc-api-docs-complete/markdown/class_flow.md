# Cisco Packet Tracer Extensions API: Flow Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_flow.html

---

[Flow](class_flow.html "Flow holds and manipulates the flow routes in FlowTable objects.") holds and manipulates the flow routes in [FlowTable](class_flow_table.html "FlowTable holds and manipulates the flow table.") objects. [More...](class_flow.html#details)

##  Public Member Functions  
  
---  
int | [getPeerCount](class_flow.html#a6611805e232f7a68fdf1a731004662d6) ()  
| Returns the number of peers. [More...](class_flow.html#a6611805e232f7a68fdf1a731004662d6)  
  
[IpsecPeer](class_ipsec_peer.html) | [getPeerAt](class_flow.html#afe5a39a4e28a091573d10ce178c3569e) (int)  
| Returns the peer at the specified index. [More...](class_flow.html#afe5a39a4e28a091573d10ce178c3569e)  
  
[IpsecPeer](class_ipsec_peer.html) | [getPeerByIp](class_flow.html#a8484025e581fa62a4954c7f711d25a10) (ip)  
| Returns the peer with the specified IP address. [More...](class_flow.html#a8484025e581fa62a4954c7f711d25a10)  
  
  
## Detailed Description

[Flow](class_flow.html "Flow holds and manipulates the flow routes in FlowTable objects.") holds and manipulates the flow routes in [FlowTable](class_flow_table.html "FlowTable holds and manipulates the flow table.") objects. 

## Member Function Documentation

## ◆ getPeerAt()

[IpsecPeer](class_ipsec_peer.html) Flow::getPeerAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the peer at the specified index. 

Parameters
     index,the| index of the peer of interest.  
---|---  
  
Returns
    [IpsecPeer](class_ipsec_peer.html "IpsecPeer handles and manipulates IPSec peers."), the [IpsecPeer](class_ipsec_peer.html "IpsecPeer handles and manipulates IPSec peers.") object at the specified index. 

## ◆ getPeerByIp()

[IpsecPeer](class_ipsec_peer.html) Flow::getPeerByIp  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Returns the peer with the specified IP address. 

Parameters
     addr,the| IP address of the peer of interest.  
---|---  
  
Returns
    [IpsecPeer](class_ipsec_peer.html "IpsecPeer handles and manipulates IPSec peers."), the [IpsecPeer](class_ipsec_peer.html "IpsecPeer handles and manipulates IPSec peers.") object with the specified IP address. 

## ◆ getPeerCount()

int Flow::getPeerCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of peers. 

Returns
    int, the number of peers. 

* * *

The documentation for this class was generated from the following file:

  * [CFlow.pki](_c_flow_8pki.html)


