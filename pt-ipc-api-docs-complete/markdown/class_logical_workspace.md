# Cisco Packet Tracer Extensions API: LogicalWorkspace Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_logical_workspace.html

---

[LogicalWorkspace](class_logical_workspace.html "LogicalWorkspace is a graphics view. Network design using logical topology icons happens in this spac...") is a graphics view. [Network](class_network.html "Network is the entry point for all device configurations in the network. It retrieves devices.") design using logical topology icons happens in this space. [More...](class_logical_workspace.html#details)

##  Public Member Functions  
  
---  
int | [getState](class_logical_workspace.html#afc8d7a99e43e9401437eb1ee5152e712) ()  
| Returns the state of the Logical workspace. [More...](class_logical_workspace.html#afc8d7a99e43e9401437eb1ee5152e712)  
  
vector< uuid > | [getCanvasItemIds](class_logical_workspace.html#af60c7cdc5dca3a6a843b120ccd1c2a05) () const  
| Returns the list of UUIDs of items on the Logical workspace. [More...](class_logical_workspace.html#af60c7cdc5dca3a6a843b120ccd1c2a05)  
  
vector< uuid > | [getCanvasNoteIds](class_logical_workspace.html#a37e5980d7895167a88361d8662c4e49d) () const  
| Returns the list of UUIDs of note items on the Logical workspace. [More...](class_logical_workspace.html#a37e5980d7895167a88361d8662c4e49d)  
  
vector< uuid > | [getCanvasRectIds](class_logical_workspace.html#a0c420a2bab071803cb7afc6f09c6a86e) () const  
| Returns the list of UUIDs of rectangle items on the Logical workspace. [More...](class_logical_workspace.html#a0c420a2bab071803cb7afc6f09c6a86e)  
  
vector< uuid > | [getCanvasEllipseIds](class_logical_workspace.html#ae55278ed2f6f51e0bb1440a00abf2d67) () const  
| Returns the list of UUIDs of ellipse items on the Logical workspace. [More...](class_logical_workspace.html#ae55278ed2f6f51e0bb1440a00abf2d67)  
  
vector< uuid > | [getCanvasLineIds](class_logical_workspace.html#a15d62dd5cb032d45396c22e32ef4f9a0) () const  
| Returns the list of UUIDs of line items on the Logical workspace. [More...](class_logical_workspace.html#a15d62dd5cb032d45396c22e32ef4f9a0)  
  
vector< uuid > | [getCanvasPolygonIds](class_logical_workspace.html#ad6b20ebf823c4562ba23a649bc4e9d18) () const  
| Returns the list of UUIDs of polygon items on the Logical workspace. [More...](class_logical_workspace.html#ad6b20ebf823c4562ba23a649bc4e9d18)  
  
vector< string > | [getRectItemData](class_logical_workspace.html#a57baa9505627f39a44fbedb5c44c9d09) (uuid) const  
| Returns a vector of data for a rectangle workspace item. [More...](class_logical_workspace.html#a57baa9505627f39a44fbedb5c44c9d09)  
  
vector< string > | [getEllipseItemData](class_logical_workspace.html#a3abcf7eb4208af8711461e229f229ce1) (uuid) const  
| Returns a vector of data for a ellipse workspace item. [More...](class_logical_workspace.html#a3abcf7eb4208af8711461e229f229ce1)  
  
vector< string > | [getLineItemData](class_logical_workspace.html#ae1b87162c7fdbfdf13ddeed3ce01be58) (uuid) const  
| Returns a vector of data for a line workspace item. [More...](class_logical_workspace.html#ae1b87162c7fdbfdf13ddeed3ce01be58)  
  
vector< string > | [getPolygonItemData](class_logical_workspace.html#a0b384013d5f3621a78cb6de9c6e7210d) (uuid) const  
| Returns a vector of data for a polygon workspace item. [More...](class_logical_workspace.html#a0b384013d5f3621a78cb6de9c6e7210d)  
  
int | [getCanvasItemX](class_logical_workspace.html#a2ef02e3c3636dbda914af15931023ad4) (uuid) const  
| Returns the x-coordinate of the Logical workspace item with the specified UUID. [More...](class_logical_workspace.html#a2ef02e3c3636dbda914af15931023ad4)  
  
int | [getCanvasItemY](class_logical_workspace.html#a7b7658e1e9fa616c637c7f9172cdc073) (uuid) const  
| Returns the y-coordinate of the Logical workspace item with the specified UUID. [More...](class_logical_workspace.html#a7b7658e1e9fa616c637c7f9172cdc073)  
  
int | [getCanvasItemRealX](class_logical_workspace.html#a944baf991dedcdbe35d92985f3a64532) (uuid) const  
| Returns the real x-coordinate of the Logical workspace item with the specified UUID. [More...](class_logical_workspace.html#a944baf991dedcdbe35d92985f3a64532)  
  
int | [getCanvasItemRealY](class_logical_workspace.html#a0da5324f3a805a0b7acf138578c5ad1b) (uuid) const  
| Returns the real y-coordinate of the Logical workspace item with the specified UUID. [More...](class_logical_workspace.html#a0da5324f3a805a0b7acf138578c5ad1b)  
  
void | [setCanvasItemRealPos](class_logical_workspace.html#a388f7776a98bb02278c6c9b8f95ffa7b) (uuid, int, int)  
| Sets the x-coordinate of the Logical workspace item with the specified UUID. [More...](class_logical_workspace.html#a388f7776a98bb02278c6c9b8f95ffa7b)  
  
void | [setCanvasItemX](class_logical_workspace.html#a160b46f786f6ea544961286b8823d9d8) (uuid, int)  
| Sets the x-coordinate of the Logical workspace item with the specified UUID. [More...](class_logical_workspace.html#a160b46f786f6ea544961286b8823d9d8)  
  
void | [setCanvasItemY](class_logical_workspace.html#a8401985598f8605f108b3fb416a3d894) (uuid, int)  
| Sets the y-coordinate of the Logical workspace item with the specified UUID. [More...](class_logical_workspace.html#a8401985598f8605f108b3fb416a3d894)  
  
void | [moveCanvasItemBy](class_logical_workspace.html#a338e99fecab812efc5f447ccd8ba71ca) (uuid, int, int)  
| Moves the Logical workspace item with the specified UUID by the specified increments. [More...](class_logical_workspace.html#a338e99fecab812efc5f447ccd8ba71ca)  
  
int | [getComponentItemsCount](class_logical_workspace.html#aa4706791cea29aa264dd91ee184c9244) ()  
| Returns the number of component items on the Logical workspace. [More...](class_logical_workspace.html#aa4706791cea29aa264dd91ee184c9244)  
  
[ComponentItem](class_component_item.html) | [getComponentItem](class_logical_workspace.html#a7a05e1ce39cb7d4681787d68c8a07239) (QString)  
| Returns the component item with the specified device name. [More...](class_logical_workspace.html#a7a05e1ce39cb7d4681787d68c8a07239)  
  
int | [getComponentChildCountFor](class_logical_workspace.html#a6c6eb377ff9a08876cbd1e4c4afc031c) (QString)  
[ComponentItem](class_component_item.html) | [getComponentChildForAt](class_logical_workspace.html#a138c24ebdda2d47d8ff4a87642d44139) (QString, int)  
[ComponentItem](class_component_item.html) | [getComponentChildForByName](class_logical_workspace.html#a829a788338ac614c50882df2cf04ae9c) (QString, QString)  
QString | [addDevice](class_logical_workspace.html#a07fb6a8d55ba95cb26461aff5437f2db) (DeviceType, string, double, double)  
| Adds a device to the Logical workspace. [More...](class_logical_workspace.html#a07fb6a8d55ba95cb26461aff5437f2db)  
  
bool | [removeDevice](class_logical_workspace.html#a4e713fb7448c7106f1357241f61d0cae) (QString)  
| Removes the specified device from the Logical workspace and network. [More...](class_logical_workspace.html#a4e713fb7448c7106f1357241f61d0cae)  
  
void | [deviceAdded](class_logical_workspace.html#add4e97de878fd91350d4f2c698cc6bf6) (QString, string, uuid)  
| This event is emitted when a device is added to the Logical workspace. [More...](class_logical_workspace.html#add4e97de878fd91350d4f2c698cc6bf6)  
  
void | [deviceRemoved](class_logical_workspace.html#a0bdbce1bf7d503d9731feffcf1a64bfd) (QString, uuid)  
| This event is emitted when a device is removed from the Logical workspace. [More...](class_logical_workspace.html#a0bdbce1bf7d503d9731feffcf1a64bfd)  
  
void | [deviceRemoving](class_logical_workspace.html#a5d9458ae0f5b33d684592401e0c6d5b9) (QString, uuid)  
| This event is emitted when a device is about to be removed from the Logical workspace. [More...](class_logical_workspace.html#a5d9458ae0f5b33d684592401e0c6d5b9)  
  
void | [canvasNoteTextChanged](class_logical_workspace.html#a5ddaf53231d0c52113560f492eed5c16) (uuid, QString)  
| This event is emitted when a canvas item note has it's text changed. [More...](class_logical_workspace.html#a5ddaf53231d0c52113560f492eed5c16)  
  
void | [canvasNoteRemoved](class_logical_workspace.html#a4fafdc25a4b7da921c68f0d15de8339d) (uuid)  
| This event is emitted when a canvas item note is removed from the Logical workspace. [More...](class_logical_workspace.html#a4fafdc25a4b7da921c68f0d15de8339d)  
  
void | [canvasNoteAdded](class_logical_workspace.html#af6c34b3277de7cb34ad03a6f4b99569d) (uuid)  
| This event is emitted when a canvas item note is added to the Logical workspace. [More...](class_logical_workspace.html#af6c34b3277de7cb34ad03a6f4b99569d)  
  
QString | [addRemoteNetwork](class_logical_workspace.html#a39a445c327887d6f7e836c43fad9d826) ()  
| Adds a Multiuser remote network to the Logical workspace. [More...](class_logical_workspace.html#a39a445c327887d6f7e836c43fad9d826)  
  
bool | [removeRemoteNetwork](class_logical_workspace.html#a7fccec2051f030ca7256cbc9b76f26b9) (QString)  
| Removes the Multiuser remote network with the specified name from the Logical workspace. [More...](class_logical_workspace.html#a7fccec2051f030ca7256cbc9b76f26b9)  
  
void | [remoteNetworkAdded](class_logical_workspace.html#a79ba5a84b4bc04e10cb3f2ad62558d9e) (QString)  
| This event is emitted when a Multiuser remote network is added to the Logical workspace. [More...](class_logical_workspace.html#a79ba5a84b4bc04e10cb3f2ad62558d9e)  
  
void | [remoteNetworkRemoved](class_logical_workspace.html#a6c4084527eff1c2a2cd0409fedba787d) (QString)  
| This event is emitted when a Multiuser remote network is removed from the Logical workspace. [More...](class_logical_workspace.html#a6c4084527eff1c2a2cd0409fedba787d)  
  
bool | [moveRemoteNetwork](class_logical_workspace.html#a6fe2fb57d263a44e10ed0af467ecbc04) (QString, int, int)  
| Moves the Multiuser remote network to the specified location. [More...](class_logical_workspace.html#a6fe2fb57d263a44e10ed0af467ecbc04)  
  
bool | [createLink](class_logical_workspace.html#a13ce86a62e19fa3b0f991bb589e2157d) (QString, string, QString, string, CONNECT_TYPES)  
| Creates a link from one device's port to another device's port. [More...](class_logical_workspace.html#a13ce86a62e19fa3b0f991bb589e2157d)  
  
void | [linkStarted](class_logical_workspace.html#a05736a2d3d82d684e9879c4c3fda393e) (QString, string, CONNECT_TYPES)  
| This event is emitted when a link starts (i.e. user connects the first end of a link) [More...](class_logical_workspace.html#a05736a2d3d82d684e9879c4c3fda393e)  
  
void | [linkCreated](class_logical_workspace.html#a5ffd46a33dc4eb35b9fe90ea0db98b11) (QString, string, QString, string, CONNECT_TYPES)  
| This event is emitted when a link has been created. [More...](class_logical_workspace.html#a5ffd46a33dc4eb35b9fe90ea0db98b11)  
  
void | [linkDeleted](class_logical_workspace.html#a915af4644afe47628859d87c12d2bec5) (QString, string, QString, string, CONNECT_TYPES)  
| This event is emitted when a link has been deleted. [More...](class_logical_workspace.html#a915af4644afe47628859d87c12d2bec5)  
  
bool | [deleteLink](class_logical_workspace.html#a5786e95bfc6287fa1aca1df36061986a) (QString, string)  
| Deletes a link from the device connected to the specified port. [More...](class_logical_workspace.html#a5786e95bfc6287fa1aca1df36061986a)  
  
bool | [clearLayer](class_logical_workspace.html#afd2e8ea0e1df8d2261d35224588dd88d) (double)  
| Clears the specified layer. [More...](class_logical_workspace.html#afd2e8ea0e1df8d2261d35224588dd88d)  
  
uuid | [drawLine](class_logical_workspace.html#a38fc8bd4f3ff993779a375b8e0c3bb6e) (int, int, int, int, double, int, int, int, int)  
| Draws a line on the Logical workspace. [More...](class_logical_workspace.html#a38fc8bd4f3ff993779a375b8e0c3bb6e)  
  
uuid | [drawCircle](class_logical_workspace.html#a4e54cb6121f307caec41628bfddf36f1) (int, int, double, int, int, int, int)  
| Draws a circle on the Logical workspace. [More...](class_logical_workspace.html#a4e54cb6121f307caec41628bfddf36f1)  
  
uuid | [addNote](class_logical_workspace.html#a72ef01582d9814ddbd86ff724f7fc013) (int, int, double, QString)  
| Adds a note on the Logical workspace. [More...](class_logical_workspace.html#a72ef01582d9814ddbd86ff724f7fc013)  
  
QString | [getCanvasNoteText](class_logical_workspace.html#abcb3c5d695b3f46adc1b579ee7d270f8) (uuid)  
| Gets text from a note on the Logical workspace. [More...](class_logical_workspace.html#abcb3c5d695b3f46adc1b579ee7d270f8)  
  
double | [getIncNoteZOrder](class_logical_workspace.html#abdbefd354b5bf6c34c659eeaeaaa6bd9) ()  
| Gets and increments the current z order to use for a new note. [More...](class_logical_workspace.html#abdbefd354b5bf6c34c659eeaeaaa6bd9)  
  
int | [getMUItemCount](class_logical_workspace.html#a319e12d23ef431e70cbe8d78654bc317) ()  
| Gets how many multiuser items there are, if any. [More...](class_logical_workspace.html#a319e12d23ef431e70cbe8d78654bc317)  
  
bool | [changeNoteText](class_logical_workspace.html#a31eac8b218f1b5420215037a067f21ae) (uuid, QString)  
| Changes text in a note on the logical workspace. [More...](class_logical_workspace.html#a31eac8b218f1b5420215037a067f21ae)  
  
bool | [removeCanvasItem](class_logical_workspace.html#a8491ca9d2e864b2e4d3710416c3ca8af) (uuid)  
| Removes the specified item from the Logical workspace. [More...](class_logical_workspace.html#a8491ca9d2e864b2e4d3710416c3ca8af)  
  
double | [getUnusedLayer](class_logical_workspace.html#a9ca108b8edde044ba0dd632ff3b42284) ()  
| Returns the unused layer. [More...](class_logical_workspace.html#a9ca108b8edde044ba0dd632ff3b42284)  
  
bool | [isLayerUsed](class_logical_workspace.html#a9236ddcd995b2554d507f2b31c138779) (double)  
| Returns true if the specified layer is used, otherwise false. [More...](class_logical_workspace.html#a9236ddcd995b2554d507f2b31c138779)  
  
double | [getLayerInbetweenComponents](class_logical_workspace.html#a461c772a3ccadcc7115dd74873790351) (QString, QString)  
| Returns the layer between the specified devices. [More...](class_logical_workspace.html#a461c772a3ccadcc7115dd74873790351)  
  
vector< byte > | [getWorkspaceImage](class_logical_workspace.html#a3f8b28ae2482f8c351b21ba51f96347b) (QString)  
| Returns the series of bytes of the Logical workspace image. [More...](class_logical_workspace.html#a3f8b28ae2482f8c351b21ba51f96347b)  
  
uuid | [addTextPopup](class_logical_workspace.html#ae04444785fbaa65914139d08d5f3d382) (int, int, double, int, QString)  
| Adds a text popup to the Logical workspace. [More...](class_logical_workspace.html#ae04444785fbaa65914139d08d5f3d382)  
  
bool | [removeTextPopup](class_logical_workspace.html#a75f6c398d26ba12e6369fa04305234a5) (uuid)  
| Removes the specified text popup from the Logical workspace. [More...](class_logical_workspace.html#a75f6c398d26ba12e6369fa04305234a5)  
  
void | [showClusterContents](class_logical_workspace.html#a544413ae4107ff109819b049853d929f) (QString)  
| Shows the content of the specified cluster. [More...](class_logical_workspace.html#a544413ae4107ff109819b049853d929f)  
  
void | [showClusterContents](class_logical_workspace.html#a544413ae4107ff109819b049853d929f) (QString)  
| Triggered when a cluster contents are shown. [More...](class_logical_workspace.html#a544413ae4107ff109819b049853d929f)  
  
void | [addCluster](class_logical_workspace.html#ab004609448e596c6b78345f5ddcb5054) ()  
| Creates new cluster object with the currently selected objects. [More...](class_logical_workspace.html#ab004609448e596c6b78345f5ddcb5054)  
  
void | [removeCluster](class_logical_workspace.html#aa216ed23b5edcaff6ae17a8dd91380c9) (QString, bool)  
| Removes csluter object with given id. [More...](class_logical_workspace.html#aa216ed23b5edcaff6ae17a8dd91380c9)  
  
void | [unCluster](class_logical_workspace.html#a43586cdf803480f555dce153521b8b36) (QString)  
| Unclusters cluster with the given clusterId. [More...](class_logical_workspace.html#a43586cdf803480f555dce153521b8b36)  
  
void | [clusterAdded](class_logical_workspace.html#a4c9e2c26d90b14128d8aecb7cde3bc98) (QString)  
| This event is emitted when a cluster object is added. [More...](class_logical_workspace.html#a4c9e2c26d90b14128d8aecb7cde3bc98)  
  
void | [clusterRemoved](class_logical_workspace.html#a1c297f4667c222271eba1ddfc4bb52df) (QString)  
| This event is emitted when a cluster is removed from the Logical workspace. [More...](class_logical_workspace.html#a1c297f4667c222271eba1ddfc4bb52df)  
  
[Cluster](class_cluster.html) | [getRootCluster](class_logical_workspace.html#aaa06b85916ec8685b99163b599f5debe) ()  
| Returns root cluster. [More...](class_logical_workspace.html#aaa06b85916ec8685b99163b599f5debe)  
  
[Cluster](class_cluster.html) | [getCurrentCluster](class_logical_workspace.html#a10d8a3620f0e60a29fb719d18aa469ed) ()  
| Returns root cluster. [More...](class_logical_workspace.html#a10d8a3620f0e60a29fb719d18aa469ed)  
  
[Cluster](class_cluster.html) | [getCluster](class_logical_workspace.html#a8c595c4006e830d28136a8edc5c87671) (QString)  
| Returns cluster object for a given cluster id. [More...](class_logical_workspace.html#a8c595c4006e830d28136a8edc5c87671)  
  
uuid | [getClusterItemId](class_logical_workspace.html#a83f8e600813bb9eae35b2e77eeb7af48) (QString)  
| Returns uuid for the item associated with this cluster object. [More...](class_logical_workspace.html#a83f8e600813bb9eae35b2e77eeb7af48)  
  
[Cluster](class_cluster.html) | [getClusterFromItem](class_logical_workspace.html#aeba0cb4142660959bfa3b3b21b4621b9) (uuid)  
| Returns cluster object assosiatete with a given cluster item. [More...](class_logical_workspace.html#aeba0cb4142660959bfa3b3b21b4621b9)  
  
[Cluster](class_cluster.html) | [getClusterForItem](class_logical_workspace.html#a6531d89ffb6ad11d0bd5c945024a97ad) (uuid)  
| Returns cluster object this item belongs to. [More...](class_logical_workspace.html#a6531d89ffb6ad11d0bd5c945024a97ad)  
  
QString | [getClusterIdForItem](class_logical_workspace.html#a17b0c8b6f4a8dd650d9eb2f3448a2678) (uuid)  
| Returns cluster id for a given workspace item. [More...](class_logical_workspace.html#a17b0c8b6f4a8dd650d9eb2f3448a2678)  
  
void | [moveItemToCluster](class_logical_workspace.html#adaa452d96039e5f5d85004166ab66629) (uuid, QString)  
| Moves item from current cluster to a cluster with given clusterId. [More...](class_logical_workspace.html#adaa452d96039e5f5d85004166ab66629)  
  
void | [autoConnectDevices](class_logical_workspace.html#a66704744bd38cb47d4e63ba8311837a0) (QString, QString)  
| Auto connect function, connect the given devices with a default cable at default ports, if possible. [More...](class_logical_workspace.html#a66704744bd38cb47d4e63ba8311837a0)  
  
void | [clusterForItemChanged](class_logical_workspace.html#a62dbe3895725509e50619981ca9359c6) (uuid, QString, QString)  
| Sent when an item is moved from one cluster to another, etc. [More...](class_logical_workspace.html#a62dbe3895725509e50619981ca9359c6)  
  
void | [onNoAutoConnectError](class_logical_workspace.html#aa5836e8c386a01e275e12357869f39ed) (QString, QString)  
| Sent when autoconnect occures and there isn't an error. [More...](class_logical_workspace.html#aa5836e8c386a01e275e12357869f39ed)  
  
void | [setDeviceCustomImage](class_logical_workspace.html#a9db7a30273b321abbba239aa5f9f90f0) (QString, QString)  
| Change [Device](class_device.html "Device is the base class for all device objects.") image in logical workspace. [More...](class_logical_workspace.html#a9db7a30273b321abbba239aa5f9f90f0)  
  
void | [centerOn](class_logical_workspace.html#a0296ed45518be9cd1fb826e4597ba25d) (double, double)  
void | [centerOnComponentByName](class_logical_workspace.html#a7940ee225634f2847222c111151a9b5b) (QString)  
int | [getCurrentZoom](class_logical_workspace.html#a7ac9c144ab4779a903391cf248cb0382) ()  
  
## Detailed Description

[LogicalWorkspace](class_logical_workspace.html "LogicalWorkspace is a graphics view. Network design using logical topology icons happens in this spac...") is a graphics view. [Network](class_network.html "Network is the entry point for all device configurations in the network. It retrieves devices.") design using logical topology icons happens in this space. 

## Member Function Documentation

## ◆ addCluster()

void LogicalWorkspace::addCluster  | ( | | ) |   
---|---|---|---|---  
  
Creates new cluster object with the currently selected objects. 

## ◆ addDevice()

QString LogicalWorkspace::addDevice  | ( | DeviceType  | ,   
---|---|---|---  
|  | string  | ,   
|  | double  | ,   
|  | double  |   
| ) | |   
  
Adds a device to the Logical workspace. 

Parameters
     type,the| type of the device. [Device](class_device.html "Device is the base class for all device objects.") types: eRouter = 0, eSwitch = 1, eCloud = 2, eBridge = 3, eHub = 4, eRepeater = 5, eCoAxialSplitter = 6, eAccessPoint = 7, ePc = 8, eServer = 9, ePrinter = 10, eWirelessRouter = 11, eIpPhone = 12, eDslModem = 13, eCableModem = 14, eRemoteNetwork = 15, eMultiLayerSwitch = 16, eLaptop = 17, eTabletPC = 18, ePda = 19, eWirelessEndDevice = 20, eWiredEndDevice = 21, eTV = 22, eHomeVoip = 23, eAnalogPhone = 24, eMultiUser = 25, eASA = 26, eIoE = 27, eHomeGateway = 28, eCellTower = 29, eCentralOfficeServer = 30 eCiscoAccessPoint = 31, eEmbeddedCiscoAccessPoint = 32, eSniffer = 33, eMCU = 34, eSBC = 35, eThing = 36, eMCUComponent = 37, eEmbeddedServer = 38,   
eWirelessLanController = 39, eCluster = 40   
---|---  
model,the| model of the device.   
x,x| coord to add the device at.   
y,y| coord to add the device at.  
  
Returns
    QString, the device name of the device. 

## ◆ addNote()

uuid LogicalWorkspace::addNote  | ( | int  | ,   
---|---|---|---  
|  | int  | ,   
|  | double  | ,   
|  | QString  |   
| ) | |   
  
Adds a note on the Logical workspace. 

Parameters
     x,the| x-coordinate for the note.   
---|---  
y,the| y-coordinate for the note.   
layer,the| layer to add the note on.   
text,the| text for the note.  
  
Returns
    uuid, the UUID of the note. 

## ◆ addRemoteNetwork()

QString LogicalWorkspace::addRemoteNetwork  | ( | | ) |   
---|---|---|---|---  
  
Adds a Multiuser remote network to the Logical workspace. 
    
    
        \brief This event is emitted when action bar button on a android device is pressed, or corresponding button on some other device.
        \arg id, .
    

\NOT APPLICABLE TO DESKTOP.

event: actionBarButtonPressed(QString id) - PrivGetNetwork;

Returns
    QString, the name of the Multiuser remote network. 

## ◆ addTextPopup()

uuid LogicalWorkspace::addTextPopup  | ( | int  | ,   
---|---|---|---  
|  | int  | ,   
|  | double  | ,   
|  | int  | ,   
|  | QString  |   
| ) | |   
  
Adds a text popup to the Logical workspace. 

Parameters
     x,the| x-coordinate for the text popup.   
---|---  
y,the| y-coordinate for the text popup.   
layer,the| layer to add the text popup to.   
width,the| width for the text popup.   
text,the| text for the text popup.  
  
Returns
    uuid, the UUID of the text popup. 

## ◆ autoConnectDevices()

void LogicalWorkspace::autoConnectDevices  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Auto connect function, connect the given devices with a default cable at default ports, if possible. 

Parameters
     device1| The originating device   
---|---  
device2| the destination device   
  
## ◆ canvasNoteAdded()

void LogicalWorkspace::canvasNoteAdded  | ( | uuid  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when a canvas item note is added to the Logical workspace. 

  * id, the uuid of the note added.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ canvasNoteRemoved()

void LogicalWorkspace::canvasNoteRemoved  | ( | uuid  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when a canvas item note is removed from the Logical workspace. 

  * id, the uuid of the note removed.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ canvasNoteTextChanged()

void LogicalWorkspace::canvasNoteTextChanged  | ( | uuid  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
This event is emitted when a canvas item note has it's text changed. 

  * id, the uuid of the note removed. 
  * text, text from the note.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ centerOn()

void LogicalWorkspace::centerOn  | ( | double  | ,   
---|---|---|---  
|  | double  |   
| ) | |   
  
## ◆ centerOnComponentByName()

void LogicalWorkspace::centerOnComponentByName  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
## ◆ changeNoteText()

bool LogicalWorkspace::changeNoteText  | ( | uuid  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Changes text in a note on the logical workspace. 

Parameters
     id,ID| of the   
---|---  
text,the| text for the note.  
  
Returns
    uuid, the UUID of the note. 

## ◆ clearLayer()

bool LogicalWorkspace::clearLayer  | ( | double  | | ) |   
---|---|---|---|---|---  
  
Clears the specified layer. 

Parameters
     layerNumber,the| layer of interest.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ clusterAdded()

void LogicalWorkspace::clusterAdded  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when a cluster object is added. 

  * addedId, Id of the new cluster.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ clusterForItemChanged()

void LogicalWorkspace::clusterForItemChanged  | ( | uuid  | ,   
---|---|---|---  
|  | QString  | ,   
|  | QString  |   
| ) | |   
  
Sent when an item is moved from one cluster to another, etc. 

  * itemUuid, item ID of an item. This can be a uuid of canvas item, [Device](class_device.html "Device is the base class for all device objects.") or [Cluster](class_cluster.html). 
  * clusterId, [Cluster](class_cluster.html) id from which to remove the item.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ clusterRemoved()

void LogicalWorkspace::clusterRemoved  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when a cluster is removed from the Logical workspace. 

  * removedId, Id of the cluster removed.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ createLink()

bool LogicalWorkspace::createLink  | ( | QString  | ,   
---|---|---|---  
|  | string  | ,   
|  | QString  | ,   
|  | string  | ,   
|  | CONNECT_TYPES  |   
| ) | |   
  
Creates a link from one device's port to another device's port. 

Parameters
     deviceName1,the| name of the first device.   
---|---  
portName1,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0   
deviceName2,the| name of the second device.   
portName2| portName can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0   
connType,the| connection type. Connection types: ETHERNET_STRAIGHT = 8100, ETHERNET_CROSS = 8101, ETHERNET_ROLL = 8102, FIBER = 8103, PHONE = 8104, CABLE = 8105, SERIAL = 8106, AUTO = 8107, CONSOLE = 8108, WIRELESS = 8109, COAXIAL = 8110, OCTAL = 8111, CELLULAR = 8112, USB = 8113, CUSTOM_IO = 8114,   
  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ deleteLink()

bool LogicalWorkspace::deleteLink  | ( | QString  | ,   
---|---|---|---  
|  | string  |   
| ) | |   
  
Deletes a link from the device connected to the specified port. 

Parameters
     deviceName1,the| name of the first device.   
---|---  
portName1,portName| can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ deviceAdded()

void LogicalWorkspace::deviceAdded  | ( | QString  | ,   
---|---|---|---  
|  | string  | ,   
|  | uuid  |   
| ) | |   
  
This event is emitted when a device is added to the Logical workspace. 

  * name, the name of the device added. 
  * model, the model of the device added.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ deviceRemoved()

void LogicalWorkspace::deviceRemoved  | ( | QString  | ,   
---|---|---|---  
|  | uuid  |   
| ) | |   
  
This event is emitted when a device is removed from the Logical workspace. 

  * name, the name of the device removed. 
  * deviceUuid, the unique ID of the device.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ deviceRemoving()

void LogicalWorkspace::deviceRemoving  | ( | QString  | ,   
---|---|---|---  
|  | uuid  |   
| ) | |   
  
This event is emitted when a device is about to be removed from the Logical workspace. 

  * name, the name of the device being removed. 
  * deviceUuid, the unique ID of the device.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ drawCircle()

uuid LogicalWorkspace::drawCircle  | ( | int  | ,   
---|---|---|---  
|  | int  | ,   
|  | double  | ,   
|  | int  | ,   
|  | int  | ,   
|  | int  | ,   
|  | int  |   
| ) | |   
  
Draws a circle on the Logical workspace. 

Parameters
     cx,the| x-coordinate of the center for the circle.   
---|---  
cy,the| y-coordinate of the center for the circle.   
layer,the| layer to draw the circle on.   
radius,the| radius for the circle.   
r,the| red color value for the circle.   
g,the| green color value for the circle.   
b,the| blue color value for the circle.  
  
Returns
    uuid, the UUID of the circle. 

## ◆ drawLine()

uuid LogicalWorkspace::drawLine  | ( | int  | ,   
---|---|---|---  
|  | int  | ,   
|  | int  | ,   
|  | int  | ,   
|  | double  | ,   
|  | int  | ,   
|  | int  | ,   
|  | int  | ,   
|  | int  |   
| ) | |   
  
Draws a line on the Logical workspace. 

Parameters
     sx,the| x-coordinate to start drawing the line from.   
---|---  
sy,the| y-coordinate to start drawing the line from.   
ex,the| x-coordinate to stop drawing the line at.   
ey,the| y-coordinate to stop drawing the line at.   
layer,the| layer to draw the line on.   
w,the| width for the line.   
r,the| red color value for the line.   
g,the| green color value for the line.   
b,the| blue color value for the line.  
  
Returns
    uuid, the UUID of the line. 

## ◆ getCanvasEllipseIds()

vector< uuid > LogicalWorkspace::getCanvasEllipseIds  | ( | | ) |  const  
---|---|---|---|---  
  
Returns the list of UUIDs of ellipse items on the Logical workspace. 

Returns
    vector<uuid>, the list of UUIDs of ellipse items on the Logical workspace. 

## ◆ getCanvasItemIds()

vector< uuid > LogicalWorkspace::getCanvasItemIds  | ( | | ) |  const  
---|---|---|---|---  
  
Returns the list of UUIDs of items on the Logical workspace. 

Returns
    vector<uuid>, the list of UUIDs of items on the Logical workspace. 

## ◆ getCanvasItemRealX()

int LogicalWorkspace::getCanvasItemRealX  | ( | uuid  | | ) |  const  
---|---|---|---|---|---  
  
Returns the real x-coordinate of the Logical workspace item with the specified UUID. 

Parameters
     item_id,the| UUID of the Logical workspace item of interest.  
---|---  
  
Returns
    int, the x-coordinate of the Logical workspace item with the specified UUID. 

## ◆ getCanvasItemRealY()

int LogicalWorkspace::getCanvasItemRealY  | ( | uuid  | | ) |  const  
---|---|---|---|---|---  
  
Returns the real y-coordinate of the Logical workspace item with the specified UUID. 

Parameters
     item_id,the| UUID of the Logical workspace item of interest.  
---|---  
  
Returns
    int, the y-coordinate of the Logical workspace item with the specified UUID. 

## ◆ getCanvasItemX()

int LogicalWorkspace::getCanvasItemX  | ( | uuid  | | ) |  const  
---|---|---|---|---|---  
  
Returns the x-coordinate of the Logical workspace item with the specified UUID. 

Parameters
     item_id,the| UUID of the Logical workspace item of interest.  
---|---  
  
Returns
    int, the x-coordinate of the Logical workspace item with the specified UUID. 

## ◆ getCanvasItemY()

int LogicalWorkspace::getCanvasItemY  | ( | uuid  | | ) |  const  
---|---|---|---|---|---  
  
Returns the y-coordinate of the Logical workspace item with the specified UUID. 

Parameters
     item_id,the| UUID of the Logical workspace item of interest.  
---|---  
  
Returns
    int, the y-coordinate of the Logical workspace item with the specified UUID. 

## ◆ getCanvasLineIds()

vector< uuid > LogicalWorkspace::getCanvasLineIds  | ( | | ) |  const  
---|---|---|---|---  
  
Returns the list of UUIDs of line items on the Logical workspace. 

Returns
    vector<uuid>, the list of UUIDs of line items on the Logical workspace. 

## ◆ getCanvasNoteIds()

vector< uuid > LogicalWorkspace::getCanvasNoteIds  | ( | | ) |  const  
---|---|---|---|---  
  
Returns the list of UUIDs of note items on the Logical workspace. 

Returns
    vector<uuid>, the list of UUIDs of note items on the Logical workspace. 

## ◆ getCanvasNoteText()

QString LogicalWorkspace::getCanvasNoteText  | ( | uuid  | | ) |   
---|---|---|---|---|---  
  
Gets text from a note on the Logical workspace. 

Parameters
     uuid,the| id of the canvas note.  
---|---  
  
Returns
    QString, the note text. 

## ◆ getCanvasPolygonIds()

vector< uuid > LogicalWorkspace::getCanvasPolygonIds  | ( | | ) |  const  
---|---|---|---|---  
  
Returns the list of UUIDs of polygon items on the Logical workspace. 

Returns
    vector<uuid>, the list of UUIDs of polygon items on the Logical workspace. 

## ◆ getCanvasRectIds()

vector< uuid > LogicalWorkspace::getCanvasRectIds  | ( | | ) |  const  
---|---|---|---|---  
  
Returns the list of UUIDs of rectangle items on the Logical workspace. 

Returns
    vector<uuid>, the list of UUIDs of rectangle items on the Logical workspace. 

## ◆ getCluster()

[Cluster](class_cluster.html) LogicalWorkspace::getCluster  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns cluster object for a given cluster id. 

  * clusterId of a cluster object. 



## ◆ getClusterForItem()

[Cluster](class_cluster.html) LogicalWorkspace::getClusterForItem  | ( | uuid  | | ) |   
---|---|---|---|---|---  
  
Returns cluster object this item belongs to. 

Parameters
     itemUuid,the| uuid an item. This can be a uuid of any canvas item, [Device](class_device.html "Device is the base class for all device objects.") uuid or [Cluster](class_cluster.html) uuid.   
---|---  
  
Returns
    [Cluster](class_cluster.html), cluster object the given item belongs to. 

## ◆ getClusterFromItem()

[Cluster](class_cluster.html) LogicalWorkspace::getClusterFromItem  | ( | uuid  | | ) |   
---|---|---|---|---|---  
  
Returns cluster object assosiatete with a given cluster item. 

Parameters
     clusterItemUuid,the| uuid for the cluster item of interest. For non-cluster items this will return NULL.   
---|---  
  
Returns
    [Cluster](class_cluster.html), the cluster object assosiatete with a given cluster item. 

## ◆ getClusterIdForItem()

QString LogicalWorkspace::getClusterIdForItem  | ( | uuid  | | ) |   
---|---|---|---|---|---  
  
Returns cluster id for a given workspace item. 

Parameters
     itemUuid| of an item. This can be a uuid of canvas item, [Device](class_device.html "Device is the base class for all device objects.") or [Cluster](class_cluster.html).   
---|---  
  
Returns
    QString, cluster id for a given workspace item. 

## ◆ getClusterItemId()

uuid LogicalWorkspace::getClusterItemId  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns uuid for the item associated with this cluster object. 

Parameters
     clusterId,ID| of a cluster object for which we want to get an item.  
---|---  
  
Returns
    uuid, the uuid for the item associated with the given cluster. 

## ◆ getComponentChildCountFor()

int LogicalWorkspace::getComponentChildCountFor  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
## ◆ getComponentChildForAt()

[ComponentItem](class_component_item.html) LogicalWorkspace::getComponentChildForAt  | ( | QString  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
## ◆ getComponentChildForByName()

[ComponentItem](class_component_item.html) LogicalWorkspace::getComponentChildForByName  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
## ◆ getComponentItem()

[ComponentItem](class_component_item.html) LogicalWorkspace::getComponentItem  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the component item with the specified device name. 

Parameters
     deviceName,the| name of the device of interest.  
---|---  
  
Returns
    [ComponentItem](class_component_item.html "ComponentItem handles and manipulates component items, such as devices, on the workspace."), the [ComponentItem](class_component_item.html "ComponentItem handles and manipulates component items, such as devices, on the workspace.") object with the specified device name. 

## ◆ getComponentItemsCount()

int LogicalWorkspace::getComponentItemsCount  | ( | | ) |   
---|---|---|---|---  
  
Returns the number of component items on the Logical workspace. 

Returns
    int, the number of component items on the Logical workspace. 

## ◆ getCurrentCluster()

[Cluster](class_cluster.html) LogicalWorkspace::getCurrentCluster  | ( | | ) |   
---|---|---|---|---  
  
Returns root cluster. 

## ◆ getCurrentZoom()

int LogicalWorkspace::getCurrentZoom  | ( | | ) |   
---|---|---|---|---  
  
Returns
    int, 0 means default zoom. a positive number indicates zoom in level. a negative number indicates zoom out level. 

## ◆ getEllipseItemData()

vector< string > LogicalWorkspace::getEllipseItemData  | ( | uuid  | | ) |  const  
---|---|---|---|---|---  
  
Returns a vector of data for a ellipse workspace item. 

Parameters
     itemID,ID| of the ellipse to get information for.  
---|---  
  
Returns
    vector<string>, Each string is part of the data, like the x position of the starting position, etc. index [0, 1] start x and y. index [2, 3] end x and y. index [4] inner color rgb 'r,g,b', empty string if not displayed. index [5] outer color rgb. 'r,g,b', empty string if not displayed. index [6] text 

## ◆ getIncNoteZOrder()

double LogicalWorkspace::getIncNoteZOrder  | ( | | ) |   
---|---|---|---|---  
  
Gets and increments the current z order to use for a new note. 

Returns
    uuid, the UUID of the note. 

## ◆ getLayerInbetweenComponents()

double LogicalWorkspace::getLayerInbetweenComponents  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Returns the layer between the specified devices. 

Parameters
     deviceName1,the| name of the first device.   
---|---  
deviceName2,the| name of the second device.  
  
Returns
    double, the layer between the specified devices. 

## ◆ getLineItemData()

vector< string > LogicalWorkspace::getLineItemData  | ( | uuid  | | ) |  const  
---|---|---|---|---|---  
  
Returns a vector of data for a line workspace item. 

Parameters
     itemID,ID| of the line to get information for.  
---|---  
  
Returns
    vector<string>, Each string is part of the data, like the x position of the starting position, etc. index [0, 1] start x and y. index [2, 3] end x and y. index [4] Color rgb 'r,g,b'. 

## ◆ getMUItemCount()

int LogicalWorkspace::getMUItemCount  | ( | | ) |   
---|---|---|---|---  
  
Gets how many multiuser items there are, if any. 

Returns
    int, the number of multiuser items. 

## ◆ getPolygonItemData()

vector< string > LogicalWorkspace::getPolygonItemData  | ( | uuid  | | ) |  const  
---|---|---|---|---|---  
  
Returns a vector of data for a polygon workspace item. 

Parameters
     itemID,ID| of the polygon to get information for.  
---|---  
  
Returns
    vector<string>, Each string is part of the data. index [0] inner color rgb. 'r,g,b', empty string if not displayed. index [1] outer color rgb. 'r,g,b', empty string if not displayed. index [2, vectorSize-1] These are the points of the polygon. [2] would be x, [3] would be y. All indexes after [1] are points in this fashion. 

## ◆ getRectItemData()

vector< string > LogicalWorkspace::getRectItemData  | ( | uuid  | | ) |  const  
---|---|---|---|---|---  
  
Returns a vector of data for a rectangle workspace item. 

Parameters
     itemID,ID| of the rectangle to retrieve information for.  
---|---  
  
Returns
    vector<string>, Each string is part of the data, like the x position of the starting position, etc. index [0, 1] start x and y. index [2, 3] end x and y. index [4] inner color rgb 'r,g,b', empty string if not displayed. index [5] outer color rgb. 'r,g,b', empty string if not displayed. index [6] text 

## ◆ getRootCluster()

[Cluster](class_cluster.html) LogicalWorkspace::getRootCluster  | ( | | ) |   
---|---|---|---|---  
  
Returns root cluster. 

## ◆ getState()

int LogicalWorkspace::getState  | ( | | ) |   
---|---|---|---|---  
  
Returns the state of the Logical workspace. 

Returns
    int, the state of the Logical workspace. States: sNone = 0, sHandScroll = 1, sAddNote = 2, sAddLine = 3, sAddEllipse = 4, sAddRectangle = 5, sDragging = 6, sDragged = 7, sConnect1 = 8, sConnect2 = 9, sAConnect1 = 10, sAConnect2 = 11, sInspect = 12, sDelete = 13, sPDU = 14, sAddDevice = 15, sAddDevices = 16, sMoveItem = 17, sZoom = 18, sZoomReset = 19, sDeviceTemplate = 20, sCtrlDrag = 21, sNameExists = 22, sResizeShape = 23, sRecable = 24, sFreeformPolygon = 100 

## ◆ getUnusedLayer()

double LogicalWorkspace::getUnusedLayer  | ( | | ) |   
---|---|---|---|---  
  
Returns the unused layer. 

Returns
    double, the unused layer. 

## ◆ getWorkspaceImage()

vector< byte > LogicalWorkspace::getWorkspaceImage  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Returns the series of bytes of the Logical workspace image. 

Parameters
     format,the| format of the image. Image formats: BMP, GIF, JPG, JPEG, PNG, PBM, PGM, PPM, XBM, XPM.  
---|---  
  
Returns
    vector<byte>, the series of bytes of the Logical workspace image. 

## ◆ isLayerUsed()

bool LogicalWorkspace::isLayerUsed  | ( | double  | | ) |   
---|---|---|---|---|---  
  
Returns true if the specified layer is used, otherwise false. 

Parameters
     layer,the| layer of interest.  
---|---  
  
Returns
    true if the specified layer is used, otherwise false. 

## ◆ linkCreated()

void LogicalWorkspace::linkCreated  | ( | QString  | ,   
---|---|---|---  
|  | string  | ,   
|  | QString  | ,   
|  | string  | ,   
|  | CONNECT_TYPES  |   
| ) | |   
  
This event is emitted when a link has been created. 

  * deviceName1, the name of the first device. 
  * portName1, portName can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0 
  * deviceName2, the name of the second device. 
  * portName2, portName can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0 
  * connType, the connection type. Connection types: ETHERNET_STRAIGHT = 8100, ETHERNET_CROSS = 8101, ETHERNET_ROLL = 8102, FIBER = 8103, PHONE = 8104, CABLE = 8105, SERIAL = 8106, AUTO = 8107, CONSOLE = 8108, WIRELESS = 8109, COAXIAL = 8110, OCTAL = 8111, CELLULAR = 8112, USB = 8113, CUSTOM_IO = 8114,   




[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ linkDeleted()

void LogicalWorkspace::linkDeleted  | ( | QString  | ,   
---|---|---|---  
|  | string  | ,   
|  | QString  | ,   
|  | string  | ,   
|  | CONNECT_TYPES  |   
| ) | |   
  
This event is emitted when a link has been deleted. 

  * deviceName1, the name of the first device. 
  * portName1, portName can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0 
  * deviceName2, the name of the second device. 
  * portName2, portName can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0 
  * connType, the connection type. Connection types: ETHERNET_STRAIGHT = 8100, ETHERNET_CROSS = 8101, ETHERNET_ROLL = 8102, FIBER = 8103, PHONE = 8104, CABLE = 8105, SERIAL = 8106, AUTO = 8107, CONSOLE = 8108, WIRELESS = 8109, COAXIAL = 8110, OCTAL = 8111, CELLULAR = 8112, USB = 8113, CUSTOM_IO = 8114,   




[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ linkStarted()

void LogicalWorkspace::linkStarted  | ( | QString  | ,   
---|---|---|---  
|  | string  | ,   
|  | CONNECT_TYPES  |   
| ) | |   
  
This event is emitted when a link starts (i.e. user connects the first end of a link) 

  * deviceName1, the name of the first device. 
  * portName1, portName can be one of the following plus a port number where appropriate: Console, Aux, Ethernet, FastEthernet, GigabitEthernet, Serial, Wireless, Loopback, [Vlan](class_vlan.html "Vlan handles and manipulates the individual VLAN."), Modem, Coaxial, Rs232, Async. Example: FastEthernet0/0 
  * connType, the connection type. Connection types: ETHERNET_STRAIGHT = 8100, ETHERNET_CROSS = 8101, ETHERNET_ROLL = 8102, FIBER = 8103, PHONE = 8104, CABLE = 8105, SERIAL = 8106, AUTO = 8107, CONSOLE = 8108, WIRELESS = 8109, COAXIAL = 8110, OCTAL = 8111, CELLULAR = 8112, USB = 8113, CUSTOM_IO = 8114,   




[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ moveCanvasItemBy()

void LogicalWorkspace::moveCanvasItemBy  | ( | uuid  | ,   
---|---|---|---  
|  | int  | ,   
|  | int  |   
| ) | |   
  
Moves the Logical workspace item with the specified UUID by the specified increments. 

Parameters
     item_id,the| UUID of the Logical workspace item of interest.   
---|---  
dx,the| value to move the item in the x-axis by.   
dy,the| value to move the item in the y-axis by.   
  
## ◆ moveItemToCluster()

void LogicalWorkspace::moveItemToCluster  | ( | uuid  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Moves item from current cluster to a cluster with given clusterId. 

Parameters
     itemUuid| of an item. This can be a uuid of canvas item, [Device](class_device.html "Device is the base class for all device objects.") or [Cluster](class_cluster.html).   
---|---  
clusterId,[Cluster](class_cluster.html)| ID of the cluster to add the item to.   
  
## ◆ moveRemoteNetwork()

bool LogicalWorkspace::moveRemoteNetwork  | ( | QString  | ,   
---|---|---|---  
|  | int  | ,   
|  | int  |   
| ) | |   
  
Moves the Multiuser remote network to the specified location. 

Parameters
     name,the| name of the Multiuser remote network of interest.   
---|---  
x,the| new x-coorindate for the Multiuser remote network.   
y,the| new y-coordinate for the Multiuser remote network.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ onNoAutoConnectError()

void LogicalWorkspace::onNoAutoConnectError  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Sent when autoconnect occures and there isn't an error. 

  * device1, one of the devices in the autoconnect that occured. 
  * device2, the other device in the autoconnect that occured.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ remoteNetworkAdded()

void LogicalWorkspace::remoteNetworkAdded  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when a Multiuser remote network is added to the Logical workspace. 

  * name, the name of the Multiuser remote network added.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ remoteNetworkRemoved()

void LogicalWorkspace::remoteNetworkRemoved  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
This event is emitted when a Multiuser remote network is removed from the Logical workspace. 

  * name, the name of the Multiuser remote network removed.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ removeCanvasItem()

bool LogicalWorkspace::removeCanvasItem  | ( | uuid  | | ) |   
---|---|---|---|---|---  
  
Removes the specified item from the Logical workspace. 

Parameters
     id,the| UUID of the item of interest.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ removeCluster()

void LogicalWorkspace::removeCluster  | ( | QString  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Removes csluter object with given id. 

Parameters
     clusterId,The| cluster ID of the cluster of interest.   
---|---  
uncluster,When| false - the cluster with everything inside will be killed. When true - is equivalent to unCluster.   
  
## ◆ removeDevice()

bool LogicalWorkspace::removeDevice  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Removes the specified device from the Logical workspace and network. 

Parameters
     deviceName,the| name of the device of interest.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ removeRemoteNetwork()

bool LogicalWorkspace::removeRemoteNetwork  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Removes the Multiuser remote network with the specified name from the Logical workspace. 

Parameters
     name,the| name of the Multiuser remote network to remove.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ removeTextPopup()

bool LogicalWorkspace::removeTextPopup  | ( | uuid  | | ) |   
---|---|---|---|---|---  
  
Removes the specified text popup from the Logical workspace. 

Parameters
     id,the| UUID of the text popup of interest.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ setCanvasItemRealPos()

void LogicalWorkspace::setCanvasItemRealPos  | ( | uuid  | ,   
---|---|---|---  
|  | int  | ,   
|  | int  |   
| ) | |   
  
Sets the x-coordinate of the Logical workspace item with the specified UUID. 

Parameters
     item_id,the| UUID of the Logical workspace item of interest.   
---|---  
x,the| x-coordinate for the Logical workspace item.   
y,the| y-coordinate for the Logical workspace item.   
  
## ◆ setCanvasItemX()

void LogicalWorkspace::setCanvasItemX  | ( | uuid  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Sets the x-coordinate of the Logical workspace item with the specified UUID. 

Parameters
     item_id,the| UUID of the Logical workspace item of interest.   
---|---  
x,the| x-coordinate for the Logical workspace item.   
  
## ◆ setCanvasItemY()

void LogicalWorkspace::setCanvasItemY  | ( | uuid  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Sets the y-coordinate of the Logical workspace item with the specified UUID. 

Parameters
     item_id,the| UUID of the Logical workspace item of interest.   
---|---  
y,the| y-coordinate for the Logical workspace item.   
  
## ◆ setDeviceCustomImage()

void LogicalWorkspace::setDeviceCustomImage  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
Change [Device](class_device.html "Device is the base class for all device objects.") image in logical workspace. 

Parameters
     deviceName,the| name of the device to set the custom image for.   
---|---  
path,path| to the image to use.   
  
## ◆ showClusterContents() [1/2]

void LogicalWorkspace::showClusterContents  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Shows the content of the specified cluster. 

Parameters
     clustid,the| cluster ID of the cluster of interest.   
---|---  
  
## ◆ showClusterContents() [2/2]

void LogicalWorkspace::showClusterContents  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Triggered when a cluster contents are shown. 

Parameters
     clustid,the| cluster ID of the cluster of interest.  
---|---  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ unCluster()

void LogicalWorkspace::unCluster  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Unclusters cluster with the given clusterId. 

  * clusterId, [Cluster](class_cluster.html) id for which to do unclustering operation. 



* * *

The documentation for this class was generated from the following file:

  * [LogicalWorkspace.pki](_logical_workspace_8pki.html)


