# Cisco Packet Tracer Extensions API: Ipv6IpProcess Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_ipv6_ip_process.html

---

[Ipv6IpProcess](class_ipv6_ip_process.html "Ipv6IpProcess handles IPv6 to IPv4 tunneling.") handles IPv6 to IPv4 tunneling. [More...](class_ipv6_ip_process.html#details)

##  Public Member Functions  
  
---  
void | [addTunnelIntByNum](class_ipv6_ip_process.html#a5fb5ad5f2f2db32c7587ce39622de678) (int)  
| Adds a tunnel interface to the device. [More...](class_ipv6_ip_process.html#a5fb5ad5f2f2db32c7587ce39622de678)  
  
void | [removeTunnelIntByNum](class_ipv6_ip_process.html#aec7d36dbbb8dfda50dc66b02842f1f30) (int)  
| Removes the tunnel interface with the specified interface number. [More...](class_ipv6_ip_process.html#aec7d36dbbb8dfda50dc66b02842f1f30)  
  
int | [getTunnelIntcount](class_ipv6_ip_process.html#a7700e3d8458a8f2865abc89a8390fefb) ()  
| Returns the number of tunnel interfaces. [More...](class_ipv6_ip_process.html#a7700e3d8458a8f2865abc89a8390fefb)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[Ipv6IpProcess](class_ipv6_ip_process.html "Ipv6IpProcess handles IPv6 to IPv4 tunneling.") handles IPv6 to IPv4 tunneling. 

## Member Function Documentation

## ◆ addTunnelIntByNum()

void Ipv6IpProcess::addTunnelIntByNum  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Adds a tunnel interface to the device. 

Parameters
     num,the| interface number for the tunnel interface.   
---|---  
  
## ◆ getTunnelIntcount()

int Ipv6IpProcess::getTunnelIntcount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of tunnel interfaces. 

Returns
    int, the number of tunnel interfaces. 

## ◆ removeTunnelIntByNum()

void Ipv6IpProcess::removeTunnelIntByNum  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Removes the tunnel interface with the specified interface number. 

Parameters
     num,the| interface number of the tunnel interface of interest.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CIpv6IpProcess.pki](_c_ipv6_ip_process_8pki.html)


