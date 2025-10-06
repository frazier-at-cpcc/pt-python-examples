# Cisco Packet Tracer Extensions API: Pool Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_pool.html

---

[Pool](class_pool.html "Pool is the base class for all variable pools for activities.") is the base class for all variable pools for activities. [More...](class_pool.html#details)

##  Public Member Functions  
  
---  
QString | [name](class_pool.html#a104b070e317895753cbdecb943bd613c) ()  
| Returns the name of the pool. [More...](class_pool.html#a104b070e317895753cbdecb943bd613c)  
  
QString | [getElementToString](class_pool.html#ab6cccb6993cfd621c17c4bbd73cb95c2) (int)  
| Returns the element in the pool at the specified index. [More...](class_pool.html#ab6cccb6993cfd621c17c4bbd73cb95c2)  
  
bool | [isInPool](class_pool.html#a04131d8e8d46cefd19eae1b7dc0ccf16) (QString)  
| Returns true if the specified value is in the pool, otherwise false. [More...](class_pool.html#a04131d8e8d46cefd19eae1b7dc0ccf16)  
  
  
## Detailed Description

[Pool](class_pool.html "Pool is the base class for all variable pools for activities.") is the base class for all variable pools for activities. 

## Member Function Documentation

## ◆ getElementToString()

QString Pool::getElementToString  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the element in the pool at the specified index. 

Parameters
     index,the| index of the element in the pool of interest.  
---|---  
  
Returns
    QString, the element in the pool at the specified index. 

## ◆ isInPool()

bool Pool::isInPool  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns true if the specified value is in the pool, otherwise false. 

Parameters
     value,value| to find in the pool.  
---|---  
  
Returns
    bool, true if the specified value is in the pool, otherwise false. 

## ◆ name()

QString Pool::name  | ( | | ) |   
---|---|---|---|---  
  
Returns the name of the pool. 

Returns
    QString, the name of the pool. 

* * *

The documentation for this class was generated from the following file:

  * [CPool.pki](_c_pool_8pki.html)


