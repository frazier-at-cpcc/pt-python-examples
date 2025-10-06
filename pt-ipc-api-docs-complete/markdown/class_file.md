# Cisco Packet Tracer Extensions API: File Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_file.html

---

[File](class_file.html "File holds and manipulates files on file systems.") holds and manipulates files on file systems. [More...](class_file.html#details)

##  Public Member Functions  
  
---  
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

[File](class_file.html "File holds and manipulates files on file systems.") holds and manipulates files on file systems. 

## Member Function Documentation

## ◆ getAbsPath()

string File::getAbsPath  | ( | | ) |   
---|---|---|---|---  
  
Returns absolute path of the [File](class_file.html "File holds and manipulates files on file systems.") object. 

Returns
    string, absolute path of the [File](class_file.html "File holds and manipulates files on file systems.") object. 

## ◆ getContent()

[FileContent](struct_file_content.html) File::getContent  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Returns the file content of the [File](class_file.html "File holds and manipulates files on file systems."). 

Parameters
     bCheckPermission,true| if check the permission of the file, otherwise false.  
---|---  
  
Returns
    [FileContent](struct_file_content.html "File content structure."), the file content of the [File](class_file.html "File holds and manipulates files on file systems."). 

## ◆ getName()

string File::getName  | ( | | ) |   
---|---|---|---|---  
  
Returns the filename of the file. 

Returns
    string, the filename of the file. 

## ◆ getParent()

[Directory](class_directory.html) File::getParent  | ( | | ) |   
---|---|---|---|---  
  
Returns the parent directory. 

Returns
    [Directory](class_directory.html "Directory is the directory of the file systems for routers and switches."), the parent directory. 

## ◆ getPermission()

FilePermission File::getPermission  | ( | | ) |   
---|---|---|---|---  
  
Returns the permissions of the file. 

Returns
    enum<FilePermission>, the permissions of the file. Permissions: eExecute = 1, eWrite = 2, eRead = 4 

## ◆ getSize()

int File::getSize  | ( | | ) |   
---|---|---|---|---  
  
Returns the filesize of the file. 

Returns
    int, the filesize of the file. 

## ◆ isDirectory()

bool File::isDirectory  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the file is a directory, otherwise false. 

Returns
    bool, true if the file is a directory, otherwise false. 

## ◆ isExecutable()

bool File::isExecutable  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the file is executable, otherwise false. 

Returns
    bool, true if the file is executable, otherwise false. 

## ◆ isReadable()

bool File::isReadable  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the file is readable, otherwise false. 

Returns
    bool, true if the file is readable, otherwise false. 

## ◆ isWritable()

bool File::isWritable  | ( | | ) |   
---|---|---|---|---  
  
Returns true if the file is writable, otherwise false. 

Returns
    bool, true if the file is writable, otherwise false. 

## ◆ setTextContent()

void File::setTextContent  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
set the content of the [File](class_file.html "File holds and manipulates files on file systems.") object. 

Parameters
     content,the| content string to set to the [File](class_file.html "File holds and manipulates files on file systems.").   
---|---  
bCheckPermission,true| if check the permission of the file, otherwise false.   
  
* * *

The documentation for this class was generated from the following file:

  * [CFile.pki](_c_file_8pki.html)


