# Cisco Packet Tracer Extensions API: SystemFileWatcher Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_system_file_watcher.html

---

[SystemFileWatcher](class_system_file_watcher.html "SystemFileWatcher provides monitoring of files and directories in the local system.") provides monitoring of files and directories in the local system. [More...](class_system_file_watcher.html#details)

##  Public Member Functions  
  
---  
bool | [addPath](class_system_file_watcher.html#ad9d2ea0c72f48a6a433330ec3ec23e04) (QString)  
| Add a file or directory to watch for changes. [More...](class_system_file_watcher.html#ad9d2ea0c72f48a6a433330ec3ec23e04)  
  
bool | [removePath](class_system_file_watcher.html#a08b8042353a25105a7a7debc9708a8d8) (QString)  
| Stop watching a file or directory for changes. [More...](class_system_file_watcher.html#a08b8042353a25105a7a7debc9708a8d8)  
  
void | [fileChanged](class_system_file_watcher.html#a9bd615d25e2dc888de5ad63ea9ba58b1) (QString)  
| This event is emitted when a file being watched has changed. [More...](class_system_file_watcher.html#a9bd615d25e2dc888de5ad63ea9ba58b1)  
  
void | [directoryChanged](class_system_file_watcher.html#a240048bd384db7267b69beeee4e731eb) (QString)  
| This event is emitted when a directory being watched has changed. [More...](class_system_file_watcher.html#a240048bd384db7267b69beeee4e731eb)  
  
  
## Detailed Description

[SystemFileWatcher](class_system_file_watcher.html "SystemFileWatcher provides monitoring of files and directories in the local system.") provides monitoring of files and directories in the local system. 

## Member Function Documentation

## ◆ addPath()

bool SystemFileWatcher::addPath  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Add a file or directory to watch for changes. 

Parameters
     path,the| full path of the file or directory to watch  
---|---  
  
Returns
    bool, true if successful, false otherwise 

## ◆ directoryChanged()

void SystemFileWatcher::directoryChanged  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when a directory being watched has changed. 

Parameters
     path,the| full path of the directory  
---|---  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ fileChanged()

void SystemFileWatcher::fileChanged  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when a file being watched has changed. 

Parameters
     path,the| full path of the file  
---|---  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ removePath()

bool SystemFileWatcher::removePath  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Stop watching a file or directory for changes. 

Parameters
     path,the| full path of the file or directory to stop watching  
---|---  
  
Returns
    bool, true if successful, false otherwise 

* * *

The documentation for this class was generated from the following file:

  * [SystemFileWatcher.pki](_system_file_watcher_8pki.html)


