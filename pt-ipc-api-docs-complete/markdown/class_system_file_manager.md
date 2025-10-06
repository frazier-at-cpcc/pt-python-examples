# Cisco Packet Tracer Extensions API: SystemFileManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_system_file_manager.html

---

[SystemFileManager](class_system_file_manager.html "SystemFileManager provides file IO to the local system.") provides file IO to the local system. [More...](class_system_file_manager.html#details)

##  Public Member Functions  
  
---  
QString | [getOpenFileName](class_system_file_manager.html#a81377da14a596ec404f1d55499cd0bd3) (QString, QString, QString)  
| Prompt the user to select a file to open. It blocks until the user has selected or canceled the dialog. [More...](class_system_file_manager.html#a81377da14a596ec404f1d55499cd0bd3)  
  
vector< String > | [getOpenFileNames](class_system_file_manager.html#a9634501f8c77ae158485aa3ee13f6efc) (QString, QString, QString)  
| Prompt the user to select one or multiple files to open. It blocks until the user has selected or canceled the dialog. [More...](class_system_file_manager.html#a9634501f8c77ae158485aa3ee13f6efc)  
  
QString | [getSelectedDirectory](class_system_file_manager.html#a6afe41b14e7ea09bfa8d8e762f73f6a8) (QString, QString)  
| Prompt the user to select a folder. It blocks until the user has selected or canceled the dialog. [More...](class_system_file_manager.html#a6afe41b14e7ea09bfa8d8e762f73f6a8)  
  
QString | [getSaveFileName](class_system_file_manager.html#ae1979f7d4ba8c4b1afb56c909eb11a1e) (QString, QString, QString)  
| Prompt the user to select a file to save. It blocks until the user has selected or canceled the dialog. [More...](class_system_file_manager.html#ae1979f7d4ba8c4b1afb56c909eb11a1e)  
  
QString | [getFileContents](class_system_file_manager.html#a1bf3bc6fbee7e62bbbbd0b9dbd7e195a) (QString)  
| Returns the content of a plain text file. [More...](class_system_file_manager.html#a1bf3bc6fbee7e62bbbbd0b9dbd7e195a)  
  
QString | [getFileBinaryContents](class_system_file_manager.html#a5935f337beb45095ef9f1ca36ab0372d) (QString)  
| Returns the content of a binary file in base 64 format. [More...](class_system_file_manager.html#a5935f337beb45095ef9f1ca36ab0372d)  
  
bool | [writeTextToFile](class_system_file_manager.html#af31699c0b46e3107ff182163852f61a8) (QString, QString)  
| Writes plain text content to a file using UTF-8 encoding. [More...](class_system_file_manager.html#af31699c0b46e3107ff182163852f61a8)  
  
bool | [writePlainTextToFile](class_system_file_manager.html#a2cea514a692e54e9d0284945d8a4d77a) (QString, QString)  
| Writes plain text content to a file using UTF-8 encoding. [More...](class_system_file_manager.html#a2cea514a692e54e9d0284945d8a4d77a)  
  
bool | [writeBinaryToFile](class_system_file_manager.html#ade1f4d59bcc3809edc1a28aa8cd619bd) (QString, QString)  
| Writes binary content to a file. [More...](class_system_file_manager.html#ade1f4d59bcc3809edc1a28aa8cd619bd)  
  
int | [getFileSize](class_system_file_manager.html#ac6b69b721154a091233364409c2f532d) (QString)  
| Returns the size of a file in bytes. [More...](class_system_file_manager.html#ac6b69b721154a091233364409c2f532d)  
  
QString | [getFileCheckSum](class_system_file_manager.html#a8e075331dea95f088d39581240230857) (QString)  
| Returns the SHA-1 checksum of a file. [More...](class_system_file_manager.html#a8e075331dea95f088d39581240230857)  
  
long | [getFileModificationTime](class_system_file_manager.html#ad7575d414c0026700539af4354cb6e3c) (QString)  
| Returns the last modification time of a file in number of seconds that have passed since 1970-01-01T00:00:00 UTC. [More...](class_system_file_manager.html#ad7575d414c0026700539af4354cb6e3c)  
  
FilePermissions | [getFilePermissions](class_system_file_manager.html#a3d255e11e7414d93b9e3ccdabc1426c7) (QString)  
| Returns the permissions of a file. [More...](class_system_file_manager.html#a3d255e11e7414d93b9e3ccdabc1426c7)  
  
bool | [setFilePermissions](class_system_file_manager.html#a2fe251cb56496bb9d704ab4a0c9473fd) (QString, FilePermissions)  
| Sets the permissions of a file. [More...](class_system_file_manager.html#a2fe251cb56496bb9d704ab4a0c9473fd)  
  
bool | [copySrcFileToDestFile](class_system_file_manager.html#a84ac82194c4738035086ec51e5ad70ff) (QString, QString)  
| Copies a file. [More...](class_system_file_manager.html#a84ac82194c4738035086ec51e5ad70ff)  
  
bool | [moveSrcFileToDestFile](class_system_file_manager.html#a325d23ac626b2cdd2df67159d834370a) (QString, QString, bool)  
| Moves or renames a file. [More...](class_system_file_manager.html#a325d23ac626b2cdd2df67159d834370a)  
  
bool | [copySrcDirectoryToDestDirectory](class_system_file_manager.html#a7cf5000c9adfb6557963c466879dce13) (QString, QString, bool, FilePermissions)  
| Copies a directory. [More...](class_system_file_manager.html#a7cf5000c9adfb6557963c466879dce13)  
  
bool | [moveSrcDirectoryToDestDirectory](class_system_file_manager.html#a366c606a2d8d5d7aa010d2e604c5a7d2) (QString, QString, bool)  
| Moves or renames a directory. [More...](class_system_file_manager.html#a366c606a2d8d5d7aa010d2e604c5a7d2)  
  
bool | [zipDirectory](class_system_file_manager.html#a9505c603b2e3e68048dd6e582a30cc81) (QString)  
| Zips up a directory into a zip file with the same name. [More...](class_system_file_manager.html#a9505c603b2e3e68048dd6e582a30cc81)  
  
bool | [zipDirectoryWithPassword](class_system_file_manager.html#a487a7c2ae5ed0075d942d082cdda5a74) (QString, QString)  
bool | [zipDirectoryTo](class_system_file_manager.html#a3983de37835a2b6d7e6b081ceb39e510) (QString, QString)  
| Zips up a directory into a zip file. [More...](class_system_file_manager.html#a3983de37835a2b6d7e6b081ceb39e510)  
  
bool | [zipDirectoryToWithPassword](class_system_file_manager.html#a78fc0b7dda813ff35687cac286ddd19e) (QString, QString, QString)  
bool | [unzipFile](class_system_file_manager.html#ac6f6b73b92cfbc40cf53e4bd858cc840) (QString)  
| Unzips up a file in the same directory with the same name. [More...](class_system_file_manager.html#ac6f6b73b92cfbc40cf53e4bd858cc840)  
  
bool | [unzipFileWithPassword](class_system_file_manager.html#a52cca0d60a05ce7cc676a06b635d7ac7) (QString, QString)  
bool | [unzipFileTo](class_system_file_manager.html#a02386a05afcbf6795d193af133504be6) (QString, QString)  
| Unzips up a file in the same directory to a specified directory. [More...](class_system_file_manager.html#a02386a05afcbf6795d193af133504be6)  
  
bool | [unzipFileToWithPassword](class_system_file_manager.html#a53e474f9093b145328fe4933d548b319) (QString, QString, QString)  
QString | [encrypt](class_system_file_manager.html#a43a1fff837ac58d2995b270e574edd0d) (QString, QString)  
| FOR INTERNAL USE ONLY. Encrypts the string using password. Returns empty string if not internal script module or exapps. [More...](class_system_file_manager.html#a43a1fff837ac58d2995b270e574edd0d)  
  
QString | [decrypt](class_system_file_manager.html#ab3d9c440478ffdfb0db2018f5ba0963e) (QString, QString)  
| FOR INTERNAL USE ONLY. Decrypts the data using password. Returns empty string if not internal script module or exapps. [More...](class_system_file_manager.html#ab3d9c440478ffdfb0db2018f5ba0963e)  
  
QString | [encryptBinary](class_system_file_manager.html#a4934139785ef98008802c7a497e4fd67) (QString, QString)  
| FOR INTERNAL USE ONLY. Encrypts the binary data using password. Returns empty string if not internal script module or exapps. [More...](class_system_file_manager.html#a4934139785ef98008802c7a497e4fd67)  
  
QString | [decryptBinary](class_system_file_manager.html#aa95130d5b5e558e6090a5a6d1aefde91) (QString, QString)  
| FOR INTERNAL USE ONLY. Decrypts the data using password. Returns empty string if not internal script module or exapps. [More...](class_system_file_manager.html#aa95130d5b5e558e6090a5a6d1aefde91)  
  
QString | [getEncryptedFileContents](class_system_file_manager.html#a4ac2052ab3ddd1859b99592a14c37c82) (QString, QString)  
| FOR INTERNAL USE ONLY. Reads and decrypts the file content using password. Returns empty string if not internal script module or exapps. [More...](class_system_file_manager.html#a4ac2052ab3ddd1859b99592a14c37c82)  
  
QString | [getEncryptedFileBinaryContents](class_system_file_manager.html#a6f5f18f3fe79c167d01dcd23a1fa5fa4) (QString, QString)  
| FOR INTERNAL USE ONLY. Reads and decrypts the binary file content using password. Returns empty string if not internal script module or exapps. [More...](class_system_file_manager.html#a6f5f18f3fe79c167d01dcd23a1fa5fa4)  
  
bool | [writeTextToEncryptedFile](class_system_file_manager.html#a67afc9c1bf39dd2d4fcb78a1d07e0fbb) (QString, QString, QString)  
| FOR INTERNAL USE ONLY. Encrypts the text content using password and writes to file. Returns false if not internal script module or exapps. [More...](class_system_file_manager.html#a67afc9c1bf39dd2d4fcb78a1d07e0fbb)  
  
bool | [writeBinaryToEncryptedFile](class_system_file_manager.html#a7673e09d6dc7063446f01753e9e62892) (QString, QString, QString)  
| FOR INTERNAL USE ONLY. Encrypts the binary content using password and writes to file. Returns false if not internal script module or exapps. [More...](class_system_file_manager.html#a7673e09d6dc7063446f01753e9e62892)  
  
bool | [writeTextToEncryptedLogFile](class_system_file_manager.html#aeee4888d847b20b889a07bf3edf34b8f) (QString, QString)  
| FOR INTERNAL USE ONLY. Encrypts the text content using same method as PT log file format and writes to file. Returns false if not internal script module or exapps. [More...](class_system_file_manager.html#aeee4888d847b20b889a07bf3edf34b8f)  
  
bool | [encryptFile](class_system_file_manager.html#a7fcb1eb78c1e603dcdb6e314f631c854) (QString, QString, QString)  
| FOR INTERNAL USE ONLY. Encrypts a file using password and writes to another file. Returns false if not internal script module or exapps. [More...](class_system_file_manager.html#a7fcb1eb78c1e603dcdb6e314f631c854)  
  
bool | [decryptFile](class_system_file_manager.html#a1c68124b724fa70aad824d748b1b44fc) (QString, QString, QString)  
| FOR INTERNAL USE ONLY. Decrypts a file using password and writes to another file. Returns false if not internal script module or exapps. [More...](class_system_file_manager.html#a1c68124b724fa70aad824d748b1b44fc)  
  
bool | [makeDirectory](class_system_file_manager.html#a251e8e824c4c10ca782c5935ecf5d1aa) (QString)  
| Creates a directory including all missing parents. [More...](class_system_file_manager.html#a251e8e824c4c10ca782c5935ecf5d1aa)  
  
bool | [removeFile](class_system_file_manager.html#a7c6ffd0909f24394f6a7761befa890c4) (QString)  
| Removes a file. [More...](class_system_file_manager.html#a7c6ffd0909f24394f6a7761befa890c4)  
  
bool | [removeDirectory](class_system_file_manager.html#a0c65df8dc237a503297022a3b45ad8f6) (QString)  
| Removes a directory recursively including all sub directories and files. [More...](class_system_file_manager.html#a0c65df8dc237a503297022a3b45ad8f6)  
  
bool | [directoryExists](class_system_file_manager.html#a1539cdf1d050341836c49eda9dd1c193) (QString)  
| Returns whether a directory exists. [More...](class_system_file_manager.html#a1539cdf1d050341836c49eda9dd1c193)  
  
bool | [fileExists](class_system_file_manager.html#ad031123c3b96d6859bf1131483fb055e) (QString)  
| Returns whether a file exists. [More...](class_system_file_manager.html#ad031123c3b96d6859bf1131483fb055e)  
  
QString | [convertToNativeSeparators](class_system_file_manager.html#a87b502be3a0d71a56104de4fa28d39f0) (QString)  
| Converts a path to native format with native separators. [More...](class_system_file_manager.html#a87b502be3a0d71a56104de4fa28d39f0)  
  
QString | [convertFromNativeSeparators](class_system_file_manager.html#a705e18437ed9b8bdfd4d426306bf91e9) (QString)  
| Converts a path to Unix format with Unix separators. [More...](class_system_file_manager.html#a705e18437ed9b8bdfd4d426306bf91e9)  
  
bool | [isAbsolutePath](class_system_file_manager.html#a5a12b69f17ad5cd737943577e356a2cc) (QString)  
| Returns whether the path is absolute. [More...](class_system_file_manager.html#a5a12b69f17ad5cd737943577e356a2cc)  
  
bool | [isRelativePath](class_system_file_manager.html#a4e1956defe0d622bb178b59abbd01593) (QString)  
| Returns whether the path is relative. [More...](class_system_file_manager.html#a4e1956defe0d622bb178b59abbd01593)  
  
QString | [getRelativePath](class_system_file_manager.html#ac1f926c82829add3ab5f695959d839a9) (QString, QString)  
| Returns path name of path2 relative to path1. [More...](class_system_file_manager.html#ac1f926c82829add3ab5f695959d839a9)  
  
QString | [getAbsolutePath](class_system_file_manager.html#a8574903903ed6a008f1c0489c11c45f9) (QString)  
| Returns absolute path name. [More...](class_system_file_manager.html#a8574903903ed6a008f1c0489c11c45f9)  
  
vector< QString > | [getFilesInDirectory](class_system_file_manager.html#a75d815e2d3e124ac00d2cdd2898eb26e) (QString)  
| Returns a list of files and directory names in a directory. [More...](class_system_file_manager.html#a75d815e2d3e124ac00d2cdd2898eb26e)  
  
[SystemFileWatcher](class_system_file_watcher.html) | [getFileWatcher](class_system_file_manager.html#a2693ab3bcf6fcbde7f8ff36ac0fa6329) ()  
| Returns the [SystemFileWatcher](class_system_file_watcher.html "SystemFileWatcher provides monitoring of files and directories in the local system.") instance for this Script [Module](class_module.html). This is not available for ExApps and will return NULL. [More...](class_system_file_manager.html#a2693ab3bcf6fcbde7f8ff36ac0fa6329)  
  
  
## Detailed Description

[SystemFileManager](class_system_file_manager.html "SystemFileManager provides file IO to the local system.") provides file IO to the local system. 

## Member Function Documentation

## ◆ convertFromNativeSeparators()

QString SystemFileManager::convertFromNativeSeparators  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Converts a path to Unix format with Unix separators. 

Parameters
     path,a| path name  
---|---  
  
Returns
    QString, the path converted to Unix format 

## ◆ convertToNativeSeparators()

QString SystemFileManager::convertToNativeSeparators  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Converts a path to native format with native separators. 

Parameters
     path,a| path name  
---|---  
  
Returns
    QString, the path converted to native format 

## ◆ copySrcDirectoryToDestDirectory()

bool SystemFileManager::copySrcDirectoryToDestDirectory  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | bool  | ,   
|  | FilePermissions  |   
| ) | |   
  
Copies a directory. 

Parameters
     srcDir,the| full path of the source   
---|---  
destDir,the| full path of the destination   
bReplace,true| if to replace, false otherwise   
permissions,standard| Unix permissions format  
  
Returns
    bool, true if successful, false otherwise 

## ◆ copySrcFileToDestFile()

bool SystemFileManager::copySrcFileToDestFile  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Copies a file. 

Parameters
     srcFile,the| full path of the source   
---|---  
destFile,the| full path of the destination  
  
Returns
    bool, true if successful, false otherwise 

## ◆ decrypt()

QString SystemFileManager::decrypt  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
FOR INTERNAL USE ONLY. Decrypts the data using password. Returns empty string if not internal script module or exapps. 

Parameters
     data,the| data to be decrypted in base 64 format   
---|---  
password,the| password to use to decrypt  
  
Returns
    QString, the decrypted string 

## ◆ decryptBinary()

QString SystemFileManager::decryptBinary  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
FOR INTERNAL USE ONLY. Decrypts the data using password. Returns empty string if not internal script module or exapps. 

Parameters
     data64,the| data to be decrypted in base 64 format   
---|---  
password,the| password to use to decrypt  
  
Returns
    QString, the decrypted data in base 64 format 

## ◆ decryptFile()

bool SystemFileManager::decryptFile  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | QString  |   
| ) | |   
  
FOR INTERNAL USE ONLY. Decrypts a file using password and writes to another file. Returns false if not internal script module or exapps. 

Parameters
     srcFile,the| full path to the source file   
---|---  
dstFile,the| full path of the destination file   
password,the| password to use to decrypt  
  
Returns
    bool, true if successful, false otherwise 

## ◆ directoryExists()

bool SystemFileManager::directoryExists  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns whether a directory exists. 

Parameters
     path,the| full path of the directory  
---|---  
  
Returns
    bool, true if it exists and is a directory, false otherwise 

## ◆ encrypt()

QString SystemFileManager::encrypt  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
FOR INTERNAL USE ONLY. Encrypts the string using password. Returns empty string if not internal script module or exapps. 

Parameters
     data,the| string to be encrypted   
---|---  
password,the| password to use to encrypt  
  
Returns
    QString, the encrypted data in base 64 format 

## ◆ encryptBinary()

QString SystemFileManager::encryptBinary  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
FOR INTERNAL USE ONLY. Encrypts the binary data using password. Returns empty string if not internal script module or exapps. 

Parameters
     data64,the| binary data to be encrypted in base 64 format   
---|---  
password,the| password to use to encrypt  
  
Returns
    QString, the encrypted data in base 64 format 

## ◆ encryptFile()

bool SystemFileManager::encryptFile  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | QString  |   
| ) | |   
  
FOR INTERNAL USE ONLY. Encrypts a file using password and writes to another file. Returns false if not internal script module or exapps. 

Parameters
     srcFile,the| full path to the source file   
---|---  
dstFile,the| full path of the destination file   
password,the| password to use to encrypt  
  
Returns
    bool, true if successful, false otherwise 

## ◆ fileExists()

bool SystemFileManager::fileExists  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns whether a file exists. 

Parameters
     path,the| full path of the file  
---|---  
  
Returns
    bool, true if it exists and is a file, false otherwise 

## ◆ getAbsolutePath()

QString SystemFileManager::getAbsolutePath  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns absolute path name. 

Parameters
     path,a| path anme  
---|---  
  
Returns
    QString, absolute path name. 

## ◆ getEncryptedFileBinaryContents()

QString SystemFileManager::getEncryptedFileBinaryContents  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
FOR INTERNAL USE ONLY. Reads and decrypts the binary file content using password. Returns empty string if not internal script module or exapps. 

Parameters
     filename,the| full path to the file   
---|---  
password,the| password to use to decrypt  
  
Returns
    QString, the decrypted data in base 64 format 

## ◆ getEncryptedFileContents()

QString SystemFileManager::getEncryptedFileContents  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
FOR INTERNAL USE ONLY. Reads and decrypts the file content using password. Returns empty string if not internal script module or exapps. 

Parameters
     filename,the| full path to the file   
---|---  
password,the| password to use to decrypt  
  
Returns
    QString, the decrypted string 

## ◆ getFileBinaryContents()

QString SystemFileManager::getFileBinaryContents  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the content of a binary file in base 64 format. 

Parameters
     filename,the| full path of the file  
---|---  
  
Returns
    QString, the content of the file 

## ◆ getFileCheckSum()

QString SystemFileManager::getFileCheckSum  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the SHA-1 checksum of a file. 

Parameters
     path,the| full path of the file.  
---|---  
  
Returns
    QString, the SHA-1 checksum of the file 

## ◆ getFileContents()

QString SystemFileManager::getFileContents  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the content of a plain text file. 

Parameters
     filename,the| full path of the file  
---|---  
  
Returns
    QString, the content of the file 

## ◆ getFileModificationTime()

long SystemFileManager::getFileModificationTime  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the last modification time of a file in number of seconds that have passed since 1970-01-01T00:00:00 UTC. 

Parameters
     path,the| full path of the file.  
---|---  
  
Returns
    int, last modification time in number of seconds that have passed since 1970-01-01T00:00:00 UTC. 

## ◆ getFilePermissions()

FilePermissions SystemFileManager::getFilePermissions  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the permissions of a file. 

Parameters
     path,the| full path of the file.  
---|---  
  
Returns
    int, the permissions of the file. 

## ◆ getFilesInDirectory()

vector< QString > SystemFileManager::getFilesInDirectory  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns a list of files and directory names in a directory. 

Parameters
     path,the| full path of the directory  
---|---  
  
Returns
    vector<QString>, the list of files and directory names 

## ◆ getFileSize()

int SystemFileManager::getFileSize  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the size of a file in bytes. 

Parameters
     path,the| full path of the file.  
---|---  
  
Returns
    int, size of file in bytes 

## ◆ getFileWatcher()

[SystemFileWatcher](class_system_file_watcher.html) SystemFileManager::getFileWatcher  | ( | | ) |   
---|---|---|---|---  
  
Returns the [SystemFileWatcher](class_system_file_watcher.html "SystemFileWatcher provides monitoring of files and directories in the local system.") instance for this Script [Module](class_module.html). This is not available for ExApps and will return NULL. 

Returns
    [SystemFileWatcher](class_system_file_watcher.html "SystemFileWatcher provides monitoring of files and directories in the local system."), the instance for this Script [Module](class_module.html)

## ◆ getOpenFileName()

QString SystemFileManager::getOpenFileName  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | QString  |   
| ) | |   
  
Prompt the user to select a file to open. It blocks until the user has selected or canceled the dialog. 

Parameters
     caption,the| title of the open dialog   
---|---  
path,the| default full path   
filter,the| filter of files to show in open dialog in the following format: <filter>[;;<filter[...]]] where each <filter> is in the following format: <name>(*.<extension>[ *.<extension>[...]])  
  
example: "Packet Tracer Activity Sequencer File (*.pks *.pksz);;Zip File (*.zip)" 

Returns
    QString, the full path of the selected file 

## ◆ getOpenFileNames()

vector< String > SystemFileManager::getOpenFileNames  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | QString  |   
| ) | |   
  
Prompt the user to select one or multiple files to open. It blocks until the user has selected or canceled the dialog. 

Parameters
     caption,the| title of the open dialog   
---|---  
path,the| default full path   
filter,the| filter of files to show in open dialog in the following format: <filter>[;;<filter[...]]] where each <filter> is in the following format: <name>(*.<extension>[ *.<extension>[...]])  
  
example: "Packet Tracer Activity Sequencer File (*.pks *.pksz);;Zip File (*.zip)" 

Returns
    vector<QString>, the full path of the selected files 

## ◆ getRelativePath()

QString SystemFileManager::getRelativePath  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Returns path name of path2 relative to path1. 

Parameters
     path1,the| full base path name   
---|---  
path2,the| full sub path name  
  
Returns
    QString, the path name of path2 relative to path1. 

## ◆ getSaveFileName()

QString SystemFileManager::getSaveFileName  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | QString  |   
| ) | |   
  
Prompt the user to select a file to save. It blocks until the user has selected or canceled the dialog. 

Parameters
     caption,the| title of the save dialog   
---|---  
path,the| default full path   
filter,the| filter of files to show in save dialog in the following format: <filter>[;;<filter[...]]] where each <filter> is in the following format: <name>(*.<extension>[ *.<extension>[...]])  
  
example: "Packet Tracer Activity Sequencer File (*.pks *.pksz);;Zip File (*.zip)" 

Returns
    QString, the full path of the selected file 

## ◆ getSelectedDirectory()

QString SystemFileManager::getSelectedDirectory  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Prompt the user to select a folder. It blocks until the user has selected or canceled the dialog. 

Parameters
     caption,the| title of the dialog   
---|---  
path,the| default full path  
  
Returns
    QString, the full path of the selected directory 

## ◆ isAbsolutePath()

bool SystemFileManager::isAbsolutePath  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns whether the path is absolute. 

Parameters
     path,a| path name  
---|---  
  
Returns
    bool, whether the path is absolute. 

## ◆ isRelativePath()

bool SystemFileManager::isRelativePath  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns whether the path is relative. 

Parameters
     path,a| path name  
---|---  
  
Returns
    bool, whether the path is relative. 

## ◆ makeDirectory()

bool SystemFileManager::makeDirectory  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Creates a directory including all missing parents. 

Parameters
     path,the| full path of the directory  
---|---  
  
Returns
    bool, true if successful, false otherwise 

## ◆ moveSrcDirectoryToDestDirectory()

bool SystemFileManager::moveSrcDirectoryToDestDirectory  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | bool  |   
| ) | |   
  
Moves or renames a directory. 

Parameters
     srcDir,the| full path of the source   
---|---  
destDir,the| full path of the destination   
bReplace,true| if to replace, false otherwise  
  
Returns
    bool, true if successful, false otherwise 

## ◆ moveSrcFileToDestFile()

bool SystemFileManager::moveSrcFileToDestFile  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | bool  |   
| ) | |   
  
Moves or renames a file. 

Parameters
     srcFile,the| full path of the source   
---|---  
destFile,the| full path of the destination   
bReplace,true| if to replace, false otherwise  
  
Returns
    bool, true if successful, false otherwise 

## ◆ removeDirectory()

bool SystemFileManager::removeDirectory  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Removes a directory recursively including all sub directories and files. 

Parameters
     path,the| full path of the directory  
---|---  
  
Returns
    bool, true if successful, false otherwise 

## ◆ removeFile()

bool SystemFileManager::removeFile  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Removes a file. 

Parameters
     path,the| full path of the file  
---|---  
  
Returns
    bool, true if successful, false otherwise 

## ◆ setFilePermissions()

bool SystemFileManager::setFilePermissions  | ( | QString  | ,   
---|---|---|---  
|  | FilePermissions  |   
| ) | |   
  
Sets the permissions of a file. 

Parameters
     path,the| full path of the file.   
---|---  
int,standard| Unix permissions format  
  
Returns
    bool, true if successful, false otherwise 

## ◆ unzipFile()

bool SystemFileManager::unzipFile  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Unzips up a file in the same directory with the same name. 

Parameters
     filePath,the| full path of the zip file   
---|---  
password,the| password to use to decrypt the encrypted zip  
  
Returns
    bool, true if successful, false otherwise 

## ◆ unzipFileTo()

bool SystemFileManager::unzipFileTo  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Unzips up a file in the same directory to a specified directory. 

Parameters
     filePath,the| full path of the zip file   
---|---  
dstPath,the| full path of the destination directory   
password,the| password to use to decrypt the encrypted zip  
  
Returns
    bool, true if successful, false otherwise 

## ◆ unzipFileToWithPassword()

bool SystemFileManager::unzipFileToWithPassword  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | QString  |   
| ) | |   
  
## ◆ unzipFileWithPassword()

bool SystemFileManager::unzipFileWithPassword  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
## ◆ writeBinaryToEncryptedFile()

bool SystemFileManager::writeBinaryToEncryptedFile  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | QString  |   
| ) | |   
  
FOR INTERNAL USE ONLY. Encrypts the binary content using password and writes to file. Returns false if not internal script module or exapps. 

Parameters
     filename,the| full path to the file   
---|---  
contents64,the| data in base 64 format   
password,the| password to use to encrypt  
  
Returns
    bool, true if successful, false otherwise 

## ◆ writeBinaryToFile()

bool SystemFileManager::writeBinaryToFile  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Writes binary content to a file. 

Parameters
     filename,the| full path of the file.   
---|---  
contents64,the| content in base 64 format  
  
Returns
    bool, true if successful, false otherwise 

## ◆ writePlainTextToFile()

bool SystemFileManager::writePlainTextToFile  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Writes plain text content to a file using UTF-8 encoding. 

Parameters
     filename,the| full path of the file.   
---|---  
contents,the| contents  
  
Returns
    bool, true if successful, false otherwise 

## ◆ writeTextToEncryptedFile()

bool SystemFileManager::writeTextToEncryptedFile  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | QString  |   
| ) | |   
  
FOR INTERNAL USE ONLY. Encrypts the text content using password and writes to file. Returns false if not internal script module or exapps. 

Parameters
     filename,the| full path to the file   
---|---  
contents,the| text content   
password,the| password to use to encrypt  
  
Returns
    bool, true if successful, false otherwise 

## ◆ writeTextToEncryptedLogFile()

bool SystemFileManager::writeTextToEncryptedLogFile  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
FOR INTERNAL USE ONLY. Encrypts the text content using same method as PT log file format and writes to file. Returns false if not internal script module or exapps. 

Parameters
     filename,the| full path to the file   
---|---  
contents,the| text content  
  
Returns
    bool, true if successful, false otherwise 

## ◆ writeTextToFile()

bool SystemFileManager::writeTextToFile  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Writes plain text content to a file using UTF-8 encoding. 

Parameters
     filename,the| full path of the file.   
---|---  
contents64,the| content in base 64 format  
  
Returns
    bool, true if successful, false otherwise 

## ◆ zipDirectory()

bool SystemFileManager::zipDirectory  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Zips up a directory into a zip file with the same name. 

Parameters
     path,the| full path of the directory   
---|---  
password,the| password to use to encrypt the zip  
  
Returns
    bool, true if successful, false otherwise 

## ◆ zipDirectoryTo()

bool SystemFileManager::zipDirectoryTo  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Zips up a directory into a zip file. 

Parameters
     path,the| full path of the directory   
---|---  
dstFile,the| full path of the destination zip file   
password,the| password to use to encrypt the zip  
  
Returns
    bool, true if successful, false otherwise 

## ◆ zipDirectoryToWithPassword()

bool SystemFileManager::zipDirectoryToWithPassword  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | QString  |   
| ) | |   
  
## ◆ zipDirectoryWithPassword()

bool SystemFileManager::zipDirectoryWithPassword  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
* * *

The documentation for this class was generated from the following file:

  * [SystemFileManager.pki](_system_file_manager_8pki.html)


