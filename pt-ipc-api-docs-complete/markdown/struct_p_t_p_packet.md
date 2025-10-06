# Cisco Packet Tracer Extensions API: PTPPacket Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_p_t_p_packet.html

---

PTP packet structure. [More...](struct_p_t_p_packet.html#details)

##  Public Attributes  
  
---  
short | [ts](struct_p_t_p_packet.html#ab214581a14c892961fe60572eb45d777)  
short | [m_msgId](struct_p_t_p_packet.html#a0e293bfb0e7fd857c049cc7c8b5ec75f)  
short | [m_version](struct_p_t_p_packet.html#ab86265bde9d201b97f047b31e5993d7f)  
short | [m_messageLength](struct_p_t_p_packet.html#a65bf7128c3685b0ba2feba7f0e15baf5)  
short | [m_domainNumber](struct_p_t_p_packet.html#a504e3ff99518a45288630ba129bf3bd2)  
int | [m_flag](struct_p_t_p_packet.html#a2ea1df8dabddd59a04fdc1f45e3fbb02)  
double | [m_correctionTime](struct_p_t_p_packet.html#adf900a7f20c8c6ff8150008647e0d34a)  
int | [m_correctionScaledFractionalTime](struct_p_t_p_packet.html#a34120104219eb62f169ed7b7266e7073)  
string | [m_sourcePortId](struct_p_t_p_packet.html#a9942b0f4c7af4a3b3aa7659fe81f91e3)  
short | [m_sourcePortNum](struct_p_t_p_packet.html#ad0ceb439e6a5edfbb6240278ba13b091)  
short | [m_sequenceId](struct_p_t_p_packet.html#a8f31e041c89942b85e4357f91e4dd925)  
short | [m_control](struct_p_t_p_packet.html#a98a56466633199a3ce6f02f67b3bac48)  
int | [m_logMsgInterval](struct_p_t_p_packet.html#ac1d38bfda5cc1a205b17ebd50fb96fdf)  
double | [m_orgTimeSeconds](struct_p_t_p_packet.html#a9d15d618cb7868d96d61932d0180ed14)  
int | [m_orgTimeNanoSeconds](struct_p_t_p_packet.html#a1fa37da4efc6ade89c6ec8f48fdf4e26)  
string | [m_requestingSourcePortId](struct_p_t_p_packet.html#a710dbc98dc54e97b77341a7f44bb55ef)  
short | [m_requestingSourcePortNum](struct_p_t_p_packet.html#a50002e532e9f1552b362a13a25546cf5)  
short | [m_currentUtcOffset](struct_p_t_p_packet.html#a7f7f009b84219616bbdd5c98f2d6bcb9)  
short | [m_grandmasterPri1](struct_p_t_p_packet.html#a39484c7d45ae67d71b0f17a9caeedda2)  
int | [m_class](struct_p_t_p_packet.html#a3601965eb77d0bab37d653766f60b59b)  
string | [m_accuracy](struct_p_t_p_packet.html#a3e338c569f4d20e1bcf81c7ef5b8d380)  
int | [m_variance](struct_p_t_p_packet.html#a647126b32ed7b72df6cb6eb49fe26a0b)  
short | [m_grandmasterPri2](struct_p_t_p_packet.html#ad8258d3a7349f4c2da598d979ebb11ea)  
string | [m_grandmasterId](struct_p_t_p_packet.html#a8a3a44f18511f849f716275583f046ca)  
short | [m_stepsRemoved](struct_p_t_p_packet.html#a8d2eceb0609b441d7eff5070ce312f6c)  
short | [m_timeSource](struct_p_t_p_packet.html#a9db0e8756f2dfe5d2fafee0258a9cf25)  
  
## Detailed Description

PTP packet structure. 

## Member Data Documentation

## ◆ m_accuracy

string PTPPacket::m_accuracy  
---  
  
## ◆ m_class

int PTPPacket::m_class  
---  
  
## ◆ m_control

short PTPPacket::m_control  
---  
  
## ◆ m_correctionScaledFractionalTime

int PTPPacket::m_correctionScaledFractionalTime  
---  
  
## ◆ m_correctionTime

double PTPPacket::m_correctionTime  
---  
  
## ◆ m_currentUtcOffset

short PTPPacket::m_currentUtcOffset  
---  
  
## ◆ m_domainNumber

short PTPPacket::m_domainNumber  
---  
  
## ◆ m_flag

int PTPPacket::m_flag  
---  
  
## ◆ m_grandmasterId

string PTPPacket::m_grandmasterId  
---  
  
## ◆ m_grandmasterPri1

short PTPPacket::m_grandmasterPri1  
---  
  
## ◆ m_grandmasterPri2

short PTPPacket::m_grandmasterPri2  
---  
  
## ◆ m_logMsgInterval

int PTPPacket::m_logMsgInterval  
---  
  
## ◆ m_messageLength

short PTPPacket::m_messageLength  
---  
  
## ◆ m_msgId

short PTPPacket::m_msgId  
---  
  
## ◆ m_orgTimeNanoSeconds

int PTPPacket::m_orgTimeNanoSeconds  
---  
  
## ◆ m_orgTimeSeconds

double PTPPacket::m_orgTimeSeconds  
---  
  
## ◆ m_requestingSourcePortId

string PTPPacket::m_requestingSourcePortId  
---  
  
## ◆ m_requestingSourcePortNum

short PTPPacket::m_requestingSourcePortNum  
---  
  
## ◆ m_sequenceId

short PTPPacket::m_sequenceId  
---  
  
## ◆ m_sourcePortId

string PTPPacket::m_sourcePortId  
---  
  
## ◆ m_sourcePortNum

short PTPPacket::m_sourcePortNum  
---  
  
## ◆ m_stepsRemoved

short PTPPacket::m_stepsRemoved  
---  
  
## ◆ m_timeSource

short PTPPacket::m_timeSource  
---  
  
## ◆ m_variance

int PTPPacket::m_variance  
---  
  
## ◆ m_version

short PTPPacket::m_version  
---  
  
## ◆ ts

short PTPPacket::ts  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [CPTPPacket.pki](_c_p_t_p_packet_8pki.html)


