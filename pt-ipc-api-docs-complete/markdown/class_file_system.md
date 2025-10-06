# Cisco Packet Tracer Extensions API: FileSystem Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_file_system.html

---

[FileSystem](class_file_system.html "FileSystem holds and manipulates the file system on routers and switches.") holds and manipulates the file system on routers and switches. [More...](class_file_system.html#details)

##  Public Member Functions  
  
---  
int | [getSize](class_file_system.html#a5545c4c3acf3c682517ca38cb93117e5) ()  
| Returns the size of the file system. [More...](class_file_system.html#a5545c4c3acf3c682517ca38cb93117e5)  
  
int | [getCapacity](class_file_system.html#ae63d4fbac3a9c89d360467f834787180) ()  
| Returns the capacity of the file system. [More...](class_file_system.html#ae63d4fbac3a9c89d360467f834787180)  
  
int | [getSpaceFree](class_file_system.html#a3f4aa79fe07151fa535e49c0592e79f9) ()  
| Returns the amount of free space on the file system. [More...](class_file_system.html#a3f4aa79fe07151fa535e49c0592e79f9)  
  
Public Member Functions inherited from [Directory](class_directory.html)  
int | [getFileCount](class_directory.html#a69d1e9dc908f00613ac15a24ff198c00) ()  
| Returns the number of files in the file system. [More...](class_directory.html#a69d1e9dc908f00613ac15a24ff198c00)  
  
[File](class_file.html) | [getFileAt](class_directory.html#a19205708e139d5838161c4d4f7fbcbdc) (int)  
| Returns the file at the specified index. [More...](class_directory.html#a19205708e139d5838161c4d4f7fbcbdc)  
  
[File](class_file.html) | [getFile](class_directory.html#ac67ba1ba8f4e083b725f6149ceb4e350) (string)  
| Returns the file with the specified filename. [More...](class_directory.html#ac67ba1ba8f4e083b725f6149ceb4e350)  
  
bool | [fileExist](class_directory.html#aaf3027d40c409675160e4708f7ee3cfc) (string)  
| Returns if a file exist in the file system. [More...](class_directory.html#aaf3027d40c409675160e4708f7ee3cfc)  
  
int | [getSpaceUsed](class_directory.html#a00c9dcc5569a6d732e1d11e802eef1fb) ()  
| Returns the amount of space used on this file system. [More...](class_directory.html#a00c9dcc5569a6d732e1d11e802eef1fb)  
  
bool | [addFile](class_directory.html#a28c7ad249aff4e10c27098b18e59006d) ([File](class_file.html), bool)  
| Add file into filesystem. [More...](class_directory.html#a28c7ad249aff4e10c27098b18e59006d)  
  
bool | [addTextFile](class_directory.html#a15a8a05472a573a173cc10847d6f9ac0) (string, string, bool)  
| Add text file into filesystem. [More...](class_directory.html#a15a8a05472a573a173cc10847d6f9ac0)  
  
bool | [addDirectory](class_directory.html#a0269eed6c0cd2255c99016e06f469410) (string, bool)  
| Add directory into filesystem. [More...](class_directory.html#a0269eed6c0cd2255c99016e06f469410)  
  
bool | [addHttpPage](class_directory.html#aaf3bc455cc5ccc9d7db96895d310fa83) (string, string, bool)  
| Returns true if the HTTP page was added successfully, false otherwise. [More...](class_directory.html#aaf3bc455cc5ccc9d7db96895d310fa83)  
  
bool | [copyAllFilesFrom](class_directory.html#a154703bdd6a421b99b5618b213b9bcd3) ([Directory](class_directory.html), bool)  
| Copy all files from another directory. [More...](class_directory.html#a154703bdd6a421b99b5618b213b9bcd3)  
  
bool | [removeFile](class_directory.html#ab5cf549b36299369073cab06a9308849) (string, bool)  
| Returns true if the file was removed successfully, false otherwise. [More...](class_directory.html#ab5cf549b36299369073cab06a9308849)  
  
bool | [removeAllFiles](class_directory.html#aeeaa8c43d117ec9f2b8877718afa5d2d) (bool)  
| Returns true if all files were removed successfully, false otherwise. [More...](class_directory.html#aeeaa8c43d117ec9f2b8877718afa5d2d)  
  
bool | [renameFile](class_directory.html#ac2776588eec5dc965a0205c169e3679d) (string, string, bool)  
| Returns true if the file was renamed successfully, false otherwise. [More...](class_directory.html#ac2776588eec5dc965a0205c169e3679d)  
  
void | [fileAdded](class_directory.html#af70f3f3cf7317cebeb1100ab4484e4fa) (string)  
| This event is emitted when a file is added successfully. [More...](class_directory.html#af70f3f3cf7317cebeb1100ab4484e4fa)  
  
void | [fileRemoved](class_directory.html#a33396bb64403ef67913ab0bd19fd977f) (string)  
| This event is emitted when a file is removed successfully. [More...](class_directory.html#a33396bb64403ef67913ab0bd19fd977f)  
  
void | [fileRenamed](class_directory.html#ad8d37c969d31211856c5f538a852f2bb) (string, string)  
| This event is emitted when a file name is changed successfully. [More...](class_directory.html#ad8d37c969d31211856c5f538a852f2bb)  
  
Public Member Functions inherited from [File](class_file.html)  
string | [getName](class_file.html#ae0d38bf3e2612ff3dcd583b4e4b86e80) ()  
| Returns the filename of the file. [More...](class_file.html#ae0d38bf3e2612ff3dcd583b4e4b86e80)  
  
FilePermission | [getPermission](class_file.html#a925037cf47fe20a76b134d1a7f2d40fe) ()  
| Returns the permissions of the file. [More...](class_file.html#a925037cf47fe20a76b134d1a7f2d40fe)  
  
bool | [isExecutable](class_file.html#ad40730bf9b38daf93f4b2b2030a46fe7) ()  
| Returns true if the file is executable, otherwise false. [More...](class_file.html#ad40730bf9b38daf93f4b2b2030a46fe7)  
  
bool | [isWritable](class_file.html#acf94b5b77c302041486f6a08660f515e) ()  
| Returns true if the file is writable, otherwise false. [More...](class_file.html#acf94b5b77c302041486f6a08660f515e)  
  
bool | [isReadable](class_file.html#a9452a31550ced93a24cb3981ef7442cc) ()  
| Returns true if the file is readable, otherwise false. [More...](class_file.html#a9452a31550ced93a24cb3981ef7442cc)  
  
bool | [isDirectory](class_file.html#a6ba5bdb943363cda56649238ccb18c27) ()  
| Returns true if the file is a directory, otherwise false. [More...](class_file.html#a6ba5bdb943363cda56649238ccb18c27)  
  
int | [getSize](class_file.html#a66119cf01fcaf7001b7ad2df487a7d7c) ()  
| Returns the filesize of the file. [More...](class_file.html#a66119cf01fcaf7001b7ad2df487a7d7c)  
  
[Directory](class_directory.html) | [getParent](class_file.html#a1b8577157ac53025b63674541952cb8a) ()  
| Returns the parent directory. [More...](class_file.html#a1b8577157ac53025b63674541952cb8a)  
  
string | [getAbsPath](class_file.html#ac5c87d0b0ed06a9040b07da28d671fa0) ()  
| Returns absolute path of the [File](class_file.html "File holds and manipulates files on file systems.") object. [More...](class_file.html#ac5c87d0b0ed06a9040b07da28d671fa0)  
  
void | [setTextContent](class_file.html#a257b51e8dbfcadc2f133e245daa0638c) (string, bool)  
| set the content of the [File](class_file.html "File holds and manipulates files on file systems.") object. [More...](class_file.html#a257b51e8dbfcadc2f133e245daa0638c)  
  
[FileContent](struct_file_content.html) | [getContent](class_file.html#a89f093fd362e459615c9d0895476d3c3) (bool)  
| Returns the file content of the [File](class_file.html "File holds and manipulates files on file systems."). [More...](class_file.html#a89f093fd362e459615c9d0895476d3c3)  
  
  
## Detailed Description

[FileSystem](class_file_system.html "FileSystem holds and manipulates the file system on routers and switches.") holds and manipulates the file system on routers and switches. 

## Member Function Documentation

## ◆ getCapacity()

int FileSystem::getCapacity  | ( | | ) |   
---|---|---|---|---  
  
Returns the capacity of the file system. 

Returns
    int, the capacity of the file system. 

## ◆ getSize()

int FileSystem::getSize  | ( | | ) |   
---|---|---|---|---  
  
Returns the size of the file system. 

Returns
    int, the size of the file system. 

## ◆ getSpaceFree()

int FileSystem::getSpaceFree  | ( | | ) |   
---|---|---|---|---  
  
Returns the amount of free space on the file system. 

Returns
    int, the amount of free space on the file system. 

* * *

The documentation for this class was generated from the following file:

  * [CFileSystem.pki](_c_file_system_8pki.html)


