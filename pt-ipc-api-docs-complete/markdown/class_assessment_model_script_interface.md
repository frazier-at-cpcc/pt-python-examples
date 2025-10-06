# Cisco Packet Tracer Extensions API: AssessmentModelScriptInterface Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_assessment_model_script_interface.html

---

This class handles the Assessment Model Script Interface. [More...](class_assessment_model_script_interface.html#details)

##  Public Member Functions  
  
---  
QString | [getAssessmentItemValue](class_assessment_model_script_interface.html#ab5dae959af7f5ac1ddaf236affc3c131) (QString, QString)  
| Returns the value of the assessment item for the specified network at the given node. [More...](class_assessment_model_script_interface.html#ab5dae959af7f5ac1ddaf236affc3c131)  
  
vector< QString > | [peakAssessmentItemID](class_assessment_model_script_interface.html#a98e14e7056cedd925bc2f8852ec20e21) (QString, QString)  
| Returns the list of child assessment node IDs for the specified network at the given node. [More...](class_assessment_model_script_interface.html#a98e14e7056cedd925bc2f8852ec20e21)  
  
bool | [setAssessmentItemFeedback](class_assessment_model_script_interface.html#a39c43f3ac946643172e5285d238fe61f) (QString, QString)  
| Sets the assessment item feedback string. [More...](class_assessment_model_script_interface.html#a39c43f3ac946643172e5285d238fe61f)  
  
bool | [refreshAssessmentItemsView](class_assessment_model_script_interface.html#a514601aba01574a3a95d30e2a2060a64) ()  
| Updates the Assessment Item tree view in the Activity Results page. [More...](class_assessment_model_script_interface.html#a514601aba01574a3a95d30e2a2060a64)  
  
void | [setUseCache](class_assessment_model_script_interface.html#acee45c985e833684ce784e5d806a7467) (bool)  
| Enables or Disable the TreeNodes to be cached. [More...](class_assessment_model_script_interface.html#acee45c985e833684ce784e5d806a7467)  
  
  
## Detailed Description

This class handles the Assessment Model Script Interface. 

## Member Function Documentation

## ◆ getAssessmentItemValue()

QString AssessmentModelScriptInterface::getAssessmentItemValue  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Returns the value of the assessment item for the specified network at the given node. 

Parameters
     networkType,where| the following are valid network types: user, answer, initial, lastAssessed, assessed.   
---|---  
idpath,the| path to the assessment item node. For example, Network:PC0:Default Gateway.  
  
Returns
    QString, the value of the assessment item for the specified network. 

## ◆ peakAssessmentItemID()

vector< QString > AssessmentModelScriptInterface::peakAssessmentItemID  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Returns the list of child assessment node IDs for the specified network at the given node. 

Parameters
     networkType,where| the following are valid network types: user, answer, initial, lastAssessed, assessed.   
---|---  
idpath,the| path to the assessment item node. For example, [Network](class_network.html "Network is the entry point for all device configurations in the network. It retrieves devices."):PC0.  
  
Returns
    vector<QString>, the list of child assessment node IDs for the specified network at the given node. 

## ◆ refreshAssessmentItemsView()

bool AssessmentModelScriptInterface::refreshAssessmentItemsView  | ( | | ) |   
---|---|---|---|---  
  
Updates the Assessment Item tree view in the Activity Results page. 

Remarks
    The Activity Results page must be displayed. Refreshing the display is required.

Returns
    bool, true if the Assessment Items view was refreshed successfully, otherwise false. 

## ◆ setAssessmentItemFeedback()

bool AssessmentModelScriptInterface::setAssessmentItemFeedback  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Sets the assessment item feedback string. 

Remarks
    Affects the Check Results display only. It does not change it in the model. The Activity Results page must be displayed. Refreshing the display is required.

Returns
    bool, true if the assessment item feedback was set successfully, otherwise false. 

## ◆ setUseCache()

void AssessmentModelScriptInterface::setUseCache  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or Disable the TreeNodes to be cached. 

Remarks
    The activity comparator tree is a huge tree in larger networks, and performance may degrade. If you do not require the latest values from the tree, you can enable the cache that will get it from the latest creation of the tree. It is best to enable the cache for a set of calls and disable it after. Disabling the cache will clear the cache. Use it in the order of: 1. enable the cache, 2. get values, 3. disable the cache

Parameters
     cache,if| true the Tree Nodes will be cached, false and they won't.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CAssessmentModelScriptInterface.pki](_c_assessment_model_script_interface_8pki.html)


