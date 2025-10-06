# Cisco Packet Tracer Extensions API: EMEAScriptEngine Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_e_m_e_a_script_engine.html

---

[EMEAScriptEngine](class_e_m_e_a_script_engine.html "EMEAScriptEngine gives access to Packet Tracer's Script Engine.") gives access to Packet Tracer's Script Engine. [More...](class_e_m_e_a_script_engine.html#details)

##  Public Member Functions  
  
---  
[ScriptValue](class_script_value.html) | [evaluateFile](class_e_m_e_a_script_engine.html#a352929d04d5e07bcdae05b69e23065ae) (QString)  
| Evaluates the specified script. [More...](class_e_m_e_a_script_engine.html#a352929d04d5e07bcdae05b69e23065ae)  
  
bool | [canEvaluate](class_e_m_e_a_script_engine.html#a737a1e4ca175d2a06ce840c0733b24f3) (QString)  
| Returns true if the specified script can be evaluated, otherwise false. [More...](class_e_m_e_a_script_engine.html#a737a1e4ca175d2a06ce840c0733b24f3)  
  
[ScriptValue](class_script_value.html) | [globalObject](class_e_m_e_a_script_engine.html#ae76812ee22cb9467b75d5331238e028f) ()  
| Returns the global [ScriptValue](class_script_value.html "ScriptValue provides functionality to convert this script Engines values to basic types.") object. [More...](class_e_m_e_a_script_engine.html#ae76812ee22cb9467b75d5331238e028f)  
  
[ScriptValue](class_script_value.html) | [evaluate](class_e_m_e_a_script_engine.html#ae55c34c791f5ff88c93f2f7c2917726d) (QString, QString)  
| Evaluates the specified script. [More...](class_e_m_e_a_script_engine.html#ae55c34c791f5ff88c93f2f7c2917726d)  
  
[ScriptValue](class_script_value.html) | [createScriptValueInt](class_e_m_e_a_script_engine.html#a8823bc7ce5ff8b8dfa6d28c9d79cc6ec) (int)  
| Creates a [ScriptValue](class_script_value.html "ScriptValue provides functionality to convert this script Engines values to basic types.") object with the specified integer value. [More...](class_e_m_e_a_script_engine.html#a8823bc7ce5ff8b8dfa6d28c9d79cc6ec)  
  
[ScriptValue](class_script_value.html) | [createScriptValueBool](class_e_m_e_a_script_engine.html#acdadf366d566ff61ded9ba1732a795be) (bool)  
| Creates a [ScriptValue](class_script_value.html "ScriptValue provides functionality to convert this script Engines values to basic types.") object with the specified boolean value. [More...](class_e_m_e_a_script_engine.html#acdadf366d566ff61ded9ba1732a795be)  
  
[ScriptValue](class_script_value.html) | [createScriptValueQString](class_e_m_e_a_script_engine.html#a404545db35f19befb6755a02d1bf7d52) (QString)  
| Creates a [ScriptValue](class_script_value.html "ScriptValue provides functionality to convert this script Engines values to basic types.") object with the specified QString value. [More...](class_e_m_e_a_script_engine.html#a404545db35f19befb6755a02d1bf7d52)  
  
  
## Detailed Description

[EMEAScriptEngine](class_e_m_e_a_script_engine.html "EMEAScriptEngine gives access to Packet Tracer's Script Engine.") gives access to Packet Tracer's Script Engine. 

## Member Function Documentation

## ◆ canEvaluate()

bool EMEAScriptEngine::canEvaluate  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns true if the specified script can be evaluated, otherwise false. 

Parameters
     program,the| code of the script of interest.  
---|---  
  
Returns
    bool, true if the specified script can be evaluated, otherwise false. 

## ◆ createScriptValueBool()

[ScriptValue](class_script_value.html) EMEAScriptEngine::createScriptValueBool  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Creates a [ScriptValue](class_script_value.html "ScriptValue provides functionality to convert this script Engines values to basic types.") object with the specified boolean value. 

Parameters
     value,the| boolean value of the [ScriptValue](class_script_value.html "ScriptValue provides functionality to convert this script Engines values to basic types.") object.  
---|---  
  
Returns
    [ScriptValue](class_script_value.html "ScriptValue provides functionality to convert this script Engines values to basic types."), the [ScriptValue](class_script_value.html "ScriptValue provides functionality to convert this script Engines values to basic types.") object. 

## ◆ createScriptValueInt()

[ScriptValue](class_script_value.html) EMEAScriptEngine::createScriptValueInt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Creates a [ScriptValue](class_script_value.html "ScriptValue provides functionality to convert this script Engines values to basic types.") object with the specified integer value. 

Parameters
     value,the| integer value of the [ScriptValue](class_script_value.html "ScriptValue provides functionality to convert this script Engines values to basic types.") object.  
---|---  
  
Returns
    [ScriptValue](class_script_value.html "ScriptValue provides functionality to convert this script Engines values to basic types."), the [ScriptValue](class_script_value.html "ScriptValue provides functionality to convert this script Engines values to basic types.") object. 

## ◆ createScriptValueQString()

[ScriptValue](class_script_value.html) EMEAScriptEngine::createScriptValueQString  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Creates a [ScriptValue](class_script_value.html "ScriptValue provides functionality to convert this script Engines values to basic types.") object with the specified QString value. 

Parameters
     value,the| QString value of the [ScriptValue](class_script_value.html "ScriptValue provides functionality to convert this script Engines values to basic types.") object.  
---|---  
  
Returns
    [ScriptValue](class_script_value.html "ScriptValue provides functionality to convert this script Engines values to basic types."), the [ScriptValue](class_script_value.html "ScriptValue provides functionality to convert this script Engines values to basic types.") object. 

## ◆ evaluate()

[ScriptValue](class_script_value.html) EMEAScriptEngine::evaluate  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Evaluates the specified script. 

Parameters
     program,the| code of the script of interest.   
---|---  
id,the| name of the script of interest.  
  
Returns
    [ScriptValue](class_script_value.html "ScriptValue provides functionality to convert this script Engines values to basic types."), the [ScriptValue](class_script_value.html "ScriptValue provides functionality to convert this script Engines values to basic types.") object of the specified script. 

## ◆ evaluateFile()

[ScriptValue](class_script_value.html) EMEAScriptEngine::evaluateFile  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Evaluates the specified script. 

Parameters
     filepath,the| filepath of the script of interest.  
---|---  
  
Returns
    [ScriptValue](class_script_value.html "ScriptValue provides functionality to convert this script Engines values to basic types."), the [ScriptValue](class_script_value.html "ScriptValue provides functionality to convert this script Engines values to basic types.") object of the specified script. 

## ◆ globalObject()

[ScriptValue](class_script_value.html) EMEAScriptEngine::globalObject  | ( | | ) |   
---|---|---|---|---  
  
Returns the global [ScriptValue](class_script_value.html "ScriptValue provides functionality to convert this script Engines values to basic types.") object. 

Returns
    [ScriptValue](class_script_value.html "ScriptValue provides functionality to convert this script Engines values to basic types."), the global [ScriptValue](class_script_value.html "ScriptValue provides functionality to convert this script Engines values to basic types.") object. 

* * *

The documentation for this class was generated from the following file:

  * [CEMEAScriptEngine.pki](_c_e_m_e_a_script_engine_8pki.html)


