# Cisco Packet Tracer Extensions API: ConsolePort Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_console_port.html

---

##  Public Member Functions  
  
---  
[TerminalLine](class_terminal_line.html) | [getTerminalLine](class_console_port.html#acddb52d1fc624a2ec6c27eef8bd5180b) ()  
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
  
  
## Member Function Documentation

## ◆ getTerminalLine()

[TerminalLine](class_terminal_line.html) ConsolePort::getTerminalLine  | ( | | ) |   
---|---|---|---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CConsole.pki](_c_console_8pki.html)


