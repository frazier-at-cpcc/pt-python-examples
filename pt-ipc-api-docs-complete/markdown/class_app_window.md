# Cisco Packet Tracer Extensions API: AppWindow Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_app_window.html

---

[AppWindow](class_app_window.html "AppWindow serves as the entry point to all GUI objects.") serves as the entry point to all GUI objects. [More...](class_app_window.html#details)

##  Public Member Functions  
  
---  
[MenuBar](class_menu_bar.html) | [getMenuBar](class_app_window.html#a4f39eb89c08142ee49456ef024f995d0) ()  
| Returns the menu bar. [More...](class_app_window.html#a4f39eb89c08142ee49456ef024f995d0)  
  
[ToolBar](class_tool_bar.html) | [getToolBar](class_app_window.html#a9d67f1d5d4622ca0f415d8fb8f51aa57) ()  
| Returns the toolbar. [More...](class_app_window.html#a9d67f1d5d4622ca0f415d8fb8f51aa57)  
  
[ToolBar](class_tool_bar.html) | [getSecondaryToolBar](class_app_window.html#a1f4f71f0fa3206efa48e90c493d518eb) ()  
| Returns the secondary toolbar. [More...](class_app_window.html#a1f4f71f0fa3206efa48e90c493d518eb)  
  
[RSSwitch](class_r_s_switch.html) | [getRSSwitch](class_app_window.html#a4230609edd8411f9a2dbe72141521e01) ()  
| Returns the Realtime/Simulation mode switch. [More...](class_app_window.html#a4230609edd8411f9a2dbe72141521e01)  
  
[PLSwitch](class_p_l_switch.html) | [getPLSwitch](class_app_window.html#a89b849550588bacff093d12616183a6b) ()  
| Returns the Physical/Logical workspace switch. [More...](class_app_window.html#a89b849550588bacff093d12616183a6b)  
  
[LogicalToolbar](class_logical_toolbar.html) | [getLogicalToolbar](class_app_window.html#a9cdc87ca3021815a52a4edae53e87b53) ()  
| Returns the Logical workspace toolbar. [More...](class_app_window.html#a9cdc87ca3021815a52a4edae53e87b53)  
  
[PhysicalToolbar](class_physical_toolbar.html) | [getPhysicalToolbar](class_app_window.html#ac53563bb1c67e9332fc3f0f71968d1f8) ()  
| Returns the Physical workspace toolbar. [More...](class_app_window.html#ac53563bb1c67e9332fc3f0f71968d1f8)  
  
[SimulationToolbar](class_simulation_toolbar.html) | [getSimulationToolbar](class_app_window.html#ab2858215d67365146f4509c13914b26a) ()  
| Returns the [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") mode toolbar. [More...](class_app_window.html#ab2858215d67365146f4509c13914b26a)  
  
[RealtimeToolbar](class_realtime_toolbar.html) | [getRealtimeToolbar](class_app_window.html#a6f60a895d4c265236c41435eb6e23842) ()  
| Returns the Realtime mode toolbar. [More...](class_app_window.html#a6f60a895d4c265236c41435eb6e23842)  
  
void | [setPLFrameVisible](class_app_window.html#a8089743f416e64b7a934c99e2cf25efe) (bool)  
void | [setRSFrameVisible](class_app_window.html#af7ed96a4f686fa2c0cc452dfd9673701) (bool)  
[PhysicalLocationDialog](class_physical_location_dialog.html) | [getPhysicalLocationDialog](class_app_window.html#af8aecfb8223141df54eb63b3fbb86482) ()  
| Returns the Physical Location dialog. [More...](class_app_window.html#af8aecfb8223141df54eb63b3fbb86482)  
  
[SimulationPanel](class_simulation_panel.html) | [getSimulationPanel](class_app_window.html#a8f9c6be12d502d6a3d5179d71ddb7a05) ()  
| Returns the [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") panel. [More...](class_app_window.html#a8f9c6be12d502d6a3d5179d71ddb7a05)  
  
[UserCreatedPDU](class_user_created_p_d_u.html) | [getUserCreatedPDU](class_app_window.html#a326b1fb50e7367780626ff7345531c46) ()  
| Returns the User Created PDU. [More...](class_app_window.html#a326b1fb50e7367780626ff7345531c46)  
  
[NetworkComponentBox](class_network_component_box.html) | [getNetworkComponentBox](class_app_window.html#a12df80076353923870352a67f3970bed) ()  
| Returns the [Network](class_network.html "Network is the entry point for all device configurations in the network. It retrieves devices.") Component Box. [More...](class_app_window.html#a12df80076353923870352a67f3970bed)  
  
[PDUListWindow](class_p_d_u_list_window.html) | [getPDUListWindow](class_app_window.html#ab82ca25824e895dfd06107cd5e97b36f) ()  
| Returns the PDU list window. [More...](class_app_window.html#ab82ca25824e895dfd06107cd5e97b36f)  
  
[ActivityWizard](class_activity_wizard.html) | [getActivityWizard](class_app_window.html#a12d59ee2d44e188785a5b749ce36a99e) ()  
| Returns the Activity Wizard. [More...](class_app_window.html#a12d59ee2d44e188785a5b749ce36a99e)  
  
[InfoDialog](class_info_dialog.html) | [getInfoDialog](class_app_window.html#ab8e4e9bf1a1a1311302a01500eebd6e4) ()  
| Returns the info dialog. [More...](class_app_window.html#ab8e4e9bf1a1a1311302a01500eebd6e4)  
  
[CommonToolbar](class_common_toolbar.html) | [getCommonToolbar](class_app_window.html#aeaffa4e1a7cff6fe4a752ae4be40181e) ()  
| Returns the Common Toolbar. [More...](class_app_window.html#aeaffa4e1a7cff6fe4a752ae4be40181e)  
  
bool | [isSimulationMode](class_app_window.html#a1c4604c99d37cda3e67ed1d0f1a17e0a) ()  
| Returns true if currently in [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") mode, otherwise false. [More...](class_app_window.html#a1c4604c99d37cda3e67ed1d0f1a17e0a)  
  
bool | [isRealtimeMode](class_app_window.html#adb82b8733972af7d3b47af5487bf2a64) ()  
| Returns true if currently in Realtime mode, otherwise false. [More...](class_app_window.html#adb82b8733972af7d3b47af5487bf2a64)  
  
bool | [isLogicalMode](class_app_window.html#a50029c993a0991b7ae4be5539726f19a) ()  
| Returns true if currently in Logical workspace, otherwise false. [More...](class_app_window.html#a50029c993a0991b7ae4be5539726f19a)  
  
bool | [isPhysicalMode](class_app_window.html#a992c207b027b8f9ddbab1d7cafdf7051) ()  
| Returns true if currently in Physical workspace, otherwise false. [More...](class_app_window.html#a992c207b027b8f9ddbab1d7cafdf7051)  
  
[Workspace](class_workspace.html) | [getActiveWorkspace](class_app_window.html#a7fd4124b34a8267a9c80c106b6214e19) ()  
| Returns the current active workspace. [More...](class_app_window.html#a7fd4124b34a8267a9c80c106b6214e19)  
  
[ActiveDialog](class_active_dialog.html) | [getActiveDialog](class_app_window.html#a3611e57b264157bef50047c487f3200f) ()  
| Returns the current active dialog. [More...](class_app_window.html#a3611e57b264157bef50047c487f3200f)  
  
[AdministrativeDialog](class_administrative_dialog.html) | [getAdminDialog](class_app_window.html#aa0cb83387658b20984e83c4f7b835efd) ()  
| Returns the administrative dialog. [More...](class_app_window.html#aa0cb83387658b20984e83c4f7b835efd)  
  
[PaletteDialog](class_palette_dialog.html) | [getPaletteDialog](class_app_window.html#a0c5b4c56772a4850cb3df2bb3a9ed0bc) ()  
| Returns the palette dialog. [More...](class_app_window.html#a0c5b4c56772a4850cb3df2bb3a9ed0bc)  
  
[PrintDialogPT4](class_print_dialog_p_t4.html) | [getPrintDialog](class_app_window.html#ae9d3d3872decba4757ce5fe89510f5f9) ()  
| Returns the print dialog. [More...](class_app_window.html#ae9d3d3872decba4757ce5fe89510f5f9)  
  
[InstructionDlg](class_instruction_dlg.html) | [getInstructionDlg](class_app_window.html#a22db14f37c8fac47a700c7a5b0388713) ()  
| Returns the activity instructions dialog. [More...](class_app_window.html#a22db14f37c8fac47a700c7a5b0388713)  
  
void | [suppressInstructionDlg](class_app_window.html#a54500c2474b0c2e90605040d6e5a3cbe) (bool)  
[WebViewManager](class_web_view_manager.html) | [getWebViewManager](class_app_window.html#a0893c734d037e24f310e4dcdf3023b38) ()  
| Returns the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules.") manager. [More...](class_app_window.html#a0893c734d037e24f310e4dcdf3023b38)  
  
[NetworkFile](class_network_file.html) | [getActiveFile](class_app_window.html#a576f640c71e1c8d8d532a97d4272be01) ()  
| Returns the current active file. [More...](class_app_window.html#a576f640c71e1c8d8d532a97d4272be01)  
  
void | [exit](class_app_window.html#aaf8b7a2008177fb6c0c23d1a673655b1) ()  
| Exits Packet Tracer. [More...](class_app_window.html#aaf8b7a2008177fb6c0c23d1a673655b1)  
  
void | [exitNoConfirm](class_app_window.html#af4eb3f6a9e5d8268167a74a2490ae194) (bool)  
| Exits packet tracer with or without save conformation. [More...](class_app_window.html#af4eb3f6a9e5d8268167a74a2490ae194)  
  
[DialogManager](class_dialog_manager.html) | [getDialogManager](class_app_window.html#a6a375ee63c34dc141ee985e9c5502fdb) ()  
| Returns the dialog manager. [More...](class_app_window.html#a6a375ee63c34dc141ee985e9c5502fdb)  
  
void | [writeToPT](class_app_window.html#a3efc839fb255cd2329147a96cf4dfdcf) (QString)  
| Writes a message to the [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") Log and shows it. [More...](class_app_window.html#a3efc839fb255cd2329147a96cf4dfdcf)  
  
QString | [getVersion](class_app_window.html#af3026b3cb41a5e0ae88a113af72a9cae) ()  
| Returns the Packet Tracer version number. [More...](class_app_window.html#af3026b3cb41a5e0ae88a113af72a9cae)  
  
QString | [getBasePath](class_app_window.html#ad56f9fafd213942e65e94fd371b64a8a) ()  
| Returns the installation directory of Packet Tracer. [More...](class_app_window.html#ad56f9fafd213942e65e94fd371b64a8a)  
  
bool | [fileNew](class_app_window.html#a24f830dfb8fa665155abaf0fe05a6d94) (bool)  
| Creates a new file. [More...](class_app_window.html#a24f830dfb8fa665155abaf0fe05a6d94)  
  
FileOpenReturnValue | [fileOpen](class_app_window.html#ac27fcd4fc1585729154883cc2a436d8e) (QString)  
| Opens the specified file. [More...](class_app_window.html#ac27fcd4fc1585729154883cc2a436d8e)  
  
FileOpenReturnValue | [promptFileOpenFolder](class_app_window.html#a44dc234f3ecae08441f27d8e4c54de1c) (QString)  
| Prompts to browse a folder for a file to open. [More...](class_app_window.html#a44dc234f3ecae08441f27d8e4c54de1c)  
  
vector< QString > | [getListOfFilesToOpen](class_app_window.html#a41bf0a210c2293be7eececf0bf029ab7) (QString)  
| Retrives list of files that can be opened location. [More...](class_app_window.html#a41bf0a210c2293be7eececf0bf029ab7)  
  
vector< QString > | [getListOfFilesSaved](class_app_window.html#afccd5174ebf4f312fb78c754e3283358) (QString)  
| Retrives list of files saved at default location. [More...](class_app_window.html#afccd5174ebf4f312fb78c754e3283358)  
  
QString | [getDefaultFileSaveLocation](class_app_window.html#a7034a8e47acacc95be2158d85f01d56c) ()  
| Retrives default save location. [More...](class_app_window.html#a7034a8e47acacc95be2158d85f01d56c)  
  
QString | [getTempFileLocation](class_app_window.html#a213ccd949429bc80413d2b0ac0bceaa3) ()  
bool | [fileSave](class_app_window.html#aa36b56b5a36cc225455dfafba23aeecb) ()  
void | [fileSaveAsync](class_app_window.html#a5a4aabd1f4b3a643e109cef8c4d956f8) ()  
| Starts save operation and returns immediately. [More...](class_app_window.html#a5a4aabd1f4b3a643e109cef8c4d956f8)  
  
bool | [fileSaveAs](class_app_window.html#a406450756eeab2b62f16d05c5b10bb68) (QString)  
void | [fileSaveAsAsync](class_app_window.html#aab39a4c18509c2abd1267ea9628ad6bf) (QString)  
| Starts save as operation to the specified file and returns immediately. [More...](class_app_window.html#aab39a4c18509c2abd1267ea9628ad6bf)  
  
void | [fileSaveAsNoPrompt](class_app_window.html#a7fc1db8f4d2c6b370d529bd3ec79276f) (QString, bool)  
| Same as [fileSaveAs()](class_app_window.html#a406450756eeab2b62f16d05c5b10bb68) except it does not prompt to overwrite the file. [More...](class_app_window.html#a7fc1db8f4d2c6b370d529bd3ec79276f)  
  
bool | [fileSaveAsPkz](class_app_window.html#ab14f13ca39b380175350ca578176c2ec) (QString)  
void | [fileSaveAsPkzAsync](class_app_window.html#a09f60e93fa2e321fe7be4c30a58c447b) (QString)  
| Starts save as pkz operation and returns immediately. [More...](class_app_window.html#a09f60e93fa2e321fe7be4c30a58c447b)  
  
void | [fileActivityWizard](class_app_window.html#ae9fb2e43f66ac4e28c68d8e93d39b8da) ()  
| Enters the Activity Wizard. [More...](class_app_window.html#ae9fb2e43f66ac4e28c68d8e93d39b8da)  
  
FileOpenReturnValue | [fileOpenFromBytes](class_app_window.html#ad67065ba3b71f4d7f821a4a23b799774) (vector< byte >, QString)  
| Opens the specified file with the specified bytes of data. [More...](class_app_window.html#ad67065ba3b71f4d7f821a4a23b799774)  
  
FileOpenReturnValue | [fileOpenFromURL](class_app_window.html#a55a7ca535dc77b796165cdc321e3b62b) (QString)  
| Opens a file at the specified URL. [More...](class_app_window.html#a55a7ca535dc77b796165cdc321e3b62b)  
  
vector< byte > | [fileSaveToBytes](class_app_window.html#ac60fe335006de82030ec42aa8c110fba) ()  
void | [fileSaveToBytesAsync](class_app_window.html#aaa9d00d4bf5bf99fe74a9fa41dcdb1b3) ()  
| Starts save to bytes operation and returns immediately. [More...](class_app_window.html#aaa9d00d4bf5bf99fe74a9fa41dcdb1b3)  
  
void | [fileNewed](class_app_window.html#a133db700491e99a132fc7826f96e1bd6) ()  
| This event is emitted when a new file is created. [More...](class_app_window.html#a133db700491e99a132fc7826f96e1bd6)  
  
void | [fileOpened](class_app_window.html#acaec3b8f2909f4e6a68c866dc7bcd737) ()  
| This event is emitted when a file is opened. [More...](class_app_window.html#acaec3b8f2909f4e6a68c866dc7bcd737)  
  
void | [activityFileOpening](class_app_window.html#a14f1b9cd9794ed4e1aaf2e717f96d31b) ()  
| This event is emitted when a activity file is opening. [More...](class_app_window.html#a14f1b9cd9794ed4e1aaf2e717f96d31b)  
  
void | [fileClosing](class_app_window.html#a9c4ad4c308f667236040cc85b91cb291) ()  
| This event is emitted when the file is closing. [More...](class_app_window.html#a9c4ad4c308f667236040cc85b91cb291)  
  
void | [fileSaved](class_app_window.html#a8aee07f7cf48fb9a06683aaa91cb0d21) ()  
| [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. [More...](class_app_window.html#a8aee07f7cf48fb9a06683aaa91cb0d21)  
  
void | [fileSaveDone](class_app_window.html#a0168b21c40fd0a573f55d71f5f48555f) (bool)  
| This event is emitted when a file is saved. [More...](class_app_window.html#a0168b21c40fd0a573f55d71f5f48555f)  
  
void | [fileSaveToBytesDone](class_app_window.html#a0ae0e68fd4f1fa0ad762686ec1878e07) (vector< byte >)  
| This event is emitted when a file is saved. [More...](class_app_window.html#a0ae0e68fd4f1fa0ad762686ec1878e07)  
  
bool | [shouldIgnoreFileNew](class_app_window.html#a5c68cd4995e0e5ea1ad7515c3d2d3fdb) ()  
| This delegate determines if PT should ignore the file->new action. If ignoring, then the script module should do something to let the user know. [More...](class_app_window.html#a5c68cd4995e0e5ea1ad7515c3d2d3fdb)  
  
bool | [shouldIgnoreFileOpenFolder](class_app_window.html#a0ca2668b3637d6e65ead09b51496a79e) (QString)  
| This delegate determines if PT should ignore the file->open folder action. If ignoring, then the script module should do something to let the user know. [More...](class_app_window.html#a0ca2668b3637d6e65ead09b51496a79e)  
  
bool | [shouldIgnoreFileOpenRecent](class_app_window.html#a12a136d1c6c4108c675736d51d021ca0) (QString)  
| This delegate determines if PT should ignore the file->open recent file action. If ignoring, then the script module should do something to let the user know. [More...](class_app_window.html#a12a136d1c6c4108c675736d51d021ca0)  
  
bool | [shouldIgnoreFileSave](class_app_window.html#a400c1f4cb6397d5e1867888eee816577) ()  
| This delegate determines if PT should ignore the file->save action. If ignoring, then the script module should do something to let the user know. [More...](class_app_window.html#a400c1f4cb6397d5e1867888eee816577)  
  
bool | [shouldIgnoreFileSaveAs](class_app_window.html#a4c0eb494d7e99861da04ef89737edfa3) (QString)  
| This delegate determines if PT should ignore the file->save as action. If ignoring, then the script module should do something to let the user know. [More...](class_app_window.html#a4c0eb494d7e99861da04ef89737edfa3)  
  
bool | [shouldIgnoreFileExit](class_app_window.html#ab17e18caf642b938927670e52c24ea51) ()  
| This delegate determines if PT should ignore the file->exit action. If ignoring, then the script module should do something to let the user know. [More...](class_app_window.html#ab17e18caf642b938927670e52c24ea51)  
  
void | [enteredActivityWizard](class_app_window.html#a814e7266ce4e64a820e31a37a5592c61) (bool)  
| This event is emitted when the activity wizard is entered. [More...](class_app_window.html#a814e7266ce4e64a820e31a37a5592c61)  
  
bool | [isPreventClose](class_app_window.html#a3fd6db7ca72c7021582cadbf43366588) ()  
| Returns true if Packet Tracer is prevented from closing, otherwise false. [More...](class_app_window.html#a3fd6db7ca72c7021582cadbf43366588)  
  
void | [setPreventClose](class_app_window.html#a1a84c46df3295608d5a93aa30b0ccef4) (bool)  
| Allows or prevents Packet Tracer from closing. [More...](class_app_window.html#a1a84c46df3295608d5a93aa30b0ccef4)  
  
long | [getProcessId](class_app_window.html#a6b6d114a6426f95ecd389e78f25e2f82) ()  
| Returns Packet Tracer application process ID. [More...](class_app_window.html#a6b6d114a6426f95ecd389e78f25e2f82)  
  
QString | [getSessionId](class_app_window.html#a58dd9a3f18392d0053d9b201dc4e67b4) ()  
| Returns the globally unique Packet Tracer application session ID. [More...](class_app_window.html#a58dd9a3f18392d0053d9b201dc4e67b4)  
  
QString | [getUserFolder](class_app_window.html#a66ca52975f90e4258d6ade5f3ce69b82) ()  
| Returns the user folder of the current user logged into the OS. [More...](class_app_window.html#a66ca52975f90e4258d6ade5f3ce69b82)  
  
void | [appExit](class_app_window.html#acea3bb83ce166f884802f18917fc8d93) ()  
| This event is emitted when the user exits application. [More...](class_app_window.html#acea3bb83ce166f884802f18917fc8d93)  
  
void | [lockedInterfaceInvoked](class_app_window.html#a6992b91c0b253ddbe7280c58c06b43c4) (QString, QString, QString, QString)  
| This event is emitted when a locked interface is invoked. [More...](class_app_window.html#a6992b91c0b253ddbe7280c58c06b43c4)  
  
void | [setVisible](class_app_window.html#ab7b09ac4e571e2446b1eaf64c6996e4b) (bool)  
| Shows or hides the Packet Tracer main window. [More...](class_app_window.html#ab7b09ac4e571e2446b1eaf64c6996e4b)  
  
void | [raise](class_app_window.html#af94073f26b7dd2cd11fa8afeb9cb87fd) ()  
void | [setDisabled](class_app_window.html#a6d95d1b7bb9bc8d850cc9fe524dfcc11) (bool)  
| Disables or enables the application. Buttons, etc will be shown as disabled and unuable. [More...](class_app_window.html#a6d95d1b7bb9bc8d850cc9fe524dfcc11)  
  
void | [isMaximized](class_app_window.html#a7c00884376c6e327a42745039e1ab36b) ()  
void | [showMaximized](class_app_window.html#a11f93d730e618d4aa15dab0f410bd57c) ()  
| Sets the Packet Tracer main window to the maximum size. [More...](class_app_window.html#a11f93d730e618d4aa15dab0f410bd57c)  
  
void | [isMinimized](class_app_window.html#a2e5260a275ec9459905ebd8967c0efaf) ()  
void | [showMinimized](class_app_window.html#aee73a637d8356f69bc2979b807d97a58) ()  
| Sets the Packet Tracer main window to the minimum size. [More...](class_app_window.html#aee73a637d8356f69bc2979b807d97a58)  
  
void | [showNormal](class_app_window.html#abb85d2a5e5b5eedb086fc8c89d9ac2dd) ()  
| Sets the Packet Tracer main window to the normal size. [More...](class_app_window.html#abb85d2a5e5b5eedb086fc8c89d9ac2dd)  
  
void | [setWindowTitle](class_app_window.html#a24e1cba91d0f45002e2428f702b26d56) (QString)  
| Sets the Packet Tracer main window title. [More...](class_app_window.html#a24e1cba91d0f45002e2428f702b26d56)  
  
void | [setWindowGeometry](class_app_window.html#acd6ad5e26881a8a2efb14dcbca092c89) (int, int, int, int)  
| Sets the Packet Tracer main window geometry and position. [More...](class_app_window.html#acd6ad5e26881a8a2efb14dcbca092c89)  
  
int | [getX](class_app_window.html#a0880d389160213caaa8fb9cdadcb09ae) ()  
| Returns the Packet Tracer main window x-coorindate. [More...](class_app_window.html#a0880d389160213caaa8fb9cdadcb09ae)  
  
int | [getY](class_app_window.html#aeacb1b1f73968978f54539cea656aef5) ()  
| Returns the Packet Tracer main window y-coorindate. [More...](class_app_window.html#aeacb1b1f73968978f54539cea656aef5)  
  
int | [getWidth](class_app_window.html#aa9fb8b40afe6800341097403edf2840e) ()  
| Returns the Packet Tracer main window width. [More...](class_app_window.html#aa9fb8b40afe6800341097403edf2840e)  
  
int | [getHeight](class_app_window.html#a00c216512caff3f876735efc6a965650) ()  
| Returns the Packet Tracer main window height. [More...](class_app_window.html#a00c216512caff3f876735efc6a965650)  
  
void | [setMaximumSize](class_app_window.html#a7e7a458e1d63dff7bd3425b2e54c246e) (int, int)  
| Sets the maximum size of the Packet Tracer main window. [More...](class_app_window.html#a7e7a458e1d63dff7bd3425b2e54c246e)  
  
void | [setMaximumWidth](class_app_window.html#a2aeed45522f44df9e6774baada13dbd5) (int)  
| Sets the maximum width of the Packet Tracer main window. [More...](class_app_window.html#a2aeed45522f44df9e6774baada13dbd5)  
  
void | [setMaximumHeight](class_app_window.html#aa158ded50b0d5c3395e6a7b4642c20af) (int)  
| Sets the maximum height of the Packet Tracer main window. [More...](class_app_window.html#aa158ded50b0d5c3395e6a7b4642c20af)  
  
int | [getMaximumWidth](class_app_window.html#aa2497c225d9449f1d88585d5c678da07) ()  
| Returns the maximum width of the Packet Tracer main window. [More...](class_app_window.html#aa2497c225d9449f1d88585d5c678da07)  
  
int | [getMaximumHeight](class_app_window.html#a38377c117ac34cfce10cddc3375e0328) ()  
| Returns the maximum height of the Packet Tracer main window. [More...](class_app_window.html#a38377c117ac34cfce10cddc3375e0328)  
  
void | [setMinimumSize](class_app_window.html#a69eb34562c3888f8bf7e8d0284be0ae5) (int, int)  
| Sets the minimum size of the Packet Tracer main window. [More...](class_app_window.html#a69eb34562c3888f8bf7e8d0284be0ae5)  
  
void | [setMinimumWidth](class_app_window.html#a474f805a51321b2cade75f7a09daf09c) (int)  
| Sets the minimum width of the Packet Tracer main window. [More...](class_app_window.html#a474f805a51321b2cade75f7a09daf09c)  
  
void | [setMinimumHeight](class_app_window.html#ab70f6e160fe1e07d8b04b0dfb14df568) (int)  
| Sets the minimum height of the Packet Tracer main window. [More...](class_app_window.html#ab70f6e160fe1e07d8b04b0dfb14df568)  
  
int | [getMinimumWidth](class_app_window.html#a224350c62b26c4faf4c5eb9e80edd6da) ()  
| Returns the minimum width of the Packet Tracer main window. [More...](class_app_window.html#a224350c62b26c4faf4c5eb9e80edd6da)  
  
int | [getMinimumHeight](class_app_window.html#a0160cc53d3b807c3e4c12d319f65378a) ()  
| Returns the minimum height of the Packet Tracer main window. [More...](class_app_window.html#a0160cc53d3b807c3e4c12d319f65378a)  
  
int | [getMainViewAreaWidth](class_app_window.html#a03d71c9be2396f4cae903666e59c31bb) ()  
| Returns the main view area's width. [More...](class_app_window.html#a03d71c9be2396f4cae903666e59c31bb)  
  
int | [getMainViewAreaHeight](class_app_window.html#a3280c0312194d53c86fdeb7e124441f2) ()  
| Returns the main view area's height. [More...](class_app_window.html#a3280c0312194d53c86fdeb7e124441f2)  
  
void | [resized](class_app_window.html#aa7dd3cb70f1d035707ace4bf7acb2507) (int, int)  
| This event is emitted when the Packet Tracer main window is resized. [More...](class_app_window.html#aa7dd3cb70f1d035707ace4bf7acb2507)  
  
bool | [isInterfaceLocked](class_app_window.html#abe4419610fa9d835b254e4bc0f373b51) (QString, QString, QString)  
| Returns true if the interface with the specified ID is locked, otherwise false. [More...](class_app_window.html#abe4419610fa9d835b254e4bc0f373b51)  
  
void | [setClipboardText](class_app_window.html#a2c5ec530e85ba752d0247e177a7c9aa4) (QString)  
| Sets the clipboard text(copy/paste text) to the given text. [More...](class_app_window.html#a2c5ec530e85ba752d0247e177a7c9aa4)  
  
QString | [getClipboardText](class_app_window.html#aa629d4bdc4f1be4ffb8cf12c434fa84d) ()  
| Returns the current clipboard text, if any. [More...](class_app_window.html#aa629d4bdc4f1be4ffb8cf12c434fa84d)  
  
void | [helpPath](class_app_window.html#a2c90c3bbd326a9a6943561e9489a88bf) (QString)  
| Open a help file at the given path. [More...](class_app_window.html#a2c90c3bbd326a9a6943561e9489a88bf)  
  
bool | [openURL](class_app_window.html#ab4d6e58677df7d6129164cc9f424110d) (QString)  
| Open URL in external web browser. [More...](class_app_window.html#ab4d6e58677df7d6129164cc9f424110d)  
  
[EnvironmentDialog](class_environment_dialog.html) | [getEnvironmentDialog](class_app_window.html#a00dfc06f0f9a7b1eb267ff994a3f8c61) ()  
| Returns the [Environment](class_environment.html "An object in the Physical Workspace.") Dialog. [More...](class_app_window.html#a00dfc06f0f9a7b1eb267ff994a3f8c61)  
  
vector< QString > | [listDirectory](class_app_window.html#ad30838e74fdd974898311ebbe53268d2) (QString, QString)  
| Temporary function used to update sample files. Not for normal use. [More...](class_app_window.html#ad30838e74fdd974898311ebbe53268d2)  
  
void | [setCheckOutdatedDevices](class_app_window.html#a9509cb5cebc9e7bb707d99548c544441) (bool)  
| Set if devices marked as outdated should be displayed for selection. [More...](class_app_window.html#a9509cb5cebc9e7bb707d99548c544441)  
  
void | [deletePTConf](class_app_window.html#a4cf329a80a43ff7db212502836bc6e8e) ()  
QString | [getPTSAMode](class_app_window.html#addd81cb3e3676c79bc1d94719ee3b57e) ()  
| Get the current PTSA Mode. [More...](class_app_window.html#addd81cb3e3676c79bc1d94719ee3b57e)  
  
void | [setPTSAMode](class_app_window.html#a020f7c53b86c6344ae45d383875f1b7a) (QString)  
| Get the current PTSA Mode. [More...](class_app_window.html#a020f7c53b86c6344ae45d383875f1b7a)  
  
bool | [isPTSA](class_app_window.html#ab2c3bfa2e9d716a2658f9ac0256aec15) ()  
| returns true if PTSA [More...](class_app_window.html#ab2c3bfa2e9d716a2658f9ac0256aec15)  
  
void | [setPTSAPluginVisible](class_app_window.html#a2e8b702e26fec123705bb0d18eb8446a) (bool)  
| show and hide pt window, called from ptsa plugin only. you still need to clear other windows, possibly with file->new [More...](class_app_window.html#a2e8b702e26fec123705bb0d18eb8446a)  
  
bool | [isActivityWizardOpen](class_app_window.html#a5e20f387dcc4a529071c4d5a452928ac) ()  
StandardButton | [showMessageBox](class_app_window.html#ae94a62174b7efbb506502d305d2c6a69) (QString, QString, QString, MessageBoxIcon, StandardButton, StandardButton, StandardButton)  
| Shows a modal message box with standard buttons over the PT main window. [More...](class_app_window.html#ae94a62174b7efbb506502d305d2c6a69)  
  
int | [showMessageBoxWithCustomButtons](class_app_window.html#ab3b625e7f2ae1af63ad117560f680cff) (QString, QString, QString, MessageBoxIcon, QString, int, int)  
| Shows a modal message box with custom buttons over the PT main window. [More...](class_app_window.html#ab3b625e7f2ae1af63ad117560f680cff)  
  
  
## Detailed Description

[AppWindow](class_app_window.html "AppWindow serves as the entry point to all GUI objects.") serves as the entry point to all GUI objects. 

## Member Function Documentation

## ◆ activityFileOpening()

void AppWindow::activityFileOpening  | ( | | ) |   
---|---|---|---|---  
  
This event is emitted when a activity file is opening. 

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ appExit()

void AppWindow::appExit  | ( | | ) |   
---|---|---|---|---  
  
This event is emitted when the user exits application. 

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ deletePTConf()

void AppWindow::deletePTConf  | ( | | ) |   
---|---|---|---|---  
  
## ◆ enteredActivityWizard()

void AppWindow::enteredActivityWizard  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when the activity wizard is entered. 

  * convertedCurrentFile, true if a existing network was converted to use as the answer network, false if not..



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ exit()

void AppWindow::exit  | ( | | ) |   
---|---|---|---|---  
  
Exits Packet Tracer. 

## ◆ exitNoConfirm()

void AppWindow::exitNoConfirm  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Exits packet tracer with or without save conformation. 

Parameters
     flag,true| to exit Packet Tracer without save confirmation, false to exit with save confirmation.   
---|---  
  
## ◆ fileActivityWizard()

void AppWindow::fileActivityWizard  | ( | | ) |   
---|---|---|---|---  
  
Enters the Activity Wizard. 

## ◆ fileClosing()

void AppWindow::fileClosing  | ( | | ) |   
---|---|---|---|---  
  
This event is emitted when the file is closing. 

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ fileNew()

bool AppWindow::fileNew  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Creates a new file. 

Parameters
     flag,true| shows the save confirmation dialog, false does not.  
---|---  
  
Returns
    bool, true if a new file was created, otherwise false. 

## ◆ fileNewed()

void AppWindow::fileNewed  | ( | | ) |   
---|---|---|---|---  
  
This event is emitted when a new file is created. 

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ fileOpen()

FileOpenReturnValue AppWindow::fileOpen  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Opens the specified file. 

Parameters
     filename,the| path of the file.  
---|---  
  
Returns
    EFileOpenReturnValue Can be of the following values: eFileReturnOk, eFileReturnBadSSL, eFileReturnBadDecompress, eFileReturnBadBinary, eFileReturnBadMetafile, eFileReturnBadConfiguration, eFileReturnUnableToReadFile, eFileReturnBadOptions, eFileReturnUserCancel 

## ◆ fileOpened()

void AppWindow::fileOpened  | ( | | ) |   
---|---|---|---|---  
  
This event is emitted when a file is opened. 

[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ fileOpenFromBytes()

FileOpenReturnValue AppWindow::fileOpenFromBytes  | ( | vector< byte > | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Opens the specified file with the specified bytes of data. 

Parameters
     data,vector| of bytes of the file.   
---|---  
filename,the| path of the file.  
  
Returns
    bool, true if the file was opened, otherwise false. 

## ◆ fileOpenFromURL()

FileOpenReturnValue AppWindow::fileOpenFromURL  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Opens a file at the specified URL. 

Parameters
     url,the| URL of the file.  
---|---  
  
Returns
    bool, true if the file was opened, otherwise false. 

## ◆ fileSave()

bool AppWindow::fileSave  | ( | | ) |   
---|---|---|---|---  
  
## ◆ fileSaveAs()

bool AppWindow::fileSaveAs  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
**[Deprecated:](deprecated.html#_deprecated000002)**
     Use [fileSaveAsAsync()](class_app_window.html#aab39a4c18509c2abd1267ea9628ad6bf "Starts save as operation to the specified file and returns immediately.") and register to [fileSaveDone()](class_app_window.html#a0168b21c40fd0a573f55d71f5f48555f "This event is emitted when a file is saved.") event. 

## ◆ fileSaveAsAsync()

void AppWindow::fileSaveAsAsync  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Starts save as operation to the specified file and returns immediately. 

Parameters
     filename,the| path of the file.  
---|---  
  
Remarks
    Register to [fileSaveDone()](class_app_window.html#a0168b21c40fd0a573f55d71f5f48555f "This event is emitted when a file is saved.") event to get the status. 

## ◆ fileSaveAsNoPrompt()

void AppWindow::fileSaveAsNoPrompt  | ( | QString  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Same as [fileSaveAs()](class_app_window.html#a406450756eeab2b62f16d05c5b10bb68) except it does not prompt to overwrite the file. 

Parameters
     filename,the| path of the file.  
---|---  
bAsync,set| to true to use [fileSaveAsAsync()](class_app_window.html#aab39a4c18509c2abd1267ea9628ad6bf "Starts save as operation to the specified file and returns immediately.")  
  
Remarks
    Register to [fileSaveDone()](class_app_window.html#a0168b21c40fd0a573f55d71f5f48555f "This event is emitted when a file is saved.") event to get the status. 

## ◆ fileSaveAsPkz()

bool AppWindow::fileSaveAsPkz  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
**[Deprecated:](deprecated.html#_deprecated000003)**
     Use [fileSaveAsPkzAsync()](class_app_window.html#a09f60e93fa2e321fe7be4c30a58c447b "Starts save as pkz operation and returns immediately.") and register to [fileSaveDone()](class_app_window.html#a0168b21c40fd0a573f55d71f5f48555f "This event is emitted when a file is saved.") event. 

## ◆ fileSaveAsPkzAsync()

void AppWindow::fileSaveAsPkzAsync  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Starts save as pkz operation and returns immediately. 

Parameters
     filename,the| path of the file.  
---|---  
  
Remarks
    Register to [fileSaveDone()](class_app_window.html#a0168b21c40fd0a573f55d71f5f48555f "This event is emitted when a file is saved.") to get the status. 

## ◆ fileSaveAsync()

void AppWindow::fileSaveAsync  | ( | | ) |   
---|---|---|---|---  
  
Starts save operation and returns immediately. 

Remarks
    Register to [fileSaveDone()](class_app_window.html#a0168b21c40fd0a573f55d71f5f48555f "This event is emitted when a file is saved.") event to get the status. 

## ◆ fileSaved()

void AppWindow::fileSaved  | ( | | ) |   
---|---|---|---|---  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

**[Deprecated:](deprecated.html#_deprecated000005)**
    . Use [fileSaveDone()](class_app_window.html#a0168b21c40fd0a573f55d71f5f48555f "This event is emitted when a file is saved.") event. 

## ◆ fileSaveDone()

void AppWindow::fileSaveDone  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when a file is saved. 

  * success, true if the file was saved successfully, otherwise false.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ fileSaveToBytes()

vector< byte > AppWindow::fileSaveToBytes  | ( | | ) |   
---|---|---|---|---  
  
**[Deprecated:](deprecated.html#_deprecated000004)**
     Use [fileSaveToBytesAsync()](class_app_window.html#aaa9d00d4bf5bf99fe74a9fa41dcdb1b3 "Starts save to bytes operation and returns immediately.") and register to [fileSaveToBytesDone()](class_app_window.html#a0ae0e68fd4f1fa0ad762686ec1878e07 "This event is emitted when a file is saved."). 

## ◆ fileSaveToBytesAsync()

void AppWindow::fileSaveToBytesAsync  | ( | | ) |   
---|---|---|---|---  
  
Starts save to bytes operation and returns immediately. 

Remarks
    Register to [fileSaveToBytesDone()](class_app_window.html#a0ae0e68fd4f1fa0ad762686ec1878e07 "This event is emitted when a file is saved.") event to get save in bytes. 

## ◆ fileSaveToBytesDone()

void AppWindow::fileSaveToBytesDone  | ( | vector< byte > | | ) |   
---|---|---|---|---|---  
  
This event is emitted when a file is saved. 

  * data, vector of bytes of the file.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ getActiveDialog()

[ActiveDialog](class_active_dialog.html) AppWindow::getActiveDialog  | ( | | ) |   
---|---|---|---|---  
  
Returns the current active dialog. 

Returns
    [ActiveDialog](class_active_dialog.html "ActiveDialog is the class of dockable active dialogs."), the current active dialog. 

## ◆ getActiveFile()

[NetworkFile](class_network_file.html) AppWindow::getActiveFile  | ( | | ) |   
---|---|---|---|---  
  
Returns the current active file. 

Returns
    [NetworkFile](class_network_file.html "NetworkFile is the main system file for the application. It holds all the configurations for the engi..."), the current active file. 

## ◆ getActiveWorkspace()

[Workspace](class_workspace.html) AppWindow::getActiveWorkspace  | ( | | ) |   
---|---|---|---|---  
  
Returns the current active workspace. 

Returns
    [Workspace](class_workspace.html "Workspace is the base class for Logical and Physical workspace related objects."), the current active workspace. 

## ◆ getActivityWizard()

[ActivityWizard](class_activity_wizard.html) AppWindow::getActivityWizard  | ( | | ) |   
---|---|---|---|---  
  
Returns the Activity Wizard. 

Returns
    [ActivityWizard](class_activity_wizard.html "ActivityWizard is an assessment creation tool."), the Activity Wizard widget. 

## ◆ getAdminDialog()

[AdministrativeDialog](class_administrative_dialog.html) AppWindow::getAdminDialog  | ( | | ) |   
---|---|---|---|---  
  
Returns the administrative dialog. 

Returns
    [AdministrativeDialog](class_administrative_dialog.html "AdministrativeDialog serves as a frontend to Options class."), the administrative dialog widget. 

## ◆ getBasePath()

QString AppWindow::getBasePath  | ( | | ) |   
---|---|---|---|---  
  
Returns the installation directory of Packet Tracer. 

Returns
    QString, the installation directory of Packet Tracer. 

## ◆ getClipboardText()

QString AppWindow::getClipboardText  | ( | | ) |   
---|---|---|---|---  
  
Returns the current clipboard text, if any. 

Returns
    QString, text stored in the copy/paste clipboard. 

## ◆ getCommonToolbar()

[CommonToolbar](class_common_toolbar.html) AppWindow::getCommonToolbar  | ( | | ) |   
---|---|---|---|---  
  
Returns the Common Toolbar. 

Returns
    [InfoDialog](class_info_dialog.html "InfoDialog handles and manipulates the network description dialog."), the Common Toolbar widget. 

## ◆ getDefaultFileSaveLocation()

QString AppWindow::getDefaultFileSaveLocation  | ( | | ) |   
---|---|---|---|---  
  
Retrives default save location. 

Returns
    Returns default save location 

## ◆ getDialogManager()

[DialogManager](class_dialog_manager.html) AppWindow::getDialogManager  | ( | | ) |   
---|---|---|---|---  
  
Returns the dialog manager. 

Returns
    [DialogManager](class_dialog_manager.html "DialogManager manages all the device dialogs."), the dialog manager. 

## ◆ getEnvironmentDialog()

[EnvironmentDialog](class_environment_dialog.html) AppWindow::getEnvironmentDialog  | ( | | ) |   
---|---|---|---|---  
  
Returns the [Environment](class_environment.html "An object in the Physical Workspace.") Dialog. 

Returns
    [Environment](class_environment.html "An object in the Physical Workspace.") Dialog 

## ◆ getHeight()

int AppWindow::getHeight  | ( | | ) |   
---|---|---|---|---  
  
Returns the Packet Tracer main window height. 

Returns
    int, the Packet Tracer main window height. 

## ◆ getInfoDialog()

[InfoDialog](class_info_dialog.html) AppWindow::getInfoDialog  | ( | | ) |   
---|---|---|---|---  
  
Returns the info dialog. 

Returns
    [InfoDialog](class_info_dialog.html "InfoDialog handles and manipulates the network description dialog."), the Info Dialog widget. 

## ◆ getInstructionDlg()

[InstructionDlg](class_instruction_dlg.html) AppWindow::getInstructionDlg  | ( | | ) |   
---|---|---|---|---  
  
Returns the activity instructions dialog. 

Returns
    [InstructionDlg](class_instruction_dlg.html "InstructionDlg is the instruction dialog associated with activity files."), the activity instructions dialog widget. 

## ◆ getListOfFilesSaved()

vector< QString > AppWindow::getListOfFilesSaved  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Retrives list of files saved at default location. 

Parameters
     location,Reserved|   
---|---  
  
Returns
    List of files that can be opened. 

## ◆ getListOfFilesToOpen()

vector< QString > AppWindow::getListOfFilesToOpen  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Retrives list of files that can be opened location. 

Parameters
     location,Reserved|   
---|---  
  
Returns
    List of files that can be opened. 

## ◆ getLogicalToolbar()

[LogicalToolbar](class_logical_toolbar.html) AppWindow::getLogicalToolbar  | ( | | ) |   
---|---|---|---|---  
  
Returns the Logical workspace toolbar. 

Returns
    [LogicalToolbar](class_logical_toolbar.html "LogicalToolbar allows manipulation of the Logical toolbar. It is the toolbar that has cluster creatio..."), the Logical workspace toolbar widget. 

## ◆ getMainViewAreaHeight()

int AppWindow::getMainViewAreaHeight  | ( | | ) |   
---|---|---|---|---  
  
Returns the main view area's height. 

Returns
    int, the main view area's height. 

## ◆ getMainViewAreaWidth()

int AppWindow::getMainViewAreaWidth  | ( | | ) |   
---|---|---|---|---  
  
Returns the main view area's width. 

Returns
    int, the main view area's width. 

## ◆ getMaximumHeight()

int AppWindow::getMaximumHeight  | ( | | ) |   
---|---|---|---|---  
  
Returns the maximum height of the Packet Tracer main window. 

## ◆ getMaximumWidth()

int AppWindow::getMaximumWidth  | ( | | ) |   
---|---|---|---|---  
  
Returns the maximum width of the Packet Tracer main window. 

## ◆ getMenuBar()

[MenuBar](class_menu_bar.html) AppWindow::getMenuBar  | ( | | ) |   
---|---|---|---|---  
  
Returns the menu bar. 

Returns
    [MenuBar](class_menu_bar.html "MenuBar allows UI manipulation of the Main Menu Bar."), the menu bar widget. 

## ◆ getMinimumHeight()

int AppWindow::getMinimumHeight  | ( | | ) |   
---|---|---|---|---  
  
Returns the minimum height of the Packet Tracer main window. 

## ◆ getMinimumWidth()

int AppWindow::getMinimumWidth  | ( | | ) |   
---|---|---|---|---  
  
Returns the minimum width of the Packet Tracer main window. 

## ◆ getNetworkComponentBox()

[NetworkComponentBox](class_network_component_box.html) AppWindow::getNetworkComponentBox  | ( | | ) |   
---|---|---|---|---  
  
Returns the [Network](class_network.html "Network is the entry point for all device configurations in the network. It retrieves devices.") Component Box. 

Returns
    [NetworkComponentBox](class_network_component_box.html "NetworkComponentBox allows UI manipulation of the Network Component Box."), the [NetworkComponentBox](class_network_component_box.html "NetworkComponentBox allows UI manipulation of the Network Component Box.") widget. 

## ◆ getPaletteDialog()

[PaletteDialog](class_palette_dialog.html) AppWindow::getPaletteDialog  | ( | | ) |   
---|---|---|---|---  
  
Returns the palette dialog. 

Returns
    [PaletteDialog](class_palette_dialog.html "PaletteDialog allows for UI manipulation of the Palette Dialog."), the palette dialog widget. 

## ◆ getPDUListWindow()

[PDUListWindow](class_p_d_u_list_window.html) AppWindow::getPDUListWindow  | ( | | ) |   
---|---|---|---|---  
  
Returns the PDU list window. 

Returns
    [PDUListWindow](class_p_d_u_list_window.html "PDUListWindow allows for manipulation of the PDU List Window."), the PDU List Window widget. 

## ◆ getPhysicalLocationDialog()

[PhysicalLocationDialog](class_physical_location_dialog.html) AppWindow::getPhysicalLocationDialog  | ( | | ) |   
---|---|---|---|---  
  
Returns the Physical Location dialog. 

Returns
    [PhysicalLocationDialog](class_physical_location_dialog.html "PhysicalLocationDialog allows for UI manipulation of the Physical Location Dialog."), the Physical Location dialog widget. 

## ◆ getPhysicalToolbar()

[PhysicalToolbar](class_physical_toolbar.html) AppWindow::getPhysicalToolbar  | ( | | ) |   
---|---|---|---|---  
  
Returns the Physical workspace toolbar. 

Returns
    [PhysicalToolbar](class_physical_toolbar.html "PhysicalToolbar allows for UI manipulation of the Physical toolbar."), the Physical workspace toolbar widget. 

## ◆ getPLSwitch()

[PLSwitch](class_p_l_switch.html) AppWindow::getPLSwitch  | ( | | ) |   
---|---|---|---|---  
  
Returns the Physical/Logical workspace switch. 

Returns
    [PLSwitch](class_p_l_switch.html "PLSwitch allows for UI manipulation of the Physical and Logical workspace toggle switches."), the Physical/Logical workspace switch widget. 

## ◆ getPrintDialog()

[PrintDialogPT4](class_print_dialog_p_t4.html) AppWindow::getPrintDialog  | ( | | ) |   
---|---|---|---|---  
  
Returns the print dialog. 

Returns
    [PrintDialogPT4](class_print_dialog_p_t4.html "PrintDialogPT4 allows for UI manipulation of the Print Dialog."), the print dialog widget. 

## ◆ getProcessId()

long AppWindow::getProcessId  | ( | | ) |   
---|---|---|---|---  
  
Returns Packet Tracer application process ID. 

Returns
    long, Packet Tracer application process ID. 

## ◆ getPTSAMode()

QString AppWindow::getPTSAMode  | ( | | ) |   
---|---|---|---|---  
  
Get the current PTSA Mode. 

Returns
    QString, current PTSA Mode. 

## ◆ getRealtimeToolbar()

[RealtimeToolbar](class_realtime_toolbar.html) AppWindow::getRealtimeToolbar  | ( | | ) |   
---|---|---|---|---  
  
Returns the Realtime mode toolbar. 

Returns
    [RealtimeToolbar](class_realtime_toolbar.html "RealtimeToolbar allows for UI manipulation of the Realtime toolbar."), the Realtime mode toolbar widget. 

## ◆ getRSSwitch()

[RSSwitch](class_r_s_switch.html) AppWindow::getRSSwitch  | ( | | ) |   
---|---|---|---|---  
  
Returns the Realtime/Simulation mode switch. 

Returns
    [RSSwitch](class_r_s_switch.html "RSSwitch allows for manipulation of the Realtime and Simulation toggle switches."), the Realtime/Simulation mode switch widget. 

## ◆ getSecondaryToolBar()

[ToolBar](class_tool_bar.html) AppWindow::getSecondaryToolBar  | ( | | ) |   
---|---|---|---|---  
  
Returns the secondary toolbar. 

Returns
    [ToolBar](class_tool_bar.html "ToolBar is the QDocWindow instatiated in QMainWindow."), the toolbar widget. 

## ◆ getSessionId()

QString AppWindow::getSessionId  | ( | | ) |   
---|---|---|---|---  
  
Returns the globally unique Packet Tracer application session ID. 

Returns
    QString, the globally unique Packet Tracer application session ID. 

## ◆ getSimulationPanel()

[SimulationPanel](class_simulation_panel.html) AppWindow::getSimulationPanel  | ( | | ) |   
---|---|---|---|---  
  
Returns the [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") panel. 

Returns
    [SimulationPanel](class_simulation_panel.html "SimulationPanel allows for UI manipulation of the Simulation Panel."), the [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") panel widget. 

## ◆ getSimulationToolbar()

[SimulationToolbar](class_simulation_toolbar.html) AppWindow::getSimulationToolbar  | ( | | ) |   
---|---|---|---|---  
  
Returns the [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") mode toolbar. 

Returns
    [SimulationToolbar](class_simulation_toolbar.html "SimulationToolbar allows UI for manipulation of the Simulation toolbar."), the [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") mode toolbar widget. 

## ◆ getTempFileLocation()

QString AppWindow::getTempFileLocation  | ( | | ) |   
---|---|---|---|---  
  
**[Deprecated:](deprecated.html#_deprecated000001)**
     Use [fileSaveAsync()](class_app_window.html#a5a4aabd1f4b3a643e109cef8c4d956f8 "Starts save operation and returns immediately.") and register to [fileSaveDone()](class_app_window.html#a0168b21c40fd0a573f55d71f5f48555f "This event is emitted when a file is saved.") event. 

## ◆ getToolBar()

[ToolBar](class_tool_bar.html) AppWindow::getToolBar  | ( | | ) |   
---|---|---|---|---  
  
Returns the toolbar. 

Returns
    [ToolBar](class_tool_bar.html "ToolBar is the QDocWindow instatiated in QMainWindow."), the toolbar widget. 

## ◆ getUserCreatedPDU()

[UserCreatedPDU](class_user_created_p_d_u.html) AppWindow::getUserCreatedPDU  | ( | | ) |   
---|---|---|---|---  
  
Returns the User Created PDU. 

Returns
    [UserCreatedPDU](class_user_created_p_d_u.html "The UserCreatedPDU widget holds all the user created pdus for different scenarios."), the User Created PDU widget. 

## ◆ getUserFolder()

QString AppWindow::getUserFolder  | ( | | ) |   
---|---|---|---|---  
  
Returns the user folder of the current user logged into the OS. 

Returns
    QString, the user folder of the current user logged into the OS. 

## ◆ getVersion()

QString AppWindow::getVersion  | ( | | ) |   
---|---|---|---|---  
  
Returns the Packet Tracer version number. 

Remarks
    The version includes the major, minor, maintainance and possibly build numbers.

Returns
    QString, the Packet Tracer version number. 

## ◆ getWebViewManager()

[WebViewManager](class_web_view_manager.html) AppWindow::getWebViewManager  | ( | | ) |   
---|---|---|---|---  
  
Returns the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules.") manager. 

Returns
    [WebViewManager](class_web_view_manager.html "WebViewManager manages all WebViews."), the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules.") manager. 

## ◆ getWidth()

int AppWindow::getWidth  | ( | | ) |   
---|---|---|---|---  
  
Returns the Packet Tracer main window width. 

Returns
    int, the Packet Tracer main window width. 

## ◆ getX()

int AppWindow::getX  | ( | | ) |   
---|---|---|---|---  
  
Returns the Packet Tracer main window x-coorindate. 

Returns
    int, the Packet Tracer main window x-coorindate. 

## ◆ getY()

int AppWindow::getY  | ( | | ) |   
---|---|---|---|---  
  
Returns the Packet Tracer main window y-coorindate. 

Returns
    int, the Packet Tracer main window y-coorindate. 

## ◆ helpPath()

void AppWindow::helpPath  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Open a help file at the given path. 

Parameters
     subPath,subpath| to the file to open.   
---|---  
  
## ◆ isActivityWizardOpen()

bool AppWindow::isActivityWizardOpen  | ( | | ) |   
---|---|---|---|---  
  
## ◆ isInterfaceLocked()

bool AppWindow::isInterfaceLocked  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | QString  |   
| ) | |   
  
Returns true if the interface with the specified ID is locked, otherwise false. 

Parameters
     ID,the| ID of the item to check if locked.   
---|---  
branchID1,limit| the search to this branch ID.   
branchID2,limit| the search to this branch ID of branchID1.  
  
Returns
    bool, true if the interface with the specified ID is locked, otherwise false. 

## ◆ isLogicalMode()

bool AppWindow::isLogicalMode  | ( | | ) |   
---|---|---|---|---  
  
Returns true if currently in Logical workspace, otherwise false. 

Returns
    bool, true if currently in Logical workspace, otherwise false. 

## ◆ isMaximized()

void AppWindow::isMaximized  | ( | | ) |   
---|---|---|---|---  
  
## ◆ isMinimized()

void AppWindow::isMinimized  | ( | | ) |   
---|---|---|---|---  
  
## ◆ isPhysicalMode()

bool AppWindow::isPhysicalMode  | ( | | ) |   
---|---|---|---|---  
  
Returns true if currently in Physical workspace, otherwise false. 

Returns
    bool, true if currently in Physical workspace, otherwise false. 

## ◆ isPreventClose()

bool AppWindow::isPreventClose  | ( | | ) |   
---|---|---|---|---  
  
Returns true if Packet Tracer is prevented from closing, otherwise false. 

Returns
    bool, true if Packet Tracer is prevented from closing, otherwise false. 

## ◆ isPTSA()

bool AppWindow::isPTSA  | ( | | ) |   
---|---|---|---|---  
  
returns true if PTSA 

Returns
    bool, true if PTSA. 

## ◆ isRealtimeMode()

bool AppWindow::isRealtimeMode  | ( | | ) |   
---|---|---|---|---  
  
Returns true if currently in Realtime mode, otherwise false. 

Returns
    bool, true if currently in Realtime mode, otherwise false. 

## ◆ isSimulationMode()

bool AppWindow::isSimulationMode  | ( | | ) |   
---|---|---|---|---  
  
Returns true if currently in [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") mode, otherwise false. 

Returns
    bool, true if currently in [Simulation](class_simulation.html "Simulation holds the traffic details like PDUs, ports, etc.") mode, otherwise false. 

## ◆ listDirectory()

vector< QString > AppWindow::listDirectory  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Temporary function used to update sample files. Not for normal use. 

## ◆ lockedInterfaceInvoked()

void AppWindow::lockedInterfaceInvoked  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | QString  | ,   
|  | QString  |   
| ) | |   
  
This event is emitted when a locked interface is invoked. 

  * lockMsg, the lock message. 
  * lockID, lock type. 
  * branch1, search limited to this branch ID 
  * branch2, search limited to this branch ID of branchID1



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ openURL()

bool AppWindow::openURL  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Open URL in external web browser. 

Parameters
     url,url| to open.   
---|---  
  
## ◆ promptFileOpenFolder()

FileOpenReturnValue AppWindow::promptFileOpenFolder  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Prompts to browse a folder for a file to open. 

Parameters
     folder,the| path of the folder to browse.  
---|---  
  
Returns
    EFileOpenReturnValue Can be of the following values: eFileReturnOk, eFileReturnBadSSL, eFileReturnBadDecompress, eFileReturnBadBinary, eFileReturnBadMetafile, eFileReturnBadConfiguration, eFileReturnUnableToReadFile, eFileReturnBadOptions, eFileReturnUserCancel 

## ◆ raise()

void AppWindow::raise  | ( | | ) |   
---|---|---|---|---  
  
## ◆ resized()

void AppWindow::resized  | ( | int  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
This event is emitted when the Packet Tracer main window is resized. 

  * width, the width of the main window 
  * height, the height of the main window



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ setCheckOutdatedDevices()

void AppWindow::setCheckOutdatedDevices  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Set if devices marked as outdated should be displayed for selection. 

Parameters
     bCheck,true| if outdated devices should be handled when setting up the toolbar, false if not.   
---|---  
  
## ◆ setClipboardText()

void AppWindow::setClipboardText  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Sets the clipboard text(copy/paste text) to the given text. 

Parameters
     text,text| to put on the clipboard to use for paste.   
---|---  
  
## ◆ setDisabled()

void AppWindow::setDisabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Disables or enables the application. Buttons, etc will be shown as disabled and unuable. 

Parameters
     flag,true| to disable the application and false to enable.   
---|---  
  
## ◆ setMaximumHeight()

void AppWindow::setMaximumHeight  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the maximum height of the Packet Tracer main window. 

## ◆ setMaximumSize()

void AppWindow::setMaximumSize  | ( | int  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Sets the maximum size of the Packet Tracer main window. 

## ◆ setMaximumWidth()

void AppWindow::setMaximumWidth  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the maximum width of the Packet Tracer main window. 

## ◆ setMinimumHeight()

void AppWindow::setMinimumHeight  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the minimum height of the Packet Tracer main window. 

## ◆ setMinimumSize()

void AppWindow::setMinimumSize  | ( | int  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Sets the minimum size of the Packet Tracer main window. 

## ◆ setMinimumWidth()

void AppWindow::setMinimumWidth  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the minimum width of the Packet Tracer main window. 

## ◆ setPLFrameVisible()

void AppWindow::setPLFrameVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
## ◆ setPreventClose()

void AppWindow::setPreventClose  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Allows or prevents Packet Tracer from closing. 

Parameters
     bPreventClose,true| to prevent Packet Tracer from closing, false to allow closing.   
---|---  
  
## ◆ setPTSAMode()

void AppWindow::setPTSAMode  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Get the current PTSA Mode. 

Returns
    QString, current PTSA Mode. 

## ◆ setPTSAPluginVisible()

void AppWindow::setPTSAPluginVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
show and hide pt window, called from ptsa plugin only. you still need to clear other windows, possibly with file->new 

Returns
    

## ◆ setRSFrameVisible()

void AppWindow::setRSFrameVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
## ◆ setVisible()

void AppWindow::setVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows or hides the Packet Tracer main window. 
    
    
        \brief This event is emitted when a message box should be displayed.
        \NOT APPLICABLE TO DESKTOP
    

event: popupMessage(QString reason, QString title, QString message, QString buttonA, QString buttonB, QString buttonC, QString buttonD) - PrivApplication;

Parameters
     flag,true| to show the Packet Tracer main window, false to hide it.   
---|---  
  
## ◆ setWindowGeometry()

void AppWindow::setWindowGeometry  | ( | int  | ,   
---|---|---|---  
|  | int  | ,   
|  | int  | ,   
|  | int  |   
| ) | |   
  
Sets the Packet Tracer main window geometry and position. 

Parameters
     x,the| x-coordinate of the main window.   
---|---  
y,the| y-coordinate of the main window.   
width,the| width of the main window.   
height,the| height of the main window.   
  
## ◆ setWindowTitle()

void AppWindow::setWindowTitle  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Sets the Packet Tracer main window title. 

Parameters
     title,the| window title   
---|---  
  
## ◆ shouldIgnoreFileExit()

bool AppWindow::shouldIgnoreFileExit  | ( | | ) |   
---|---|---|---|---  
  
This delegate determines if PT should ignore the file->exit action. If ignoring, then the script module should do something to let the user know. 

Returns
    bool, true if PT should ignore the file->exit action. 

## ◆ shouldIgnoreFileNew()

bool AppWindow::shouldIgnoreFileNew  | ( | | ) |   
---|---|---|---|---  
  
This delegate determines if PT should ignore the file->new action. If ignoring, then the script module should do something to let the user know. 

Returns
    bool, true if PT should ignore the file->new action. 

## ◆ shouldIgnoreFileOpenFolder()

bool AppWindow::shouldIgnoreFileOpenFolder  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
This delegate determines if PT should ignore the file->open folder action. If ignoring, then the script module should do something to let the user know. 

  * folder, the folder the user wants to browse for files to open.



Returns
    bool, true if PT should ignore the file->open folder action. 

## ◆ shouldIgnoreFileOpenRecent()

bool AppWindow::shouldIgnoreFileOpenRecent  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
This delegate determines if PT should ignore the file->open recent file action. If ignoring, then the script module should do something to let the user know. 

  * file, the path of the recent file to open.



Returns
    bool, true if PT should ignore the file->open recent file action. 

## ◆ shouldIgnoreFileSave()

bool AppWindow::shouldIgnoreFileSave  | ( | | ) |   
---|---|---|---|---  
  
This delegate determines if PT should ignore the file->save action. If ignoring, then the script module should do something to let the user know. 

Returns
    bool, true if PT should ignore the file->save action. 

## ◆ shouldIgnoreFileSaveAs()

bool AppWindow::shouldIgnoreFileSaveAs  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
This delegate determines if PT should ignore the file->save as action. If ignoring, then the script module should do something to let the user know. 

  * file, the file to save as



Returns
    bool, true if PT should ignore the file->save as action. 

## ◆ showMaximized()

void AppWindow::showMaximized  | ( | | ) |   
---|---|---|---|---  
  
Sets the Packet Tracer main window to the maximum size. 

## ◆ showMessageBox()

StandardButton AppWindow::showMessageBox  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | QString  | ,   
|  | MessageBoxIcon  | ,   
|  | StandardButton  | ,   
|  | StandardButton  | ,   
|  | StandardButton  |   
| ) | |   
  
Shows a modal message box with standard buttons over the PT main window. 

  * title, window title 
  * message, message text 
  * informativeText, sub message text 
  * icon, an icon next to the message, can be one of the following: NoIcon = 0, Information = 1, Warning = 2, Critical = 3, Question = 4 
  * buttons, a StandardButton value combining all standard buttons to show 
  * defaultButton, the StandardButton value for the default button 
  * escapeButton, the StandardButton value for the default button



StandardButton values: Ok = 0x00000400, // An "OK" button defined with the AcceptRole. Open = 0x00002000, // An "Open" button defined with the AcceptRole. Save = 0x00000800, // A "Save" button defined with the AcceptRole. Cancel = 0x00400000, // A "Cancel" button defined with the RejectRole. Close = 0x00200000, // A "Close" button defined with the RejectRole. Discard = 0x00800000, // A "Discard" or "Don't Save" button, depending on the platform, defined with the DestructiveRole. Apply = 0x02000000, // An "Apply" button defined with the ApplyRole. Reset = 0x04000000, // A "Reset" button defined with the ResetRole. RestoreDefaults = 0x08000000, // A "Restore Defaults" button defined with the ResetRole. Help = 0x01000000, // A "Help" button defined with the HelpRole. SaveAll = 0x00001000, // A "Save All" button defined with the AcceptRole. Yes = 0x00004000, // A "Yes" button defined with the YesRole. YesToAll = 0x00008000, // A "Yes to All" button defined with the YesRole. No = 0x00010000, // A "No" button defined with the NoRole. NoToAll = 0x00020000, // A "No to All" button defined with the NoRole. Abort = 0x00040000, // An "Abort" button defined with the RejectRole. Retry = 0x00080000, // A "Retry" button defined with the AcceptRole. Ignore = 0x00100000, // An "Ignore" button defined with the AcceptRole. NoButton = 0x00000000 // An invalid button.

Returns
    StandardButton value, the value of the selected button 

## ◆ showMessageBoxWithCustomButtons()

int AppWindow::showMessageBoxWithCustomButtons  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | QString  | ,   
|  | MessageBoxIcon  | ,   
|  | QString  | ,   
|  | int  | ,   
|  | int  |   
| ) | |   
  
Shows a modal message box with custom buttons over the PT main window. 

  * title, window title 
  * message, message text 
  * informativeText, sub message text 
  * icon, an icon next to the message, can be one of the following: NoIcon = 0, Information = 1, Warning = 2, Critical = 3, Question = 4 
  * buttonsJson, an array of strings for buttons in JSON string representation 
  * defaultButtonIndex, the index of the default button 
  * escapeButtonIndex, the index of the escape button, or -1 if not used



Returns
    int, the index of the selected button or -1 if no selection 

## ◆ showMinimized()

void AppWindow::showMinimized  | ( | | ) |   
---|---|---|---|---  
  
Sets the Packet Tracer main window to the minimum size. 

## ◆ showNormal()

void AppWindow::showNormal  | ( | | ) |   
---|---|---|---|---  
  
Sets the Packet Tracer main window to the normal size. 

## ◆ suppressInstructionDlg()

void AppWindow::suppressInstructionDlg  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
## ◆ writeToPT()

void AppWindow::writeToPT  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Writes a message to the [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") Log and shows it. 

Parameters
     msg,the| message to write to the [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") Log.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [AppWindow.pki](_app_window_8pki.html)


