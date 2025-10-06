# Cisco Packet Tracer Extensions API: HostPort Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_host_port.html

---

[HostPort](class_host_port.html "HostPort handles and manipulates the port configurations on end devices.") handles and manipulates the port configurations on end devices. [More...](class_host_port.html#details)

##  Public Member Functions  
  
---  
void | [setIpSubnetMask](class_host_port.html#a88b74892c8465fe6048701fe045135c9) (ip, ip)  
| Configures a static IP address and subnet mask on the port. [More...](class_host_port.html#a88b74892c8465fe6048701fe045135c9)  
  
void | [setDefaultArpTimeout](class_host_port.html#a35eda491a3f065e9a3851d1adf8e6934) ()  
| Sets the default timer time for ARP. [More...](class_host_port.html#a35eda491a3f065e9a3851d1adf8e6934)  
  
void | [setDhcpClientFlag](class_host_port.html#aee4e45f249e21e0bb0eae08fc8a2d4bb) (bool)  
| Enables or disables the DHCP client on the port. [More...](class_host_port.html#aee4e45f249e21e0bb0eae08fc8a2d4bb)  
  
bool | [isDhcpClientOn](class_host_port.html#ab91e67209a680ae03e74bd3dea35f1cd) ()  
| Returns true if the DHCP client is enabled, otherwise false. [More...](class_host_port.html#ab91e67209a680ae03e74bd3dea35f1cd)  
  
ip | [getIpAddress](class_host_port.html#ab3f008e4241a8051d8decaa492c5bda6) ()  
| Returns the IP address configured on the port. [More...](class_host_port.html#ab3f008e4241a8051d8decaa492c5bda6)  
  
ip | [getSubnetMask](class_host_port.html#af37c1248fba58cad13e31a811a57b3f5) ()  
| Returns the subnet mask configured on the port. [More...](class_host_port.html#af37c1248fba58cad13e31a811a57b3f5)  
  
void | [ipChanged](class_host_port.html#a26fb2a4c92884d2e92aa4c8e5e36d732) (ip, ip, ip, ip)  
| This event is emitted when the IP address or subnet mask changes. [More...](class_host_port.html#a26fb2a4c92884d2e92aa4c8e5e36d732)  
  
void | [setIpv6Enabled](class_host_port.html#ac30a22ec62c86a0a01641f117798ca3a) (bool)  
| Enables or disables IPv6 on the port. [More...](class_host_port.html#ac30a22ec62c86a0a01641f117798ca3a)  
  
bool | [isIpv6Enabled](class_host_port.html#a2b14c6ac93641295f715ecb499ad314f) ()  
| Returns true if IPv6 is enabled on the port, otherwise false. [More...](class_host_port.html#a2b14c6ac93641295f715ecb499ad314f)  
  
void | [setIpv6AddressAutoConfig](class_host_port.html#a1a60b26beedb577340456f6abd444f4b) (bool)  
| Enables or disables IPv6 auto config. [More...](class_host_port.html#a1a60b26beedb577340456f6abd444f4b)  
  
bool | [isIpv6AddressAutoConfig](class_host_port.html#a8fc1dbc6398b47ba35ad654ee71af138) ()  
| Returns true if IPv6 auto config is enabled, otherwise false. [More...](class_host_port.html#a8fc1dbc6398b47ba35ad654ee71af138)  
  
bool | [isSetToDhcpv6](class_host_port.html#a0a5bf56c9ac644859f6e3f1642e4ef2a) ()  
| Returns true if port is set to DHCP v6, otherwise false. [More...](class_host_port.html#a0a5bf56c9ac644859f6e3f1642e4ef2a)  
  
void | [setIpv6LinkLocal](class_host_port.html#adb0f0f6876129094756b921767b4de74) (ipv6)  
| Sets the IPv6 link-local address. [More...](class_host_port.html#adb0f0f6876129094756b921767b4de74)  
  
ipv6 | [getIpv6LinkLocal](class_host_port.html#acdf90e589816283a87c4695865088a97) ()  
| Returns the IPv6 link-local address. [More...](class_host_port.html#acdf90e589816283a87c4695865088a97)  
  
void | [ipv6LinkLocalChanged](class_host_port.html#a7e9753217fe2f52e224cd2ebdaf9012b) (ipv6, ipv6)  
| This event is emitted when the IPv6 link-local address changes. [More...](class_host_port.html#a7e9753217fe2f52e224cd2ebdaf9012b)  
  
bool | [addIpv6Address](class_host_port.html#a46b0690c03524996b608098ffb77c147) (ipv6, int, Ipv6AddressType, bool)  
| Configures a static IPv6 address and network prefix on the port. [More...](class_host_port.html#a46b0690c03524996b608098ffb77c147)  
  
void | [ipv6AddressAdded](class_host_port.html#ac5c79b9fbbbfd8a2d88cdc36198bd4d9) (ipv6, int, Ipv6AddressType)  
| This event is emitted when the IPv6 address changes. [More...](class_host_port.html#ac5c79b9fbbbfd8a2d88cdc36198bd4d9)  
  
bool | [removeIpv6Address](class_host_port.html#ac29344e5093f2e7c28a0fd72682814ed) (ipv6, int, Ipv6AddressType)  
| Removes the IPv6 configuration from the port. [More...](class_host_port.html#ac29344e5093f2e7c28a0fd72682814ed)  
  
void | [ipv6AddressRemoved](class_host_port.html#a3e3efaa5965e03ac2e79ad77a9d56acc) (ipv6, int, Ipv6AddressType)  
| This event is emitted when the IPv6 address configuration is removed. [More...](class_host_port.html#a3e3efaa5965e03ac2e79ad77a9d56acc)  
  
void | [removeAllIpv6Addresses](class_host_port.html#aef04e4be963bdb7b97509d565510d482) ()  
| Removes all IPv6 address configurations. [More...](class_host_port.html#aef04e4be963bdb7b97509d565510d482)  
  
bool | [hasIpv6Address](class_host_port.html#ad80b29c8c58d3ba20b4d784f0387b7c9) (ipv6)  
| Returns true if the specified IPv6 address is configured on the port, otherwise false. [More...](class_host_port.html#ad80b29c8c58d3ba20b4d784f0387b7c9)  
  
[Ipv6AddressConfig](struct_ipv6_address_config.html) | [getIpv6Address](class_host_port.html#a25667a229354bad3be95ea6cee33bfe4) (ipv6)  
| Returns the [Ipv6AddressConfig](struct_ipv6_address_config.html "Data element for Ipv6AddressConfig.") object of the specified IPv6 address. [More...](class_host_port.html#a25667a229354bad3be95ea6cee33bfe4)  
  
ipv6 | [getUnicastIpv6Address](class_host_port.html#a7f9a645eb07f1c6bd7ef6181cac846ab) () const  
| Returns a list of [Ipv6AddressConfig](struct_ipv6_address_config.html "Data element for Ipv6AddressConfig.") objects associated to the port. [More...](class_host_port.html#a7f9a645eb07f1c6bd7ef6181cac846ab)  
  
int | [getUnicastIpv6Prefix](class_host_port.html#ac54e83a30592d056ce432bbf1f69882d) ()  
| Returns the port's Unicast Ipv6 Prefix. [More...](class_host_port.html#ac54e83a30592d056ce432bbf1f69882d)  
  
vector< [Ipv6AddressConfig](struct_ipv6_address_config.html) > | [getIpv6Addresses](class_host_port.html#a4172c225334f17124c46270762408c8e) ()  
| Returns a list of [Ipv6AddressConfig](struct_ipv6_address_config.html "Data element for Ipv6AddressConfig.") objects associated to the port. [More...](class_host_port.html#a4172c225334f17124c46270762408c8e)  
  
bool | [isInIpv6Multicast](class_host_port.html#ac8d36a2d76106ec2a15947fe9ce4af0d) (ipv6)  
| Returns true if specified IPv6 address is a multicast address, otherwise false. [More...](class_host_port.html#ac8d36a2d76106ec2a15947fe9ce4af0d)  
  
vector< ipv6 > | [getIpv6Multicast](class_host_port.html#a008935699a6394a15c3ac60084a86155) ()  
| Returns a list of IPv6 multicast addresses configured on the port. [More...](class_host_port.html#a008935699a6394a15c3ac60084a86155)  
  
void | [setMtu](class_host_port.html#af48990f52272bb5402245ab4f928a875) (int)  
| Sets the maximum transmission unit (MTU) value on the port. [More...](class_host_port.html#af48990f52272bb5402245ab4f928a875)  
  
int | [getMtu](class_host_port.html#abb610cb7518ed433e578a63237d8706b) ()  
| Returns the maximum transmission unit (MTU) value configured on the port. [More...](class_host_port.html#abb610cb7518ed433e578a63237d8706b)  
  
void | [setIpMtu](class_host_port.html#a5196cf34ca806bf7bbb62b66d9068b2f) (int)  
| Sets the IP maximum transmission unit (MTU) value on the port. [More...](class_host_port.html#a5196cf34ca806bf7bbb62b66d9068b2f)  
  
int | [getIpMtu](class_host_port.html#a4040f37417fa32ffcbd1b011c96d21da) ()  
| Returns the IP maximum transmission unit (MTU) value configured on the port. [More...](class_host_port.html#a4040f37417fa32ffcbd1b011c96d21da)  
  
void | [setIpv6Mtu](class_host_port.html#a5f325b1c94b8491e9c91438a9d13abfe) (int)  
| Sets the IPv6 maximum transmission unit (MTU) value on the port. [More...](class_host_port.html#a5f325b1c94b8491e9c91438a9d13abfe)  
  
int | [getIpv6Mtu](class_host_port.html#a676444b91e72c3c5920fbdc84bb600a9) ()  
| Returns the IPv6 maximum transmission unit (MTU) value configured on the port. [More...](class_host_port.html#a676444b91e72c3c5920fbdc84bb600a9)  
  
void | [setDefaultGateway](class_host_port.html#a75fd62c3529104209e78fed13c069fdd) (ip)  
| Sets the default gateway for this port. [More...](class_host_port.html#a75fd62c3529104209e78fed13c069fdd)  
  
void | [setDnsServerIp](class_host_port.html#a551c795d1de2aea55b9b2efe68a7efbf) (ip)  
| Sets the DNS server gateway for this port. [More...](class_host_port.html#a551c795d1de2aea55b9b2efe68a7efbf)  
  
void | [setv6ServerIp](class_host_port.html#aee67eec5bb9a665d09736bed727700ad) (ipv6)  
| Sets the DNS [Server](class_server.html "Server is Server device object with a terminal line.") IPv6 gateway for this port. [More...](class_host_port.html#aee67eec5bb9a665d09736bed727700ad)  
  
void | [setv6DefaultGateway](class_host_port.html#ad4da4af7975fb9cfe2dac391b09421b5) (ipv6)  
| Sets the default IPv6 gateway for this port. [More...](class_host_port.html#ad4da4af7975fb9cfe2dac391b09421b5)  
  
bool | [isInboundFirewallOn](class_host_port.html#a42a58969dddec21e2e39e8c18542f72d) ()  
| Returns true if the IPv4 inbound firewall is enabled, otherwise false. [More...](class_host_port.html#a42a58969dddec21e2e39e8c18542f72d)  
  
void | [setInboundFirewallService](class_host_port.html#a2bccd5ba32e4ca8057f8a56a4ece78aa) (bool)  
| Enables or disables the IPv4 inbound firewall. [More...](class_host_port.html#a2bccd5ba32e4ca8057f8a56a4ece78aa)  
  
bool | [isInboundIpv6FirewallOn](class_host_port.html#afedb242cbda463ad8800bfad51fa0a54) ()  
| Returns true if the IPv6 inbound firewall is enabled, otherwise false. [More...](class_host_port.html#afedb242cbda463ad8800bfad51fa0a54)  
  
void | [setInboundIpv6FirewallService](class_host_port.html#a1ef23d7484e953b775d82e57e651753a) (bool)  
| Enables or disables the IPv6 inbound firewall. [More...](class_host_port.html#a1ef23d7484e953b775d82e57e651753a)  
  
Public Member Functions inherited from [Port](class_port.html)  
string | [getName](class_port.html#a16e393f7d744d91a7d7f8eb6bd675860) ()  
| Returns the name of the port. [More...](class_port.html#a16e393f7d744d91a7d7f8eb6bd675860)  
  
int | [getChannel](class_port.html#a87893c7a973c575c5375b65896bc3645) ()  
| Returns the channel of the port. [More...](class_port.html#a87893c7a973c575c5375b65896bc3645)  
  
void | [setChannel](class_port.html#a0dae816321c608da25651df6b01ba4de) (int)  
| Sets the channel of the port. [More...](class_port.html#a0dae816321c608da25651df6b01ba4de)  
  
string | [getTerminalTypeShortString](class_port.html#a6eb43115f73f9097bdd1770cac229906) ()  
| Returns the name of the port shortened, without number. [More...](class_port.html#a6eb43115f73f9097bdd1770cac229906)  
  
string | [getPortNameNumber](class_port.html#a2d1531b18df3a84f0f94f75bfab59994) ()  
| Returns the port number. Can have something like 0/0/0, etc. [More...](class_port.html#a2d1531b18df3a84f0f94f75bfab59994)  
  
PortType | [getType](class_port.html#a5859f5d788d56c0103f4274b6d62b725) ()  
| Returns the type of the port. [More...](class_port.html#a5859f5d788d56c0103f4274b6d62b725)  
  
void | [setDescription](class_port.html#a5d6eff9e062169bd07f504176a173ada) (string)  
| Sets the description for the port. [More...](class_port.html#a5d6eff9e062169bd07f504176a173ada)  
  
string | [getDescription](class_port.html#a67ea29398aac6fb56b781ed1edf0d50d) ()  
| Returns the description of the port. [More...](class_port.html#a67ea29398aac6fb56b781ed1edf0d50d)  
  
void | [setPower](class_port.html#a80d7ee576d8171e1aac2a427f0df4076) (bool)  
| Sets the power state for the port. [More...](class_port.html#a80d7ee576d8171e1aac2a427f0df4076)  
  
bool | [getPower](class_port.html#a3589cb8fb156fe3efe8b72335787ffd7) ()  
| Returns true if the port is on, false if the port is off. [More...](class_port.html#a3589cb8fb156fe3efe8b72335787ffd7)  
  
void | [powerChanged](class_port.html#a0b45a31698c1c3282ed5e7b6b2100606) (bool)  
| This event is emitted when the power state of the port changes. [More...](class_port.html#a0b45a31698c1c3282ed5e7b6b2100606)  
  
bool | [isStraightPins](class_port.html#a6ae4bdc8c2b8f70f97e73b85be59518e) ()  
| Returns true if the pins are straight, for ethernet. [More...](class_port.html#a6ae4bdc8c2b8f70f97e73b85be59518e)  
  
bool | [isAutoCross](class_port.html#a870388a0553821c08b43930befb0a7b5) ()  
| Returns true if the port is configured for auto crossover, for ethernet. [More...](class_port.html#a870388a0553821c08b43930befb0a7b5)  
  
void | [setBandwidth](class_port.html#aef9e53afdaad84b4c752974e4c68f379) (int)  
| Sets the bandwidth for the port. [More...](class_port.html#aef9e53afdaad84b4c752974e4c68f379)  
  
int | [getBandwidth](class_port.html#ab5ab9f68452a3238e18b17628542d633) ()  
| Returns the bandwidth of the port. [More...](class_port.html#ab5ab9f68452a3238e18b17628542d633)  
  
void | [setBandwidthAutoNegotiate](class_port.html#acab833f74b1216d8087cb3731a547195) (bool)  
| Enables or disables bandwidth auto negotiation. [More...](class_port.html#acab833f74b1216d8087cb3731a547195)  
  
bool | [isBandwidthAutoNegotiate](class_port.html#a863308825fbe5c487fc06ae672ddef5d) ()  
| Returns true if bandwidth auto negotiation is enabled, otherwise false. [More...](class_port.html#a863308825fbe5c487fc06ae672ddef5d)  
  
void | [setFullDuplex](class_port.html#a6dba4142d237e59632734234b71a543f) (bool)  
| Enables or disables full duplex mode. [More...](class_port.html#a6dba4142d237e59632734234b71a543f)  
  
bool | [isFullDuplex](class_port.html#af68d358ac2703ed40942661b4e31ccbe) ()  
| Returns true if full duplex mode is enabled, otherwise false. [More...](class_port.html#af68d358ac2703ed40942661b4e31ccbe)  
  
void | [setDuplexAutoNegotiate](class_port.html#a82f5f70e4b313ce8a7fd2026e6b7d9a5) (bool)  
| Enables or disables duplex auto negotiation. [More...](class_port.html#a82f5f70e4b313ce8a7fd2026e6b7d9a5)  
  
bool | [isDuplexAutoNegotiate](class_port.html#a72bbe58e532b8d4d36827bae9ab4dd10) ()  
| Returns true if duplex auto negotiation is enabled, otherwise false. [More...](class_port.html#a72bbe58e532b8d4d36827bae9ab4dd10)  
  
void | [setMacAddress](class_port.html#a5c8bd8890fd5f6122c86912e39fb440e) (mac)  
| Sets the MAC address on the port. [More...](class_port.html#a5c8bd8890fd5f6122c86912e39fb440e)  
  
mac | [getMacAddress](class_port.html#a79200dd52f980ec0bf58638b05fd3450) ()  
| Returns the MAC address set on the port. [More...](class_port.html#a79200dd52f980ec0bf58638b05fd3450)  
  
void | [macChanged](class_port.html#ab304bf37b6d03514b0bf8af46798d842) (mac, mac)  
| This event is emitted when the MAC address on the port changes. [More...](class_port.html#ab304bf37b6d03514b0bf8af46798d842)  
  
mac | [getBia](class_port.html#a444ebe1015acd782cfc18c7e9103b73e) ()  
| Returns the burned-in address of the port. [More...](class_port.html#a444ebe1015acd782cfc18c7e9103b73e)  
  
void | [setClockRate](class_port.html#adeb6f8d0b85c94151f044a38ff5cd602) (int)  
| Sets the clock rate on the port. [More...](class_port.html#adeb6f8d0b85c94151f044a38ff5cd602)  
  
int | [getClockRate](class_port.html#a3948f94a30c2282920d2a150f50f3ca6) ()  
| Returns the clock rate on the port. [More...](class_port.html#a3948f94a30c2282920d2a150f50f3ca6)  
  
[Link](class_link.html) | [getLink](class_port.html#a5237e8c410a5509961640926f8a6d820) ()  
| Returns the link connected to the port. [More...](class_port.html#a5237e8c410a5509961640926f8a6d820)  
  
bool | [isProtocolUp](class_port.html#a74824f0ac10ff8b0ec665df88fe826d4) ()  
| Returns true if the line protocol is up on the port, otherwise false. [More...](class_port.html#a74824f0ac10ff8b0ec665df88fe826d4)  
  
bool | [isPortUp](class_port.html#a44cef34691ce545a2e9974e0416a8ade) ()  
| Returns true if the status is up on the port, otherwise false. [More...](class_port.html#a44cef34691ce545a2e9974e0416a8ade)  
  
[Process](class_process.html) | [getEncapProcess](class_port.html#a8a6bdc96231f44300d9c1a775cc592e8) ()  
| Returns the encapsulation process. [More...](class_port.html#a8a6bdc96231f44300d9c1a775cc592e8)  
  
[Process](class_process.html) | [getKeepAliveProcess](class_port.html#a4691e4765bb77ccb09e6c280ccecb750) ()  
| Returns the keepalive process. [More...](class_port.html#a4691e4765bb77ccb09e6c280ccecb750)  
  
QString | [getRemotePortName](class_port.html#a7ed3ed43f2e9ab97d95175f08086335f) ()  
| Returns the name of the remote port. [More...](class_port.html#a7ed3ed43f2e9ab97d95175f08086335f)  
  
LightStatus | [getLightStatus](class_port.html#a5af81c13e3a9c138da8aedd6ade544a2) ()  
| Returns the link light status. [More...](class_port.html#a5af81c13e3a9c138da8aedd6ade544a2)  
  
void | [lightStatusChanged](class_port.html#abcb1af6e65de5f290d0fdfb0bd5d8dce) (LightStatus)  
| This event is emitted when the link light changes. [More...](class_port.html#abcb1af6e65de5f290d0fdfb0bd5d8dce)  
  
void | [lightBlinked](class_port.html#a828f4dd54d335c31ff8fea258cc5655b) ()  
| This event is emitted when the link light blinks. [More...](class_port.html#a828f4dd54d335c31ff8fea258cc5655b)  
  
void | [portStatusChanged](class_port.html#a65ff9bb831cea163a4e255a13d3d36e5) (bool)  
| This event is emitted when the port status changes. [More...](class_port.html#a65ff9bb831cea163a4e255a13d3d36e5)  
  
void | [lineProtocolChanged](class_port.html#a001a8b55d859ca09bf746f0fb221f2a3) (bool)  
| This event is emitted when the line protocol status changes. [More...](class_port.html#a001a8b55d859ca09bf746f0fb221f2a3)  
  
void | [packetReceived](class_port.html#a92024fa73b2246eeed54df22275e34cd) (string, int)  
| This event is emitted when the port receives a packet. [More...](class_port.html#a92024fa73b2246eeed54df22275e34cd)  
  
void | [packetSent](class_port.html#a3f1050f079f379d21bb37ed49c2c2720) (string, int)  
| This event is emitted when the port sends a packet. [More...](class_port.html#a3f1050f079f379d21bb37ed49c2c2720)  
  
void | [packetReceivedWithDetails](class_port.html#a2c3469b089608ded0a80674f9eba3cb1) ([Signal](struct_signal.html), int)  
| This event is emitted when the port receives a packet with details. [More...](class_port.html#a2c3469b089608ded0a80674f9eba3cb1)  
  
void | [packetSentWithDetails](class_port.html#a29f94c48cee2ff64a453be0776917fec) ([Signal](struct_signal.html), int)  
| This event is emitted when the port sends a packet with details. [More...](class_port.html#a29f94c48cee2ff64a453be0776917fec)  
  
int | [getHigherProcessCount](class_port.html#a94592523a27ec80cac93dcb6d91abcc7) ()  
| Returns the higher process count. [More...](class_port.html#a94592523a27ec80cac93dcb6d91abcc7)  
  
[HardwareQueue](class_hardware_queue.html) | [getHardwareQueue](class_port.html#a5ffc60880a7ad8fa575c3b8c425a780c) ()  
| Returns the hardware queue. [More...](class_port.html#a5ffc60880a7ad8fa575c3b8c425a780c)  
  
[QueueProcess](class_queue_process.html) | [getQosQueue](class_port.html#a1aa1a4f0679c4a608f3ebab991818bc5) ()  
| Returns the qos queue. [More...](class_port.html#a1aa1a4f0679c4a608f3ebab991818bc5)  
  
bool | [isEthernetPort](class_port.html#a2788014b226e99fb8850624ba8a186c8) ()  
| Returns true if it is a ethernet port, false if not. [More...](class_port.html#a2788014b226e99fb8850624ba8a186c8)  
  
bool | [isWirelessPort](class_port.html#a82120c12f873c02b719688ed6d4dfdc4) ()  
| Returns true if it is a wireless port, false if not. [More...](class_port.html#a82120c12f873c02b719688ed6d4dfdc4)  
  
bool | [isPowerOn](class_port.html#a96d6736b106c497dfbb0bdddbe994939) ()  
| Returns true if the power is on, false if not. [More...](class_port.html#a96d6736b106c497dfbb0bdddbe994939)  
  
void | [deleteLink](class_port.html#a778777b63e3a21af0d969dfd57acf148) ()  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[HostPort](class_host_port.html "HostPort handles and manipulates the port configurations on end devices.") handles and manipulates the port configurations on end devices. 

## Member Function Documentation

## ◆ addIpv6Address()

bool HostPort::addIpv6Address  | ( | ipv6  | ,   
---|---|---|---  
|  | int  | ,   
|  | Ipv6AddressType  | ,   
|  | bool  |   
| ) | |   
  
Configures a static IPv6 address and network prefix on the port. 

Parameters
     ipAddress,the| IPv6 address.   
---|---  
prefix,the| network prefix.   
type,the| IPv6 address type. IPv6 address types: eUnicast = 0, eAnycast = 1, eEui64 = 2, eNdAssigned = 3, eDhcpAssigned = 4   
bAllowDup,true| to allow duplicate IPv6 addresses, false to disallow duplicate IPv6 addresses.   
  
## ◆ getIpAddress()

ip HostPort::getIpAddress  | ( | | ) |   
---|---|---|---|---  
  
Returns the IP address configured on the port. 

Returns
    ip, the IP address configured on the port. 

## ◆ getIpMtu()

int HostPort::getIpMtu  | ( | | ) |   
---|---|---|---|---  
  
Returns the IP maximum transmission unit (MTU) value configured on the port. 

Returns
    int, the IP MTU value. 

## ◆ getIpv6Address()

[Ipv6AddressConfig](struct_ipv6_address_config.html) HostPort::getIpv6Address  | ( | ipv6  | | ) |   
---|---|---|---|---|---  
  
Returns the [Ipv6AddressConfig](struct_ipv6_address_config.html "Data element for Ipv6AddressConfig.") object of the specified IPv6 address. 

Parameters
     ipAddress,the| IPv6 address of interest.  
---|---  
  
Returns
    [Ipv6AddressConfig](struct_ipv6_address_config.html "Data element for Ipv6AddressConfig."), the [Ipv6AddressConfig](struct_ipv6_address_config.html "Data element for Ipv6AddressConfig.") object of the specified IPv6 address. 

## ◆ getIpv6Addresses()

vector< [Ipv6AddressConfig](struct_ipv6_address_config.html) > HostPort::getIpv6Addresses  | ( | | ) |   
---|---|---|---|---  
  
Returns a list of [Ipv6AddressConfig](struct_ipv6_address_config.html "Data element for Ipv6AddressConfig.") objects associated to the port. 

Returns
    vector<Ipv6AddressConfig>, a list of [Ipv6AddressConfig](struct_ipv6_address_config.html "Data element for Ipv6AddressConfig.") objects associated to the port. 

## ◆ getIpv6LinkLocal()

ipv6 HostPort::getIpv6LinkLocal  | ( | | ) |   
---|---|---|---|---  
  
Returns the IPv6 link-local address. 

Returns
    ipv6, the IPv6 link-local address. 

## ◆ getIpv6Mtu()

int HostPort::getIpv6Mtu  | ( | | ) |   
---|---|---|---|---  
  
Returns the IPv6 maximum transmission unit (MTU) value configured on the port. 

Returns
    int, the IPv6 MTU value. 

## ◆ getIpv6Multicast()

vector< ipv6 > HostPort::getIpv6Multicast  | ( | | ) |   
---|---|---|---|---  
  
Returns a list of IPv6 multicast addresses configured on the port. 

Returns
    vector<ipv6>, a list of IPv6 multicast addresses configured on the port. 

## ◆ getMtu()

int HostPort::getMtu  | ( | | ) |   
---|---|---|---|---  
  
Returns the maximum transmission unit (MTU) value configured on the port. 

Returns
    int, the MTU value. 

## ◆ getSubnetMask()

ip HostPort::getSubnetMask  | ( | | ) |   
---|---|---|---|---  
  
Returns the subnet mask configured on the port. 

Returns
    ip, the subnet mask configured on the port. 

## ◆ getUnicastIpv6Address()

ipv6 HostPort::getUnicastIpv6Address  | ( | | ) |  const  
---|---|---|---|---  
  
Returns a list of [Ipv6AddressConfig](struct_ipv6_address_config.html "Data element for Ipv6AddressConfig.") objects associated to the port. 

Returns
    vector<Ipv6AddressConfig>, a list of [Ipv6AddressConfig](struct_ipv6_address_config.html "Data element for Ipv6AddressConfig.") objects associated to the port. 

## ◆ getUnicastIpv6Prefix()

int HostPort::getUnicastIpv6Prefix  | ( | | ) |   
---|---|---|---|---  
  
Returns the port's Unicast Ipv6 Prefix. 

Returns
    int, the port's Unicast Ipv6 Prefix. 

## ◆ hasIpv6Address()

bool HostPort::hasIpv6Address  | ( | ipv6  | | ) |   
---|---|---|---|---|---  
  
Returns true if the specified IPv6 address is configured on the port, otherwise false. 

Parameters
     ipAddress,the| IPv6 address of interest.  
---|---  
  
Returns
    bool, true if the specified IPv6 address is configured on the port, otherwise false. 

## ◆ ipChanged()

void HostPort::ipChanged  | ( | ip  | ,   
---|---|---|---  
|  | ip  | ,   
|  | ip  | ,   
|  | ip  |   
| ) | |   
  
This event is emitted when the IP address or subnet mask changes. 

  * newIp, the new IP address. 
  * newMask, the new subnet mask. 
  * oldIp, the old IP address. 
  * oldMask, the old subnet mask.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ ipv6AddressAdded()

void HostPort::ipv6AddressAdded  | ( | ipv6  | ,   
---|---|---|---  
|  | int  | ,   
|  | Ipv6AddressType  |   
| ) | |   
  
This event is emitted when the IPv6 address changes. 

Parameters
     ipAddress,the| IPv6 address.   
---|---  
prefix,the| network prefix.   
type,the| IPv6 address type. IPv6 address types: eUnicast = 0, eAnycast = 1, eEui64 = 2, eNdAssigned = 3, eDhcpAssigned = 4  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ ipv6AddressRemoved()

void HostPort::ipv6AddressRemoved  | ( | ipv6  | ,   
---|---|---|---  
|  | int  | ,   
|  | Ipv6AddressType  |   
| ) | |   
  
This event is emitted when the IPv6 address configuration is removed. 

Parameters
     ipAddress,the| IPv6 address.   
---|---  
prefix,the| network prefix.   
type,the| IPv6 address type. IPv6 address types: eUnicast = 0, eAnycast = 1, eEui64 = 2, eNdAssigned = 3, eDhcpAssigned = 4  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ ipv6LinkLocalChanged()

void HostPort::ipv6LinkLocalChanged  | ( | ipv6  | ,   
---|---|---|---  
|  | ipv6  |   
| ) | |   
  
This event is emitted when the IPv6 link-local address changes. 

  * newIp, the new IPv6 link-local address. 
  * oldIp, the old IPv6 link-local address.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ isDhcpClientOn()

bool HostPort::isDhcpClientOn  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the DHCP client is enabled, otherwise false. 

Returns
    bool, true if the DHCP client is enabled, otherwise false. 

## ◆ isInboundFirewallOn()

bool HostPort::isInboundFirewallOn  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the IPv4 inbound firewall is enabled, otherwise false. 

Returns
    bool, true if the IPv4 inbound firewall is enabled, otherwise false. 

## ◆ isInboundIpv6FirewallOn()

bool HostPort::isInboundIpv6FirewallOn  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the IPv6 inbound firewall is enabled, otherwise false. 

Returns
    bool, true if the IPv6 inbound firewall is enabled, otherwise false. 

## ◆ isInIpv6Multicast()

bool HostPort::isInIpv6Multicast  | ( | ipv6  | | ) |   
---|---|---|---|---|---  
  
Returns true if specified IPv6 address is a multicast address, otherwise false. 

Parameters
     ipAddress,the| IPv6 address of interest.  
---|---  
  
Returns
    bool, true if specified IPv6 address is a multicast address, otherwise false. 

## ◆ isIpv6AddressAutoConfig()

bool HostPort::isIpv6AddressAutoConfig  | ( | | ) |   
---|---|---|---|---  
  
Returns true if IPv6 auto config is enabled, otherwise false. 

Returns
    bool, true if IPv6 auto config is enabled, otherwise false. 

## ◆ isIpv6Enabled()

bool HostPort::isIpv6Enabled  | ( | | ) |   
---|---|---|---|---  
  
Returns true if IPv6 is enabled on the port, otherwise false. 

Returns
    bool, true if IPv6 is enabled on the port, otherwise false. 

## ◆ isSetToDhcpv6()

bool HostPort::isSetToDhcpv6  | ( | | ) |   
---|---|---|---|---  
  
Returns true if port is set to DHCP v6, otherwise false. 

Returns
    bool, true if port is set to DHCP v6, otherwise false. 

## ◆ removeAllIpv6Addresses()

void HostPort::removeAllIpv6Addresses  | ( | | ) |   
---|---|---|---|---  
  
Removes all IPv6 address configurations. 

## ◆ removeIpv6Address()

bool HostPort::removeIpv6Address  | ( | ipv6  | ,   
---|---|---|---  
|  | int  | ,   
|  | Ipv6AddressType  |   
| ) | |   
  
Removes the IPv6 configuration from the port. 

Parameters
     ipAddress,the| IPv6 address.   
---|---  
prefix,the| network prefix.   
type,the| IPv6 address type. IPv6 address types: eUnicast = 0, eAnycast = 1, eEui64 = 2, eNdAssigned = 3, eDhcpAssigned = 4   
  
## ◆ setDefaultArpTimeout()

void HostPort::setDefaultArpTimeout  | ( | | ) |   
---|---|---|---|---  
  
Sets the default timer time for ARP. 

## ◆ setDefaultGateway()

void HostPort::setDefaultGateway  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Sets the default gateway for this port. 

Parameters
     gateway,the| IP address of the default gateway.   
---|---  
  
## ◆ setDhcpClientFlag()

void HostPort::setDhcpClientFlag  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables the DHCP client on the port. 

Parameters
     bFlag,true| to enable the DHCP client, false to disable it.   
---|---  
  
## ◆ setDnsServerIp()

void HostPort::setDnsServerIp  | ( | ip  | | ) |   
---|---|---|---|---|---  
  
Sets the DNS server gateway for this port. 

Parameters
     gateway,the| IP address of the DNS gateway.   
---|---  
  
## ◆ setInboundFirewallService()

void HostPort::setInboundFirewallService  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables the IPv4 inbound firewall. 

Parameters
     bEnable,true| to enable the IPv4 inbound firewall, false to disable it.   
---|---  
  
## ◆ setInboundIpv6FirewallService()

void HostPort::setInboundIpv6FirewallService  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables the IPv6 inbound firewall. 

Parameters
     bEnable,true| to enable the IPv6 inbound firewall, false to disable it.   
---|---  
  
## ◆ setIpMtu()

void HostPort::setIpMtu  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the IP maximum transmission unit (MTU) value on the port. 

Parameters
     mtu,the| IP MTU value.   
---|---  
  
## ◆ setIpSubnetMask()

void HostPort::setIpSubnetMask  | ( | ip  | ,   
---|---|---|---  
|  | ip  |   
| ) | |   
  
Configures a static IP address and subnet mask on the port. 

Parameters
     newIpAddress,the| IP address.   
---|---  
newMask,the| subnet mask.   
  
## ◆ setIpv6AddressAutoConfig()

void HostPort::setIpv6AddressAutoConfig  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables IPv6 auto config. 

Parameters
     bAutoConfig,true| to enable IPv6 auto config, false to disable it.   
---|---  
  
## ◆ setIpv6Enabled()

void HostPort::setIpv6Enabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables IPv6 on the port. 

Parameters
     bEnable,true| to enable IPv6, false to disable it.   
---|---  
  
## ◆ setIpv6LinkLocal()

void HostPort::setIpv6LinkLocal  | ( | ipv6  | | ) |   
---|---|---|---|---|---  
  
Sets the IPv6 link-local address. 

Parameters
     ipAddress,the| IPv6 link-local address.   
---|---  
  
## ◆ setIpv6Mtu()

void HostPort::setIpv6Mtu  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the IPv6 maximum transmission unit (MTU) value on the port. 

Parameters
     mtu,the| IP MTU value.   
---|---  
  
## ◆ setMtu()

void HostPort::setMtu  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the maximum transmission unit (MTU) value on the port. 

Parameters
     mtu,the| MTU value.   
---|---  
  
## ◆ setv6DefaultGateway()

void HostPort::setv6DefaultGateway  | ( | ipv6  | | ) |   
---|---|---|---|---|---  
  
Sets the default IPv6 gateway for this port. 

Parameters
     gateway,the| IPv6 address of the default gateway.   
---|---  
  
## ◆ setv6ServerIp()

void HostPort::setv6ServerIp  | ( | ipv6  | | ) |   
---|---|---|---|---|---  
  
Sets the DNS [Server](class_server.html "Server is Server device object with a terminal line.") IPv6 gateway for this port. 

Parameters
     gateway,the| IPv6 address of the DNS gateway.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CHostPort.pki](_c_host_port_8pki.html)


