# Cisco Packet Tracer Extensions API: ClassMap Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_class_map.html

---

[ClassMap](class_class_map.html "ClassMap handles the class maps for QoS.") handles the class maps for QoS. [More...](class_class_map.html#details)

##  Public Member Functions  
  
---  
string | [getMapName](class_class_map.html#aaec16de9f5921709511b1c931fa02194) ()  
| Returns the class map name. [More...](class_class_map.html#aaec16de9f5921709511b1c931fa02194)  
  
void | [setDescription](class_class_map.html#ab32210703732278c3873ebf974f5e2c8) (string)  
| Sets the class map description. [More...](class_class_map.html#ab32210703732278c3873ebf974f5e2c8)  
  
string | [getDescription](class_class_map.html#a9671151edd219301856f75a0f3ee8552) ()  
| Returns the class map description. [More...](class_class_map.html#a9671151edd219301856f75a0f3ee8552)  
  
string | [getMatchTypeString](class_class_map.html#a6cf5479eac91b65fef8aa3281e81238e) ()  
| Returns the class map match types. [More...](class_class_map.html#a6cf5479eac91b65fef8aa3281e81238e)  
  
QoS::EClassMapMatchType | [getMatchType](class_class_map.html#ade7620d93282c85bedbcfa62c574cbf5) ()  
| Returns the class map match type. [More...](class_class_map.html#ade7620d93282c85bedbcfa62c574cbf5)  
  
void | [setMatchType](class_class_map.html#a33630c314bcd51bf8d4df5e5b0dbeabb) (QoS::EClassMapMatchType)  
| Sets the class map match type. [More...](class_class_map.html#a33630c314bcd51bf8d4df5e5b0dbeabb)  
  
string | [toReverseString](class_class_map.html#ad6ab52f12741a2b0b4319a044487718b) ()  
| Returns the class map string. [More...](class_class_map.html#ad6ab52f12741a2b0b4319a044487718b)  
  
string | [toString](class_class_map.html#a1a4d1c6ff8f483571e19df15a6c5c597) ()  
| Returns the class map reverse string. [More...](class_class_map.html#a1a4d1c6ff8f483571e19df15a6c5c597)  
  
QoS::eMapType | [getMapType](class_class_map.html#abbe5e920f83e71df3fb3eab613bedf7b) ()  
| Returns the class map type. [More...](class_class_map.html#abbe5e920f83e71df3fb3eab613bedf7b)  
  
void | [setMapType](class_class_map.html#a9c5832c5c54a03e2c1cc2414bc2cced1) (QoS::eMapType)  
| Sets the class map type. [More...](class_class_map.html#a9c5832c5c54a03e2c1cc2414bc2cced1)  
  
int | [getStatementCnt](class_class_map.html#a1a694b140a4282cb18c926308995ba04) ()  
| Returns the number of statements in this class map. [More...](class_class_map.html#a1a694b140a4282cb18c926308995ba04)  
  
bool | [isClassDefault](class_class_map.html#ae1d0a6fa4f909788ccdf45fb6850a762) ()  
| Returns true if this class map is class-default, otherwise false. [More...](class_class_map.html#ae1d0a6fa4f909788ccdf45fb6850a762)  
  
  
## Detailed Description

[ClassMap](class_class_map.html "ClassMap handles the class maps for QoS.") handles the class maps for QoS. 

## Member Function Documentation

## ◆ getDescription()

string ClassMap::getDescription  | ( | | ) |   
---|---|---|---|---  
  
Returns the class map description. 

Returns
    string, the class map description. 

## ◆ getMapName()

string ClassMap::getMapName  | ( | | ) |   
---|---|---|---|---  
  
Returns the class map name. 

Returns
    string, the class map name. 

## ◆ getMapType()

QoS::eMapType ClassMap::getMapType  | ( | | ) |   
---|---|---|---|---  
  
Returns the class map type. 

Returns
    enum<QoS::eMapType>, the map type. Map types: type_default = 0, type_control = 1, type_inspect = 2, type_logging = 3 

## ◆ getMatchType()

QoS::EClassMapMatchType ClassMap::getMatchType  | ( | | ) |   
---|---|---|---|---  
  
Returns the class map match type. 

Returns
    enum<QoS::EClassMapMatchType>, the class map match type. Match types: eMatchAny = 0, eMatchAll = 1 

## ◆ getMatchTypeString()

string ClassMap::getMatchTypeString  | ( | | ) |   
---|---|---|---|---  
  
Returns the class map match types. 

Returns
    string, the class map match types. 

## ◆ getStatementCnt()

int ClassMap::getStatementCnt  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of statements in this class map. 

Returns
    int, the number of statements in this class map. 

## ◆ isClassDefault()

bool ClassMap::isClassDefault  | ( | | ) |   
---|---|---|---|---  
  
Returns true if this class map is class-default, otherwise false. 

Returns
    bool, true if this class map is class-default, otherwise false. 

## ◆ setDescription()

void ClassMap::setDescription  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Sets the class map description. 

Parameters
     description,the| class map description.   
---|---  
  
## ◆ setMapType()

void ClassMap::setMapType  | ( | QoS::eMapType  | | ) |   
---|---|---|---|---|---  
  
Sets the class map type. 

Parameters
     mapType,the| map type. Map types: type_default = 0, type_control = 1, type_inspect = 2, type_logging = 3   
---|---  
  
## ◆ setMatchType()

void ClassMap::setMatchType  | ( | QoS::EClassMapMatchType  | | ) |   
---|---|---|---|---|---  
  
Sets the class map match type. 

Parameters
     enum<QoS::EClassMapMatchType>,the| class map match type. Match types: eMatchAny = 0, eMatchAll = 1   
---|---  
  
## ◆ toReverseString()

string ClassMap::toReverseString  | ( | | ) |   
---|---|---|---|---  
  
Returns the class map string. 

Parameters
     string,the| class map string.   
---|---  
  
## ◆ toString()

string ClassMap::toString  | ( | | ) |   
---|---|---|---|---  
  
Returns the class map reverse string. 

Parameters
     string,the| class map reverse string.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CClassMap.pki](_c_class_map_8pki.html)


