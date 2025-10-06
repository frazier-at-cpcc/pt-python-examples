# Cisco Packet Tracer Extensions API: IpsecProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_ipsec_process.html

---

[IpsecProcess](class_ipsec_process.html "IpsecProcess is the process that handles IPSec.") is the process that handles IPSec. [More...](class_ipsec_process.html#details)

##  Public Member Functions  
  
---  
int | [getGlobalLifeTime](class_ipsec_process.html#af093c21f8c3fc4e240fab8ac6bc021fc) ()  
| Returns the global lifetime for encryption. [More...](class_ipsec_process.html#af093c21f8c3fc4e240fab8ac6bc021fc)  
  
void | [setGlobalLifeTime](class_ipsec_process.html#ab417624908ff96b0f3558b10f413dbbe) (int)  
| Sets the global lifetime for encryption. [More...](class_ipsec_process.html#ab417624908ff96b0f3558b10f413dbbe)  
  
int | [getCryptoMapSetCount](class_ipsec_process.html#afd0d9095e5ddf37008e575981448b927) ()  
| Returns the number of crypto map sets. [More...](class_ipsec_process.html#afd0d9095e5ddf37008e575981448b927)  
  
[CryptoMapSet](class_crypto_map_set.html) | [getCryptoMapSetAt](class_ipsec_process.html#ab25cbfcaea0737514197c637ea2e3c28) (int)  
| Returns the crypto map set at the specified index. [More...](class_ipsec_process.html#ab25cbfcaea0737514197c637ea2e3c28)  
  
void | [addCryptoMapSetByNameSeq](class_ipsec_process.html#a38e93bb5a3b5b567ccf36bf4880421b8) (string, int)  
| Adds a crypto map set with the specified name and sequence number. [More...](class_ipsec_process.html#a38e93bb5a3b5b567ccf36bf4880421b8)  
  
int | [getTransformSetCount](class_ipsec_process.html#aa735a53d11b5bb6b09bd5d19c67001ad) ()  
| Returns the number of transform sets. [More...](class_ipsec_process.html#aa735a53d11b5bb6b09bd5d19c67001ad)  
  
[TransformSet](class_transform_set.html) | [getTransformSetAt](class_ipsec_process.html#a1bc577e0be1a5e0ed83da97534228f90) (int)  
| Returns the transform set at the specified index. [More...](class_ipsec_process.html#a1bc577e0be1a5e0ed83da97534228f90)  
  
[TransformSet](class_transform_set.html) | [getTransformSetbyName](class_ipsec_process.html#a9aaba249c7271d23ffcbf4e1b64fe800) (string)  
| Returns the transform set with the specified name. [More...](class_ipsec_process.html#a9aaba249c7271d23ffcbf4e1b64fe800)  
  
void | [addTransformSetByName](class_ipsec_process.html#a0aac1732001c73e0832824d974f10b0c) (string)  
| Adds a transform set with the specified name. [More...](class_ipsec_process.html#a0aac1732001c73e0832824d974f10b0c)  
  
void | [removeTransformSetByName](class_ipsec_process.html#a8d1cd830862514996213657e30d80c8f) (string)  
| Removes the transform set with the specified name. [More...](class_ipsec_process.html#a8d1cd830862514996213657e30d80c8f)  
  
bool | [isTransformSetUsedByMap](class_ipsec_process.html#a4e0e94795e53b20f3207e8077506e195) (string)  
| Returns true if the specified transform set is used by the crypto map, otherwise false. [More...](class_ipsec_process.html#a4e0e94795e53b20f3207e8077506e195)  
  
int | [getIkePolicyCount](class_ipsec_process.html#acd966abdf5673d81ef5852cc8850b9a3) ()  
| Returns the number of IKE policies. [More...](class_ipsec_process.html#acd966abdf5673d81ef5852cc8850b9a3)  
  
[IkePolicy](class_ike_policy.html) | [getIkePolicyAt](class_ipsec_process.html#aff5c8ec84003c32eac8f0b5f4099dbcc) (int)  
| Returns IKE policy at the specified index. [More...](class_ipsec_process.html#aff5c8ec84003c32eac8f0b5f4099dbcc)  
  
int | [getTunnelGrpCount](class_ipsec_process.html#a8fef0d0c3ea35347149efc5310fd5d28) ()  
| Returns the number of Tunnel Group. [More...](class_ipsec_process.html#a8fef0d0c3ea35347149efc5310fd5d28)  
  
[TunnelGroup](class_tunnel_group.html) | [getTunnelGrpByName](class_ipsec_process.html#a1e32984ab34b7098b3e9ea942700830d) (string)  
| gets the tunnel group with the specified name. [More...](class_ipsec_process.html#a1e32984ab34b7098b3e9ea942700830d)  
  
void | [addTunnelGrpByName](class_ipsec_process.html#aeedab6fdcc56dc885e6442934c1993f0) (string)  
| Adds a Tunnel Group with the specified name. [More...](class_ipsec_process.html#aeedab6fdcc56dc885e6442934c1993f0)  
  
void | [removeTunnelGrpByName](class_ipsec_process.html#a80dcd31f1582734b2428ca7a1994bdd7) (string)  
| Removes the Tunnel Group with the specified name. [More...](class_ipsec_process.html#a80dcd31f1582734b2428ca7a1994bdd7)  
  
[TunnelGroup](class_tunnel_group.html) | [getTunnelGrpAt](class_ipsec_process.html#aef0c40a523e2eaf5aa7a651dff98e4a9) (int)  
| Returns Tunnel Group at the specified index. [More...](class_ipsec_process.html#aef0c40a523e2eaf5aa7a651dff98e4a9)  
  
int | [getCryptoMapSetV6Count](class_ipsec_process.html#aad81ec5a7a6d98314351a54810c57aca) ()  
| Returns the number of crypto map sets. [More...](class_ipsec_process.html#aad81ec5a7a6d98314351a54810c57aca)  
  
[CryptoMapSet](class_crypto_map_set.html) | [getCryptoMapSetV6At](class_ipsec_process.html#af24370d14048b42bb6832c9be15aafb3) (int)  
| Returns the crypto map set at the specified index. [More...](class_ipsec_process.html#af24370d14048b42bb6832c9be15aafb3)  
  
void | [addCryptoMapSetByNameSeqV6](class_ipsec_process.html#a0750e6e70e9826c3806bed7ef883a4e4) (string, int)  
| Adds a crypto map set with the specified name and sequence number. [More...](class_ipsec_process.html#a0750e6e70e9826c3806bed7ef883a4e4)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[IpsecProcess](class_ipsec_process.html "IpsecProcess is the process that handles IPSec.") is the process that handles IPSec. 

## Member Function Documentation

## ◆ addCryptoMapSetByNameSeq()

void IpsecProcess::addCryptoMapSetByNameSeq  | ( | string  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Adds a crypto map set with the specified name and sequence number. 

Parameters
     name,the| name of the crypto map set.   
---|---  
sequence,the| sequence number of the crypto map set.   
  
## ◆ addCryptoMapSetByNameSeqV6()

void IpsecProcess::addCryptoMapSetByNameSeqV6  | ( | string  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Adds a crypto map set with the specified name and sequence number. 

Parameters
     name,the| name of the crypto map set.   
---|---  
sequence,the| sequence number of the crypto map set.   
  
## ◆ addTransformSetByName()

void IpsecProcess::addTransformSetByName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Adds a transform set with the specified name. 

Parameters
     name,the| name for the transform set.   
---|---  
  
## ◆ addTunnelGrpByName()

void IpsecProcess::addTunnelGrpByName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Adds a Tunnel Group with the specified name. 

Parameters
     name,the| name for the Tunnel Group .   
---|---  
  
## ◆ getCryptoMapSetAt()

[CryptoMapSet](class_crypto_map_set.html) IpsecProcess::getCryptoMapSetAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the crypto map set at the specified index. 

Parameters
     index,the| index of the crypto map set of interest.  
---|---  
  
Returns
    [CryptoMapSet](class_crypto_map_set.html "CryptoMapSet holds and manipulates crypto map sets."), the [CryptoMapSet](class_crypto_map_set.html "CryptoMapSet holds and manipulates crypto map sets.") object at the specified index. 

## ◆ getCryptoMapSetCount()

int IpsecProcess::getCryptoMapSetCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of crypto map sets. 

Returns
    int, the number of crypto map sets. 

## ◆ getCryptoMapSetV6At()

[CryptoMapSet](class_crypto_map_set.html) IpsecProcess::getCryptoMapSetV6At  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the crypto map set at the specified index. 

Parameters
     index,the| index of the crypto map set of interest.  
---|---  
  
Returns
    [CryptoMapSet](class_crypto_map_set.html "CryptoMapSet holds and manipulates crypto map sets."), the [CryptoMapSet](class_crypto_map_set.html "CryptoMapSet holds and manipulates crypto map sets.") object at the specified index. 

## ◆ getCryptoMapSetV6Count()

int IpsecProcess::getCryptoMapSetV6Count  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of crypto map sets. 

Returns
    int, the number of crypto map sets. 

## ◆ getGlobalLifeTime()

int IpsecProcess::getGlobalLifeTime  | ( | | ) |   
---|---|---|---|---  
  
Returns the global lifetime for encryption. 

Returns
    int, the global lifetime for encryption. 

## ◆ getIkePolicyAt()

[IkePolicy](class_ike_policy.html) IpsecProcess::getIkePolicyAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns IKE policy at the specified index. 

Parameters
     index,the| index of the IKE policy of interest.  
---|---  
  
Returns
    [IkePolicy](class_ike_policy.html "IkePolicy handles and manipulates IKE policies."), the [IkePolicy](class_ike_policy.html "IkePolicy handles and manipulates IKE policies.") object at the specified index. 

## ◆ getIkePolicyCount()

int IpsecProcess::getIkePolicyCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of IKE policies. 

Returns
    int, the number of IKE policies. 

## ◆ getTransformSetAt()

[TransformSet](class_transform_set.html) IpsecProcess::getTransformSetAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the transform set at the specified index. 

Parameters
     index,the| index of the transform set of interest.  
---|---  
  
Returns
    [TransformSet](class_transform_set.html "TransformSet handles and manipulates IPSec transform sets."), the [TransformSet](class_transform_set.html "TransformSet handles and manipulates IPSec transform sets.") object at the specified index. 

## ◆ getTransformSetbyName()

[TransformSet](class_transform_set.html) IpsecProcess::getTransformSetbyName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the transform set with the specified name. 

Parameters
     name,the| name of the transform set of interest.  
---|---  
  
Returns
    [TransformSet](class_transform_set.html "TransformSet handles and manipulates IPSec transform sets."), the [TransformSet](class_transform_set.html "TransformSet handles and manipulates IPSec transform sets.") object with the specified name. 

## ◆ getTransformSetCount()

int IpsecProcess::getTransformSetCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of transform sets. 

Returns
    int, the number of transform sets. 

## ◆ getTunnelGrpAt()

[TunnelGroup](class_tunnel_group.html) IpsecProcess::getTunnelGrpAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns Tunnel Group at the specified index. 

Parameters
     index,the| index of the Tunnel Group of interest.  
---|---  
  
Returns
    Tunnel Group, the Tunnel Group object at the specified index. 

## ◆ getTunnelGrpByName()

[TunnelGroup](class_tunnel_group.html) IpsecProcess::getTunnelGrpByName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
gets the tunnel group with the specified name. 

Parameters
     name,the| name for the tunnelGroup.   
---|---  
  
## ◆ getTunnelGrpCount()

int IpsecProcess::getTunnelGrpCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of Tunnel Group. 

Returns
    int, the number of Tunnel Group. 

## ◆ isTransformSetUsedByMap()

bool IpsecProcess::isTransformSetUsedByMap  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns true if the specified transform set is used by the crypto map, otherwise false. 

Parameters
     name,the| name of the transform set of interest.  
---|---  
  
Returns
    bool, true if the specified transform set is used by the crypto map, otherwise false. 

## ◆ removeTransformSetByName()

void IpsecProcess::removeTransformSetByName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes the transform set with the specified name. 

Parameters
     name,the| name for the transform set.   
---|---  
  
## ◆ removeTunnelGrpByName()

void IpsecProcess::removeTunnelGrpByName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes the Tunnel Group with the specified name. 

Parameters
     name,the| name for the Tunnel Group.   
---|---  
  
## ◆ setGlobalLifeTime()

void IpsecProcess::setGlobalLifeTime  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the global lifetime for encryption. 

Parameters
     lifetime,the| global lifetime for encryption.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CIpsecProcess.pki](_c_ipsec_process_8pki.html)


