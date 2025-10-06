# Cisco Packet Tracer Extensions API: VariableManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_variable_manager.html

---

[VariableManager](class_variable_manager.html "VariableManager manages the variables and pools in an activity.") manages the variables and pools in an activity. [More...](class_variable_manager.html#details)

##  Public Member Functions  
  
---  
int | [getVariableSize](class_variable_manager.html#a20be790b563338a78c010dd1aaf7f838) ()  
| Returns the total number of variables. [More...](class_variable_manager.html#a20be790b563338a78c010dd1aaf7f838)  
  
[Variable](class_variable.html) | [getVariable](class_variable_manager.html#a73123304c2d248d1250410e51e29f87d) (int)  
| Returns the variable at the specified index. [More...](class_variable_manager.html#a73123304c2d248d1250410e51e29f87d)  
  
[Variable](class_variable.html) | [getVariableByName](class_variable_manager.html#ae5bce0831ad4fb814b2bc7008d948255) (QString)  
| Returns the variable with the specified name. [More...](class_variable_manager.html#ae5bce0831ad4fb814b2bc7008d948255)  
  
int | [getNumberPoolSize](class_variable_manager.html#af98e25f88d74b777d3c7c8985a6f8ebf) ()  
| Returns the number of variables in the number pool. [More...](class_variable_manager.html#af98e25f88d74b777d3c7c8985a6f8ebf)  
  
int | [getStringPoolSize](class_variable_manager.html#ac492c90dc511c604bc45f42d7a520ba4) ()  
| Returns the number of variables in the string pool. [More...](class_variable_manager.html#ac492c90dc511c604bc45f42d7a520ba4)  
  
int | [getIpPoolSize](class_variable_manager.html#abe0c19e3c6278a31b0fd3bbd826c0c2e) ()  
| Returns the number of variables in the IP pool. [More...](class_variable_manager.html#abe0c19e3c6278a31b0fd3bbd826c0c2e)  
  
[Pool](class_pool.html) | [getNumberPoolAt](class_variable_manager.html#a5fd8c3e094d8193433dd3064bccc640a) (int)  
| Returns the number pool at the specified index. [More...](class_variable_manager.html#a5fd8c3e094d8193433dd3064bccc640a)  
  
[Pool](class_pool.html) | [getStringPoolAt](class_variable_manager.html#a969be794daae9abbec62a14be2fec071) (int)  
| Returns the string pool at the specified index. [More...](class_variable_manager.html#a969be794daae9abbec62a14be2fec071)  
  
[Pool](class_pool.html) | [getIpPoolAt](class_variable_manager.html#a408b70151018f788095d769b680d386e) (int)  
| Returns the IP pool at the specified index. [More...](class_variable_manager.html#a408b70151018f788095d769b680d386e)  
  
  
## Detailed Description

[VariableManager](class_variable_manager.html "VariableManager manages the variables and pools in an activity.") manages the variables and pools in an activity. 

## Member Function Documentation

## ◆ getIpPoolAt()

[Pool](class_pool.html) VariableManager::getIpPoolAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the IP pool at the specified index. 

Parameters
     i,the| index of the IP pool of interest.  
---|---  
  
Returns
    [Pool](class_pool.html "Pool is the base class for all variable pools for activities."), the [Pool](class_pool.html "Pool is the base class for all variable pools for activities.") object at the specified index. 

## ◆ getIpPoolSize()

int VariableManager::getIpPoolSize  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of variables in the IP pool. 

Returns
    int, the number of variables in the IP pool. 

## ◆ getNumberPoolAt()

[Pool](class_pool.html) VariableManager::getNumberPoolAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the number pool at the specified index. 

Parameters
     i,the| index of the number pool of interest.  
---|---  
  
Returns
    [Pool](class_pool.html "Pool is the base class for all variable pools for activities."), the [Pool](class_pool.html "Pool is the base class for all variable pools for activities.") object at the specified index. 

## ◆ getNumberPoolSize()

int VariableManager::getNumberPoolSize  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of variables in the number pool. 

Returns
    int, the number of variables in the number pool. 

## ◆ getStringPoolAt()

[Pool](class_pool.html) VariableManager::getStringPoolAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the string pool at the specified index. 

Parameters
     i,the| index of the string pool of interest.  
---|---  
  
Returns
    [Pool](class_pool.html "Pool is the base class for all variable pools for activities."), the [Pool](class_pool.html "Pool is the base class for all variable pools for activities.") object at the specified index. 

## ◆ getStringPoolSize()

int VariableManager::getStringPoolSize  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of variables in the string pool. 

Returns
    int, the number of variables in the string pool. 

## ◆ getVariable()

[Variable](class_variable.html) VariableManager::getVariable  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the variable at the specified index. 

Parameters
     i,the| index of the variable of interest.  
---|---  
  
Returns
    [Variable](class_variable.html "Variable is the base class for variables in the VariableManager."), the [Variable](class_variable.html "Variable is the base class for variables in the VariableManager.") object at the specified index. 

## ◆ getVariableByName()

[Variable](class_variable.html) VariableManager::getVariableByName  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the variable with the specified name. 

Parameters
     name,the| name of the variable of interest.  
---|---  
  
Returns
    [Variable](class_variable.html "Variable is the base class for variables in the VariableManager."), the [Variable](class_variable.html "Variable is the base class for variables in the VariableManager.") object with the specified name. 

## ◆ getVariableSize()

int VariableManager::getVariableSize  | ( | | ) |   
---|---|---|---|---  
  
Returns the total number of variables. 

Returns
    int, the total number of variables. 

* * *

The documentation for this class was generated from the following file:

  * [CVariableManager.pki](_c_variable_manager_8pki.html)


