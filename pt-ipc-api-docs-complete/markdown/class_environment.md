# Cisco Packet Tracer Extensions API: Environment Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_environment.html

---

An object in the Physical [Workspace](class_workspace.html "Workspace is the base class for Logical and Physical workspace related objects."). [More...](class_environment.html#details)

##  Public Member Functions  
  
---  
void | [pauseTime](class_environment.html#a10a62bf71eef210fd1b606da66d3db3a) ()  
| Pauses the environment time. [More...](class_environment.html#a10a62bf71eef210fd1b606da66d3db3a)  
  
void | [resumeTime](class_environment.html#aa009ba26bd5d9e04881a11771f1c0fd0) ()  
| Resumes the environment time. [More...](class_environment.html#aa009ba26bd5d9e04881a11771f1c0fd0)  
  
bool | [isTimeRunning](class_environment.html#a968c8439b0abdb6dd746613cc2f6a781) ()  
| Returns true if the environment time is running, false if paused. [More...](class_environment.html#a968c8439b0abdb6dd746613cc2f6a781)  
  
int | [getTimeInSeconds](class_environment.html#a103b6c6e74f3b28771a4a06b1a83d272) ()  
| Returns the current environment runtime, in seconds. The value loops, so after 24 hours it resets to 0. [More...](class_environment.html#a103b6c6e74f3b28771a4a06b1a83d272)  
  
void | [setTimeInSeconds](class_environment.html#a0fabcda8a93f739b6e840c2f9ba59e04) (int)  
| Sets the current environment time to the given time, in seconds. Time loops every 24 hours. [More...](class_environment.html#a0fabcda8a93f739b6e840c2f9ba59e04)  
  
float | [getTimeMultiplier](class_environment.html#a628d94f8ad1f8889282d510e61c955e5) ()  
| Multiplier used when calculating how much environment time passes each step, in seconds. [More...](class_environment.html#a628d94f8ad1f8889282d510e61c955e5)  
  
void | [setTimeMultiplier](class_environment.html#af29843b834e753f263998f70e5b563ac) (float)  
| Sets the multiplier used when calculating how much environment time passes each step, in seconds. [More...](class_environment.html#af29843b834e753f263998f70e5b563ac)  
  
int | [getKeyframeCount](class_environment.html#a331fbd9c3fc0d71f511557e54e00026e) ()  
| How many key frames are in the environment. [More...](class_environment.html#a331fbd9c3fc0d71f511557e54e00026e)  
  
[EnvironmentKeyframe](class_environment_keyframe.html) | [getKeyframeAt](class_environment.html#aacd67fb35360d20b1b46f178923bb834) (int)  
| How Returns a keyframe at a specified index. [More...](class_environment.html#aacd67fb35360d20b1b46f178923bb834)  
  
[EnvironmentKeyframe](class_environment_keyframe.html) | [addKeyframe](class_environment.html#a67adfc337531bbabbeacdacc99f5ab14) (int)  
| Adds a keyframe at the specified time and returns the new keyframe. [More...](class_environment.html#a67adfc337531bbabbeacdacc99f5ab14)  
  
bool | [hasKeyframeAtTime](class_environment.html#a68765e725bd670e09a4f6d906c16f177) (int)  
| Returns if there is a keyframe at the given time. [More...](class_environment.html#a68765e725bd670e09a4f6d906c16f177)  
  
int | [getKeyframeIndexAtTime](class_environment.html#a9a06782ea1e9ab7cec2fa23c599d5e95) (int)  
| Returns the index of a keyframe at the given time if one exists. [More...](class_environment.html#a9a06782ea1e9ab7cec2fa23c599d5e95)  
  
[EnvironmentKeyframe](class_environment_keyframe.html) | [getStagingKeyframe](class_environment.html#aa74a66dbf9e613882cc765c6c1bcb562) ()  
| Returns the staging keyframe. [More...](class_environment.html#aa74a66dbf9e613882cc765c6c1bcb562)  
  
int | [addKeyframeFromStaging](class_environment.html#a75af625f2d9476cd8be794cbdee9f6ff) ()  
| Adds a keyframe from staging. [More...](class_environment.html#a75af625f2d9476cd8be794cbdee9f6ff)  
  
void | [removeKeyframe](class_environment.html#ae52bc7cf60673bc614c211ea7cba3ffb) (int)  
| Removes the keyframe at the given index if the keyframe exists and isn't the start or end. [More...](class_environment.html#ae52bc7cf60673bc614c211ea7cba3ffb)  
  
int | [getEnvironmentOptionsCount](class_environment.html#a11de968dcc8e06826c8bef191e6c572b) ()  
[EnvironmentOptions](class_environment_options.html) | [getEnvironment](class_environment.html#a0832780b38784cb5ca323f38a03781d9) (QString)  
| Returns the options for a specified environment value type, like "CO" for carbon monoxide. [More...](class_environment.html#a0832780b38784cb5ca323f38a03781d9)  
  
vector< QString > | [getEnvironmentKeys](class_environment.html#ac56e19eb6ddd8b0105c012b9bccdd6d7) ()  
| Returns a list of all the environment value types. [More...](class_environment.html#ac56e19eb6ddd8b0105c012b9bccdd6d7)  
  
float | [getEnvironmentValue](class_environment.html#a72be7f2e9344b9696ae045d4a61ef64d) (QString)  
| Returns the value for the specified environment property. [More...](class_environment.html#a72be7f2e9344b9696ae045d4a61ef64d)  
  
QString | [getUnit](class_environment.html#a7a0984761962fa9e5c8d5b521c88a9f1) (QString)  
| Returns the unit used for the specified environment property. [More...](class_environment.html#a7a0984761962fa9e5c8d5b521c88a9f1)  
  
QString | [getValueWithUnit](class_environment.html#a519968b3be4505531fb64387ab7165e4) (QString)  
| Returns a string combining the specified environment property and the display unit is uses. [More...](class_environment.html#a519968b3be4505531fb64387ab7165e4)  
  
float | [getMetricValue](class_environment.html#a831d360bb018eadda248072397496a71) (QString)  
| Returns the metric value for the given environment value. [More...](class_environment.html#a831d360bb018eadda248072397496a71)  
  
void | [setCurrentKeyTime](class_environment.html#a142b1b52756c70d8eed943b2317893df) (int)  
void | [setNextKeyTime](class_environment.html#aecaabe93afd0fa26d419b46b5e297eda) (int)  
void | [setEditMode](class_environment.html#aa06cfb473db41cacb82bfbff238c7d6e) (bool)  
bool | [isEditMode](class_environment.html#ac4a31d7a93c8f2b3ac1dd7aeb70ef1d7) ()  
| Returns true if the environment editor window is in Edit mode. [More...](class_environment.html#ac4a31d7a93c8f2b3ac1dd7aeb70ef1d7)  
  
void | [exportToFile](class_environment.html#af74c90ee235bfa9b1e29108092f37696) ()  
| Starts the process for saving the environment window values to an xml file. [More...](class_environment.html#af74c90ee235bfa9b1e29108092f37696)  
  
void | [importFromFile](class_environment.html#ad4b0ebd1bdbbd00371ead8de8c6b3ba8) ()  
| Starts the save process for importing the environment window values from an xml file. [More...](class_environment.html#ad4b0ebd1bdbbd00371ead8de8c6b3ba8)  
  
void | [setAllActive](class_environment.html#addd407a6aaf82da6a270920029ea5ec4) (QString, bool)  
| Goes through all keyframes and staging keyframes and looks for keyframes with the given environment value type and sets them active/inactive. [More...](class_environment.html#addd407a6aaf82da6a270920029ea5ec4)  
  
void | [setKeyframeActive](class_environment.html#a2f24e766263405a7a04cde4df532c3cb) (int, QString, bool)  
| Sets the specified keyframe to active and the environment value in it to be active. [More...](class_environment.html#a2f24e766263405a7a04cde4df532c3cb)  
  
void | [setAllShow](class_environment.html#a018feb8637fde6ec4e1bfaa456a5fda4) (QString, bool)  
| Goes through all keyframes and staging keyframes and looks for keyframes with the given environment value type and sets the stored value for show. [More...](class_environment.html#a018feb8637fde6ec4e1bfaa456a5fda4)  
  
void | [setAllTransference](class_environment.html#a925ac30b3f7993350efe88a7a71c9b0f) (QString, float)  
| Goes through all keyframes and staging keyframes and looks for keyframes with the given environment value type and sets the stored value for transference. [More...](class_environment.html#a925ac30b3f7993350efe88a7a71c9b0f)  
  
void | [setAllInterpolate](class_environment.html#a1608859b0f5d29bbcc69b9188ae3837b) (QString, bool)  
| Goes through all keyframes and staging keyframes and looks for keyframes with the given environment value type and sets the stored value for interpolate. [More...](class_environment.html#a1608859b0f5d29bbcc69b9188ae3837b)  
  
void | [setAllMin](class_environment.html#a5fd23dc5c3bb8e2a2b0c75215b62809e) (QString, float)  
| Goes through all keyframes and staging keyframes and looks for keyframes with the given environment value type and sets the stored value for min value allowed. [More...](class_environment.html#a5fd23dc5c3bb8e2a2b0c75215b62809e)  
  
void | [setAllMax](class_environment.html#ad68558377f1b9e4fb6445e7358ca596f) (QString, float)  
| Goes through all keyframes and staging keyframes and looks for keyframes with the given environment value type and sets the stored value for max value allowed. [More...](class_environment.html#ad68558377f1b9e4fb6445e7358ca596f)  
  
void | [setAllMinRate](class_environment.html#ad59f75a2ef3f5accf3594511b08a8f29) (QString, float)  
| Goes through all keyframes and staging keyframes and looks for keyframes with the given environment value type and sets the stored value for min rate allowed. [More...](class_environment.html#ad59f75a2ef3f5accf3594511b08a8f29)  
  
void | [setAllMaxRate](class_environment.html#aab59293f434b933ec506946f2ed2a131) (QString, float)  
| Goes through all keyframes and staging keyframes and looks for keyframes with the given environment value type and sets the stored value for max rate allowed. [More...](class_environment.html#aab59293f434b933ec506946f2ed2a131)  
  
void | [setManualAdjustment](class_environment.html#a96ea1470eb0ba2d8f31df3bc13689fb3) (QString, float)  
| Sets the manual adjustment property of the given environment value type. [More...](class_environment.html#a96ea1470eb0ba2d8f31df3bc13689fb3)  
  
float | [getCumulativeContribution](class_environment.html#ab42f696ef678eb3d8cc7fbcf7e50d31a) (QString, QString)  
| Retrives the cumulative contribution for a device and environment value type. [More...](class_environment.html#ab42f696ef678eb3d8cc7fbcf7e50d31a)  
  
void | [setContribution](class_environment.html#a40982421780a6d589f2b6bcc91cce324) (QString, QString, double, double, bool)  
| Sets the rate, limit and if it is cumulative properties for the environment value for the specified device. [More...](class_environment.html#a40982421780a6d589f2b6bcc91cce324)  
  
void | [removeCumulativeContribution](class_environment.html#aa03cf2cb8f3997a35eeb0e28362ca39b) (QString, QString)  
| Removes the cumulative contribution for the environment value and device pair. [More...](class_environment.html#aa03cf2cb8f3997a35eeb0e28362ca39b)  
  
void | [setThingTransferenceMultiplier](class_environment.html#add4bedbf97f4eb34a77e76034f1185e9) (QString, QString, float)  
| Sets the thing transference multipler the environment value and device pair. [More...](class_environment.html#add4bedbf97f4eb34a77e76034f1185e9)  
  
float | [getTotalContributions](class_environment.html#a559d9812d173854ebb54279d99d5a441) (QString)  
| Retrives the total contribution for all environment entries of the given environment value type. [More...](class_environment.html#a559d9812d173854ebb54279d99d5a441)  
  
int | [getSimTimeSetting](class_environment.html#aece22a7171670dd21d185d5268bcb526) ()  
| Retrives second value of the "Simulation Time Scale:". [More...](class_environment.html#aece22a7171670dd21d185d5268bcb526)  
  
int | [getRealTimeSetting](class_environment.html#aa9f7d4d29dcb44d0321a745e76cada52) ()  
| Retrives first value of the "Simulation Time Scale:". [More...](class_environment.html#aa9f7d4d29dcb44d0321a745e76cada52)  
  
int | [getSimTimeCombo](class_environment.html#addf7914d11400191565f56f1c3607a20) ()  
int | [getRealTimeCombo](class_environment.html#a2e4dbf33633aff8ee7ff93cf1df1d112) ()  
void | [setSimTimeSetting](class_environment.html#ab983dcd7d465687d73300696dfd289b4) (int)  
void | [setRealTimeSetting](class_environment.html#a626e08fa5310d84c3d2160160c34a2a8) (int)  
void | [setSimTimeCombo](class_environment.html#a6be53f7ff9e93936e8a767e0d9455467) (int)  
void | [setRealTimeCombo](class_environment.html#a3c529d011945e2acf350eb19c290e44d) (int)  
bool | [isUsingMetric](class_environment.html#a1ff3902f3b1ab2169ea05aa47c2c7c3c) ()  
| Returns if the environment is using the metric system or imperial. [More...](class_environment.html#a1ff3902f3b1ab2169ea05aa47c2c7c3c)  
  
QString | [getNotes](class_environment.html#a1470b0106c0a144834726a9982e3ca48) ()  
void | [setNotes](class_environment.html#a2c0492b3cd1d1fbb5ee16376f2fb53bd) (QString)  
bool | [isShowNotes](class_environment.html#a6c7bf824981fd5538e59107a950534c7) ()  
| Returns if notes are set to show in the environment advanced options window. [More...](class_environment.html#a6c7bf824981fd5538e59107a950534c7)  
  
void | [setShowNotes](class_environment.html#a4815440365b3c522d2f5e4a4e57ac49a) (bool)  
| Sets the environment window property for whether notes should be shown in the advanced window. [More...](class_environment.html#a4815440365b3c522d2f5e4a4e57ac49a)  
  
bool | [isEditingLocked](class_environment.html#a132a7c3b26eae5551aa47cc5100c62f4) ()  
| Returns if the environment editing window has been locked by interace locking option. [More...](class_environment.html#a132a7c3b26eae5551aa47cc5100c62f4)  
  
void | [addCustomEnvironment](class_environment.html#ab615b7e96806d4eb761e134c0ae4903f) (QString, QString, QString, QString, QString, QString, QString, QString)  
| Adds a custom environment value type to the environment. [More...](class_environment.html#ab615b7e96806d4eb761e134c0ae4903f)  
  
void | [removeCustomEnvironment](class_environment.html#ad5d858c2321eed57bf352c21a9e72f31) (QString)  
| Removes a custom environment value type from the environment. This is only for custom properties, not for included properties like "CO2". [More...](class_environment.html#ad5d858c2321eed57bf352c21a9e72f31)  
  
bool | [isCustomEnvironment](class_environment.html#a919ab0a4bc401b6d91b328a80495a35e) (QString)  
| Returns true if the environment value is a custom environment value. [More...](class_environment.html#a919ab0a4bc401b6d91b328a80495a35e)  
  
int | [getNextKeyTime](class_environment.html#acbdc76704abdbbc65c416056abd0f822) ()  
| Debugging tool for getting the next keyframe time. [More...](class_environment.html#acbdc76704abdbbc65c416056abd0f822)  
  
int | [getCurrentKeyTime](class_environment.html#a6389d87625bf46672b6ea1f4c0df075b) ()  
| Debugging tool for getting the current keyframe time. [More...](class_environment.html#a6389d87625bf46672b6ea1f4c0df075b)  
  
int | [getElapsedTime](class_environment.html#a683c7161c407fd0c163e081c8cdfc156) (int)  
| Returns the time difference between the given time and the current environment time, in seconds. [More...](class_environment.html#a683c7161c407fd0c163e081c8cdfc156)  
  
int | [getKeyframeTemplateCount](class_environment.html#a1d83c3b9ed7cff4ed3d56c51003be286) ()  
| Returns how many default keyframe categores there are in the "Defaults:" section of the environment window when setting up advanced keyframes. [More...](class_environment.html#a1d83c3b9ed7cff4ed3d56c51003be286)  
  
QString | [getKeyframeTemplateAt](class_environment.html#a3501e9a002f9bdc89f0da36c41c98336) (int)  
| Returns the default keyframe template name at the given index. [More...](class_environment.html#a3501e9a002f9bdc89f0da36c41c98336)  
  
void | [importKeyframeTemplate](class_environment.html#a4916b8ed089673e51e40440217d15ddd) (QString)  
| Starts importing a default keyframe template. [More...](class_environment.html#a4916b8ed089673e51e40440217d15ddd)  
  
[Environment](class_environment.html) | [parentEnvironment](class_environment.html#a28d5ba68c17bae41cad934e1f2bc0c41) ()  
| Returns the parent environment. [More...](class_environment.html#a28d5ba68c17bae41cad934e1f2bc0c41)  
  
void | [setGraphEnvironment](class_environment.html#ad44d2024c53a980d7f0519aa5c8db89a) (QString)  
QString | [getGraphEnvironment](class_environment.html#a765fa21cbf9107e9aef867e2926ec5fa) ()  
float | [getVolume](class_environment.html#ad57ac513891d410bc15c62c85fd54a67) ()  
| Returns the total volume of the object that contains the environment. [More...](class_environment.html#ad57ac513891d410bc15c62c85fd54a67)  
  
QString | [getChangesAsJSON](class_environment.html#ad7a7e8246c88db45785d27795e7314c2) ()  
| Returns change information as JSON data. [More...](class_environment.html#ad7a7e8246c88db45785d27795e7314c2)  
  
QString | [getKeyframeDataAsJSON](class_environment.html#ac352ebe9197168e7ed3b5df0cfdd0741) (QString)  
| Returns keyframes with the given environment value as JSON data. [More...](class_environment.html#ac352ebe9197168e7ed3b5df0cfdd0741)  
  
bool | [removeEnvironmentKeyframe](class_environment.html#a9acfc3d30434a89ef9f51092e4ac58a5) (QString, int)  
| Removes the environment keyframe at the given time if it has the given environment variable type and it isn't the start or end keyframe. [More...](class_environment.html#a9acfc3d30434a89ef9f51092e4ac58a5)  
  
  
## Detailed Description

An object in the Physical [Workspace](class_workspace.html "Workspace is the base class for Logical and Physical workspace related objects."). 

[Environment](class_environment.html "An object in the Physical Workspace.") Dialog. 

## Member Function Documentation

## ◆ addCustomEnvironment()

void Environment::addCustomEnvironment  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | QString  | ,   
|  | QString  | ,   
|  | QString  | ,   
|  | QString  | ,   
|  | QString  | ,   
|  | QString  |   
| ) | |   
  
Adds a custom environment value type to the environment. 

Parameters
     categoryId,category| to add the value to, like "Radiation" or "Other".   
---|---  
category,category| to add, make it the same as categoryId.   
id,name| of the environment value. Like "Sweetness"   
name,name| to display in the editor window for the environment value.   
metricUnit,metric| unit to display when display the value is in metric units.   
imperialUnit,imperial| unit to display when value is in imperial units.   
imperialFormula,conversion| formula to convert from   
  
## ◆ addKeyframe()

[EnvironmentKeyframe](class_environment_keyframe.html) Environment::addKeyframe  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Adds a keyframe at the specified time and returns the new keyframe. 

Parameters
     time,the| time to add the keyframe at, in seconds. Time loops every 24 hours so the valid range is [0, 86400).  
---|---  
  
Returns
    [EnvironmentKeyframe](class_environment_keyframe.html "An object in the Physical Workspace."), the keyframe added. 

## ◆ addKeyframeFromStaging()

int Environment::addKeyframeFromStaging  | ( | | ) |   
---|---|---|---|---  
  
Adds a keyframe from staging. 

Returns
    int, value is index of the keyframe after it gets added from staging. 

## ◆ exportToFile()

void Environment::exportToFile  | ( | | ) |   
---|---|---|---|---  
  
Starts the process for saving the environment window values to an xml file. 

## ◆ getChangesAsJSON()

QString Environment::getChangesAsJSON  | ( | | ) |   
---|---|---|---|---  
  
Returns change information as JSON data. 

Returns
    QString, return is the change information as JSON data. 

## ◆ getCumulativeContribution()

float Environment::getCumulativeContribution  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Retrives the cumulative contribution for a device and environment value type. 

Parameters
     env,name| of the environment to read the value for.   
---|---  
devName,device| to find the environment value for.  
  
Returns
    float, value is the cumulative contribution based on the params. 

## ◆ getCurrentKeyTime()

int Environment::getCurrentKeyTime  | ( | | ) |   
---|---|---|---|---  
  
Debugging tool for getting the current keyframe time. 

Returns
    int, return is the current keyframe time. 

## ◆ getElapsedTime()

int Environment::getElapsedTime  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the time difference between the given time and the current environment time, in seconds. 

Parameters
     lastTime,time| to subtract from the current time to find the difference.  
---|---  
  
Returns
    int, return is the time difference between the current time and the given time. 

## ◆ getEnvironment()

[EnvironmentOptions](class_environment_options.html) Environment::getEnvironment  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the options for a specified environment value type, like "CO" for carbon monoxide. 

Parameters
     env,name| of the environment value to retrive, like "CO".  
---|---  
  
Returns
    [EnvironmentOptions](class_environment_options.html "An object in the Physical Workspace."), value is the options for the specificed environment value type. 

## ◆ getEnvironmentKeys()

vector< QString > Environment::getEnvironmentKeys  | ( | | ) |   
---|---|---|---|---  
  
Returns a list of all the environment value types. 

Returns
    vector<QString>, value is a list of all the environment value types. 

## ◆ getEnvironmentOptionsCount()

int Environment::getEnvironmentOptionsCount  | ( | | ) |   
---|---|---|---|---  
  
\Returns how many environment value types there are. Categories are not included in the count, just the contents of all combined.   


Returns
    int, value is the count of all environment values. 

## ◆ getEnvironmentValue()

float Environment::getEnvironmentValue  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the value for the specified environment property. 

Parameters
     env,name| of the environment value to retrive, like "CO".  
---|---  
  
Returns
    float, value is the value of the environment value. If not found it will return -1, but that can also be a valued value. 

## ◆ getGraphEnvironment()

QString Environment::getGraphEnvironment  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getKeyframeAt()

[EnvironmentKeyframe](class_environment_keyframe.html) Environment::getKeyframeAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
How Returns a keyframe at a specified index. 

Parameters
     index,the| keyframe to retrive. Range of [0, [getKeyframeCount()](class_environment.html#a331fbd9c3fc0d71f511557e54e00026e "How many key frames are in the environment.")).  
---|---  
  
Returns
    [EnvironmentKeyframe](class_environment_keyframe.html "An object in the Physical Workspace."), the keyframe at the given index. 

## ◆ getKeyframeCount()

int Environment::getKeyframeCount  | ( | | ) |   
---|---|---|---|---  
  
How many key frames are in the environment. 

Returns
    int, the number of key frames in the environment. 

## ◆ getKeyframeDataAsJSON()

QString Environment::getKeyframeDataAsJSON  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns keyframes with the given environment value as JSON data. 

Parameters
     envID,the| environment variable type to get the information for.  
---|---  
  
Returns
    QString, return is the keyframes' information for the given environment value as JSON data. 

## ◆ getKeyframeIndexAtTime()

int Environment::getKeyframeIndexAtTime  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the index of a keyframe at the given time if one exists. 

Parameters
     time,time| in seconds to retrive the keyframe index for. Time loops every 24 hours so the valid range is [0, 86400).  
---|---  
  
Returns
    int, value is the index if a match was found, -1 if not. 

## ◆ getKeyframeTemplateAt()

QString Environment::getKeyframeTemplateAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the default keyframe template name at the given index. 

Parameters
     index,index| of the template to retrive. Range (0, getKeyFrameTemplateCount())  
---|---  
  
Returns
    QString, return is the default keyframe template name at the given index if it exists, crash if it doesn't. 

## ◆ getKeyframeTemplateCount()

int Environment::getKeyframeTemplateCount  | ( | | ) |   
---|---|---|---|---  
  
Returns how many default keyframe categores there are in the "Defaults:" section of the environment window when setting up advanced keyframes. 

Returns
    int, return is how many default keyframe categores there are in the "Defaults:" section of the environment window when setting up advanced keyframes. 

## ◆ getMetricValue()

float Environment::getMetricValue  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the metric value for the given environment value. 

Parameters
     env,name| of the environment value to retrive, like "CO".  
---|---  
  
Returns
    float, value is the metric value of the environment value. 

## ◆ getNextKeyTime()

int Environment::getNextKeyTime  | ( | | ) |   
---|---|---|---|---  
  
Debugging tool for getting the next keyframe time. 

Returns
    int, return is the next keyframe time. 

## ◆ getNotes()

QString Environment::getNotes  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getRealTimeCombo()

int Environment::getRealTimeCombo  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getRealTimeSetting()

int Environment::getRealTimeSetting  | ( | | ) |   
---|---|---|---|---  
  
Retrives first value of the "Simulation Time Scale:". 

Returns
    int, retun is the value of the first property of "Simulation Time Scale:". 

## ◆ getSimTimeCombo()

int Environment::getSimTimeCombo  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getSimTimeSetting()

int Environment::getSimTimeSetting  | ( | | ) |   
---|---|---|---|---  
  
Retrives second value of the "Simulation Time Scale:". 

Returns
    int, retun is the value of the second property of "Simulation Time Scale:". 

## ◆ getStagingKeyframe()

[EnvironmentKeyframe](class_environment_keyframe.html) Environment::getStagingKeyframe  | ( | | ) |   
---|---|---|---|---  
  
Returns the staging keyframe. 

Returns
    [EnvironmentKeyframe](class_environment_keyframe.html "An object in the Physical Workspace."), value is the staging keyframe. 

## ◆ getTimeInSeconds()

int Environment::getTimeInSeconds  | ( | | ) |   
---|---|---|---|---  
  
Returns the current environment runtime, in seconds. The value loops, so after 24 hours it resets to 0. 

Returns
    int, the current environment runtime, in seconds. 

## ◆ getTimeMultiplier()

float Environment::getTimeMultiplier  | ( | | ) |   
---|---|---|---|---  
  
Multiplier used when calculating how much environment time passes each step, in seconds. 

Returns
    float, the current environment runtime, in seconds. 

## ◆ getTotalContributions()

float Environment::getTotalContributions  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Retrives the total contribution for all environment entries of the given environment value type. 

Parameters
     env,name| of the environment to read the value for.  
---|---  
  
Returns
    float, value is the total contribution based of the given environment value type. 

## ◆ getUnit()

QString Environment::getUnit  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the unit used for the specified environment property. 

Parameters
     env,name| of the environment value to retrive, like "CO".  
---|---  
  
Returns
    QString, value is the unit displayed for the environment value type, like "%" for gasses. The return can be an empty string. 

## ◆ getValueWithUnit()

QString Environment::getValueWithUnit  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns a string combining the specified environment property and the display unit is uses. 

Parameters
     env,name| of the environment value to retrive, like "CO".  
---|---  
  
Returns
    QString, value is a string combining the specified environment property and the display unit is uses. 

## ◆ getVolume()

float Environment::getVolume  | ( | | ) |   
---|---|---|---|---  
  
Returns the total volume of the object that contains the environment. 

Returns
    float, return is the total volume of the object that contains the environment. 

## ◆ hasKeyframeAtTime()

bool Environment::hasKeyframeAtTime  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns if there is a keyframe at the given time. 

Parameters
     time,time| in seconds to retrive the keyframe for. Time loops every 24 hours so the valid range is [0, 86400).  
---|---  
  
Returns
    bool, true if there was a keyframe, false if not. 

## ◆ importFromFile()

void Environment::importFromFile  | ( | | ) |   
---|---|---|---|---  
  
Starts the save process for importing the environment window values from an xml file. 

## ◆ importKeyframeTemplate()

void Environment::importKeyframeTemplate  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Starts importing a default keyframe template. 

Parameters
     file,the| name of the template to import. Like "Blank.xml".  
---|---  
  
Returns
    QString, return is the default keyframe template name at the given index if it exists, crash if it doesn't. 

## ◆ isCustomEnvironment()

bool Environment::isCustomEnvironment  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns true if the environment value is a custom environment value. 

Returns
    bool, return is true if the environment exists and is a custom property or doesn't exist, false if it is not custom. 

## ◆ isEditingLocked()

bool Environment::isEditingLocked  | ( | | ) |   
---|---|---|---|---  
  
Returns if the environment editing window has been locked by interace locking option. 

Returns
    bool, retun is true if the environment window is locked, false if not. 

## ◆ isEditMode()

bool Environment::isEditMode  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the environment editor window is in Edit mode. 

Returns
    bool, value is true if the enviroment window is in Edit mode, false if it is in View mode. 

## ◆ isShowNotes()

bool Environment::isShowNotes  | ( | | ) |   
---|---|---|---|---  
  
Returns if notes are set to show in the environment advanced options window. 

Returns
    bool, retun is true if notes are set to show, false if set to hidden. 

## ◆ isTimeRunning()

bool Environment::isTimeRunning  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the environment time is running, false if paused. 

Returns
    bool, true if the environment time is running, false if paused. 

## ◆ isUsingMetric()

bool Environment::isUsingMetric  | ( | | ) |   
---|---|---|---|---  
  
Returns if the environment is using the metric system or imperial. 

Returns
    bool, retun is true if the environment it set to use the metric system, false for imperial. 

## ◆ parentEnvironment()

[Environment](class_environment.html) Environment::parentEnvironment  | ( | | ) |   
---|---|---|---|---  
  
Returns the parent environment. 

Returns
    [Environment](class_environment.html "An object in the Physical Workspace."), return is the parent environment if it exists, null if not. 

## ◆ pauseTime()

void Environment::pauseTime  | ( | | ) |   
---|---|---|---|---  
  
Pauses the environment time. 

## ◆ removeCumulativeContribution()

void Environment::removeCumulativeContribution  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Removes the cumulative contribution for the environment value and device pair. 

Parameters
     env,name| of the environment value to remove for.   
---|---  
devName,device| to remove for.   
  
## ◆ removeCustomEnvironment()

void Environment::removeCustomEnvironment  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Removes a custom environment value type from the environment. This is only for custom properties, not for included properties like "CO2". 

Parameters
     env,name| of the environment value. Like "Sweetness"   
---|---  
  
## ◆ removeEnvironmentKeyframe()

bool Environment::removeEnvironmentKeyframe  | ( | QString  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Removes the environment keyframe at the given time if it has the given environment variable type and it isn't the start or end keyframe. 

Parameters
     envID,the| environment variable type that must be in the specified keyframe time for it to be removed.   
---|---  
time,the| environment time of the keyframe to remove.  
  
Returns
    bool, return is true a keyframe was removed, false if not. 

## ◆ removeKeyframe()

void Environment::removeKeyframe  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Removes the keyframe at the given index if the keyframe exists and isn't the start or end. 

Parameters
     index,index| of the keyframe to remove. Range of (1, [getKeyframeCount()](class_environment.html#a331fbd9c3fc0d71f511557e54e00026e "How many key frames are in the environment.")-1).   
---|---  
  
## ◆ resumeTime()

void Environment::resumeTime  | ( | | ) |   
---|---|---|---|---  
  
Resumes the environment time. 

## ◆ setAllActive()

void Environment::setAllActive  | ( | QString  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Goes through all keyframes and staging keyframes and looks for keyframes with the given environment value type and sets them active/inactive. 

Parameters
     envId,name| of the environment to check keyframes for.   
---|---  
bOn,true| if keyframes containing the value should be activated, false if deactivated.   
  
## ◆ setAllInterpolate()

void Environment::setAllInterpolate  | ( | QString  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Goes through all keyframes and staging keyframes and looks for keyframes with the given environment value type and sets the stored value for interpolate. 

Parameters
     envId,name| of the environment to check keyframes for.   
---|---  
bOn,true| to use interpolation, false to not.   
  
## ◆ setAllMax()

void Environment::setAllMax  | ( | QString  | ,   
---|---|---|---  
|  | float  |   
| ) | |   
  
Goes through all keyframes and staging keyframes and looks for keyframes with the given environment value type and sets the stored value for max value allowed. 

Parameters
     envId,name| of the environment to check keyframes for.   
---|---  
value,max| value allowed by the environment value.   
  
## ◆ setAllMaxRate()

void Environment::setAllMaxRate  | ( | QString  | ,   
---|---|---|---  
|  | float  |   
| ) | |   
  
Goes through all keyframes and staging keyframes and looks for keyframes with the given environment value type and sets the stored value for max rate allowed. 

Parameters
     envId,name| of the environment to check keyframes for.   
---|---  
value,max| rate value used by the environment value.   
  
## ◆ setAllMin()

void Environment::setAllMin  | ( | QString  | ,   
---|---|---|---  
|  | float  |   
| ) | |   
  
Goes through all keyframes and staging keyframes and looks for keyframes with the given environment value type and sets the stored value for min value allowed. 

Parameters
     envId,name| of the environment to check keyframes for.   
---|---  
value,min| value allowed by the environment value.   
  
## ◆ setAllMinRate()

void Environment::setAllMinRate  | ( | QString  | ,   
---|---|---|---  
|  | float  |   
| ) | |   
  
Goes through all keyframes and staging keyframes and looks for keyframes with the given environment value type and sets the stored value for min rate allowed. 

Parameters
     envId,name| of the environment to check keyframes for.   
---|---  
value,min| rate value used by the environment value.   
  
## ◆ setAllShow()

void Environment::setAllShow  | ( | QString  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Goes through all keyframes and staging keyframes and looks for keyframes with the given environment value type and sets the stored value for show. 

Parameters
     envId,name| of the environment to check keyframes for.   
---|---  
bOn,true| if keyframes containing the value and the value should be shown, false if not shown.   
  
## ◆ setAllTransference()

void Environment::setAllTransference  | ( | QString  | ,   
---|---|---|---  
|  | float  |   
| ) | |   
  
Goes through all keyframes and staging keyframes and looks for keyframes with the given environment value type and sets the stored value for transference. 

Parameters
     envId,name| of the environment to check keyframes for.   
---|---  
value,transference| to use.   
  
## ◆ setContribution()

void Environment::setContribution  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | double  | ,   
|  | double  | ,   
|  | bool  |   
| ) | |   
  
Sets the rate, limit and if it is cumulative properties for the environment value for the specified device. 

Parameters
     env,name| of the environment value to set the values for.   
---|---  
devName,device| to set for.   
rate,rate| to use. If 0 it wipes out all the values and doesn't set any of the values passed.   
limit,limit| to use.   
bCumulative,true| if it should be set to cumulative, false if not.   
  
## ◆ setCurrentKeyTime()

void Environment::setCurrentKeyTime  | ( | int  | | ) |   
---|---|---|---|---|---  
  
## ◆ setEditMode()

void Environment::setEditMode  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
## ◆ setGraphEnvironment()

void Environment::setGraphEnvironment  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
## ◆ setKeyframeActive()

void Environment::setKeyframeActive  | ( | int  | ,   
---|---|---|---  
|  | QString  | ,   
|  | bool  |   
| ) | |   
  
Sets the specified keyframe to active and the environment value in it to be active. 

Parameters
     currentKeyframeIndex,index| of the keyframe to set.   
---|---  
envId,name| of the environment to set for in the keyframe.   
bOn,true| if keyframes containing the value should be activated, false if deactivated.   
  
## ◆ setManualAdjustment()

void Environment::setManualAdjustment  | ( | QString  | ,   
---|---|---|---  
|  | float  |   
| ) | |   
  
Sets the manual adjustment property of the given environment value type. 

Parameters
     env,the| name of the environment value type to set the property for. Like "CO2".  
---|---  
value,value| to set the env property value with.   
  
## ◆ setNextKeyTime()

void Environment::setNextKeyTime  | ( | int  | | ) |   
---|---|---|---|---|---  
  
## ◆ setNotes()

void Environment::setNotes  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
## ◆ setRealTimeCombo()

void Environment::setRealTimeCombo  | ( | int  | | ) |   
---|---|---|---|---|---  
  
## ◆ setRealTimeSetting()

void Environment::setRealTimeSetting  | ( | int  | | ) |   
---|---|---|---|---|---  
  
## ◆ setShowNotes()

void Environment::setShowNotes  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Sets the environment window property for whether notes should be shown in the advanced window. 

Parameters
     b,true| to set notes to show when advanced options are viewied, false if they should be hidden.   
---|---  
  
## ◆ setSimTimeCombo()

void Environment::setSimTimeCombo  | ( | int  | | ) |   
---|---|---|---|---|---  
  
## ◆ setSimTimeSetting()

void Environment::setSimTimeSetting  | ( | int  | | ) |   
---|---|---|---|---|---  
  
## ◆ setThingTransferenceMultiplier()

void Environment::setThingTransferenceMultiplier  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | float  |   
| ) | |   
  
Sets the thing transference multipler the environment value and device pair. 

Parameters
     env,name| of the environment value to remove for.   
---|---  
devName,device| to remove for.   
multiplier,multiplier| to store.   
  
## ◆ setTimeInSeconds()

void Environment::setTimeInSeconds  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the current environment time to the given time, in seconds. Time loops every 24 hours. 

Parameters
     seconds,the| number of seconds to set the current environment time to. Time loops every 24 hours so the valid range is [0, 86400).   
---|---  
  
## ◆ setTimeMultiplier()

void Environment::setTimeMultiplier  | ( | float  | | ) |   
---|---|---|---|---|---  
  
Sets the multiplier used when calculating how much environment time passes each step, in seconds. 

Parameters
     x,the| number of seconds to set the step multipler as.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [Environment.pki](_environment_8pki.html)


