# Cisco Packet Tracer Extensions API: ParserView Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_parser_view.html

---

[ParserView](class_parser_view.html "ParserView handles and manipulates parser views.") handles and manipulates parser views. [More...](class_parser_view.html#details)

##  Public Member Functions  
  
---  
void | [setSecret](class_parser_view.html#afd78e63d26fd0f362fccc7b46f19284e) (string)  
| Sets the secret. [More...](class_parser_view.html#afd78e63d26fd0f362fccc7b46f19284e)  
  
string | [getSecret](class_parser_view.html#a00b5403850c1d8c5a8f70f02fc5e8200) ()  
| Returns the secret. [More...](class_parser_view.html#a00b5403850c1d8c5a8f70f02fc5e8200)  
  
bool | [addCommand](class_parser_view.html#a8fb21f963705891627ca942c0824f278) (string, string, bool, CommandSet::EViewCommandAction)  
| Adds the specified command to the view. [More...](class_parser_view.html#a8fb21f963705891627ca942c0824f278)  
  
bool | [removeCommand](class_parser_view.html#adfd12fdac852809aae063736e45478bf) (string, string, CommandSet::EViewCommandAction)  
| Removes the specified command from the view. [More...](class_parser_view.html#adfd12fdac852809aae063736e45478bf)  
  
int | [getModeCount](class_parser_view.html#aa414997df0a55901a8b107669611851e) ()  
| Returns the number of modes. [More...](class_parser_view.html#aa414997df0a55901a8b107669611851e)  
  
string | [getModeAt](class_parser_view.html#a4cd5740c9b1d357847dfbebce2af5c66) (int)  
| Returns the mode at the specified index. [More...](class_parser_view.html#a4cd5740c9b1d357847dfbebce2af5c66)  
  
int | [getIncludeCommandForModeCount](class_parser_view.html#a55fa6fcee571ce0daee2d9921a8f7488) (string)  
| Returns the number of include commands for the specified mode. [More...](class_parser_view.html#a55fa6fcee571ce0daee2d9921a8f7488)  
  
pair< string, bool > | [getIncludeCommandForModeAt](class_parser_view.html#af8e05549f77bae15b6c42d11ed689e66) (string, int)  
| Returns the include command in the specified mode at the specified index. [More...](class_parser_view.html#af8e05549f77bae15b6c42d11ed689e66)  
  
pair< string, bool > | [getIncludeCommandForMode](class_parser_view.html#a308dec2367ed0d51a8f43661ab86e362) (string, string)  
| Returns the include command in the specified mode with the specified command. [More...](class_parser_view.html#a308dec2367ed0d51a8f43661ab86e362)  
  
void | [incrementUserCount](class_parser_view.html#a6aea7fe7a35807af0c0e1778dee2303e) ()  
| Increments the number of users. [More...](class_parser_view.html#a6aea7fe7a35807af0c0e1778dee2303e)  
  
void | [decrementUserCount](class_parser_view.html#ad7bf6c8c20e9a1385f94b6549c5cf7e0) ()  
| Decrements the number of users. [More...](class_parser_view.html#ad7bf6c8c20e9a1385f94b6549c5cf7e0)  
  
int | [getUserCount](class_parser_view.html#a5bfa548bf73ab597db051ebdc2ea63d6) ()  
| Returns the number of users. [More...](class_parser_view.html#a5bfa548bf73ab597db051ebdc2ea63d6)  
  
bool | [isCommandAdded](class_parser_view.html#a95ae0e829c0d3dd2ad63848ca14f2d0d) (string)  
| Returns true if the specified command is already added to this view, otherwise false. [More...](class_parser_view.html#a95ae0e829c0d3dd2ad63848ca14f2d0d)  
  
  
## Detailed Description

[ParserView](class_parser_view.html "ParserView handles and manipulates parser views.") handles and manipulates parser views. 

## Member Function Documentation

## ◆ addCommand()

bool ParserView::addCommand  | ( | string  | ,   
---|---|---|---  
|  | string  | ,   
|  | bool  | ,   
|  | CommandSet::EViewCommandAction  |   
| ) | |   
  
Adds the specified command to the view. 

Parameters
     mode,the| mode to add the command to. Valid modes: user, enable, global.   
---|---  
command,the| command of interest.   
bAll,true| to include all, false to not include all.   
action,the| view command action. Actions: eViewCommandInclude = 0, eViewCommandExclude = 1, eViewCommandIncludeExclusive = 2  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ decrementUserCount()

void ParserView::decrementUserCount  | ( | | ) |   
---|---|---|---|---  
  
Decrements the number of users. 

## ◆ getIncludeCommandForMode()

pair< string, bool > ParserView::getIncludeCommandForMode  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Returns the include command in the specified mode with the specified command. 

Parameters
     mode,the| mode of interest. Valid modes: user, enable, global.   
---|---  
command,the| command of interest.  
  
Returns
    pair<string, bool>, the include command and a boolean value that is true if included in all, otherwise false. 

## ◆ getIncludeCommandForModeAt()

pair< string, bool > ParserView::getIncludeCommandForModeAt  | ( | string  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Returns the include command in the specified mode at the specified index. 

Parameters
     mode,the| mode of interest. Valid modes: user, enable, global.   
---|---  
index,the| index of the include command of interest.  
  
Returns
    pair<string, bool>, the include command and a boolean value that is true if included in all, otherwise false. 

## ◆ getIncludeCommandForModeCount()

int ParserView::getIncludeCommandForModeCount  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the number of include commands for the specified mode. 

Parameters
     mode,the| mode of interest. Valid modes: user, enable, global.  
---|---  
  
Returns
    int, the number of include commands for the specified mode. 

## ◆ getModeAt()

string ParserView::getModeAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the mode at the specified index. 

Parameters
     index,the| index of the mode of interest.  
---|---  
  
Returns
    string, mode at the specified index. 

## ◆ getModeCount()

int ParserView::getModeCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of modes. 

Returns
    int, the number of modes. 

## ◆ getSecret()

string ParserView::getSecret  | ( | | ) |   
---|---|---|---|---  
  
Returns the secret. 

Returns
    string, the secret. 

## ◆ getUserCount()

int ParserView::getUserCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of users. 

Returns
    int, the number of users. 

## ◆ incrementUserCount()

void ParserView::incrementUserCount  | ( | | ) |   
---|---|---|---|---  
  
Increments the number of users. 

## ◆ isCommandAdded()

bool ParserView::isCommandAdded  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns true if the specified command is already added to this view, otherwise false. 

Parameters
     commandStr,the| command string to use.  
---|---  
  
Returns
    bool, true if the specified command is already added to this view, otherwise false. 

## ◆ removeCommand()

bool ParserView::removeCommand  | ( | string  | ,   
---|---|---|---  
|  | string  | ,   
|  | CommandSet::EViewCommandAction  |   
| ) | |   
  
Removes the specified command from the view. 

Parameters
     mode,the| mode to remove the command from. Valid modes: user, enable, global.   
---|---  
command,the| command of interest.   
action,the| view command action. Actions: eViewCommandInclude = 0, eViewCommandExclude = 1, eViewCommandIncludeExclusive = 2  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ setSecret()

void ParserView::setSecret  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the secret. 

Parameters
     secretStr,the| secret.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CParserView.pki](_c_parser_view_8pki.html)


