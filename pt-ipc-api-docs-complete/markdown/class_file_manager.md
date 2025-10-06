# Cisco Packet Tracer Extensions API: FileManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_file_manager.html

---

[FileManager](class_file_manager.html "FileManager holds and manipulates the file manager process on routers and switches.") holds and manipulates the file manager process on routers and switches. [More...](class_file_manager.html#details)

##  Public Member Functions  
  
---  
[FileSystem](class_file_system.html) | [getFileSystem](class_file_manager.html#aa0870098debdbc428d3faf94edd5d0dc) (string)  
| Returns the file system with the specified name. [More...](class_file_manager.html#aa0870098debdbc428d3faf94edd5d0dc)  
  
[File](class_file.html) | [getFile](class_file_manager.html#a7fc34c7adb93e93ab4296fae3ed846d6) (string, bool)  
| Returns the [File](class_file.html "File holds and manipulates files on file systems.") given the path and check permission. [More...](class_file_manager.html#a7fc34c7adb93e93ab4296fae3ed846d6)  
  
[Directory](class_directory.html) | [getDirectory](class_file_manager.html#ad93c68022b426e7fc454f86dc3a59bb6) (string, bool)  
| Returns the [Directory](class_directory.html "Directory is the directory of the file systems for routers and switches.") given the path and check permission. [More...](class_file_manager.html#ad93c68022b426e7fc454f86dc3a59bb6)  
  
Public Member Functions inherited from [Process](class_process.html)  
[Device](class_device.html) | [getOwnerDevice](class_process.html#a9cc34f553b0325e0f4074301fd36b77b) ()  
| Returns the device for this process. [More...](class_process.html#a9cc34f553b0325e0f4074301fd36b77b)  
  
  
## Detailed Description

[FileManager](class_file_manager.html "FileManager holds and manipulates the file manager process on routers and switches.") holds and manipulates the file manager process on routers and switches. 

## Member Function Documentation

## ◆ getDirectory()

[Directory](class_directory.html) FileManager::getDirectory  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Returns the [Directory](class_directory.html "Directory is the directory of the file systems for routers and switches.") given the path and check permission. 

Parameters
     absPath,the| absolute path to directory.   
---|---  
bCheckPermission,true| if check permission of directory, false otherwise.  
  
Returns
    [Directory](class_directory.html "Directory is the directory of the file systems for routers and switches."), the directory of given path. 

## ◆ getFile()

[File](class_file.html) FileManager::getFile  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Returns the [File](class_file.html "File holds and manipulates files on file systems.") given the path and check permission. 

Parameters
     absPath,the| absolute path to [File](class_file.html "File holds and manipulates files on file systems.").   
---|---  
bCheckPermission,true| if check permission of file, false otherwise.  
  
Returns
    [File](class_file.html "File holds and manipulates files on file systems."), the [File](class_file.html "File holds and manipulates files on file systems.") of given path. 

## ◆ getFileSystem()

[FileSystem](class_file_system.html) FileManager::getFileSystem  | ( | string  | | ) |   
---|---|---|---|---|---  
  
Returns the file system with the specified name. 

Parameters
     name,the| name of the file system. [File](class_file.html "File holds and manipulates files on file systems.") systems: flash:, nvram:  
---|---  
  
Returns
    [FileSystem](class_file_system.html "FileSystem holds and manipulates the file system on routers and switches."), the [FileSystem](class_file_system.html "FileSystem holds and manipulates the file system on routers and switches.") object with the specified name. 

* * *

The documentation for this class was generated from the following file:

  * [CFileManager.pki](_c_file_manager_8pki.html)


