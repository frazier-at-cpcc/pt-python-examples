# Cisco Packet Tracer Extensions API: ParserViewManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_parser_view_manager.html

---

[ParserViewManager](class_parser_view_manager.html "ParserViewManager manages and manipulates the parser view.") manages and manipulates the parser view. [More...](class_parser_view_manager.html#details)

##  Public Member Functions  
  
---  
bool | [addView](class_parser_view_manager.html#a92c5356fc74bed6e054a65e3e3a8a59c) (string)  
| Adds a view with the specified name. [More...](class_parser_view_manager.html#a92c5356fc74bed6e054a65e3e3a8a59c)  
  
bool | [removeView](class_parser_view_manager.html#a75f8b70edcbf26e2ea3f88138902e16f) (string)  
| Removes the view the specified name. [More...](class_parser_view_manager.html#a75f8b70edcbf26e2ea3f88138902e16f)  
  
int | [getViewCount](class_parser_view_manager.html#a642c5593ef0e090391a091e0f73da62d) ()  
| Returns the number of views. [More...](class_parser_view_manager.html#a642c5593ef0e090391a091e0f73da62d)  
  
[ParserView](class_parser_view.html) | [getViewAt](class_parser_view_manager.html#a643f147c58c34e75b387f59203e3f9c8) (int)  
| Returns the view at the specified index. [More...](class_parser_view_manager.html#a643f147c58c34e75b387f59203e3f9c8)  
  
[ParserView](class_parser_view.html) | [getView](class_parser_view_manager.html#a73c542c2bc773aece71a066ecd69c1ab) (string)  
| Returns the view with the specified name. [More...](class_parser_view_manager.html#a73c542c2bc773aece71a066ecd69c1ab)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[ParserViewManager](class_parser_view_manager.html "ParserViewManager manages and manipulates the parser view.") manages and manipulates the parser view. 

## Member Function Documentation

## ◆ addView()

bool ParserViewManager::addView  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Adds a view with the specified name. 

Parameters
     viewName,the| name for the view.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ getView()

[ParserView](class_parser_view.html) ParserViewManager::getView  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the view with the specified name. 

Parameters
     name,the| name of the view of interest.  
---|---  
  
Returns
    [ParserView](class_parser_view.html "ParserView handles and manipulates parser views."), the [ParserView](class_parser_view.html "ParserView handles and manipulates parser views.") object with the specified name. 

## ◆ getViewAt()

[ParserView](class_parser_view.html) ParserViewManager::getViewAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the view at the specified index. 

Parameters
     index,the| index of the view of interest.  
---|---  
  
Returns
    [ParserView](class_parser_view.html "ParserView handles and manipulates parser views."), the [ParserView](class_parser_view.html "ParserView handles and manipulates parser views.") object at the specified index. 

## ◆ getViewCount()

int ParserViewManager::getViewCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of views. 

Returns
    int, the number of views. 

## ◆ removeView()

bool ParserViewManager::removeView  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes the view the specified name. 

Parameters
     viewName,the| name of the view.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

* * *

The documentation for this class was generated from the following file:

  * [CParserViewManager.pki](_c_parser_view_manager_8pki.html)


