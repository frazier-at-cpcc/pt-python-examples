# Cisco Packet Tracer Extensions API: TerminalLine Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_terminal_line.html

---

[TerminalLine](class_terminal_line.html "TerminalLine manages the terminal lines, virtual terminal lines, and console lines.") manages the terminal lines, virtual terminal lines, and console lines. [More...](class_terminal_line.html#details)

##  Public Member Functions  
  
---  
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

[TerminalLine](class_terminal_line.html "TerminalLine manages the terminal lines, virtual terminal lines, and console lines.") manages the terminal lines, virtual terminal lines, and console lines. 

## Member Function Documentation

## ◆ commandAutoCompleted()

void TerminalLine::commandAutoCompleted  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
This event is emitted when a command has been auto completed. 

  * inputCommand, the user-entered command. 
  * completeCommand, the resolved complete command.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ commandEnded()

void TerminalLine::commandEnded  | ( | string  | ,   
---|---|---|---  
|  | CommandStatus  |   
| ) | |   
  
This event is emitted when a command has ended. 

  * inputCommand, the user-entered command. 
  * status, the command status. Command statuses: eStatusOk = 0, eErrorAmbiguous = 1, eErrorInvalid = 2, eErrorIncomplete = 3, eErrorNotImplemented = 4



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ commandSelectedFromHistory()

void TerminalLine::commandSelectedFromHistory  | ( | string  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when a command from the history has been selected. 

  * historyCommand, the command from the history that was selected.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ commandStarted()

void TerminalLine::commandStarted  | ( | string  | ,   
---|---|---|---  
|  | string  | ,   
|  | string  | ,   
|  | string  |   
| ) | |   
  
This event is emitted when a command has started. 

  * inputCommand, the user-entered command. 
  * completeCommand, the resolved complete command. 
  * processedCommand, the completed commands processed without errors. 
  * inputMode, the mode where the command is executed.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ cursorPositionChanged()

void TerminalLine::cursorPositionChanged  | ( | int  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when the cursor position has moved to the specified position from the end of the terminal. 

  * positionFromEnd, the position from the end of the terminal.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ directiveSent()

void TerminalLine::directiveSent  | ( | DirectiveCommand  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
This event is emitted when a directive command is sent. 

  * directiveCommand, the directive command that was sent. Directive commands: eBackspace = 0, eDeleteLine = 1 
  * cursorPositionFromEnd, where the output is inserted from the end of the buffer as a positive number or 0; 0 means the end.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ enterChar()

void TerminalLine::enterChar  | ( | byte  | ,   
---|---|---|---  
|  | SpecialChar  |   
| ) | |   
  
Enters the specified ascii or special character into the terminal. 

Parameters
     ascii,any| ASCII character. Includes: Backspace = 8 Ctrl+C = 3 Ctrl+Z = 26 Ctrl+Shift+6 = 30 Enter = 13 Line Feed = 10 Tab = 9 Question = '?' Space = ' ' Ctrl+B = 2 Ctrl+F = 6 Ctrl+P = 16 Ctrl+N = 14 Ctrl+A = 1 Ctrl+E = 5 Ctrl+U = 21   
---|---  
enum<SpecialChar>,a| special character key. Special characters: eNoChar = 0, eArrowRight = 1, eArrowLeft, eArrowUp, eArrowDown  
  
Remarks
    If ascii is 0, then specialChar will be examined. 

## ◆ enterCommand()

void TerminalLine::enterCommand  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Enters a command to the terminal line. 

## ◆ flush()

void TerminalLine::flush  | ( | int  | | ) |   
---|---|---|---|---|---  
  
This function remove the first number of lines in the buffer. 

Parameters
     lineCount,the| number of lines to be removed   
---|---  
  
## ◆ getCommandInput()

string TerminalLine::getCommandInput  | ( | | ) |   
---|---|---|---|---  
  
Returns the command input. 

Returns
    string, the command input. 

## ◆ getConfigHistory()

[CommandHistory](struct_command_history.html) TerminalLine::getConfigHistory  | ( | | ) |   
---|---|---|---|---  
  
Returns the config history of this terminal line. 

Returns
    [CommandHistory](struct_command_history.html "Data element for CommandHistory."), the [CommandHistory](struct_command_history.html "Data element for CommandHistory.") object. 

## ◆ getCurrentHistory()

[CommandHistory](struct_command_history.html) TerminalLine::getCurrentHistory  | ( | | ) |   
---|---|---|---|---  
  
Returns the current history of this terminal line. 

Returns
    [CommandHistory](struct_command_history.html "Data element for CommandHistory."), the [CommandHistory](struct_command_history.html "Data element for CommandHistory.") object. 

## ◆ getDataBits()

byte TerminalLine::getDataBits  | ( | | ) |  const  
---|---|---|---|---  
  
This function gets the data bits. 

## ◆ getFlowControl()

FlowControl TerminalLine::getFlowControl  | ( | | ) |  const  
---|---|---|---|---  
  
This function gets the flow control. 

## ◆ getHistorySize()

int TerminalLine::getHistorySize  | ( | | ) |   
---|---|---|---|---  
  
Returns the history size. 

Returns
    int, the history size. 

## ◆ getMode()

string TerminalLine::getMode  | ( | | ) |   
---|---|---|---|---  
  
Returns the mode this terminal line is in. 

Returns
    string, the mode this terminal line is in. 

## ◆ getName()

string TerminalLine::getName  | ( | | ) |   
---|---|---|---|---  
  
Returns the name of this terminal line. 

Returns
    string, the name of this terminal line. 

## ◆ getOwnerDevice()

[Device](class_device.html) TerminalLine::getOwnerDevice  | ( | | ) |   
---|---|---|---|---  
  
Returns the owner device of this terminal line. 

Returns
    [Device](class_device.html "Device is the base class for all device objects."), the device that owns this terminal line. 

## ◆ getParity()

Parity TerminalLine::getParity  | ( | | ) |  const  
---|---|---|---|---  
  
Parameters
     [in]| parity| a parity bit value 
    
    
        This function sets the parity bit.
      
  
---|---|---  
  
## ◆ getPrompt()

string TerminalLine::getPrompt  | ( | | ) |   
---|---|---|---|---  
  
Returns the prompt of this terminal line. 

Returns
    string, the prompt of this terminal line. 

## ◆ getSpeed()

int TerminalLine::getSpeed  | ( | | ) |  const  
---|---|---|---|---  
  
This function gets the baud rate. 

## ◆ getStopBits()

string TerminalLine::getStopBits  | ( | | ) |  const  
---|---|---|---|---  
  
This function gets the stop bits. 

## ◆ getTelnetClientAt()

[TelnetClientProcess](class_telnet_client_process.html) TerminalLine::getTelnetClientAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the telnet client at the specified index. 

Parameters
     index,the| index of the telnet client of interest.  
---|---  
  
Returns
    [TelnetClientProcess](class_telnet_client_process.html "TelnetClientProcess handles and manipulates the Telnet client."), the [TelnetClientProcess](class_telnet_client_process.html "TelnetClientProcess handles and manipulates the Telnet client.") object at the specified index. 

## ◆ getTelnetClientCount()

int TerminalLine::getTelnetClientCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of telnet clients. 

Returns
    int, the number of telnet clients. 

## ◆ getUserHistory()

[CommandHistory](struct_command_history.html) TerminalLine::getUserHistory  | ( | | ) |   
---|---|---|---|---  
  
Returns the user history of this terminal line. 

Returns
    [CommandHistory](struct_command_history.html "Data element for CommandHistory."), the [CommandHistory](struct_command_history.html "Data element for CommandHistory.") object. 

## ◆ modeChanged()

void TerminalLine::modeChanged  | ( | string  | ,   
---|---|---|---  
|  | string  | ,   
|  | string  |   
| ) | |   
  
This event is emitted when the mode has changed. 

  * newMode, the new mode name. 
  * newModeArg, includes extra info to identify the new mode. 
  * newPrompt, the new prompt.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ moreDisplayed()

void TerminalLine::moreDisplayed  | ( | | ) |   
---|---|---|---|---  
  
Event happens when a –More– display is generated. 

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ outputWritten()

void TerminalLine::outputWritten  | ( | string  | ,   
---|---|---|---  
|  | bool  | ,   
|  | int  |   
| ) | |   
  
This event is emitted when output is written to the terminal line. 

  * newOutput, the output appended to the terminal. 
  * isDebug, true if the output is debug output, otherwise false. 
  * cursorPositionFromEnd, where the output is inserted from the end of the buffer as a positive number or 0; 0 means the end.



Remarks
    This event replaces [terminalUpdated(string updatedStr)](class_terminal_line.html#a4a975b659dc49d70da82b03b85edbf87 "IPC event."). 
     [VirtualLine](class_virtual_line.html "VirtualLine handles and manipulates the virtual terminal line.") also sends out this event for outputs to Telnet or SSH.

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ println()

void TerminalLine::println  | ( | string  | | ) |   
---|---|---|---|---|---  
  
This function gets the flow control. 

Parameters
     output,the| output string to be printed to terminal line   
---|---  
  
## ◆ promptChanged()

void TerminalLine::promptChanged  | ( | string  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when the prompt has changed. 

  * newPrompt, the new prompt.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ setSettings()

void TerminalLine::setSettings  | ( | int  | ,   
---|---|---|---  
|  | string  | ,   
|  | Parity  | ,   
|  | string  | ,   
|  | FlowControl  |   
| ) | |   
  
Sets the connection settings to this terminal. 

Parameters
     int| speed, any Speed setting of either: 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200   
---|---  
char| bits, The number of data bits, from 5 to 8, inclusive   
enum<Parity>| parity, The parity mode, even, odd, none, mark, space   
string| stopbits, The stop bits, 1, 1.5, or 2   
enum<FlowControl>| flowcontrol, The flow control method, Xon/Xoff, Hardware, None   
  
## ◆ terminalUpdated()

void TerminalLine::terminalUpdated  | ( | string  | | ) |   
---|---|---|---|---|---  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

**[Deprecated:](deprecated.html#_deprecated000006)**
     This event is emitted when the terminal line is updated.

  * updatedStr, the output appended to the terminal. 



* * *

The documentation for this class was generated from the following file:

  * [CTerminalLine.pki](_c_terminal_line_8pki.html)


