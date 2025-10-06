# Cisco Packet Tracer Extensions API: BgpUpdate Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_bgp_update.html

---

BGP Update message structure. [More...](struct_bgp_update.html#details)

##  Public Attributes  
  
---  
short | [unfeasibleLength](struct_bgp_update.html#a05c2df19258b1fa29c1dcfe56ce9266c)  
vector< [BgpPrefix](struct_bgp_prefix.html) > | [withdrawnRoutes](struct_bgp_update.html#abf9a7f8b4d69e22b0d028730b14c4943)  
short | [pathAttributeLength](struct_bgp_update.html#ac4b08200cf99ca8b55f4253d877418d7)  
vector< [BgpAttribute](struct_bgp_attribute.html) > | [pathAttributes](struct_bgp_update.html#a3bc8dbc8f3d4423a1aaff1e817dc4691)  
vector< [BgpPrefix](struct_bgp_prefix.html) > | [NLRI](struct_bgp_update.html#aea2b22954d69ba52b794e5b850fcf064)  
Public Attributes inherited from [BgpPacket](struct_bgp_packet.html)  
short | [length](struct_bgp_packet.html#a7c44da47a5e4e3eb2cbf37485a0c272d)  
byte | [type](struct_bgp_packet.html#af14d757cacf0e029691f4a77f6e1e431)  
  
## Detailed Description

BGP Update message structure. 

## Member Data Documentation

## ◆ NLRI

vector<[BgpPrefix](struct_bgp_prefix.html)> BgpUpdate::NLRI  
---  
  
## ◆ pathAttributeLength

short BgpUpdate::pathAttributeLength  
---  
  
## ◆ pathAttributes

vector<[BgpAttribute](struct_bgp_attribute.html)> BgpUpdate::pathAttributes  
---  
  
## ◆ unfeasibleLength

short BgpUpdate::unfeasibleLength  
---  
  
## ◆ withdrawnRoutes

vector<[BgpPrefix](struct_bgp_prefix.html)> BgpUpdate::withdrawnRoutes  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [CBgpUpdate.pki](_c_bgp_update_8pki.html)


