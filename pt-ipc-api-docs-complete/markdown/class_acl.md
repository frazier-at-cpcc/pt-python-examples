# Cisco Packet Tracer Extensions API: Acl Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_acl.html

---

[Acl](class_acl.html "Acl holds and manipulates AclStatements.") holds and manipulates AclStatements. [More...](class_acl.html#details)

##  Public Member Functions  
  
---  
bool | [addStatement](class_acl.html#ae94cdc51c8cce00e1a9125c6e3424f98) (string)  
| Adds an ACL statement to this ACL. [More...](class_acl.html#ae94cdc51c8cce00e1a9125c6e3424f98)  
  
bool | [addExtStatement](class_acl.html#a00e8474c5eb24d2dbc1bdf57b6383340) (bool, string, bool, string, string, int, string, string, int)  
| Adds an ACL statement to this ACL with the specified parameters. [More...](class_acl.html#a00e8474c5eb24d2dbc1bdf57b6383340)  
  
bool | [removeStatement](class_acl.html#ab93d8a2bafd53c2ae138354cc2b5e715) (string)  
| Removes an ACL statement from this ACL. [More...](class_acl.html#ab93d8a2bafd53c2ae138354cc2b5e715)  
  
bool | [removeExtStatement](class_acl.html#a008c3083afc6a5c6a9e61fc9a4e3befb) (bool, string, bool, string, string, int, string, string, int)  
| Removes the ACL statement from this ACL with the specified parameters. [More...](class_acl.html#a008c3083afc6a5c6a9e61fc9a4e3befb)  
  
[AclStatement](struct_acl_statement.html) | [getStatementAt](class_acl.html#a75826698d5fd04a2bc2ea0bd7dfce93e) (int)  
| Returns an ACL statement at the specified index. [More...](class_acl.html#a75826698d5fd04a2bc2ea0bd7dfce93e)  
  
int | [getStatementCount](class_acl.html#a7775f3f6c69b9ff30f935753ca477d47) ()  
| Returns the number of ACL statements. [More...](class_acl.html#a7775f3f6c69b9ff30f935753ca477d47)  
  
void | [addRemark](class_acl.html#add9af66065e85244b77e8e9dac9e375a) (string)  
| Adds a remark to this ACL. [More...](class_acl.html#add9af66065e85244b77e8e9dac9e375a)  
  
string | [getRemark](class_acl.html#af6824262a7c2a9931f666219a006586d) (int)  
| Returns the remark at the specified index. [More...](class_acl.html#af6824262a7c2a9931f666219a006586d)  
  
int | [getRemarkCount](class_acl.html#a08fdcf1ce3b6ea2ac1b3909e6c4ac6fd) ()  
| Returns the number of remarks in this ACL. [More...](class_acl.html#a08fdcf1ce3b6ea2ac1b3909e6c4ac6fd)  
  
int | [getCommandCount](class_acl.html#a6d05b86247d6cd5598dc7e3d5fd48cd9) ()  
| Returns the number of ACL commands. [More...](class_acl.html#a6d05b86247d6cd5598dc7e3d5fd48cd9)  
  
string | [getCommandAt](class_acl.html#aa65387b3ea99588349ec5953170275a8) (int)  
| Returns the ACL command at the specified index. [More...](class_acl.html#aa65387b3ea99588349ec5953170275a8)  
  
bool | [isExtended](class_acl.html#a1b69e589007a64e0425b98a655eda414) ()  
| Returns true if this ACL is an extended ACL, false if it is a standard ACL. [More...](class_acl.html#a1b69e589007a64e0425b98a655eda414)  
  
string | [getAclId](class_acl.html#a09b4773e04995f5affd79c77830b5b5c) ()  
| Returns this ACL's ID. [More...](class_acl.html#a09b4773e04995f5affd79c77830b5b5c)  
  
vector< string > | [getExtStatementDataAt](class_acl.html#a3ecef5f304e5e6b0bdccb1ca7b3adf36) (bool, int)  
| Returns a vector of the data of the ACL statement at the specified index. [More...](class_acl.html#a3ecef5f304e5e6b0bdccb1ca7b3adf36)  
  
bool | [evaluate](class_acl.html#aea641f67d991455202349acf8ecbb083) (QString)  
| Evaluates the ACL against a packet/PDU, and returns true if permitted, false otherwise. [More...](class_acl.html#aea641f67d991455202349acf8ecbb083)  
  
[AclStatement](struct_acl_statement.html) | [getMatch](class_acl.html#a4d29e3c0fbaac92e7a30e1e27ef4d360) (QString)  
| Evaluates the ACL against a packet/PDU, and returns the matched [AclStatement](struct_acl_statement.html "Data element for AclStatement."). [More...](class_acl.html#a4d29e3c0fbaac92e7a30e1e27ef4d360)  
  
  
## Detailed Description

[Acl](class_acl.html "Acl holds and manipulates AclStatements.") holds and manipulates AclStatements. 

## Member Function Documentation

## ◆ addExtStatement()

bool Acl::addExtStatement  | ( | bool  | ,   
---|---|---|---  
|  | string  | ,   
|  | bool  | ,   
|  | string  | ,   
|  | string  | ,   
|  | int  | ,   
|  | string  | ,   
|  | string  | ,   
|  | int  |   
| ) | |   
  
Adds an ACL statement to this ACL with the specified parameters. 

Parameters
     protocol,valid| protocols are IP, ICMP, TCP, and UDP.   
---|---  
remoteIp,the| remote IP adddress.   
remoteMask,the| remote wildcard mask.   
remotePort,the| remote port for TCP and UDP.   
localIp,the| local IP address.   
localMask,the| local wildcard mask.   
localPort,the| local port for TCP and UDP.  
  
Returns
    bool, true if added successfully, otherwise false. 

## ◆ addRemark()

void Acl::addRemark  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Adds a remark to this ACL. 

Parameters
     remark,the| remark to be added.   
---|---  
  
## ◆ addStatement()

bool Acl::addStatement  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Adds an ACL statement to this ACL. 

Parameters
     statement,the| IOS ACL statement. "access-list [this-aclid]" should be omitted. Start with "permit, deny, or remark".  
---|---  
  
Returns
    bool, true if added successfully, otherwise false. 

## ◆ evaluate()

bool Acl::evaluate  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Evaluates the ACL against a packet/PDU, and returns true if permitted, false otherwise. 

Parameters
     jsonPdu,the| PDU in JSON serialized format  
---|---  
  
Returns
    bool, true if permitted, false otherwise 

## ◆ getAclId()

string Acl::getAclId  | ( | | ) |   
---|---|---|---|---  
  
Returns this ACL's ID. 

Returns
    string, this ACL's ID. 

## ◆ getCommandAt()

string Acl::getCommandAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the ACL command at the specified index. 

Parameters
     int| index, the index of the ACL command.  
---|---  
  
Returns
    string, the ACL command at the specified index. 

## ◆ getCommandCount()

int Acl::getCommandCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of ACL commands. 

Returns
    int, the number of ACL commands. 

## ◆ getExtStatementDataAt()

vector< string > Acl::getExtStatementDataAt  | ( | bool  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Returns a vector of the data of the ACL statement at the specified index. 

Parameters
     index,the| index of the ACL statement of interest.  
---|---  
  
Returns
    vector<string>, a vector of the data of the ACL statement at the specified index. 

## ◆ getMatch()

[AclStatement](struct_acl_statement.html) Acl::getMatch  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Evaluates the ACL against a packet/PDU, and returns the matched [AclStatement](struct_acl_statement.html "Data element for AclStatement."). 

Parameters
     jsonPdu,the| PDU in JSON serialized format  
---|---  
  
Returns
    [AclStatement](struct_acl_statement.html "Data element for AclStatement."), the matched statement, or null if no match 

## ◆ getRemark()

string Acl::getRemark  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the remark at the specified index. 

Parameters
     index,the| index of the remark.  
---|---  
  
Returns
    string, the remark at the specified index. 

## ◆ getRemarkCount()

int Acl::getRemarkCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of remarks in this ACL. 

Returns
    int, the number of remarks in this ACL. 

## ◆ getStatementAt()

[AclStatement](struct_acl_statement.html) Acl::getStatementAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns an ACL statement at the specified index. 

Parameters
     index,the| index of the ACL statement.  
---|---  
  
Returns
    [AclStatement](struct_acl_statement.html "Data element for AclStatement."), the ACL statement at the specified index. 

## ◆ getStatementCount()

int Acl::getStatementCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of ACL statements. 

Returns
    int, the number of ACL statements. 

## ◆ isExtended()

bool Acl::isExtended  | ( | | ) |   
---|---|---|---|---  
  
Returns true if this ACL is an extended ACL, false if it is a standard ACL. 

Returns
    bool, true if this ACL is an extended ACL, false if it is a standard ACL. 

## ◆ removeExtStatement()

bool Acl::removeExtStatement  | ( | bool  | ,   
---|---|---|---  
|  | string  | ,   
|  | bool  | ,   
|  | string  | ,   
|  | string  | ,   
|  | int  | ,   
|  | string  | ,   
|  | string  | ,   
|  | int  |   
| ) | |   
  
Removes the ACL statement from this ACL with the specified parameters. 

Parameters
     protocol,valid| protocols are IP, ICMP, TCP, and UDP.   
---|---  
remoteIp,the| remote IP adddress.   
remoteMask,the| remote wildcard mask.   
remotePort,the| remote port for TCP and UDP.   
localIp,the| local IP address.   
localMask,the| local wildcard mask.   
localPort,the| local port for TCP and UDP.  
  
Returns
    bool, true if removed successfully, otherwise false. 

## ◆ removeStatement()

bool Acl::removeStatement  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes an ACL statement from this ACL. 

Parameters
     statement| the IOS ACL statement. "access-list [this-aclid]" should be omitted. Start with "permit, deny, or remark".  
---|---  
  
Returns
    bool, true if removed successfully, otherwise false. 

* * *

The documentation for this class was generated from the following file:

  * [CAcl.pki](_c_acl_8pki.html)


