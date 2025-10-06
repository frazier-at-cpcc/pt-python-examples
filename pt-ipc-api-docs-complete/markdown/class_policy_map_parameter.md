# Cisco Packet Tracer Extensions API: PolicyMapParameter Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_policy_map_parameter.html

---

##  Public Member Functions  
  
---  
string | [getPolicyMapName](class_policy_map_parameter.html#a03b05b889a85232d34982f252677e186) ()  
| Returns the policyMap name that is being used. [More...](class_policy_map_parameter.html#a03b05b889a85232d34982f252677e186)  
  
vector< string > | [getRunningConfig](class_policy_map_parameter.html#a14704c93ab2d966d41b988cafd234239) ()  
| Returns the running config string representation of policy map parameter. [More...](class_policy_map_parameter.html#a14704c93ab2d966d41b988cafd234239)  
  
int | [getStatementCnt](class_policy_map_parameter.html#ae7dd434b674ac98de6294dfa2e8b985f) ()  
| Returns the number of statements configured under policy map parameter. [More...](class_policy_map_parameter.html#ae7dd434b674ac98de6294dfa2e8b985f)  
  
[PolicyMapParameterStatement](class_policy_map_parameter_statement.html) | [getStatementAt](class_policy_map_parameter.html#a65cc478c17ff21f20c4f69e629a60b09) (int)  
| Returns the policyMap name parameter statement based on index. [More...](class_policy_map_parameter.html#a65cc478c17ff21f20c4f69e629a60b09)  
  
[PolicyMapParameterStatement](class_policy_map_parameter_statement.html) | [getStatement](class_policy_map_parameter.html#ad5cd7796aaa47d1ecb9e8e35df910d1d) (string)  
| Returns the policy map parameter statement based on the string representation. [More...](class_policy_map_parameter.html#ad5cd7796aaa47d1ecb9e8e35df910d1d)  
  
string | [toString](class_policy_map_parameter.html#a2f1f308395b4e9e4cae182e019415dc2) ()  
| Return the configuration in string. [More...](class_policy_map_parameter.html#a2f1f308395b4e9e4cae182e019415dc2)  
  
  
## Member Function Documentation

## ◆ getPolicyMapName()

string PolicyMapParameter::getPolicyMapName  | ( | | ) |   
---|---|---|---|---  
  
Returns the policyMap name that is being used. 

Returns
    string, the policy map name. 

## ◆ getRunningConfig()

vector< string > PolicyMapParameter::getRunningConfig  | ( | | ) |   
---|---|---|---|---  
  
Returns the running config string representation of policy map parameter. 

Returns
    vector<string> returns the running config string representation of policy map parameter. 

## ◆ getStatement()

[PolicyMapParameterStatement](class_policy_map_parameter_statement.html) PolicyMapParameter::getStatement  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the policy map parameter statement based on the string representation. 

Parameters
     statement,statement| to get the policy map for.  
---|---  
  
Returns
    PolicyMapParametersStatement, the policy map parameter statement based on the string representation. 

## ◆ getStatementAt()

[PolicyMapParameterStatement](class_policy_map_parameter_statement.html) PolicyMapParameter::getStatementAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the policyMap name parameter statement based on index. 

Parameters
     index,index| to get the policy map from.  
---|---  
  
Returns
    [PolicyMapParameterStatement](class_policy_map_parameter_statement.html), the policyMap name parameter statement based on index 

## ◆ getStatementCnt()

int PolicyMapParameter::getStatementCnt  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of statements configured under policy map parameter. 

return int, the number of statements configured under policy map parameter. 

## ◆ toString()

string PolicyMapParameter::toString  | ( | | ) |   
---|---|---|---|---  
  
Return the configuration in string. 

Returns
    string, the configuration as a string. 

* * *

The documentation for this class was generated from the following file:

  * [CPolicyMapParameter.pki](_c_policy_map_parameter_8pki.html)


