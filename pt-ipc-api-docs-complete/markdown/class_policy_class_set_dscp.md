# Cisco Packet Tracer Extensions API: PolicyClassSetDscp Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_policy_class_set_dscp.html

---

[PolicyClassSetDscp](class_policy_class_set_dscp.html "PolicyClassSetDscp handles and manipulates policy-map class DSCP and IP precedence.") handles and manipulates policy-map class DSCP and IP precedence. [More...](class_policy_class_set_dscp.html#details)

##  Public Member Functions  
  
---  
QoS::EWredType | [getType](class_policy_class_set_dscp.html#abfa8801c2e67d3614acb802144ed2200) ()  
| Returns the policy map class type. [More...](class_policy_class_set_dscp.html#abfa8801c2e67d3614acb802144ed2200)  
  
bool | [isIpv4Only](class_policy_class_set_dscp.html#a4ec3c7a12cb9ddbcce77394d08afd57c) ()  
| Returns true if the policy map class is for IPv4 only, otherwise false. [More...](class_policy_class_set_dscp.html#a4ec3c7a12cb9ddbcce77394d08afd57c)  
  
int | [getValue](class_policy_class_set_dscp.html#ac5a72daf417db1f6b930f8273379c695) ()  
| Returns the value of the DSCP or IP precedence. [More...](class_policy_class_set_dscp.html#ac5a72daf417db1f6b930f8273379c695)  
  
void | [update](class_policy_class_set_dscp.html#ac3985c2c99dfe3699b6910a9923be199) (QoS::EWredType, bool, int)  
| Updates the policy map class with the specified type and value. [More...](class_policy_class_set_dscp.html#ac3985c2c99dfe3699b6910a9923be199)  
  
string | [toString](class_policy_class_set_dscp.html#af10349633e34bf559edc3b1261d8d220) (bool)  
| Returns the output of the policy map class. [More...](class_policy_class_set_dscp.html#af10349633e34bf559edc3b1261d8d220)  
  
  
## Detailed Description

[PolicyClassSetDscp](class_policy_class_set_dscp.html "PolicyClassSetDscp handles and manipulates policy-map class DSCP and IP precedence.") handles and manipulates policy-map class DSCP and IP precedence. 

## Member Function Documentation

## ◆ getType()

QoS::EWredType PolicyClassSetDscp::getType  | ( | | ) |   
---|---|---|---|---  
  
Returns the policy map class type. 

Returns
    enum<QoS::EWredType>, the QoS policy type. QoS policy types: eWredDscp = 0, eWredPrec = 1 

## ◆ getValue()

int PolicyClassSetDscp::getValue  | ( | | ) |   
---|---|---|---|---  
  
Returns the value of the DSCP or IP precedence. 

Returns
    int, the value of the DSCP or IP precedence. 

## ◆ isIpv4Only()

bool PolicyClassSetDscp::isIpv4Only  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the policy map class is for IPv4 only, otherwise false. 

Returns
    bool, true if the policy map class is for IPv4 only, otherwise false. 

## ◆ toString()

string PolicyClassSetDscp::toString  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Returns the output of the policy map class. 

Parameters
     showIpType,true| to display the ip type, false to not display it.  
---|---  
  
Returns
    string, the output of the policy map class. 

## ◆ update()

void PolicyClassSetDscp::update  | ( | QoS::EWredType  | ,   
---|---|---|---  
|  | bool  | ,   
|  | int  |   
| ) | |   
  
Updates the policy map class with the specified type and value. 

Parameters
     enum<QoS::EWredType>,the| QoS policy type. QoS policy types: eWredDscp = 0, eWredPrec = 1   
---|---  
ipv4Only,true| for IPv4 only, false for IPv4 and IPv6.   
value,the| value for the QoS policy type.   
  
* * *

The documentation for this class was generated from the following file:

  * [CPolicyClassSetDscp.pki](_c_policy_class_set_dscp_8pki.html)


