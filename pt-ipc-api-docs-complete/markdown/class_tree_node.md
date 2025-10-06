# Cisco Packet Tracer Extensions API: TreeNode Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_tree_node.html

---

[TreeNode](class_tree_node.html "TreeNode handles and manipulates the activity assessment nodes.") handles and manipulates the activity assessment nodes. [More...](class_tree_node.html#details)

##  Public Member Functions  
  
---  
QString | [getNodeId](class_tree_node.html#ae4b91d3e1ea926dcb132604b7807ad2d) ()  
| Returns the ID of this node. [More...](class_tree_node.html#ae4b91d3e1ea926dcb132604b7807ad2d)  
  
QString | [getNodeName](class_tree_node.html#a8b9c959f94414413cdc5037b33dc70b2) ()  
| Returns the name of this node. [More...](class_tree_node.html#a8b9c959f94414413cdc5037b33dc70b2)  
  
QString | [getNodeValue](class_tree_node.html#a12227564a5963947728865c579201032) ()  
| Returns the value of this node. [More...](class_tree_node.html#a12227564a5963947728865c579201032)  
  
[TreeNode](class_tree_node.html) | [getParentNode](class_tree_node.html#a3135ffda6ad2df2e376a089852a57c3f) ()  
| Returns the parent node of this node. [More...](class_tree_node.html#a3135ffda6ad2df2e376a089852a57c3f)  
  
int | [getChildCount](class_tree_node.html#a674ddbe7b9e921643f5c1cfc5e661713) ()  
| Returns the number of child nodes for this node. [More...](class_tree_node.html#a674ddbe7b9e921643f5c1cfc5e661713)  
  
ActivityCheckType | [getCheckType](class_tree_node.html#aa918a36a2f889d8d91decc3cb2b18e86) ()  
| Returns the checktype of this node. [More...](class_tree_node.html#aa918a36a2f889d8d91decc3cb2b18e86)  
  
[TreeNode](class_tree_node.html) | [getChildNodeAt](class_tree_node.html#acb8257cd270489c23c27cf2f7a46598b) (int)  
| Returns the child node at the specified index of this node. [More...](class_tree_node.html#acb8257cd270489c23c27cf2f7a46598b)  
  
[TreeNode](class_tree_node.html) | [getChildNodeBy](class_tree_node.html#a33fd820dc28fa6d6fdff6a0ae8e963c7) (QString)  
| Returns the child node with the specified ID of this node. [More...](class_tree_node.html#a33fd820dc28fa6d6fdff6a0ae8e963c7)  
  
[TreeNode](class_tree_node.html) | [getCheckOnlyTree](class_tree_node.html#aa5d84db2289d10a618b59543d2053449) ()  
| Returns a tree with only half or full checktype nodes. [More...](class_tree_node.html#aa5d84db2289d10a618b59543d2053449)  
  
QString | [getIncorrectFeedback](class_tree_node.html#a125f6c2b6e634cfa9e7f28f2b70f752d) ()  
| Returns the incorrect feedback of this node. [More...](class_tree_node.html#a125f6c2b6e634cfa9e7f28f2b70f752d)  
  
void | [setIncorrectFeedback](class_tree_node.html#a4fa5e8b278e943354e8696fcc900af1f) (QString)  
| Sets the incorrect feedback for this node. [More...](class_tree_node.html#a4fa5e8b278e943354e8696fcc900af1f)  
  
int | [getLeafCount](class_tree_node.html#a10d95a784e83edb4e579e8ca6d5525af) ()  
| Returns the total number of leaf nodes for this node. [More...](class_tree_node.html#a10d95a784e83edb4e579e8ca6d5525af)  
  
int | [getCheckLeafCount](class_tree_node.html#aed2b73ed3d627dd5677be7050778eda4) ()  
| Returns the number of full checktype leaf nodes. [More...](class_tree_node.html#aed2b73ed3d627dd5677be7050778eda4)  
  
int | [getTotalLeafPoints](class_tree_node.html#a05b8dc9467e94a1a5b253b41f07a2ef9) ()  
| Returns the total points of leaf nodes. [More...](class_tree_node.html#a05b8dc9467e94a1a5b253b41f07a2ef9)  
  
bool | [isVariableEnabled](class_tree_node.html#a013e0621a2ec72f44abe6e4171c3084b) ()  
| Returns true if this node is variable enabled, otherwise false. [More...](class_tree_node.html#a013e0621a2ec72f44abe6e4171c3084b)  
  
QString | [getVariableName](class_tree_node.html#a46a7273f6e061cbbf43af465d3638a9e) ()  
| Returns the variable name of this node. [More...](class_tree_node.html#a46a7273f6e061cbbf43af465d3638a9e)  
  
QString | [getVariableToString](class_tree_node.html#ac33066a1a2538357442c41ae482a038c) ()  
| Returns the variable name if the value type of the node is entire range, otherwise the value of this node. [More...](class_tree_node.html#ac33066a1a2538357442c41ae482a038c)  
  
void | [setCheck](class_tree_node.html#a2fc16f66481a7abccdac8f130e54e477) (bool)  
| Checks or unchecks this node. [More...](class_tree_node.html#a2fc16f66481a7abccdac8f130e54e477)  
  
ComparatorClass | [getComparatorClass](class_tree_node.html#a5f642ee19fffbd29cb63d3a387f305b7) ()  
| Returns the comparator class. [More...](class_tree_node.html#a5f642ee19fffbd29cb63d3a387f305b7)  
  
void | [setNodeName](class_tree_node.html#ae80201130724e519927680ff6ec539a3) (QString)  
| Sets the node of this node. [More...](class_tree_node.html#ae80201130724e519927680ff6ec539a3)  
  
void | [setNodeValue](class_tree_node.html#a966f0d58e5ae7a7a06cadf19df4cf727) (QString)  
| Sets the value of this node. [More...](class_tree_node.html#a966f0d58e5ae7a7a06cadf19df4cf727)  
  
int | [getLeafCountByComponent](class_tree_node.html#a8b25a26264e20ffeb2a8583ce454646a) (QString)  
| Returns the number of leaves with the specified component name (includes all children). [More...](class_tree_node.html#a8b25a26264e20ffeb2a8583ce454646a)  
  
int | [getCheckLeafCountByComponent](class_tree_node.html#ac0ebb19b4d1992a30ded452c45baf0c0) (QString)  
| Returns the number of checked leaves with the specified component name (including all children). [More...](class_tree_node.html#ac0ebb19b4d1992a30ded452c45baf0c0)  
  
int | [getCheckLeafPointsByComponent](class_tree_node.html#a862c69530be9a9d9b2f99ebfb9e15d39) (QString)  
| Returns the total points of checked leaves with the specified component name (including all children). [More...](class_tree_node.html#a862c69530be9a9d9b2f99ebfb9e15d39)  
  
int | [getTotalLeafPointsByComponent](class_tree_node.html#a4ddf71276eeed61d796b73568c2d7b5d) (QString)  
| Returns the total points of leaves with the specified component name (including all children). [More...](class_tree_node.html#a4ddf71276eeed61d796b73568c2d7b5d)  
  
int | [getCheckLeafPoints](class_tree_node.html#a7d654338816b1616030b169b8d4e13c3) ()  
| Returns the total points of all nodes that have checks, including all children. [More...](class_tree_node.html#a7d654338816b1616030b169b8d4e13c3)  
  
pair< QString, QString > | [getCompPointPair](class_tree_node.html#a9185b1b866b429c38d63ed0a90b7fce5) ()  
| Returns the component and points as a pair associated with only this node. There can be many components and points per node. [More...](class_tree_node.html#a9185b1b866b429c38d63ed0a90b7fce5)  
  
void | [checkChanged](class_tree_node.html#a14e4ff4b4121b305bfc44294d75e31ac) (QString, QString, int)  
| This event is emitted when the checktype of a node changes. [More...](class_tree_node.html#a14e4ff4b4121b305bfc44294d75e31ac)  
  
[TreeNode](class_tree_node.html) | [getChildNodeByFullId](class_tree_node.html#a8e27c2168f5eb34737ce1a7cfeeac9ca) (QString)  
| Returns the child node with the specified full ID of this node. [More...](class_tree_node.html#a8e27c2168f5eb34737ce1a7cfeeac9ca)  
  
[TreeNode](class_tree_node.html) | [addChildNode](class_tree_node.html#a83adf484c54b578e91553dd47b17ec05) (ComparatorClass, QString, QString, QString, bool)  
| Create a new child node and add it to the tree. [More...](class_tree_node.html#a83adf484c54b578e91553dd47b17ec05)  
  
  
## Detailed Description

[TreeNode](class_tree_node.html "TreeNode handles and manipulates the activity assessment nodes.") handles and manipulates the activity assessment nodes. 

## Member Function Documentation

## ◆ addChildNode()

[TreeNode](class_tree_node.html) TreeNode::addChildNode  | ( | ComparatorClass  | ,   
---|---|---|---  
|  | QString  | ,   
|  | QString  | ,   
|  | QString  | ,   
|  | bool  |   
| ) | |   
  
Create a new child node and add it to the tree. 

Parameters
     classType,enum<ComparatorClass>| eCompClass_Ip = 0, eCompClass_Routing = 1, eCompClass_Acl = 2, eCompClass_Nat = 3, eCompClass_Physical = 4, eCompClass_Switching = 5, eCompClass_Connectivity = 6, eCompClass_Logical = 7, eCompClass_All = 8, eCompClass_Encircling_Head = 9, eCompClass_Encircling_Sub = 10  
---|---  
nodeName,the| name of the node.  
nodeId,the| id of the node.  
nodeValue,the| value of the node.  
bVariableEnabled,bool-true| if variable is enabled and false if it's not on this node  
  
Returns
    [TreeNode](class_tree_node.html "TreeNode handles and manipulates the activity assessment nodes."), the child node that was newly created 

## ◆ checkChanged()

void TreeNode::checkChanged  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | int  |   
| ) | |   
  
This event is emitted when the checktype of a node changes. 

  * nodeName, the name of the node. 
  * nodePath, the path of the node. 
  * checkType, the checktype of the node.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ getCheckLeafCount()

int TreeNode::getCheckLeafCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of full checktype leaf nodes. 

Returns
    int, the number of full checktype leaf nodes. 

## ◆ getCheckLeafCountByComponent()

int TreeNode::getCheckLeafCountByComponent  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the number of checked leaves with the specified component name (including all children). 

Parameters
     component,the| name of the component of interest.  
---|---  
  
Returns
    int, the number of checked leaves with the specified component name (including all children). 

## ◆ getCheckLeafPoints()

int TreeNode::getCheckLeafPoints  | ( | | ) |   
---|---|---|---|---  
  
Returns the total points of all nodes that have checks, including all children. 

Returns
    int, the total points of all nodes that have checks, including all children. 

## ◆ getCheckLeafPointsByComponent()

int TreeNode::getCheckLeafPointsByComponent  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the total points of checked leaves with the specified component name (including all children). 

Parameters
     component,the| name of the component of interest.  
---|---  
  
Returns
    int, the total points of checked leaves with the specified component name (including all children). 

## ◆ getCheckOnlyTree()

[TreeNode](class_tree_node.html) TreeNode::getCheckOnlyTree  | ( | | ) |   
---|---|---|---|---  
  
Returns a tree with only half or full checktype nodes. 

Returns
    [TreeNode](class_tree_node.html "TreeNode handles and manipulates the activity assessment nodes."), the [TreeNode](class_tree_node.html "TreeNode handles and manipulates the activity assessment nodes.") object with only half or full checktype nodes. 

## ◆ getCheckType()

ActivityCheckType TreeNode::getCheckType  | ( | | ) |   
---|---|---|---|---  
  
Returns the checktype of this node. 

Returns
    int, the checktype for this node. Checktypes: eCheckTypeBlank = 0, eCheckTypeHalf = 1, eCheckTypeFull = 2

Remarks
    Full is correct, blank is incorrect, and half means there are correct and incorrect children. 

## ◆ getChildCount()

int TreeNode::getChildCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of child nodes for this node. 

Returns
    int, the number of child nodes for this node. 

## ◆ getChildNodeAt()

[TreeNode](class_tree_node.html) TreeNode::getChildNodeAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Returns the child node at the specified index of this node. 

Parameters
     index,the| index of the child node of interest.  
---|---  
  
Returns
    [TreeNode](class_tree_node.html "TreeNode handles and manipulates the activity assessment nodes."), the child node at the specified index of this node. 

## ◆ getChildNodeBy()

[TreeNode](class_tree_node.html) TreeNode::getChildNodeBy  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the child node with the specified ID of this node. 

Parameters
     ID,the| ID of the child node of interest.  
---|---  
  
Returns
    [TreeNode](class_tree_node.html "TreeNode handles and manipulates the activity assessment nodes."), the child node with the specified ID of this node. 

## ◆ getChildNodeByFullId()

[TreeNode](class_tree_node.html) TreeNode::getChildNodeByFullId  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the child node with the specified full ID of this node. 

Parameters
     ID,the| full ID of the child node of interest.  
---|---  
  
Returns
    [TreeNode](class_tree_node.html "TreeNode handles and manipulates the activity assessment nodes."), the child node with the specified full ID of this node. 

## ◆ getComparatorClass()

ComparatorClass TreeNode::getComparatorClass  | ( | | ) |   
---|---|---|---|---  
  
Returns the comparator class. 

Returns
    enum<ComparatorClass>, the comparator class. eCompClass_Ip = 0, eCompClass_Routing = 1, eCompClass_Acl = 2, eCompClass_Nat = 3, eCompClass_Physical = 4, eCompClass_Switching = 5, eCompClass_Connectivity = 6, eCompClass_Logical = 7, eCompClass_All = 8, eCompClass_Encircling_Head = 9, eCompClass_Encircling_Sub = 10 

## ◆ getCompPointPair()

pair< QString, QString > TreeNode::getCompPointPair  | ( | | ) |   
---|---|---|---|---  
  
Returns the component and points as a pair associated with only this node. There can be many components and points per node. 

Returns
    pair<QString, QString>, the list of comma-separated components and list of comma-separated points. 

## ◆ getIncorrectFeedback()

QString TreeNode::getIncorrectFeedback  | ( | | ) |   
---|---|---|---|---  
  
Returns the incorrect feedback of this node. 

Returns
    QString, the incorrect feedback of this node. 

## ◆ getLeafCount()

int TreeNode::getLeafCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the total number of leaf nodes for this node. 

Returns
    int, the total number of leaf nodes for this node. 

## ◆ getLeafCountByComponent()

int TreeNode::getLeafCountByComponent  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the number of leaves with the specified component name (includes all children). 

Parameters
     component,the| name of the component of interest.  
---|---  
  
Returns
    int, the number of leaves with the specified component name (includes all children). 

## ◆ getNodeId()

QString TreeNode::getNodeId  | ( | | ) |   
---|---|---|---|---  
  
Returns the ID of this node. 

Returns
    QString, the ID of this node. 

## ◆ getNodeName()

QString TreeNode::getNodeName  | ( | | ) |   
---|---|---|---|---  
  
Returns the name of this node. 

Returns
    QString, the name of this node. 

## ◆ getNodeValue()

QString TreeNode::getNodeValue  | ( | | ) |   
---|---|---|---|---  
  
Returns the value of this node. 

Returns
    QString, the value of this node. 

## ◆ getParentNode()

[TreeNode](class_tree_node.html) TreeNode::getParentNode  | ( | | ) |   
---|---|---|---|---  
  
Returns the parent node of this node. 

Returns
    [TreeNode](class_tree_node.html "TreeNode handles and manipulates the activity assessment nodes."), the [TreeNode](class_tree_node.html "TreeNode handles and manipulates the activity assessment nodes.") object of the parent node of this node. 

## ◆ getTotalLeafPoints()

int TreeNode::getTotalLeafPoints  | ( | | ) |   
---|---|---|---|---  
  
Returns the total points of leaf nodes. 

Returns
    int, the total points of leaf nodes. 

## ◆ getTotalLeafPointsByComponent()

int TreeNode::getTotalLeafPointsByComponent  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the total points of leaves with the specified component name (including all children). 

Parameters
     component,the| name of the component of interest.  
---|---  
  
Returns
    int, the total points of leaves with the specified component name (including all children). 

## ◆ getVariableName()

QString TreeNode::getVariableName  | ( | | ) |   
---|---|---|---|---  
  
Returns the variable name of this node. 

Returns
    QString, the variable name of this node. 

## ◆ getVariableToString()

QString TreeNode::getVariableToString  | ( | | ) |   
---|---|---|---|---  
  
Returns the variable name if the value type of the node is entire range, otherwise the value of this node. 

Returns
    QString, the variable name if the value type of the node is entire range, otherwise the value of this node. 

## ◆ isVariableEnabled()

bool TreeNode::isVariableEnabled  | ( | | ) |   
---|---|---|---|---  
  
Returns true if this node is variable enabled, otherwise false. 

Returns
    bool, true if this node is variable enabled, otherwise false. 

## ◆ setCheck()

void TreeNode::setCheck  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Checks or unchecks this node. 

Parameters
     bCheck,true| to check this node, false to uncheck it.   
---|---  
  
## ◆ setIncorrectFeedback()

void TreeNode::setIncorrectFeedback  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Sets the incorrect feedback for this node. 

Parameters
     feedbackStr,the| incorrect feedback for this node.   
---|---  
  
## ◆ setNodeName()

void TreeNode::setNodeName  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Sets the node of this node. 

Parameters
     name,the| node of this node.   
---|---  
  
## ◆ setNodeValue()

void TreeNode::setNodeValue  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Sets the value of this node. 

Parameters
     value,the| value of this node.   
---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [CTreeNode.pki](_c_tree_node_8pki.html)


