# Cisco Packet Tracer Extensions API: ClassMapManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_class_map_manager.html

---

[ClassMapManager](class_class_map_manager.html "ClassMapManager is the manager for QoS class maps.") is the manager for QoS class maps. [More...](class_class_map_manager.html#details)

##  Public Member Functions  
  
---  
void | [deleteClassMap](class_class_map_manager.html#acda9292e4dcd97639e88f7667009c75f) (string)  
| Removes the specified class map. [More...](class_class_map_manager.html#acda9292e4dcd97639e88f7667009c75f)  
  
bool | [classMapExist](class_class_map_manager.html#a228bc9eb324b8ed36688ccdaa43a6f45) (string)  
| Returns true if the specified class map exists, otherwise false. [More...](class_class_map_manager.html#a228bc9eb324b8ed36688ccdaa43a6f45)  
  
short | [getClassMapCount](class_class_map_manager.html#aa423e3c5866f3c8f145d5123ab164268) ()  
| Returns the number of class maps. [More...](class_class_map_manager.html#aa423e3c5866f3c8f145d5123ab164268)  
  
[ClassMap](class_class_map.html) | [getClassMapAt](class_class_map_manager.html#ad9ebc45575ded4fe8522b897f813bd20) (int)  
| Returns the [ClassMap](class_class_map.html "ClassMap handles the class maps for QoS.") object at the specified index. [More...](class_class_map_manager.html#ad9ebc45575ded4fe8522b897f813bd20)  
  
[ClassMap](class_class_map.html) | [getClassMap](class_class_map_manager.html#a845c3f9c48aeb0aa052bc5bdfe51f363) (string)  
| Returns the [ClassMap](class_class_map.html "ClassMap handles the class maps for QoS.") object with the specified class map name. [More...](class_class_map_manager.html#a845c3f9c48aeb0aa052bc5bdfe51f363)  
  
bool | [hasCircularReference](class_class_map_manager.html#a5cd8542c6b04d8d5435b2307bc5671d3) (string, string)  
| Returns true if the two specified class maps are the same, otherwise false. [More...](class_class_map_manager.html#a5cd8542c6b04d8d5435b2307bc5671d3)  
  
void | [rearrangeMaps](class_class_map_manager.html#aa1c95bd143ede64aaa45948702d138a4) (string, string)  
| Rearranges the specified class maps such that map1 precedes map2. [More...](class_class_map_manager.html#aa1c95bd143ede64aaa45948702d138a4)  
  
  
## Detailed Description

[ClassMapManager](class_class_map_manager.html "ClassMapManager is the manager for QoS class maps.") is the manager for QoS class maps. 

## Member Function Documentation

## ◆ classMapExist()

bool ClassMapManager::classMapExist  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns true if the specified class map exists, otherwise false. 

Parameters
     name,the| name of the class map of interest.  
---|---  
  
Returns
    bool, true if the specified class map exists, otherwise false. 

## ◆ deleteClassMap()

void ClassMapManager::deleteClassMap  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Removes the specified class map. 

Parameters
     name,the| name of the class map of interest.  
---|---  
string,the| class map name.   
  
## ◆ getClassMap()

[ClassMap](class_class_map.html) ClassMapManager::getClassMap  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the [ClassMap](class_class_map.html "ClassMap handles the class maps for QoS.") object with the specified class map name. 

Parameters
     mapname,the| name of the class map of interest.  
---|---  
  
Returns
    [ClassMap](class_class_map.html "ClassMap handles the class maps for QoS."), the [ClassMap](class_class_map.html "ClassMap handles the class maps for QoS.") object with the associated class map name. 

## ◆ getClassMapAt()

[ClassMap](class_class_map.html) ClassMapManager::getClassMapAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the [ClassMap](class_class_map.html "ClassMap handles the class maps for QoS.") object at the specified index. 

Parameters
     mapname,the| index of the class map of interest.  
---|---  
  
Returns
    [ClassMap](class_class_map.html "ClassMap handles the class maps for QoS."), the [ClassMap](class_class_map.html "ClassMap handles the class maps for QoS.") object at the specified index. 

## ◆ getClassMapCount()

short ClassMapManager::getClassMapCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of class maps. 

Returns
    short, the number of class maps. 

## ◆ hasCircularReference()

bool ClassMapManager::hasCircularReference  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Returns true if the two specified class maps are the same, otherwise false. 

Parameters
     map1,the| name of the first class map.   
---|---  
map2,the| name of the second class map.  
  
Returns
    bool, true if the two specified class maps are the same, otherwise false. 

## ◆ rearrangeMaps()

void ClassMapManager::rearrangeMaps  | ( | string  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Rearranges the specified class maps such that map1 precedes map2. 

Parameters
     map1,the| name of the first class map.   
---|---  
map2,the| name of the second class map.   
  
* * *

The documentation for this class was generated from the following file:

  * [CClassMapManager.pki](_c_class_map_manager_8pki.html)


