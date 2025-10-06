# Cisco Packet Tracer Extensions API: Cluster Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_cluster.html

---

##  Public Member Functions  
  
---  
void | [setName](class_cluster.html#a650208d0dbedf76f0d28fe93b883fd61) (QString)  
| Allows to change cluster name to newName. [More...](class_cluster.html#a650208d0dbedf76f0d28fe93b883fd61)  
  
QString | [getName](class_cluster.html#a00994026d934519d0a0c7d46fe6bb8e0) ()  
| Returns cluster name. [More...](class_cluster.html#a00994026d934519d0a0c7d46fe6bb8e0)  
  
void | [nameChanged](class_cluster.html#abf8ebd46660136aa8021d678695a52db) (QString, QString)  
| Generated when cluster name changes to a new one. [More...](class_cluster.html#abf8ebd46660136aa8021d678695a52db)  
  
QString | [getId](class_cluster.html#ac4c28dd21d7989c5b475acfdd3a9d289) ()  
| Returns cluster ID. [More...](class_cluster.html#ac4c28dd21d7989c5b475acfdd3a9d289)  
  
void | [idChanged](class_cluster.html#a2fc642e3a1c029a277b1195d89159f20) (QString, QString)  
| Generated when cluster ID changes to a new one. [More...](class_cluster.html#a2fc642e3a1c029a277b1195d89159f20)  
  
int | [getChildClusterCount](class_cluster.html#a5a8934a53a0a099a1c16887f556d7163) ()  
| Returns the number of child cluster objects. [More...](class_cluster.html#a5a8934a53a0a099a1c16887f556d7163)  
  
[Cluster](class_cluster.html) | [getChildClusterAt](class_cluster.html#abf96284f2f67254f19d81aacff3728da) (int)  
| Returns child cluster object at a given index. [More...](class_cluster.html#abf96284f2f67254f19d81aacff3728da)  
  
[Cluster](class_cluster.html) | [getParentCluster](class_cluster.html#a11e90e68dc4cf45cd00312e578a1ed14) ()  
| Returns parent cluster object. [More...](class_cluster.html#a11e90e68dc4cf45cd00312e578a1ed14)  
  
double | [getXCoordinate](class_cluster.html#aaeee48912d11be1ff4cb4bfb0c47e301) ()  
| Returns the current x-coordinate position in the Logical workspace for this cluster. [More...](class_cluster.html#aaeee48912d11be1ff4cb4bfb0c47e301)  
  
double | [getYCoordinate](class_cluster.html#acd46885a3c3466d6c031e7d32f68a306) ()  
| Returns the current y-coordinate position in the Logical workspace for this cluster. [More...](class_cluster.html#acd46885a3c3466d6c031e7d32f68a306)  
  
double | [getCenterXCoordinate](class_cluster.html#a6270a1d441c42a32edfffc128fdf2172) ()  
| Returns the current x-coordinate position in the Logical workspace for this cluster. [More...](class_cluster.html#a6270a1d441c42a32edfffc128fdf2172)  
  
double | [getCenterYCoordinate](class_cluster.html#a06c4f6eb81299b1da110ffdeeb4dcbd7) ()  
| Returns the current y-coordinate position in the Logical workspace for this cluster. [More...](class_cluster.html#a06c4f6eb81299b1da110ffdeeb4dcbd7)  
  
bool | [moveToLocationCentered](class_cluster.html#aeef740d59387105a4e2a1569685841ec) (int, int)  
| Moves this cluster to the specified location for its center in Logical workspace. [More...](class_cluster.html#aeef740d59387105a4e2a1569685841ec)  
  
bool | [moveToLocation](class_cluster.html#af47907a11a56df1ef500c27fc41ced15) (int, int)  
| Moves this cluster to the specified location in Logical workspace. [More...](class_cluster.html#af47907a11a56df1ef500c27fc41ced15)  
  
void | [setIconPath](class_cluster.html#a89a02d3889bc37fe7bd4d7d69723d7c2) (QString)  
| Sets the icon to use for the cluster. [More...](class_cluster.html#a89a02d3889bc37fe7bd4d7d69723d7c2)  
  
QString | [getIconPath](class_cluster.html#a0e1906d0ced2ca97e3a6e7326cd20716) ()  
| Returns the path to the image to use for the cluster icon. [More...](class_cluster.html#a0e1906d0ced2ca97e3a6e7326cd20716)  
  
  
## Detailed Description
    
    
    \brief Clusters used to group clusters inside logical workspace
    

## Member Function Documentation

## ◆ getCenterXCoordinate()

double Cluster::getCenterXCoordinate  | ( | | ) |   
---|---|---|---|---  
  
Returns the current x-coordinate position in the Logical workspace for this cluster. 

Returns
    double, the current x-coordinate. 

## ◆ getCenterYCoordinate()

double Cluster::getCenterYCoordinate  | ( | | ) |   
---|---|---|---|---  
  
Returns the current y-coordinate position in the Logical workspace for this cluster. 

Returns
    double, the current y-coordinate. 

## ◆ getChildClusterAt()

[Cluster](class_cluster.html) Cluster::getChildClusterAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns child cluster object at a given index. 

Parameters
     index,the| index of child cluster to return.  
---|---  
  
Returns
    [Cluster](class_cluster.html), value is the child cluster at the given index. Range(0, getContainerCount()-1) 

## ◆ getChildClusterCount()

int Cluster::getChildClusterCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of child cluster objects. 

Returns
    int, the number of child clusters inside the cluster. 

## ◆ getIconPath()

QString Cluster::getIconPath  | ( | | ) |   
---|---|---|---|---  
  
Returns the path to the image to use for the cluster icon. 

Returns
    QString, the cluster image icon path. 

## ◆ getId()

QString Cluster::getId  | ( | | ) |   
---|---|---|---|---  
  
Returns cluster ID. 

Returns
    QString, value is the ID of the cluster. 

## ◆ getName()

QString Cluster::getName  | ( | | ) |   
---|---|---|---|---  
  
Returns cluster name. 

Returns
    QString, value is the cluster name. 

## ◆ getParentCluster()

[Cluster](class_cluster.html) Cluster::getParentCluster  | ( | | ) |   
---|---|---|---|---  
  
Returns parent cluster object. 

Returns
    [Cluster](class_cluster.html), value is the parent of the cluster. 

## ◆ getXCoordinate()

double Cluster::getXCoordinate  | ( | | ) |   
---|---|---|---|---  
  
Returns the current x-coordinate position in the Logical workspace for this cluster. 

Returns
    double, the current x-coordinate. 

## ◆ getYCoordinate()

double Cluster::getYCoordinate  | ( | | ) |   
---|---|---|---|---  
  
Returns the current y-coordinate position in the Logical workspace for this cluster. 

Returns
    double, the current y-coordinate. 

## ◆ idChanged()

void Cluster::idChanged  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Generated when cluster ID changes to a new one. 

  * newId, the new ID of the cluster. 
  * , oldId, the new ID of the cluster.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ moveToLocation()

bool Cluster::moveToLocation  | ( | int  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Moves this cluster to the specified location in Logical workspace. 

Parameters
     x,the| new x-coordinate position.   
---|---  
y,the| new y-coordinate position.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ moveToLocationCentered()

bool Cluster::moveToLocationCentered  | ( | int  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Moves this cluster to the specified location for its center in Logical workspace. 

Parameters
     x,the| new x-coordinate position.   
---|---  
y,the| new y-coordinate position.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ nameChanged()

void Cluster::nameChanged  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Generated when cluster name changes to a new one. 

  * newName, the name the cluster was given. 
  * oldName, the name the cluster had before it was given the new name.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ setIconPath()

void Cluster::setIconPath  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Sets the icon to use for the cluster. 

Parameters
     str,path| to the image to use for the cluster icon.   
---|---  
  
## ◆ setName()

void Cluster::setName  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Allows to change cluster name to newName. 

Parameters
     newName,name| to use.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [Cluster.pki](_cluster_8pki.html)


