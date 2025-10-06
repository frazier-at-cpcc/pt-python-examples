# Cisco Packet Tracer Extensions API: IpsecSaGroup Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_ipsec_sa_group.html

---

[IpsecSaGroup](class_ipsec_sa_group.html "IpsecSaGroup handles and manipulates IPSec SA groups.") handles and manipulates IPSec SA groups. [More...](class_ipsec_sa_group.html#details)

##  Public Member Functions  
  
---  
[IpsecSa](class_ipsec_sa.html) | [getEspOutbound](class_ipsec_sa_group.html#a4fe8bc6a593dc5f633fa2b4e91619add) ()  
| Returns the ESP outbound IPSec SA. [More...](class_ipsec_sa_group.html#a4fe8bc6a593dc5f633fa2b4e91619add)  
  
[IpsecSa](class_ipsec_sa.html) | [getEspInbound](class_ipsec_sa_group.html#a1c3b3ef5a2b34214e7b84e61e54b635c) ()  
| Returns the ESP inbound IPSec SA. [More...](class_ipsec_sa_group.html#a1c3b3ef5a2b34214e7b84e61e54b635c)  
  
[IpsecSa](class_ipsec_sa.html) | [getAhOutbound](class_ipsec_sa_group.html#a24ff8dbdb34d5f994eb24f8107d406c8) ()  
| Returns the AH outbound IPSec SA. [More...](class_ipsec_sa_group.html#a24ff8dbdb34d5f994eb24f8107d406c8)  
  
[IpsecSa](class_ipsec_sa.html) | [getAhInbound](class_ipsec_sa_group.html#ab07248d51275750349dea846a47a16f5) ()  
| Returns the AH inbound IPSec SA. [More...](class_ipsec_sa_group.html#ab07248d51275750349dea846a47a16f5)  
  
int | [getLifeTime](class_ipsec_sa_group.html#a3870d5c1fcf40ce1443304ca68300533) ()  
| Returns the lifetime for the IPSec SA group. [More...](class_ipsec_sa_group.html#a3870d5c1fcf40ce1443304ca68300533)  
  
  
## Detailed Description

[IpsecSaGroup](class_ipsec_sa_group.html "IpsecSaGroup handles and manipulates IPSec SA groups.") handles and manipulates IPSec SA groups. 

## Member Function Documentation

## ◆ getAhInbound()

[IpsecSa](class_ipsec_sa.html) IpsecSaGroup::getAhInbound  | ( | | ) |   
---|---|---|---|---  
  
Returns the AH inbound IPSec SA. 

Returns
    [IpsecSa](class_ipsec_sa.html "IpsecSa handles and manipulates IPSec SAs."), the [IpsecSa](class_ipsec_sa.html "IpsecSa handles and manipulates IPSec SAs.") object for the AH inbound IPSec SA. 

## ◆ getAhOutbound()

[IpsecSa](class_ipsec_sa.html) IpsecSaGroup::getAhOutbound  | ( | | ) |   
---|---|---|---|---  
  
Returns the AH outbound IPSec SA. 

Returns
    [IpsecSa](class_ipsec_sa.html "IpsecSa handles and manipulates IPSec SAs."), the [IpsecSa](class_ipsec_sa.html "IpsecSa handles and manipulates IPSec SAs.") object for the AH outbound IPSec SA. 

## ◆ getEspInbound()

[IpsecSa](class_ipsec_sa.html) IpsecSaGroup::getEspInbound  | ( | | ) |   
---|---|---|---|---  
  
Returns the ESP inbound IPSec SA. 

Returns
    [IpsecSa](class_ipsec_sa.html "IpsecSa handles and manipulates IPSec SAs."), the [IpsecSa](class_ipsec_sa.html "IpsecSa handles and manipulates IPSec SAs.") object for the ESP inbound IPSec SA. 

## ◆ getEspOutbound()

[IpsecSa](class_ipsec_sa.html) IpsecSaGroup::getEspOutbound  | ( | | ) |   
---|---|---|---|---  
  
Returns the ESP outbound IPSec SA. 

Returns
    [IpsecSa](class_ipsec_sa.html "IpsecSa handles and manipulates IPSec SAs."), the [IpsecSa](class_ipsec_sa.html "IpsecSa handles and manipulates IPSec SAs.") object for the ESP outbound IPSec SA. 

## ◆ getLifeTime()

int IpsecSaGroup::getLifeTime  | ( | | ) |   
---|---|---|---|---  
  
Returns the lifetime for the IPSec SA group. 

Returns
    int, the lifetime for the IPSec SA group. 

* * *

The documentation for this class was generated from the following file:

  * [CIpsecSaGroup.pki](_c_ipsec_sa_group_8pki.html)


