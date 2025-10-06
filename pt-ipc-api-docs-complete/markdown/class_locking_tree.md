# Cisco Packet Tracer Extensions API: LockingTree Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_locking_tree.html

---

[LockingTree](class_locking_tree.html "LockingTree handles and manipulates the activity file locking tree.") handles and manipulates the activity file locking tree. [More...](class_locking_tree.html#details)

##  Public Member Functions  
  
---  
bool | [setLock](class_locking_tree.html#abe7122b02d51a9ba7951c747e75a8ead) (QString, QString, QString, bool)  
| Locks or unlocks the specified locking item. [More...](class_locking_tree.html#abe7122b02d51a9ba7951c747e75a8ead)  
  
bool | [isLocked](class_locking_tree.html#a19f1bdf416639f45da4eefdf5bcc58fc) (QString, QString, QString)  
| Returns true if the specified item is locked, otherwise false. [More...](class_locking_tree.html#a19f1bdf416639f45da4eefdf5bcc58fc)  
  
  
## Detailed Description

[LockingTree](class_locking_tree.html "LockingTree handles and manipulates the activity file locking tree.") handles and manipulates the activity file locking tree. 

## Member Function Documentation

## ◆ isLocked()

bool LockingTree::isLocked  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | QString  |   
| ) | |   
  
Returns true if the specified item is locked, otherwise false. 

Parameters
     ID,the| name of the locking item.   
---|---  
branchID1,the| name from branch 1 (default is empty).   
branchID2,the| name from branch 2 in branch 1 (default is empty).   
  
## ◆ setLock()

bool LockingTree::setLock  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | QString  | ,   
|  | bool  |   
| ) | |   
  
Locks or unlocks the specified locking item. 

Parameters
     ID,the| name of the locking item.   
---|---  
branchID1,the| name from branch 1 (default is empty).   
branchID2,the| name from branch 2 in branch 1 (default is empty).   
locked,true| to lock the item, false to unlock the item.   
  
* * *

The documentation for this class was generated from the following file:

  * [LockingTree.pki](_locking_tree_8pki.html)


