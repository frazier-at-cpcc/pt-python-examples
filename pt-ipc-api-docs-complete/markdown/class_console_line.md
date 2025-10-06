# Cisco Packet Tracer Extensions API: ConsoleLine Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_console_line.html

---

[ConsoleLine](class_console_line.html "ConsoleLine is the console line handler for the TerminalLine object.") is the console line handler for the [TerminalLine](class_terminal_line.html "TerminalLine manages the terminal lines, virtual terminal lines, and console lines.") object. [More...](class_console_line.html#details)

##  Public Member Functions  
  
---  
string | [getOutput](class_console_line.html#aa2fec3cd0291da6bda7c6344ff95a489) ()  
| Returns the output from the console line. [More...](class_console_line.html#aa2fec3cd0291da6bda7c6344ff95a489)  
  
void | [idledOut](class_console_line.html#a24ee01c56378993b53d9bce49122e45b) ()  
| When the terminal line idles out this event is generated. [More...](class_console_line.html#a24ee01c56378993b53d9bce49122e45b)  
  
Public Member Functions inherited from [TerminalLine](class_terminal_line.html)  
string | [getName](class_terminal_line.html#ac9943ba37ee341fb6a8942b058f9c6ec) ()  
| Returns the name of this terminal line. [More...](class_terminal_line.html#ac9943ba37ee341fb6a8942b058f9c6ec)  
  
[Device](class_device.html) | [getOwnerDevice](class_terminal_line.html#abdd04045ff7a69beb0bd6e7197657525) ()  
| Returns the owner device of this terminal line. [More...](class_terminal_line.html#abdd04045ff7a69beb0bd6e7197657525)  
  
string | [getMode](class_terminal_line.html#a9ce0a873bc32f0962c82105a5a0d8a7b) ()  
| Returns the mode this terminal line is in. [More...](class_terminal_line.html#a9ce0a873bc32f0962c82105a5a0d8a7b)  
  
string | [getPrompt](class_terminal_line.html#afa06679fbfc42ee14282721184b2531c) ()  
| Returns the prompt of this terminal line. [More...](class_terminal_line.html#afa06679fbfc42ee14282721184b2531c)  
  
[CommandHistory](struct_command_history.html) | [getUserHistory](class_terminal_line.html#abc1db6ce7dccd405d25c0cf81ba80006) ()  
| Returns the user history of this terminal line. [More...](class_terminal_line.html#abc1db6ce7dccd405d25c0cf81ba80006)  
  
[CommandHistory](struct_command_history.html) | [getConfigHistory](class_terminal_line.html#a4368feafbe4728a80964ccaeb6b5ba73) ()  
| Returns the config history of this terminal line. [More...](class_terminal_line.html#a4368feafbe4728a80964ccaeb6b5ba73)  
  
[CommandHistory](struct_command_history.html) | [getCurrentHistory](class_terminal_line.html#ad7dafae12b5b9bc991ad0cf075bc0f9d) ()  
| Returns the current history of this terminal line. [More...](class_terminal_line.html#ad7dafae12b5b9bc991ad0cf075bc0f9d)  
  
int | [getHistorySize](class_terminal_line.html#ab7348cc84b66599236f9e2a2efddad78) ()  
| Returns the history size. [More...](class_terminal_line.html#ab7348cc84b66599236f9e2a2efddad78)  
  
string | [getCommandInput](class_terminal_line.html#a13ea7732d8a55998e60d96c8e797c8c9) ()  
| Returns the command input. [More...](class_terminal_line.html#a13ea7732d8a55998e60d96c8e797c8c9)  
  
int | [getTelnetClientCount](class_terminal_line.html#ac0460da67d957952cc4c308a11664adb) ()  
| Returns the number of telnet clients. [More...](class_terminal_line.html#ac0460da67d957952cc4c308a11664adb)  
  
[TelnetClientProcess](class_telnet_client_process.html) | [getTelnetClientAt](class_terminal_line.html#a4be5763088362f0f28e133d18e93806f) (int)  
| Returns the telnet client at the specified index. [More...](class_terminal_line.html#a4be5763088362f0f28e133d18e93806f)  
  
void | [enterCommand](class_terminal_line.html#a70d6a4cb8c959c920778e90632c9eab8) (string)  
| Enters a command to the terminal line. [More...](class_terminal_line.html#a70d6a4cb8c959c920778e90632c9eab8)  
  
void | [terminalUpdated](class_terminal_line.html#a4a975b659dc49d70da82b03b85edbf87) (string)  
| [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. [More...](class_terminal_line.html#a4a975b659dc49d70da82b03b85edbf87)  
  
void | [moreDisplayed](class_terminal_line.html#aa8b3fbe81be8e8d090ab967c15dc02ae) ()  
| Event happens when a –More– display is generated. [More...](class_terminal_line.html#aa8b3fbe81be8e8d090ab967c15dc02ae)  
  
void | [enterChar](class_terminal_line.html#a6df8d9d2cbf321dda2f80764b0a7f9c4) (byte, SpecialChar)  
| Enters the specified ascii or special character into the terminal. [More...](class_terminal_line.html#a6df8d9d2cbf321dda2f80764b0a7f9c4)  
  
void | [outputWritten](class_terminal_line.html#a3708edcec4d0a2b48754fa44d1d16cfd) (string, bool, int)  
| This event is emitted when output is written to the terminal line. [More...](class_terminal_line.html#a3708edcec4d0a2b48754fa44d1d16cfd)  
  
void | [cursorPositionChanged](class_terminal_line.html#a048769188c51bb6179c1d5c981c0bb92) (int)  
| This event is emitted when the cursor position has moved to the specified position from the end of the terminal. [More...](class_terminal_line.html#a048769188c51bb6179c1d5c981c0bb92)  
  
void | [directiveSent](class_terminal_line.html#a3cfb6a714239ebf3d8b4ddcc4bcbeff3) (DirectiveCommand, int)  
| This event is emitted when a directive command is sent. [More...](class_terminal_line.html#a3cfb6a714239ebf3d8b4ddcc4bcbeff3)  
  
void | [commandStarted](class_terminal_line.html#a10c3f8749a6c7e222f635c59659c3c12) (string, string, string, string)  
| This event is emitted when a command has started. [More...](class_terminal_line.html#a10c3f8749a6c7e222f635c59659c3c12)  
  
void | [commandEnded](class_terminal_line.html#a7ddbecb43ec1195b545b54f1c683a699) (string, CommandStatus)  
| This event is emitted when a command has ended. [More...](class_terminal_line.html#a7ddbecb43ec1195b545b54f1c683a699)  
  
void | [commandAutoCompleted](class_terminal_line.html#a01dd8523a2f17a3161474d88572de762) (string, string)  
| This event is emitted when a command has been auto completed. [More...](class_terminal_line.html#a01dd8523a2f17a3161474d88572de762)  
  
void | [modeChanged](class_terminal_line.html#ae7587768dac1add7c8c04e20f45ed52d) (string, string, string)  
| This event is emitted when the mode has changed. [More...](class_terminal_line.html#ae7587768dac1add7c8c04e20f45ed52d)  
  
void | [promptChanged](class_terminal_line.html#ade7a580a7054ee3f3f1f89a8efeb02cb) (string)  
| This event is emitted when the prompt has changed. [More...](class_terminal_line.html#ade7a580a7054ee3f3f1f89a8efeb02cb)  
  
void | [commandSelectedFromHistory](class_terminal_line.html#aeaf25f1cb4f33673d114b8eb24350adc) (string)  
| This event is emitted when a command from the history has been selected. [More...](class_terminal_line.html#aeaf25f1cb4f33673d114b8eb24350adc)  
  
void | [setSettings](class_terminal_line.html#a1bc41a2b5c3bf785600694f1ad2ffd36) (int, string, Parity, string, FlowControl)  
| Sets the connection settings to this terminal. [More...](class_terminal_line.html#a1bc41a2b5c3bf785600694f1ad2ffd36)  
  
int | [getSpeed](class_terminal_line.html#a25f350ccc9d7d8c3bac9ef89054ddb0b) () const  
byte | [getDataBits](class_terminal_line.html#a4c98ba5080dc64e6dd07549727587585) () const  
Parity | [getParity](class_terminal_line.html#a2a50b35c66832d8eff8c7d2f3af32ce2) () const  
string | [getStopBits](class_terminal_line.html#a5bd813bef863fde0edc52c2bc6c55ad3) () const  
FlowControl | [getFlowControl](class_terminal_line.html#a6bc85e3c77bd759224e4734ed6dc5217) () const  
void | [println](class_terminal_line.html#ac74ba0c140a4a00f6642fa56b4ed5c6d) (string)  
| This function gets the flow control. [More...](class_terminal_line.html#ac74ba0c140a4a00f6642fa56b4ed5c6d)  
  
void | [flush](class_terminal_line.html#a838023327a1971ddc0ebdc3a12b7d123) (int)  
| This function remove the first number of lines in the buffer. [More...](class_terminal_line.html#a838023327a1971ddc0ebdc3a12b7d123)  
  
  
## Detailed Description

[ConsoleLine](class_console_line.html "ConsoleLine is the console line handler for the TerminalLine object.") is the console line handler for the [TerminalLine](class_terminal_line.html "TerminalLine manages the terminal lines, virtual terminal lines, and console lines.") object. 

## Member Function Documentation

## ◆ getOutput()

string ConsoleLine::getOutput  | ( | | ) |   
---|---|---|---|---  
  
Returns the output from the console line. 

Parameters
     string,the| output from the console line.   
---|---  
  
## ◆ idledOut()

void ConsoleLine::idledOut  | ( | | ) |   
---|---|---|---|---  
  
When the terminal line idles out this event is generated. 

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

* * *

The documentation for this class was generated from the following file:

  * [CConsoleLine.pki](_c_console_line_8pki.html)


