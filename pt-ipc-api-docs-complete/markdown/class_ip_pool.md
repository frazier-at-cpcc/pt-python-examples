# Cisco Packet Tracer Extensions API: IpPool Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_ip_pool.html

---

[IpPool](class_ip_pool.html "IpPool is the class that manages the IP pool in the Variable Manager for activity files.") is the class that manages the IP pool in the [Variable](class_variable.html "Variable is the base class for variables in the VariableManager.") Manager for activity files. [More...](class_ip_pool.html#details)

##  Public Member Functions  
  
---  
ip | [getNetworkIp](class_ip_pool.html#a16dd36c1bc589ff443fa90a1dd5fbbbb) ()  
| Returns the drawn network address. [More...](class_ip_pool.html#a16dd36c1bc589ff443fa90a1dd5fbbbb)  
  
ip | [getMaskIp](class_ip_pool.html#ac9ef5cc61766a1566525d621c010bcd5) ()  
| Returns the drawn network mask. [More...](class_ip_pool.html#ac9ef5cc61766a1566525d621c010bcd5)  
  
ip | [getFirstIp](class_ip_pool.html#ab3015baaaf5d717a21cc31ade6d03bec) ()  
| Returns the drawn first IP address. [More...](class_ip_pool.html#ab3015baaaf5d717a21cc31ade6d03bec)  
  
ip | [getLastIp](class_ip_pool.html#aa53840d373561588e290c8168306dc68) ()  
| Returns the drawn last IP address. [More...](class_ip_pool.html#aa53840d373561588e290c8168306dc68)  
  
QString | [getAuthoredNetworkIp](class_ip_pool.html#a107674997d83031cd043b24a47ba0f97) ()  
| Returns the authored network address. [More...](class_ip_pool.html#a107674997d83031cd043b24a47ba0f97)  
  
QString | [getAuthoredMaskIp](class_ip_pool.html#a3ed1c2fc43dd050f4379da742068dcdc) ()  
| Returns the authored network address. [More...](class_ip_pool.html#a3ed1c2fc43dd050f4379da742068dcdc)  
  
QString | [getAuthoredFirstIp](class_ip_pool.html#ad47f86ca6693efb89dab3adc15c99b62) ()  
| Returns the authored first IP address. [More...](class_ip_pool.html#ad47f86ca6693efb89dab3adc15c99b62)  
  
QString | [getAuthoredLastIp](class_ip_pool.html#a1c771b988fc74c01768c05a0c74f24e0) ()  
| Returns the authored last IP address. [More...](class_ip_pool.html#a1c771b988fc74c01768c05a0c74f24e0)  
  
Public Member Functions inherited from [Pool](class_pool.html)  
QString | [name](class_pool.html#a104b070e317895753cbdecb943bd613c) ()  
| Returns the name of the pool. [More...](class_pool.html#a104b070e317895753cbdecb943bd613c)  
  
QString | [getElementToString](class_pool.html#ab6cccb6993cfd621c17c4bbd73cb95c2) (int)  
| Returns the element in the pool at the specified index. [More...](class_pool.html#ab6cccb6993cfd621c17c4bbd73cb95c2)  
  
bool | [isInPool](class_pool.html#a04131d8e8d46cefd19eae1b7dc0ccf16) (QString)  
| Returns true if the specified value is in the pool, otherwise false. [More...](class_pool.html#a04131d8e8d46cefd19eae1b7dc0ccf16)  
  
  
## Detailed Description

[IpPool](class_ip_pool.html "IpPool is the class that manages the IP pool in the Variable Manager for activity files.") is the class that manages the IP pool in the [Variable](class_variable.html "Variable is the base class for variables in the VariableManager.") Manager for activity files. 

## Member Function Documentation

## ◆ getAuthoredFirstIp()

QString IpPool::getAuthoredFirstIp  | ( | | ) |   
---|---|---|---|---  
  
Returns the authored first IP address. 

Returns
    QString, the authored first IP address. 

## ◆ getAuthoredLastIp()

QString IpPool::getAuthoredLastIp  | ( | | ) |   
---|---|---|---|---  
  
Returns the authored last IP address. 

Returns
    QString, the authored last IP address. 

## ◆ getAuthoredMaskIp()

QString IpPool::getAuthoredMaskIp  | ( | | ) |   
---|---|---|---|---  
  
Returns the authored network address. 

Returns
    QString, the authored network address. 

## ◆ getAuthoredNetworkIp()

QString IpPool::getAuthoredNetworkIp  | ( | | ) |   
---|---|---|---|---  
  
Returns the authored network address. 

Returns
    QString, the authored network address. 

## ◆ getFirstIp()

ip IpPool::getFirstIp  | ( | | ) |   
---|---|---|---|---  
  
Returns the drawn first IP address. 

Returns
    ip, the drawn first IP address. 

## ◆ getLastIp()

ip IpPool::getLastIp  | ( | | ) |   
---|---|---|---|---  
  
Returns the drawn last IP address. 

Returns
    ip, the drawn last IP address. 

## ◆ getMaskIp()

ip IpPool::getMaskIp  | ( | | ) |   
---|---|---|---|---  
  
Returns the drawn network mask. 

Returns
    ip, the drawn network mask. 

## ◆ getNetworkIp()

ip IpPool::getNetworkIp  | ( | | ) |   
---|---|---|---|---  
  
Returns the drawn network address. 

Returns
    ip, the drawn network address. 

* * *

The documentation for this class was generated from the following file:

  * [CIpPool.pki](_c_ip_pool_8pki.html)


