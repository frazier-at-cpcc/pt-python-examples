# Cisco Packet Tracer Extensions API: ActivityFile Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_activity_file.html

---

[ActivityFile](class_activity_file.html "ActivityFile extends from NetworkFile. It adds the activity layer to the file.") extends from [NetworkFile](class_network_file.html "NetworkFile is the main system file for the application. It holds all the configurations for the engi..."). It adds the activity layer to the file. [More...](class_activity_file.html#details)

##  Public Member Functions  
  
---  
QString | [getInstruction](class_activity_file.html#af1d058a1ca96ab99f58596328e65e051) (int)  
| Returns the evaluated instructions at the specified index. [More...](class_activity_file.html#af1d058a1ca96ab99f58596328e65e051)  
  
QString | [getInstructionSource](class_activity_file.html#a69d8acf217d39470b9d3b4e9bab467a4) (int)  
| Returns the instruction source at the specified index. [More...](class_activity_file.html#a69d8acf217d39470b9d3b4e9bab467a4)  
  
QString | [getCurrentInstructionSource](class_activity_file.html#ad0fa05da1e56b150294e9d4bc3f2a2bb) ()  
| Returns the current intruction source. [More...](class_activity_file.html#ad0fa05da1e56b150294e9d4bc3f2a2bb)  
  
QString | [getCurrentInstruction](class_activity_file.html#aec5562a70fbcdaf1c3c4ad7f8c1714f2) ()  
| Returns the current evaluated instructions. [More...](class_activity_file.html#aec5562a70fbcdaf1c3c4ad7f8c1714f2)  
  
int | [getInstructionCount](class_activity_file.html#a6b5b06d59ac65dfac2f5e4a29919f677) ()  
| Returns the number of instruction pages. [More...](class_activity_file.html#a6b5b06d59ac65dfac2f5e4a29919f677)  
  
void | [resetActivity](class_activity_file.html#ae6f947046f6d09bbdb10808df4f34d92) ()  
| Resets the activity. [More...](class_activity_file.html#ae6f947046f6d09bbdb10808df4f34d92)  
  
double | [getPercentageComplete](class_activity_file.html#a62ba5b9bedf1f557295c9930d1f4189f) ()  
| Returns the percentage complete. [More...](class_activity_file.html#a62ba5b9bedf1f557295c9930d1f4189f)  
  
double | [getAssessmentItemsCount](class_activity_file.html#a43d933017e7c8dea30c74835d0849e30) ()  
| Returns the total number of assessment items. [More...](class_activity_file.html#a43d933017e7c8dea30c74835d0849e30)  
  
double | [getCorrectAssessmentItemsCount](class_activity_file.html#a411e1c5b4e7d8544c92876fda3cdeb6c) ()  
| Returns the number of correct assessment items. [More...](class_activity_file.html#a411e1c5b4e7d8544c92876fda3cdeb6c)  
  
double | [getAssessmentScoreCount](class_activity_file.html#a371b35b19e7d68cbb5382b0f807adcda) ()  
| Returns the total number of assessment scores. [More...](class_activity_file.html#a371b35b19e7d68cbb5382b0f807adcda)  
  
double | [getCorrectAssessmentScoreCount](class_activity_file.html#a6d6012a333984e0d480b1f160fe0f9e8) ()  
| Returns the number of correct assessment scores. [More...](class_activity_file.html#a6d6012a333984e0d480b1f160fe0f9e8)  
  
void | [runConnectivityTests](class_activity_file.html#a33644274c1519e05f727286fd55f5dd6) ()  
| Runs the connectivity tests. [More...](class_activity_file.html#a33644274c1519e05f727286fd55f5dd6)  
  
double | [getConnectivityCount](class_activity_file.html#add6fe3c8d9f1ff46d9213cafd826608d) ()  
| Returns the total number of connectivity tests. [More...](class_activity_file.html#add6fe3c8d9f1ff46d9213cafd826608d)  
  
QString | [getLastConnectivityTestResultAt](class_activity_file.html#ac36fc99f1c7c4d5e6741e70e766acb0e) (int)  
| Returns the connectivity test result of the last run at index. [More...](class_activity_file.html#ac36fc99f1c7c4d5e6741e70e766acb0e)  
  
int | [getLastConnectivityTestCorrectCount](class_activity_file.html#a34cc3f55ac6d8e390fb75f3e86f244d2) ()  
| Returns the number of correct connectivity tests at the last run. [More...](class_activity_file.html#a34cc3f55ac6d8e390fb75f3e86f244d2)  
  
[TreeNode](class_tree_node.html) | [getComparatorTree](class_activity_file.html#a85e5edd468dd6a8d63d2e0a9e7466baa) ()  
| Returns the assessment item tree. [More...](class_activity_file.html#a85e5edd468dd6a8d63d2e0a9e7466baa)  
  
[TreeNode](class_tree_node.html) | [getAssessedComparatorTree](class_activity_file.html#ad929ae041a345e68d969394b6853b3fd) ()  
| Returns the item's assessed assessment item tree. [More...](class_activity_file.html#ad929ae041a345e68d969394b6853b3fd)  
  
[TreeNode](class_tree_node.html) | [getLastAssessedComparatorTree](class_activity_file.html#af8c4073238cdf67ed779d5f8ef25d0ef) ()  
| Returns the item's last assessed assessment item tree. [More...](class_activity_file.html#af8c4073238cdf67ed779d5f8ef25d0ef)  
  
QString | [nextInstructionPage](class_activity_file.html#ad329b4ea4e5edc96ca8bf8106dddeac1) ()  
| Go to the next instruction page and returns the evaluated instruction. [More...](class_activity_file.html#ad329b4ea4e5edc96ca8bf8106dddeac1)  
  
QString | [prevInstructionPage](class_activity_file.html#a7be59139d824a37f619a32f66651b54d) ()  
| Go to the previous instruction page and returns the evaluated instruction. [More...](class_activity_file.html#a7be59139d824a37f619a32f66651b54d)  
  
QString | [removeInstructionPage](class_activity_file.html#a26a57289491bfcf71da906d14caf22d6) ()  
| Remove the current instruction page and returns the evaluated instruction. [More...](class_activity_file.html#a26a57289491bfcf71da906d14caf22d6)  
  
QString | [insertInstructionPage](class_activity_file.html#acd6ebf0e4b585f8d85cc37694dfed85c) ()  
| Insert an instruction page and returns the current page evaluated instruction. [More...](class_activity_file.html#acd6ebf0e4b585f8d85cc37694dfed85c)  
  
[LockingTree](class_locking_tree.html) | [getLockingTree](class_activity_file.html#ac5488f7d76c54dd28f6138d4e11ae19c) ()  
| Returns the locking tree. [More...](class_activity_file.html#ac5488f7d76c54dd28f6138d4e11ae19c)  
  
[NetworkFile](class_network_file.html) | [getInitNetworkFile](class_activity_file.html#a616e24a0300d8bd37cd0dcac4f781866) ()  
| Returns the initial network file. [More...](class_activity_file.html#a616e24a0300d8bd37cd0dcac4f781866)  
  
[NetworkFile](class_network_file.html) | [getAnsNetworkFile](class_activity_file.html#a992356a4ea47f97bc74e0a49f953c93e) ()  
| Returns the answer network file. [More...](class_activity_file.html#a992356a4ea47f97bc74e0a49f953c93e)  
  
[NetworkFile](class_network_file.html) | [getUserNetworkFile](class_activity_file.html#abebfa27785c1a3630cc3a4af401db18e) ()  
| Returns the user network file. [More...](class_activity_file.html#abebfa27785c1a3630cc3a4af401db18e)  
  
[NetworkFile](class_network_file.html) | [getVarNetworkFile](class_activity_file.html#ae94f5323dc4dea2bedf028d9ee617491) ()  
| Returns the var network file. [More...](class_activity_file.html#ae94f5323dc4dea2bedf028d9ee617491)  
  
[NetworkFile](class_network_file.html) | [getCurrentNetworkFile](class_activity_file.html#a24cb073b8a27ec3de22ed356f47aa0b1) ()  
| Returns the current network file in activity wizard, which can be the init, answer, or user network file. [More...](class_activity_file.html#a24cb073b8a27ec3de22ed356f47aa0b1)  
  
QString | [getHashedPassword](class_activity_file.html#a59edc4d00056b891450c8fb1142098e6) ()  
| Returns the MD5 hash of the activity password. [More...](class_activity_file.html#a59edc4d00056b891450c8fb1142098e6)  
  
vector< QString > | [getComponentList](class_activity_file.html#a43ddf8169f579d1ffedff4193a7c7c3a) ()  
| Returns the list of components. [More...](class_activity_file.html#a43ddf8169f579d1ffedff4193a7c7c3a)  
  
void | [setCountDownTime](class_activity_file.html#a5345258cbe015fc34b6c3a7a61073b1f) (int)  
| Sets the countdown time. [More...](class_activity_file.html#a5345258cbe015fc34b6c3a7a61073b1f)  
  
int | [getCountDownTime](class_activity_file.html#aa623081a9f0f077aa7b4b1bc27f6a905) ()  
| Returns the total countdown time in milliseconds. [More...](class_activity_file.html#aa623081a9f0f077aa7b4b1bc27f6a905)  
  
int | [getCountDownTimeLeft](class_activity_file.html#aedea0865f0250b92d7be349ee8dffbfe) ()  
| Returns the countdown time left in milliseconds. [More...](class_activity_file.html#aedea0865f0250b92d7be349ee8dffbfe)  
  
void | [setTimerType](class_activity_file.html#af441e4ca2929fbf3f0d3101749a32add) (ACTIVITYTIMERTYPE)  
| Sets the timer type. [More...](class_activity_file.html#af441e4ca2929fbf3f0d3101749a32add)  
  
ACTIVITYTIMERTYPE | [getTimerType](class_activity_file.html#a6e4bf2f3555a12e6da2f1c71c3b06858) ()  
| Returns the current timer type. [More...](class_activity_file.html#a6e4bf2f3555a12e6da2f1c71c3b06858)  
  
DYNAMICTYPE | [getDynamicPercentageFeedbackType](class_activity_file.html#a987f14190118b9f49e5953c24258d8e3) ()  
| Returns the dynamic feedback type. [More...](class_activity_file.html#a987f14190118b9f49e5953c24258d8e3)  
  
void | [setDynamicPF](class_activity_file.html#aafa96f60ded12a39e3dfaef00cae86c5) (bool)  
| Sets the dynamic feedback to be enabled or disabled. [More...](class_activity_file.html#aafa96f60ded12a39e3dfaef00cae86c5)  
  
bool | [isDynamicPercentageFeedback](class_activity_file.html#ab1b4eb2c7148fe1816612e59e87b6d29) ()  
| Returns the state of the dynamic feedback. [More...](class_activity_file.html#ab1b4eb2c7148fe1816612e59e87b6d29)  
  
[VariableManager](class_variable_manager.html) | [getVariableManager](class_activity_file.html#afd9f62e486a3f2c2aa797644bd9b6c97) ()  
| Returns the [Variable](class_variable.html "Variable is the base class for variables in the VariableManager.") Manager. [More...](class_activity_file.html#afd9f62e486a3f2c2aa797644bd9b6c97)  
  
void | [percentageCompleteChanged](class_activity_file.html#a510730ffb294c8d5b4ab8c75029f170a) (int, int)  
| This event is emitted when the percentage complete changes. [More...](class_activity_file.html#a510730ffb294c8d5b4ab8c75029f170a)  
  
void | [activityReset](class_activity_file.html#ac98c694bd1daac6b2cb39e1d82288da6) ()  
| This event is emitted when the percentage complete changes. [More...](class_activity_file.html#ac98c694bd1daac6b2cb39e1d82288da6)  
  
void | [networkSwitched](class_activity_file.html#af48ea312c3e56257b7c4c95be3bd0a41) (ActivityNetworkType)  
| This event is emitted when changing between networks, like switching to the answer network or the initial network. [More...](class_activity_file.html#af48ea312c3e56257b7c4c95be3bd0a41)  
  
void | [networkFileClosing](class_activity_file.html#a00a75dfe5037693af6bf9078934ad87e) ()  
| This event is emitted when the network file is closed, like when testing the pka. [More...](class_activity_file.html#a00a75dfe5037693af6bf9078934ad87e)  
  
QString | [getDyFeedbackString](class_activity_file.html#a454e41052967f79e0e80fbfc6af51551) ()  
| Returns the dynamic feedback percentage points, percentage score, points, or score. [More...](class_activity_file.html#a454e41052967f79e0e80fbfc6af51551)  
  
double | [getPercentageCompleteScore](class_activity_file.html#a567068b77c5415061829f06e57e839ab) ()  
| Returns the percentage complete score. [More...](class_activity_file.html#a567068b77c5415061829f06e57e839ab)  
  
bool | [isUserProfileLocked](class_activity_file.html#a33080977341a2e4e5934485e1683ea77) ()  
| Returns whether this activity file is profile locked or not. [More...](class_activity_file.html#a33080977341a2e4e5934485e1683ea77)  
  
void | [setCompletedFeedback](class_activity_file.html#a6fefd056ac9acdc887d9a381c3f2cca0) (QString)  
| Sets the text shown on activity completion to be the given text. [More...](class_activity_file.html#a6fefd056ac9acdc887d9a381c3f2cca0)  
  
QString | [getCompletedFeedback](class_activity_file.html#a5a344478dac0d7686465b6e7abf4963b) ()  
| Returns the activity completion feedback text. [More...](class_activity_file.html#a5a344478dac0d7686465b6e7abf4963b)  
  
void | [setInCompleteFeedback](class_activity_file.html#a24a18d5ce83cc37902980df90af46b8b) (QString)  
| Sets the text shown on activity is not yet completed. [More...](class_activity_file.html#a24a18d5ce83cc37902980df90af46b8b)  
  
QString | [getIncompleteFeedback](class_activity_file.html#a2a8f64b391c77f6b3106fbffe0baa7a4) ()  
| Returns the activity incomplete feedback text. [More...](class_activity_file.html#a2a8f64b391c77f6b3106fbffe0baa7a4)  
  
int | [getTimeElapsed](class_activity_file.html#ae479e04b85c9b978f44d1ad9b73e1226) ()  
| Returns the activity run time. [More...](class_activity_file.html#ae479e04b85c9b978f44d1ad9b73e1226)  
  
void | [setTimeElapsed](class_activity_file.html#a12d2e764683e6bf90fd50a8f3eeb5112) (int)  
| Sets the activity current run time. [More...](class_activity_file.html#a12d2e764683e6bf90fd50a8f3eeb5112)  
  
vector< int > | [getChallengeKeyAsInts](class_activity_file.html#ab60b99d80cd90a041d2ffdbcc06d1c5f) ()  
| Get the challenge key for the password. [More...](class_activity_file.html#ab60b99d80cd90a041d2ffdbcc06d1c5f)  
  
QString | [getChallengeKeyAsBase64](class_activity_file.html#adc9d71fcf1ec569b0e88fc8dc0032fa2) ()  
| Get the challenge key for the password. [More...](class_activity_file.html#adc9d71fcf1ec569b0e88fc8dc0032fa2)  
  
bool | [confirmPassword](class_activity_file.html#a9ff1bf2267c93bcf461eab2a738aad93) (QString)  
| Confirm the password, only then will [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") work. [More...](class_activity_file.html#a9ff1bf2267c93bcf461eab2a738aad93)  
  
bool | [isPasswordConfirmed](class_activity_file.html#a69e0855133c0d1f67a6606834838596f) ()  
| Check if password is confirmed. [More...](class_activity_file.html#a69e0855133c0d1f67a6606834838596f)  
  
QString | [getCertInfo](class_activity_file.html#a4f88d80758f8f7e52f17fb996eee6985) ()  
bool | [isActivityFile](class_activity_file.html#ab34fb43bdb8c240dac03d833320ef4b3) ()  
| Returns whether this file is an activity file or regular network file. [More...](class_activity_file.html#ab34fb43bdb8c240dac03d833320ef4b3)  
  
Public Member Functions inherited from [NetworkFile](class_network_file.html)  
QString | [getSavedFilename](class_network_file.html#ad39db310fcbe9537acdb83cb2d0cc3a0) ()  
| Returns the filename of the currently opened file. [More...](class_network_file.html#ad39db310fcbe9537acdb83cb2d0cc3a0)  
  
QString | [getVersion](class_network_file.html#add899ff676d13c9cbb68e8e98ce89acd) ()  
| Returns the version the current file was saved in. [More...](class_network_file.html#add899ff676d13c9cbb68e8e98ce89acd)  
  
QString | [getNetworkDescription](class_network_file.html#ac31096b326e652e38fdc21b707ec14d2) ()  
| Returns the network description of the current file. [More...](class_network_file.html#ac31096b326e652e38fdc21b707ec14d2)  
  
void | [setNetworkDescription](class_network_file.html#a6026d74e5a7116cb545647b1c42b36c9) (QString)  
| Sets the network description for the current file. [More...](class_network_file.html#a6026d74e5a7116cb545647b1c42b36c9)  
  
[Options](class_options.html) | [getOptions](class_network_file.html#a926ba5389b2cb60cd95c7286654f47dc) ()  
| Returns the option settings of the current file. [More...](class_network_file.html#a926ba5389b2cb60cd95c7286654f47dc)  
  
[Network](class_network.html) | [getMainNetwork](class_network_file.html#a46ac622d2a6d64602a46b3e31e987f30) ()  
| Returns the network of the current file. [More...](class_network_file.html#a46ac622d2a6d64602a46b3e31e987f30)  
  
[UserProfile](class_user_profile.html) | [getUserProfile](class_network_file.html#a38c546e9debf684bdc2c953f9f7bdf9a) ()  
| Returns the user profile of the current file. [More...](class_network_file.html#a38c546e9debf684bdc2c953f9f7bdf9a)  
  
[Simulation](class_simulation.html) | [getMainSimulation](class_network_file.html#aa26979829f2dc835543ab93535c9fe67) ()  
| Returns the simulation of the current file. [More...](class_network_file.html#aa26979829f2dc835543ab93535c9fe67)  
  
[Workspace](class_workspace.html) | [getWorkspace](class_network_file.html#a10b424fdf82d159ab8f19d3330df9ae0) ()  
| Returns the workspace of the current file. [More...](class_network_file.html#a10b424fdf82d159ab8f19d3330df9ae0)  
  
[ActivityScriptEngine](class_activity_script_engine.html) | [getActivityScriptEngine](class_network_file.html#ae73eb5b0e7ec7e1bf702da7db6b9c4c0) ()  
| Returns the activity script engine of the current file. [More...](class_network_file.html#ae73eb5b0e7ec7e1bf702da7db6b9c4c0)  
  
[ActivityScriptEngine](class_activity_script_engine.html) | [getScriptEngine](class_network_file.html#a4b33c57dda5d441fd05f326601a1b427) ()  
| Returns the script engine of the current file. [More...](class_network_file.html#a4b33c57dda5d441fd05f326601a1b427)  
  
void | [resetScriptEngine](class_network_file.html#ab297523cea8744d42abfc1621dfcc568) ()  
| Removes the current activity script engine and creates a new one. [More...](class_network_file.html#ab297523cea8744d42abfc1621dfcc568)  
  
bool | [addScript](class_network_file.html#a54de70849c764976e7a84f45e8e801e6) (QString, QString)  
| Adds a script to the activity file. [More...](class_network_file.html#a54de70849c764976e7a84f45e8e801e6)  
  
bool | [addScriptFile](class_network_file.html#ae585096d5a909b477c81d2279569dce1) (QString, QString)  
| Adds the script contents to the activity file from a file path. [More...](class_network_file.html#ae585096d5a909b477c81d2279569dce1)  
  
void | [addDefaultScripts](class_network_file.html#a429ac3bcafa3fca82506b111198e66ac) ()  
| Resets the scripts to the default scripts. [More...](class_network_file.html#a429ac3bcafa3fca82506b111198e66ac)  
  
bool | [removeScript](class_network_file.html#aed9b12765b9fd44fc69d0144405f829f) (QString)  
| Removes the specified script from the activity file hash. [More...](class_network_file.html#aed9b12765b9fd44fc69d0144405f829f)  
  
QString | [getScript](class_network_file.html#ae5988d3f64efe5c4601c2b00d8773648) (QString)  
| Returns the content of the script with the specified ID. [More...](class_network_file.html#ae5988d3f64efe5c4601c2b00d8773648)  
  
vector< QString > | [getScriptIDs](class_network_file.html#a0060962a0f0f49c59e945c4a59b86a65) ()  
| Returns the list of IDs currently in the system. [More...](class_network_file.html#a0060962a0f0f49c59e945c4a59b86a65)  
  
bool | [addScriptDataStore](class_network_file.html#aa576377ab63aa1dc39e31041a7b4581b) (QString, QString)  
| Adds script data store for persistent storage (e.g. constants, options, settings). [More...](class_network_file.html#aa576377ab63aa1dc39e31041a7b4581b)  
  
bool | [removeScriptDataStore](class_network_file.html#a30e07d8196c8573d63f672def5570d35) (QString)  
| Removes the specified script data store for persistent storage (e.g. constants, options, settings). [More...](class_network_file.html#a30e07d8196c8573d63f672def5570d35)  
  
QString | [getScriptDataStore](class_network_file.html#ad280660efe843f30dee566c867920877) (QString)  
| Returns the content of the specified script data store. [More...](class_network_file.html#ad280660efe843f30dee566c867920877)  
  
vector< QString > | [getScriptDataStoreIDs](class_network_file.html#a0f1b26d4c4784eda8b34052546924cfb) ()  
| Returns the list of IDs of script data stores. [More...](class_network_file.html#a0f1b26d4c4784eda8b34052546924cfb)  
  
[FilterSet](class_filter_set.html) | [getFilterSet](class_network_file.html#ad9d6a773f3a77bbeda36f2728e14873d) ()  
| Returns the engine filter set for simulation packets, what is filtered out. [More...](class_network_file.html#ad9d6a773f3a77bbeda36f2728e14873d)  
  
bool | [addCustomTrafficType](class_network_file.html#a30bba52fe1d6fa46ed97742e85007140) (QString)  
| Adds a custom traffic type. Returns true if successful, false otherwise. [More...](class_network_file.html#a30bba52fe1d6fa46ed97742e85007140)  
  
bool | [hasCustomTrafficType](class_network_file.html#a2dc37057bed1c3443f381db1c2eb3dab) (QString)  
| Returns whether a custom traffic type is already added. [More...](class_network_file.html#a2dc37057bed1c3443f381db1c2eb3dab)  
  
bool | [addCustomPduType](class_network_file.html#a04659f37526b157b807ef4a32f979315) (QString, QString)  
| Adds a custom PDU type. Returns true if successful, false otherwise. [More...](class_network_file.html#a04659f37526b157b807ef4a32f979315)  
  
bool | [hasCustomPduType](class_network_file.html#a1a9a50d9b3a26348ed9285de70ec86d8) (QString)  
| Returns whether a custom PDU type is already added. [More...](class_network_file.html#a1a9a50d9b3a26348ed9285de70ec86d8)  
  
void | [duplicateDevice](class_network_file.html#a7faa39e73d4472750e6f46263d61474b) ([Device](class_device.html))  
| Creates and stores a copy of the given device. [More...](class_network_file.html#a7faa39e73d4472750e6f46263d61474b)  
  
bool | [isActivityFile](class_network_file.html#a6eb32fb45be25823b7bb0850dd5c7aaa) ()  
| Returns whether this file is an activity file or regular network file. [More...](class_network_file.html#a6eb32fb45be25823b7bb0850dd5c7aaa)  
  
  
## Detailed Description

[ActivityFile](class_activity_file.html "ActivityFile extends from NetworkFile. It adds the activity layer to the file.") extends from [NetworkFile](class_network_file.html "NetworkFile is the main system file for the application. It holds all the configurations for the engi..."). It adds the activity layer to the file. 

## Member Function Documentation

## ◆ activityReset()

void ActivityFile::activityReset  | ( | | ) |   
---|---|---|---|---  
  
This event is emitted when the percentage complete changes. 

  * oldPercent, the last percentage complete. 
  * newPercent, the new percentage complete.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ confirmPassword()

bool ActivityFile::confirmPassword  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Confirm the password, only then will [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") work. 

## ◆ getAnsNetworkFile()

[NetworkFile](class_network_file.html) ActivityFile::getAnsNetworkFile  | ( | | ) |   
---|---|---|---|---  
  
Returns the answer network file. 

Remarks
    The answer network file is used to compare against the user network.

Returns
    [NetworkFile](class_network_file.html "NetworkFile is the main system file for the application. It holds all the configurations for the engi..."), the answer network file. 

## ◆ getAssessedComparatorTree()

[TreeNode](class_tree_node.html) ActivityFile::getAssessedComparatorTree  | ( | | ) |   
---|---|---|---|---  
  
Returns the item's assessed assessment item tree. 

Remarks
    This tree is compared.

Returns
    [TreeNode](class_tree_node.html "TreeNode handles and manipulates the activity assessment nodes."), the item's assessed assessment item tree. 

## ◆ getAssessmentItemsCount()

double ActivityFile::getAssessmentItemsCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the total number of assessment items. 

Returns
    double, the total number of assessment items. 

## ◆ getAssessmentScoreCount()

double ActivityFile::getAssessmentScoreCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the total number of assessment scores. 

Returns
    double, the total number of assessment scores. 

## ◆ getCertInfo()

QString ActivityFile::getCertInfo  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getChallengeKeyAsBase64()

QString ActivityFile::getChallengeKeyAsBase64  | ( | | ) |   
---|---|---|---|---  
  
Get the challenge key for the password. 

## ◆ getChallengeKeyAsInts()

vector< int > ActivityFile::getChallengeKeyAsInts  | ( | | ) |   
---|---|---|---|---  
  
Get the challenge key for the password. 

## ◆ getComparatorTree()

[TreeNode](class_tree_node.html) ActivityFile::getComparatorTree  | ( | | ) |   
---|---|---|---|---  
  
Returns the assessment item tree. 
    
    
        \brief Returns a structure representing users progress towards the completion of this activity.
        \param refresh - refresh results obtained from the most recent call to this method.
        \param format - defines string representation for the information: "json", "xml", etc.
        \return int, the number of correct connectivity tests at the last run.
    
        \NOT PORTED TO PT DESKTOP
    

QString getActivityProgressInfo(bool refresh, QString format) - PrivActivityWizard;

Remarks
    This tree defines what assessment items can be and what is currently being assessed by this activity.

Returns
    [TreeNode](class_tree_node.html "TreeNode handles and manipulates the activity assessment nodes."), the assessment item tree. 

## ◆ getCompletedFeedback()

QString ActivityFile::getCompletedFeedback  | ( | | ) |   
---|---|---|---|---  
  
Returns the activity completion feedback text. 

Returns
    QString, the activity completion feedback text. 

## ◆ getComponentList()

vector< QString > ActivityFile::getComponentList  | ( | | ) |   
---|---|---|---|---  
  
Returns the list of components. 

Returns
    vector<QString>, the list of components. 

## ◆ getConnectivityCount()

double ActivityFile::getConnectivityCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the total number of connectivity tests. 

Returns
    double, the the total number of connectivity tests. 

## ◆ getCorrectAssessmentItemsCount()

double ActivityFile::getCorrectAssessmentItemsCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of correct assessment items. 

Returns
    double, the number of correct assessment items. 

## ◆ getCorrectAssessmentScoreCount()

double ActivityFile::getCorrectAssessmentScoreCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of correct assessment scores. 

Returns
    double, the number of correct assessment scores. 

## ◆ getCountDownTime()

int ActivityFile::getCountDownTime  | ( | | ) |   
---|---|---|---|---  
  
Returns the total countdown time in milliseconds. 

Returns
    int, the total countdown time in milliseconds. 

## ◆ getCountDownTimeLeft()

int ActivityFile::getCountDownTimeLeft  | ( | | ) |   
---|---|---|---|---  
  
Returns the countdown time left in milliseconds. 

Returns
    int, countdown time left in milliseconds. 

## ◆ getCurrentInstruction()

QString ActivityFile::getCurrentInstruction  | ( | | ) |   
---|---|---|---|---  
  
Returns the current evaluated instructions. 

Returns
    QString, the current evaluated instructions. 

## ◆ getCurrentInstructionSource()

QString ActivityFile::getCurrentInstructionSource  | ( | | ) |   
---|---|---|---|---  
  
Returns the current intruction source. 

Returns
    QString, the current intruction source. 

## ◆ getCurrentNetworkFile()

[NetworkFile](class_network_file.html) ActivityFile::getCurrentNetworkFile  | ( | | ) |   
---|---|---|---|---  
  
Returns the current network file in activity wizard, which can be the init, answer, or user network file. 

Returns
    [NetworkFile](class_network_file.html "NetworkFile is the main system file for the application. It holds all the configurations for the engi..."), the current network file. 

## ◆ getDyFeedbackString()

QString ActivityFile::getDyFeedbackString  | ( | | ) |   
---|---|---|---|---  
  
Returns the dynamic feedback percentage points, percentage score, points, or score. 

Returns
    QString, the dynamic feedback if the type is not set to NOFEEDBACK, otherwise an empty string. 

## ◆ getDynamicPercentageFeedbackType()

DYNAMICTYPE ActivityFile::getDynamicPercentageFeedbackType  | ( | | ) |   
---|---|---|---|---  
  
Returns the dynamic feedback type. 

Returns
    enum<DYNAMICTYPE>, the dynamic feedback type. Dynamic feedback types: NOFEEDBACK = 0, PERCENTAGEPOINT = 1, PERCENTAGESCORE = 2, POINTS = 3, SCORE = 4 

## ◆ getHashedPassword()

QString ActivityFile::getHashedPassword  | ( | | ) |   
---|---|---|---|---  
  
Returns the MD5 hash of the activity password. 

Returns
    QString, the MD5 hash of the activity password. 

## ◆ getIncompleteFeedback()

QString ActivityFile::getIncompleteFeedback  | ( | | ) |   
---|---|---|---|---  
  
Returns the activity incomplete feedback text. 

Returns
    QString, the activity incomplete completion feedback text. 

## ◆ getInitNetworkFile()

[NetworkFile](class_network_file.html) ActivityFile::getInitNetworkFile  | ( | | ) |   
---|---|---|---|---  
  
Returns the initial network file. 

Remarks
    The initial network file is the starting network file. It is used to replace the user network on a new activity or when the user resets the activity.

Returns
    [NetworkFile](class_network_file.html "NetworkFile is the main system file for the application. It holds all the configurations for the engi..."), the initial network file. 

## ◆ getInstruction()

QString ActivityFile::getInstruction  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the evaluated instructions at the specified index. 

Parameters
     index,the| instruction page index. -1 returns the current page.  
---|---  
  
Returns
    QString, the evaluated instructions at the specified index. 

## ◆ getInstructionCount()

int ActivityFile::getInstructionCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of instruction pages. 

Returns
    int, the number of instruction pages. 

## ◆ getInstructionSource()

QString ActivityFile::getInstructionSource  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the instruction source at the specified index. 

Parameters
     index,the| instruction page index.  
---|---  
  
Returns
    QString, the instruction source at the specified index. 

## ◆ getLastAssessedComparatorTree()

[TreeNode](class_tree_node.html) ActivityFile::getLastAssessedComparatorTree  | ( | | ) |   
---|---|---|---|---  
  
Returns the item's last assessed assessment item tree. 

Remarks
    This tree is compared.

Returns
    [TreeNode](class_tree_node.html "TreeNode handles and manipulates the activity assessment nodes."), the item's last assessed assessment item tree. 

## ◆ getLastConnectivityTestCorrectCount()

int ActivityFile::getLastConnectivityTestCorrectCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of correct connectivity tests at the last run. 

Returns
    int, the number of correct connectivity tests at the last run. 

## ◆ getLastConnectivityTestResultAt()

QString ActivityFile::getLastConnectivityTestResultAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the connectivity test result of the last run at index. 

Remarks
    Valid strings are:

  * "Correct" - correct
  * "Incorrect" - incorrect
  * "Do Not Test" - the connectivity test is not configured to be tested
  * "" - the connectivity test has not been ran yet



Returns
    QString, the connectivity test result at index. 

## ◆ getLockingTree()

[LockingTree](class_locking_tree.html) ActivityFile::getLockingTree  | ( | | ) |   
---|---|---|---|---  
  
Returns the locking tree. 

Returns
    [LockingTree](class_locking_tree.html "LockingTree handles and manipulates the activity file locking tree."), the locking tree. 

## ◆ getPercentageComplete()

double ActivityFile::getPercentageComplete  | ( | | ) |   
---|---|---|---|---  
  
Returns the percentage complete. 

Returns
    double, the percentage complete. 

## ◆ getPercentageCompleteScore()

double ActivityFile::getPercentageCompleteScore  | ( | | ) |   
---|---|---|---|---  
  
Returns the percentage complete score. 

Returns
    double, the percentage complete score. 

## ◆ getTimeElapsed()

int ActivityFile::getTimeElapsed  | ( | | ) |   
---|---|---|---|---  
  
Returns the activity run time. 

Returns
    int, how long the activity has been running, in milliseconds. 

## ◆ getTimerType()

ACTIVITYTIMERTYPE ActivityFile::getTimerType  | ( | | ) |   
---|---|---|---|---  
  
Returns the current timer type. 

Returns
    enum<TIMER_TYPE>, the current timer type. Timer types: ELAPSED = 0, COUNTDOWN = 1, NONE = 2 

## ◆ getUserNetworkFile()

[NetworkFile](class_network_file.html) ActivityFile::getUserNetworkFile  | ( | | ) |   
---|---|---|---|---  
  
Returns the user network file. 

Remarks
    The user network file is the network file that the user works with during an activity.

Returns
    [NetworkFile](class_network_file.html "NetworkFile is the main system file for the application. It holds all the configurations for the engi..."), the user network file. 

## ◆ getVariableManager()

[VariableManager](class_variable_manager.html) ActivityFile::getVariableManager  | ( | | ) |   
---|---|---|---|---  
  
Returns the [Variable](class_variable.html "Variable is the base class for variables in the VariableManager.") Manager. 

Returns
    [VariableManager](class_variable_manager.html "VariableManager manages the variables and pools in an activity."), the [Variable](class_variable.html "Variable is the base class for variables in the VariableManager.") Manager. 

## ◆ getVarNetworkFile()

[NetworkFile](class_network_file.html) ActivityFile::getVarNetworkFile  | ( | | ) |   
---|---|---|---|---  
  
Returns the var network file. 

Returns
    [NetworkFile](class_network_file.html "NetworkFile is the main system file for the application. It holds all the configurations for the engi..."), the var network file. 

## ◆ insertInstructionPage()

QString ActivityFile::insertInstructionPage  | ( | | ) |   
---|---|---|---|---  
  
Insert an instruction page and returns the current page evaluated instruction. 

Returns
    QString, the evaluated instructions on the current page.   


## ◆ isActivityFile()

bool ActivityFile::isActivityFile  | ( | | ) |   
---|---|---|---|---  
  
Returns whether this file is an activity file or regular network file. 

## ◆ isDynamicPercentageFeedback()

bool ActivityFile::isDynamicPercentageFeedback  | ( | | ) |   
---|---|---|---|---  
  
Returns the state of the dynamic feedback. 

Returns
    bool, true if dynamic percentage feedback is enabled, otherwise false. 

## ◆ isPasswordConfirmed()

bool ActivityFile::isPasswordConfirmed  | ( | | ) |   
---|---|---|---|---  
  
Check if password is confirmed. 

## ◆ isUserProfileLocked()

bool ActivityFile::isUserProfileLocked  | ( | | ) |   
---|---|---|---|---  
  
Returns whether this activity file is profile locked or not. 

Returns
    bool, true if the user profile is locked and false if not.   


## ◆ networkFileClosing()

void ActivityFile::networkFileClosing  | ( | | ) |   
---|---|---|---|---  
  
This event is emitted when the network file is closed, like when testing the pka. 

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ networkSwitched()

void ActivityFile::networkSwitched  | ( | ActivityNetworkType  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when changing between networks, like switching to the answer network or the initial network. 

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ nextInstructionPage()

QString ActivityFile::nextInstructionPage  | ( | | ) |   
---|---|---|---|---  
  
Go to the next instruction page and returns the evaluated instruction. 

Returns
    QString, the evaluated instructions the next page.   


## ◆ percentageCompleteChanged()

void ActivityFile::percentageCompleteChanged  | ( | int  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
This event is emitted when the percentage complete changes. 

  * oldPercent, the last percentage complete. 
  * newPercent, the new percentage complete.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ prevInstructionPage()

QString ActivityFile::prevInstructionPage  | ( | | ) |   
---|---|---|---|---  
  
Go to the previous instruction page and returns the evaluated instruction. 

Returns
    QString, the evaluated instructions the previous page.   


## ◆ removeInstructionPage()

QString ActivityFile::removeInstructionPage  | ( | | ) |   
---|---|---|---|---  
  
Remove the current instruction page and returns the evaluated instruction. 

Returns
    QString, the evaluated instructions on the page after the removal.   


## ◆ resetActivity()

void ActivityFile::resetActivity  | ( | | ) |   
---|---|---|---|---  
  
Resets the activity. 

## ◆ runConnectivityTests()

void ActivityFile::runConnectivityTests  | ( | | ) |   
---|---|---|---|---  
  
Runs the connectivity tests. 

Remarks
    Use [getLastConnectivityTestResultAt()](class_activity_file.html#ac36fc99f1c7c4d5e6741e70e766acb0e "Returns the connectivity test result of the last run at index.") and [getLastConnectivityTestCorrectCount()](class_activity_file.html#a34cc3f55ac6d8e390fb75f3e86f244d2 "Returns the number of correct connectivity tests at the last run.") to get results afterwards. 

## ◆ setCompletedFeedback()

void ActivityFile::setCompletedFeedback  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Sets the text shown on activity completion to be the given text. 

Parameters
     str,the| text to use for activity completion message.   
  
---|---  
  
## ◆ setCountDownTime()

void ActivityFile::setCountDownTime  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the countdown time. 

Parameters
     ms,countdown| time in milliseconds.   
---|---  
  
## ◆ setDynamicPF()

void ActivityFile::setDynamicPF  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Sets the dynamic feedback to be enabled or disabled. 

Parameters
     enable,true| enables dynamic percentage feedback, false disables it.   
---|---  
  
## ◆ setInCompleteFeedback()

void ActivityFile::setInCompleteFeedback  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Sets the text shown on activity is not yet completed. 

Parameters
     str,the| text to use for activity incomplete message.   
  
---|---  
  
## ◆ setTimeElapsed()

void ActivityFile::setTimeElapsed  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the activity current run time. 

Parameters
     ms,runtime| time in milliseconds.   
---|---  
  
## ◆ setTimerType()

void ActivityFile::setTimerType  | ( | ACTIVITYTIMERTYPE  | | ) |   
---|---|---|---|---|---  
  
Sets the timer type. 

Parameters
     e,the| type of timer. Timer types: ELAPSED = 0, COUNTDOWN = 1, NONE = 2   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [ActivityFile.pki](_activity_file_8pki.html)


