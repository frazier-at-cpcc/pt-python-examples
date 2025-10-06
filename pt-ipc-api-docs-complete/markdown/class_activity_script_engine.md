# Cisco Packet Tracer Extensions API: ActivityScriptEngine Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_activity_script_engine.html

---

This class provides access to activity related scripting functions. [More...](class_activity_script_engine.html#details)

##  Public Member Functions  
  
---  
[AssessmentModelScriptInterface](class_assessment_model_script_interface.html) | [getAssessmentModelScriptInterface](class_activity_script_engine.html#a208169850c6a8d31999160de49dd85a1) ()  
| Returns the Assessment Model Script Interface. [More...](class_activity_script_engine.html#a208169850c6a8d31999160de49dd85a1)  
  
Public Member Functions inherited from [EMEAScriptEngine](class_e_m_e_a_script_engine.html)  
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

This class provides access to activity related scripting functions. 

## Member Function Documentation

## ◆ getAssessmentModelScriptInterface()

[AssessmentModelScriptInterface](class_assessment_model_script_interface.html) ActivityScriptEngine::getAssessmentModelScriptInterface  | ( | | ) |   
---|---|---|---|---  
  
Returns the Assessment Model Script Interface. 

Remarks
    The Assessment Model Script Interface's functions are mainly used to expose core functionality to the script engine, but may also be used in the [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.").

Returns
    [AssessmentModelScriptInterface](class_assessment_model_script_interface.html "This class handles the Assessment Model Script Interface."), the Assessment Model Script Interface. 

* * *

The documentation for this class was generated from the following file:

  * [CActivityScriptEngine.pki](_c_activity_script_engine_8pki.html)


