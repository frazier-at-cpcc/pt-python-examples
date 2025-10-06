# Cisco Packet Tracer Extensions API: Variable Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_variable.html

---

[Variable](class_variable.html "Variable is the base class for variables in the VariableManager.") is the base class for variables in the [VariableManager](class_variable_manager.html "VariableManager manages the variables and pools in an activity."). [More...](class_variable.html#details)

##  Public Member Functions  
  
---  
QString | [name](class_variable.html#aa9d78e5313a6ff7317cef5b785b43d8a) ()  
| Returns the name of the variable. [More...](class_variable.html#aa9d78e5313a6ff7317cef5b785b43d8a)  
  
QString | [valueToString](class_variable.html#a2e598f5f7eb745f1593913be9ed624a2) ()  
| Returns the value of the variable. [More...](class_variable.html#a2e598f5f7eb745f1593913be9ed624a2)  
  
QString | [valueOfIndex](class_variable.html#a292bff5dca246b8dcf5fe288baf7a25d) (int)  
| Returns the value of the variable at the specified index. [More...](class_variable.html#a292bff5dca246b8dcf5fe288baf7a25d)  
  
[Pool](class_pool.html) | [getPool](class_variable.html#afac1ffb16ae422889a2912f913744b1b) ()  
| Returns the pool that this variable is associated with. [More...](class_variable.html#afac1ffb16ae422889a2912f913744b1b)  
  
bool | [isInPool](class_variable.html#a2c7efc8cb26f7c1d5d1b2fa549a3272e) (QString)  
| Returns true if the specified value is in the pool, otherwise false. [More...](class_variable.html#a2c7efc8cb26f7c1d5d1b2fa549a3272e)  
  
VARIABLETYPE | [getType](class_variable.html#a6fb04945c721fe381fafc24d6c864382) ()  
| Returns the type of the variable. [More...](class_variable.html#a6fb04945c721fe381fafc24d6c864382)  
  
  
## Detailed Description

[Variable](class_variable.html "Variable is the base class for variables in the VariableManager.") is the base class for variables in the [VariableManager](class_variable_manager.html "VariableManager manages the variables and pools in an activity."). 

## Member Function Documentation

## ◆ getPool()

[Pool](class_pool.html) Variable::getPool  | ( | | ) |   
---|---|---|---|---  
  
Returns the pool that this variable is associated with. 

Returns
    [Pool](class_pool.html "Pool is the base class for all variable pools for activities."), the [Pool](class_pool.html "Pool is the base class for all variable pools for activities.") object that this variable is associated with. 

## ◆ getType()

VARIABLETYPE Variable::getType  | ( | | ) |   
---|---|---|---|---  
  
Returns the type of the variable. 

Returns
    enum<VARIABLETYPE>, the type of the variable. [Variable](class_variable.html "Variable is the base class for variables in the VariableManager.") types: ENTIRE_RANGE = 0, RANDOM = 1, STATIC = 2, SEED = 3 

## ◆ isInPool()

bool Variable::isInPool  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns true if the specified value is in the pool, otherwise false. 

Parameters
     value,the| value of interest.  
---|---  
  
Returns
    bool, true if the specified value is in the pool, otherwise false. 

## ◆ name()

QString Variable::name  | ( | | ) |   
---|---|---|---|---  
  
Returns the name of the variable. 

Returns
    QString, the name of the variable. 

## ◆ valueOfIndex()

QString Variable::valueOfIndex  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the value of the variable at the specified index. 

Parameters
     index,the| index of the variable of interest.  
---|---  
  
Returns
    QString, the value of the variable. 

## ◆ valueToString()

QString Variable::valueToString  | ( | | ) |   
---|---|---|---|---  
  
Returns the value of the variable. 

Returns
    QString, the value of the variable. 

* * *

The documentation for this class was generated from the following file:

  * [CVariable.pki](_c_variable_8pki.html)


