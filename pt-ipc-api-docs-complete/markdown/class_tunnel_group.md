# Cisco Packet Tracer Extensions API: TunnelGroup Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_tunnel_group.html

---

[TunnelGroup](class_tunnel_group.html "TunnelGroup handles and manipulates IKE Tunnel Groups.") handles and manipulates IKE Tunnel Groups. [More...](class_tunnel_group.html#details)

##  Public Member Functions  
  
---  
string | [getName](class_tunnel_group.html#ad9ac3b5502533b7433c923febbd63865) ()  
| Returns the Name for the tunnelgroup. [More...](class_tunnel_group.html#ad9ac3b5502533b7433c923febbd63865)  
  
void | [setName](class_tunnel_group.html#a21837ec2a2141144431d653a77615215) (string)  
| Sets the name for the tunnelgroup. [More...](class_tunnel_group.html#a21837ec2a2141144431d653a77615215)  
  
[TunnelIpsecAttribute](class_tunnel_ipsec_attribute.html) | [getTunnelIpsecAtt](class_tunnel_group.html#a3adf7a121f84da81aa6ae0c9c129e0de) ()  
| Returns [TunnelIpsecAttribute](class_tunnel_ipsec_attribute.html "This class holds the Ipsec Tunnel Attributes.") . [More...](class_tunnel_group.html#a3adf7a121f84da81aa6ae0c9c129e0de)  
  
void | [setTunnelIpsecAtt](class_tunnel_group.html#a75e950fe46b0c6b6f9e3de3a5da68d0c) ([TunnelIpsecAttribute](class_tunnel_ipsec_attribute.html))  
| sets CTunnelIpsecAttribute. [More...](class_tunnel_group.html#a75e950fe46b0c6b6f9e3de3a5da68d0c)  
  
TunnelType | [getType](class_tunnel_group.html#a022fca93b75df5fabab247fb52d35be5) ()  
| Return the tunnel type in enum eRemoteAccess = 0, eL2L = 1, eTunnelTypeNone = 2, eWebVpn = 3. [More...](class_tunnel_group.html#a022fca93b75df5fabab247fb52d35be5)  
  
string | [getTypeString](class_tunnel_group.html#ab1da12690a15ded8aa5140d0785d5f30) ()  
| Return the tunnel type in string format. [More...](class_tunnel_group.html#ab1da12690a15ded8aa5140d0785d5f30)  
  
void | [setType](class_tunnel_group.html#ace8c6e1a966ef25c3f6c49cd4c807621) (TunnelType)  
| Set the tunnel type in enum. [More...](class_tunnel_group.html#ace8c6e1a966ef25c3f6c49cd4c807621)  
  
[TunnelGeneralAttributes](class_tunnel_general_attributes.html) | [getGeneralAttributes](class_tunnel_group.html#a1abe0e9e64924805dc144cb4b7f03e4c) ()  
| Returns [TunnelGeneralAttributes](class_tunnel_general_attributes.html "This class holds the General Tunnel Attributes.") . [More...](class_tunnel_group.html#a1abe0e9e64924805dc144cb4b7f03e4c)  
  
[TunnelGeneralAttributes](class_tunnel_general_attributes.html) | [createGeneralAttributes](class_tunnel_group.html#ae10902a5eef0bb18a2cbe4f2faf1a41d) ()  
| Create [TunnelGeneralAttributes](class_tunnel_general_attributes.html "This class holds the General Tunnel Attributes.") . [More...](class_tunnel_group.html#ae10902a5eef0bb18a2cbe4f2faf1a41d)  
  
void | [removeGeneralAttributes](class_tunnel_group.html#af46a6f39300938ff0d10835b11211be5) ()  
| Remove [TunnelGeneralAttributes](class_tunnel_general_attributes.html "This class holds the General Tunnel Attributes.") . [More...](class_tunnel_group.html#af46a6f39300938ff0d10835b11211be5)  
  
  
## Detailed Description

[TunnelGroup](class_tunnel_group.html "TunnelGroup handles and manipulates IKE Tunnel Groups.") handles and manipulates IKE Tunnel Groups. 

## Member Function Documentation

## ◆ createGeneralAttributes()

[TunnelGeneralAttributes](class_tunnel_general_attributes.html) TunnelGroup::createGeneralAttributes  | ( | | ) |   
---|---|---|---|---  
  
Create [TunnelGeneralAttributes](class_tunnel_general_attributes.html "This class holds the General Tunnel Attributes.") . 

Returns
    [TunnelGeneralAttributes](class_tunnel_general_attributes.html "This class holds the General Tunnel Attributes."), the newly created [TunnelGeneralAttributes](class_tunnel_general_attributes.html "This class holds the General Tunnel Attributes.") object. 

## ◆ getGeneralAttributes()

[TunnelGeneralAttributes](class_tunnel_general_attributes.html) TunnelGroup::getGeneralAttributes  | ( | | ) |   
---|---|---|---|---  
  
Returns [TunnelGeneralAttributes](class_tunnel_general_attributes.html "This class holds the General Tunnel Attributes.") . 

Returns
    [TunnelGeneralAttributes](class_tunnel_general_attributes.html "This class holds the General Tunnel Attributes."), the CTunnelGeneralAttributes object. 

## ◆ getName()

string TunnelGroup::getName  | ( | | ) |   
---|---|---|---|---  
  
Returns the Name for the tunnelgroup. 

Returns
    string. 

## ◆ getTunnelIpsecAtt()

[TunnelIpsecAttribute](class_tunnel_ipsec_attribute.html) TunnelGroup::getTunnelIpsecAtt  | ( | | ) |   
---|---|---|---|---  
  
Returns [TunnelIpsecAttribute](class_tunnel_ipsec_attribute.html "This class holds the Ipsec Tunnel Attributes.") . 

Returns
    [TunnelIpsecAttribute](class_tunnel_ipsec_attribute.html "This class holds the Ipsec Tunnel Attributes."), the CTunnelIpsecAttribute object. 

## ◆ getType()

TunnelType TunnelGroup::getType  | ( | | ) |   
---|---|---|---|---  
  
Return the tunnel type in enum eRemoteAccess = 0, eL2L = 1, eTunnelTypeNone = 2, eWebVpn = 3. 

## ◆ getTypeString()

string TunnelGroup::getTypeString  | ( | | ) |   
---|---|---|---|---  
  
Return the tunnel type in string format. 

## ◆ removeGeneralAttributes()

void TunnelGroup::removeGeneralAttributes  | ( | | ) |   
---|---|---|---|---  
  
Remove [TunnelGeneralAttributes](class_tunnel_general_attributes.html "This class holds the General Tunnel Attributes.") . 

Returns
    none 

## ◆ setName()

void TunnelGroup::setName  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the name for the tunnelgroup. 

Parameters
     string.|   
---|---  
  
## ◆ setTunnelIpsecAtt()

void TunnelGroup::setTunnelIpsecAtt  | ( | [TunnelIpsecAttribute](class_tunnel_ipsec_attribute.html) | | ) |   
---|---|---|---|---|---  
  
sets CTunnelIpsecAttribute. 

Parameters
     tunnelIpsecAtt,the| CTunnelIpsecAttribute object.   
---|---  
  
## ◆ setType()

void TunnelGroup::setType  | ( | TunnelType  | | ) |   
---|---|---|---|---|---  
  
Set the tunnel type in enum. 

Parameters
     type| eRemoteAccess = 0, eL2L = 1, eTunnelTypeNone = 2, eWebVpn = 3   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CTunnelGroup.pki](_c_tunnel_group_8pki.html)


