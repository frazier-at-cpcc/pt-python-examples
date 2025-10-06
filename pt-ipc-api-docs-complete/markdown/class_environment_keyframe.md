# Cisco Packet Tracer Extensions API: EnvironmentKeyframe Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_environment_keyframe.html

---

An object in the Physical [Workspace](class_workspace.html "Workspace is the base class for Logical and Physical workspace related objects."). [More...](class_environment_keyframe.html#details)

##  Public Member Functions  
  
---  
int | [getTime](class_environment_keyframe.html#a21478187034592c325a4dbe0e1845800) ()  
| Returns the time the keyframe is set to exist at, in seconds. [More...](class_environment_keyframe.html#a21478187034592c325a4dbe0e1845800)  
  
void | [setTime](class_environment_keyframe.html#af04dd07a8936321e5a8476c9dc546fd6) (int)  
| Sets the time the keyframe exists at, in seconds. [More...](class_environment_keyframe.html#af04dd07a8936321e5a8476c9dc546fd6)  
  
int | [getEnvironmentOptionsCount](class_environment_keyframe.html#a1231ef181911091a2f687757c34afbe5) ()  
| Returns how many different environment value properties ("CO", "Sunlight", etc) are in the key frame. [More...](class_environment_keyframe.html#a1231ef181911091a2f687757c34afbe5)  
  
vector< QString > | [getEnvironmentKeys](class_environment_keyframe.html#ab3a44de8eaf19096aec265a6d3c010b4) ()  
| Returns the names of all the environment value properties ("CO", "Sunlight", etc) are in the key frame. [More...](class_environment_keyframe.html#ab3a44de8eaf19096aec265a6d3c010b4)  
  
[EnvironmentOptions](class_environment_options.html) | [getEnvironment](class_environment_keyframe.html#a82324616ab2c695504f559546641dc94) (QString)  
| Returns the environment properties for the environment value property type passed. [More...](class_environment_keyframe.html#a82324616ab2c695504f559546641dc94)  
  
  
## Detailed Description

An object in the Physical [Workspace](class_workspace.html "Workspace is the base class for Logical and Physical workspace related objects."). 

## Member Function Documentation

## ◆ getEnvironment()

[EnvironmentOptions](class_environment_options.html) EnvironmentKeyframe::getEnvironment  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the environment properties for the environment value property type passed. 

Parameters
     env,Name| of the environment property type to get the properties for. Like "CO", "Sunlight", etc.  
---|---  
  
Returns
    [EnvironmentOptions](class_environment_options.html "An object in the Physical Workspace."), the enivronment options for the given environment value type. 

## ◆ getEnvironmentKeys()

vector< QString > EnvironmentKeyframe::getEnvironmentKeys  | ( | | ) |   
---|---|---|---|---  
  
Returns the names of all the environment value properties ("CO", "Sunlight", etc) are in the key frame. 

Returns
    vector<QString>, a list with an entry for each environment property name in the keyframe. 

## ◆ getEnvironmentOptionsCount()

int EnvironmentKeyframe::getEnvironmentOptionsCount  | ( | | ) |   
---|---|---|---|---  
  
Returns how many different environment value properties ("CO", "Sunlight", etc) are in the key frame. 

Returns
    int, value is how many different environment value properties ("CO", "Sunlight", etc) are in the key frame. 

## ◆ getTime()

int EnvironmentKeyframe::getTime  | ( | | ) |   
---|---|---|---|---  
  
Returns the time the keyframe is set to exist at, in seconds. 

Returns
    int, value is the time the keyframe resides at, in seconds. 

## ◆ setTime()

void EnvironmentKeyframe::setTime  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the time the keyframe exists at, in seconds. 

Parameters
     time,value| is the time the keyframe resides at, in seconds.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [EnvironmentKeyframe.pki](_environment_keyframe_8pki.html)


