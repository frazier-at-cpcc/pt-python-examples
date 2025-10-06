# Cisco Packet Tracer Extensions API: WebView Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_web_view.html

---

[WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules.") allows manipulation of WebViews such as the Instruction dialog and Script Modules. [More...](class_web_view.html#details)

##  Public Member Functions  
  
---  
uuid | [getWebViewId](class_web_view.html#ac80fc9efb745a3918e49af8ee4f2e63c) ()  
| Returns the UUID of this [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."). [More...](class_web_view.html#ac80fc9efb745a3918e49af8ee4f2e63c)  
  
QString | [evaluateToVariant](class_web_view.html#abba8b40c8516d8cb05fb07bc739009d7) (QString)  
| Evaluates the specified script. [More...](class_web_view.html#abba8b40c8516d8cb05fb07bc739009d7)  
  
void | [evaluateJavaScriptAsync](class_web_view.html#a88e312608b33c34a0ba40d2b60ca007d) (QString)  
| Evaluates the specified script asynchronously. [More...](class_web_view.html#a88e312608b33c34a0ba40d2b60ca007d)  
  
void | [setHtml](class_web_view.html#ae54d1d1c774ca3a7b2284536f2cad287) (QString)  
| Sets the HTML content of the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."). [More...](class_web_view.html#ae54d1d1c774ca3a7b2284536f2cad287)  
  
void | [setUrl](class_web_view.html#a86e0385c99da3234425ce1223b438980) (QString)  
| Sets the URL of the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."). [More...](class_web_view.html#a86e0385c99da3234425ce1223b438980)  
  
QString | [getUrl](class_web_view.html#af72ebe149ae9cca022badda802ba9ebb) ()  
| Returns the URL of the current page being displayed. [More...](class_web_view.html#af72ebe149ae9cca022badda802ba9ebb)  
  
QString | [getRequestedUrl](class_web_view.html#ad0641bd5cc366050f09956887aac54b8) ()  
| Returns the requested URL, which may be different than what [getUrl()](class_web_view.html#af72ebe149ae9cca022badda802ba9ebb "Returns the URL of the current page being displayed.") returns. [More...](class_web_view.html#ad0641bd5cc366050f09956887aac54b8)  
  
void | [show](class_web_view.html#a380dad1d4b2eac6dd9b0a5e114ddb126) ()  
| Shows the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."). [More...](class_web_view.html#a380dad1d4b2eac6dd9b0a5e114ddb126)  
  
void | [hide](class_web_view.html#a89021d71e07eb8ee6a8d8fa6ead2279f) ()  
| Hides the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."). [More...](class_web_view.html#a89021d71e07eb8ee6a8d8fa6ead2279f)  
  
void | [raise](class_web_view.html#a4adfabd3b220e1667e6b06f02ec2129b) ()  
| Shows the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules.") on top of other windows. [More...](class_web_view.html#a4adfabd3b220e1667e6b06f02ec2129b)  
  
void | [setWindowTitle](class_web_view.html#adbd3755bf7fa32fc1d431958966e8896) (QString)  
| Sets the window title of the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."). [More...](class_web_view.html#adbd3755bf7fa32fc1d431958966e8896)  
  
void | [setGeometry](class_web_view.html#a2c907436ea8ad7c2fc550c5db2951203) (int, int, int, int)  
| Sets the window position and geometry of the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."). [More...](class_web_view.html#a2c907436ea8ad7c2fc550c5db2951203)  
  
int | [getX](class_web_view.html#a734cea104aea6b8934c2e3c908de485d) ()  
| Returns the x position of the webview. [More...](class_web_view.html#a734cea104aea6b8934c2e3c908de485d)  
  
int | [getY](class_web_view.html#a81b3e7cf84941526af57ea29a95e4041) ()  
| Returns the y position of the webview. [More...](class_web_view.html#a81b3e7cf84941526af57ea29a95e4041)  
  
int | [getWidth](class_web_view.html#af23fd16a2e6e26147b7e88aec6599d5c) ()  
| Returns the width of the webview. [More...](class_web_view.html#af23fd16a2e6e26147b7e88aec6599d5c)  
  
int | [getHeight](class_web_view.html#a336444411a1a7fd9b98b3abe5d26b9ab) ()  
| Returns the height of the webview. [More...](class_web_view.html#a336444411a1a7fd9b98b3abe5d26b9ab)  
  
void | [setMaximumSize](class_web_view.html#a62aa82bf6f8ff3d64718896cee6d0166) (int, int)  
| Sets the maximum size of the web view. [More...](class_web_view.html#a62aa82bf6f8ff3d64718896cee6d0166)  
  
void | [setMaximumWidth](class_web_view.html#a33dab03632531b886d2ae526adcccc4b) (int)  
| Sets the maximum width of the webview. [More...](class_web_view.html#a33dab03632531b886d2ae526adcccc4b)  
  
void | [setMaximumHeight](class_web_view.html#ae215d1daccb8d1aacc216955fc7dec64) (int)  
| Sets the maximum height of the webview. [More...](class_web_view.html#ae215d1daccb8d1aacc216955fc7dec64)  
  
int | [getMaximumWidth](class_web_view.html#a8b97e3fdd56f9d4abebbbc9171c4795c) ()  
| Returns the maximum width of the webview. [More...](class_web_view.html#a8b97e3fdd56f9d4abebbbc9171c4795c)  
  
int | [getMaximumHeight](class_web_view.html#a9d522bd9241cecb2a2293a988b43a696) ()  
| Returns the maximum height of the webview. [More...](class_web_view.html#a9d522bd9241cecb2a2293a988b43a696)  
  
void | [setMinimumSize](class_web_view.html#a84e70e491cf6230953758509843b074c) (int, int)  
| Sets the minimum size of the web view. [More...](class_web_view.html#a84e70e491cf6230953758509843b074c)  
  
void | [setMinimumWidth](class_web_view.html#af17a8aba941f8e7b92f8b7e6063593a1) (int)  
| Sets the minimum width of the webview. [More...](class_web_view.html#af17a8aba941f8e7b92f8b7e6063593a1)  
  
void | [setMinimumHeight](class_web_view.html#ad8b380a133b851b30df0d3bc88c1506c) (int)  
| Sets the minimum height of the webview. [More...](class_web_view.html#ad8b380a133b851b30df0d3bc88c1506c)  
  
int | [getMinimumWidth](class_web_view.html#abd96ca84d9109ca0002024bd6b40309b) ()  
| Returns the minimum width of the webview. [More...](class_web_view.html#abd96ca84d9109ca0002024bd6b40309b)  
  
int | [getMinimumHeight](class_web_view.html#a6245aed1ea9742faaaaf1226801b988f) ()  
| Returns the minimum height of the webview. [More...](class_web_view.html#a6245aed1ea9742faaaaf1226801b988f)  
  
void | [setPreferredSize](class_web_view.html#a673da463c79d827132a60d9901c47145) (int, int)  
| Sets the preferred size of the webview. [More...](class_web_view.html#a673da463c79d827132a60d9901c47145)  
  
int | [getPreferredWidth](class_web_view.html#ab71416637f25e1d0fb0d64ca7cb065ee) ()  
| Returns the preferred width of the webview. [More...](class_web_view.html#ab71416637f25e1d0fb0d64ca7cb065ee)  
  
int | [getPreferredHeight](class_web_view.html#a56c0cdbfd5732df4aea7a453e10b91b2) ()  
| Returns the preferred height of the webview. [More...](class_web_view.html#a56c0cdbfd5732df4aea7a453e10b91b2)  
  
void | [isFullScreen](class_web_view.html#a564a1a3fb9e2ae7692ec719c6c28985e) ()  
void | [showFullScreen](class_web_view.html#a0c942719f4cb010f0e867fb5b3e448bf) ()  
void | [isMaximized](class_web_view.html#a33d97fd8c2ac726893d95c4e13d123fa) ()  
void | [showMaximized](class_web_view.html#a9a7cd96ce206d7c28d9e2e28318849e5) ()  
void | [isMinimized](class_web_view.html#a337f67b338a0bf7b691b098aec78a6f2) ()  
void | [showMinimized](class_web_view.html#af37f0bef811d94d10f3e16ebb80b4b84) ()  
void | [showNormal](class_web_view.html#ac1360d32f18b657f39c277d8925a6525) ()  
void | [setWindowFlags](class_web_view.html#af507a5beb9f215ddf228cf25c9e3a9ca) (WindowFlags)  
WindowFlags | [getWindowFlags](class_web_view.html#a4ebb17c7c93774a7f3e25feb309d8186) ()  
| Returns the window flags for the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."). See [setWindowFlags()](class_web_view.html#af507a5beb9f215ddf228cf25c9e3a9ca) for enum values. [More...](class_web_view.html#a4ebb17c7c93774a7f3e25feb309d8186)  
  
void | [setWindowModality](class_web_view.html#a097899ac1949ffc63f9b42486fbf7123) (WindowModality)  
| Sets the window modality for the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."). [More...](class_web_view.html#a097899ac1949ffc63f9b42486fbf7123)  
  
void | [setCanClose](class_web_view.html#ac8537f9abe4175aaf669cf52fcee9cb8) (bool)  
| Allows or disallows closing of the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."). [More...](class_web_view.html#ac8537f9abe4175aaf669cf52fcee9cb8)  
  
void | [closeRequested](class_web_view.html#abf449bedb7d908f011d4995a180789a1) (uuid)  
| [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. [More...](class_web_view.html#abf449bedb7d908f011d4995a180789a1)  
  
void | [closed](class_web_view.html#a586feaaf1ab82d377f5249848007bf05) (uuid)  
| [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. [More...](class_web_view.html#a586feaaf1ab82d377f5249848007bf05)  
  
void | [onFocus](class_web_view.html#ab65ff95f39dba9d1d59df4e8ec8e61c3) ()  
| [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. [More...](class_web_view.html#ab65ff95f39dba9d1d59df4e8ec8e61c3)  
  
void | [offFocus](class_web_view.html#a56148b9c7e6ca362c3921402e4363d17) ()  
| [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. [More...](class_web_view.html#a56148b9c7e6ca362c3921402e4363d17)  
  
bool | [addAllowedExternalFilter](class_web_view.html#a887eb930f2fb0a27b4eadd35c047ef3c) (QString)  
bool | [removeAllowedExternalFilter](class_web_view.html#a9ed761d8d35ff16b9c542df2b5083878) (QString)  
bool | [hasAllowedExternalFilter](class_web_view.html#aedd62c68403a2d101fab9248760efec6) (QString)  
vector< QString > | [getAllowedExternalFilters](class_web_view.html#a137787f2f6c710bc1eeb6413e7d7c965) ()  
void | [clearAllowedExternalFilters](class_web_view.html#aa79831e7a94de6cb8745563b02714587) ()  
void | [close](class_web_view.html#af5c86effbf16d071d09ac94fb8ed393c) ()  
void | [attachToMainViewArea](class_web_view.html#aeda165089550cc69e61be2591ce47273) ()  
void | [detachFromMainViewArea](class_web_view.html#ac7c5923925d3943b7cc3466515ade095) ()  
bool | [isAttachedToMainViewArea](class_web_view.html#afbac590e8599909c0f7b8620055f60f0) ()  
void | [javascriptDone](class_web_view.html#ae970742dae5b38cf8b73d9d7b86e42df) (QString, QString)  
| [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. [More...](class_web_view.html#ae970742dae5b38cf8b73d9d7b86e42df)  
  
void | [dockToMainViewArea](class_web_view.html#af0aad446f811e6dc67003b957ed8e921) ()  
void | [dockToMainViewAreaWithOptions](class_web_view.html#a8bfc7ce69e7db4821cc156b81132e8e0) (QString, DockWidgetArea, DockWidgetArea, Orientation, DockWidgetFeatures)  
void | [undockFromMainViewArea](class_web_view.html#a71e082fb595188d2d153a5cb38d44c22) ()  
bool | [isDockedToMainViewArea](class_web_view.html#a1785f0328fcfe21012c449f55b41b736) ()  
QString | [getDockWidgetWindowTitle](class_web_view.html#a351f311f5abeba3686f48e42e60ef391) ()  
void | [setDockWidgetWindowTitle](class_web_view.html#a17313a6db853fb7c15f55e25ee55676c) (QString)  
void | [setBackgroundColor](class_web_view.html#afe3f735df902feaf87171978a80cc1b1) (long)  
long | [getBackgroundColor](class_web_view.html#a17e146265c65db432ca547201b5e32c2) ()  
void | [setZoomFactor](class_web_view.html#ade72c042432d9cd0500eecf551d69aca) (double)  
double | [getZoomFactor](class_web_view.html#a7414183bfffc612a9063a5447de83592) ()  
void | [fileSystemResourceRequested](class_web_view.html#a88f450ef0e074061afc6014926be7310) ([SmFileSystemResourceRequest](class_sm_file_system_resource_request.html))  
| [IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. [More...](class_web_view.html#a88f450ef0e074061afc6014926be7310)  
  
void | [enableRightClickMenu](class_web_view.html#a7e8dc200a091398bfbb871f87b39149b) (bool)  
  
## Detailed Description

[WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules.") allows manipulation of WebViews such as the Instruction dialog and Script Modules. 

## Member Function Documentation

## ◆ addAllowedExternalFilter()

bool WebView::addAllowedExternalFilter  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
## ◆ attachToMainViewArea()

void WebView::attachToMainViewArea  | ( | | ) |   
---|---|---|---|---  
  
## ◆ clearAllowedExternalFilters()

void WebView::clearAllowedExternalFilters  | ( | | ) |   
---|---|---|---|---  
  
## ◆ close()

void WebView::close  | ( | | ) |   
---|---|---|---|---  
  
## ◆ closed()

void WebView::closed  | ( | uuid  | | ) |   
---|---|---|---|---|---  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ closeRequested()

void WebView::closeRequested  | ( | uuid  | | ) |   
---|---|---|---|---|---  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ detachFromMainViewArea()

void WebView::detachFromMainViewArea  | ( | | ) |   
---|---|---|---|---  
  
## ◆ dockToMainViewArea()

void WebView::dockToMainViewArea  | ( | | ) |   
---|---|---|---|---  
  
## ◆ dockToMainViewAreaWithOptions()

void WebView::dockToMainViewAreaWithOptions  | ( | QString  | ,   
---|---|---|---  
|  | DockWidgetArea  | ,   
|  | DockWidgetArea  | ,   
|  | Orientation  | ,   
|  | DockWidgetFeatures  |   
| ) | |   
  
## ◆ enableRightClickMenu()

void WebView::enableRightClickMenu  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
## ◆ evaluateJavaScriptAsync()

void WebView::evaluateJavaScriptAsync  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Evaluates the specified script asynchronously. 

Parameters
     scriptSource,the| path or source of the script.   
---|---  
  
## ◆ evaluateToVariant()

QString WebView::evaluateToVariant  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Evaluates the specified script. 

Parameters
     scriptSource,the| path or source of the script.  
---|---  
  
Returns
    QString, returns the a unique string to match result from generated event. 

## ◆ fileSystemResourceRequested()

void WebView::fileSystemResourceRequested  | ( | [SmFileSystemResourceRequest](class_sm_file_system_resource_request.html) | | ) |   
---|---|---|---|---|---  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ getAllowedExternalFilters()

vector< QString > WebView::getAllowedExternalFilters  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getBackgroundColor()

long WebView::getBackgroundColor  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getDockWidgetWindowTitle()

QString WebView::getDockWidgetWindowTitle  | ( | | ) |   
---|---|---|---|---  
  
## ◆ getHeight()

int WebView::getHeight  | ( | | ) |   
---|---|---|---|---  
  
Returns the height of the webview. 

## ◆ getMaximumHeight()

int WebView::getMaximumHeight  | ( | | ) |   
---|---|---|---|---  
  
Returns the maximum height of the webview. 

## ◆ getMaximumWidth()

int WebView::getMaximumWidth  | ( | | ) |   
---|---|---|---|---  
  
Returns the maximum width of the webview. 

## ◆ getMinimumHeight()

int WebView::getMinimumHeight  | ( | | ) |   
---|---|---|---|---  
  
Returns the minimum height of the webview. 

## ◆ getMinimumWidth()

int WebView::getMinimumWidth  | ( | | ) |   
---|---|---|---|---  
  
Returns the minimum width of the webview. 

## ◆ getPreferredHeight()

int WebView::getPreferredHeight  | ( | | ) |   
---|---|---|---|---  
  
Returns the preferred height of the webview. 

## ◆ getPreferredWidth()

int WebView::getPreferredWidth  | ( | | ) |   
---|---|---|---|---  
  
Returns the preferred width of the webview. 

## ◆ getRequestedUrl()

QString WebView::getRequestedUrl  | ( | | ) |   
---|---|---|---|---  
  
Returns the requested URL, which may be different than what [getUrl()](class_web_view.html#af72ebe149ae9cca022badda802ba9ebb "Returns the URL of the current page being displayed.") returns. 

## ◆ getUrl()

QString WebView::getUrl  | ( | | ) |   
---|---|---|---|---  
  
Returns the URL of the current page being displayed. 

## ◆ getWebViewId()

uuid WebView::getWebViewId  | ( | | ) |   
---|---|---|---|---  
  
Returns the UUID of this [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."). 

Returns
    uuid, the UUID of this [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."). 

## ◆ getWidth()

int WebView::getWidth  | ( | | ) |   
---|---|---|---|---  
  
Returns the width of the webview. 

## ◆ getWindowFlags()

WindowFlags WebView::getWindowFlags  | ( | | ) |   
---|---|---|---|---  
  
Returns the window flags for the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."). See [setWindowFlags()](class_web_view.html#af507a5beb9f215ddf228cf25c9e3a9ca) for enum values. 

## ◆ getX()

int WebView::getX  | ( | | ) |   
---|---|---|---|---  
  
Returns the x position of the webview. 

## ◆ getY()

int WebView::getY  | ( | | ) |   
---|---|---|---|---  
  
Returns the y position of the webview. 

## ◆ getZoomFactor()

double WebView::getZoomFactor  | ( | | ) |   
---|---|---|---|---  
  
## ◆ hasAllowedExternalFilter()

bool WebView::hasAllowedExternalFilter  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
## ◆ hide()

void WebView::hide  | ( | | ) |   
---|---|---|---|---  
  
Hides the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."). 

## ◆ isAttachedToMainViewArea()

bool WebView::isAttachedToMainViewArea  | ( | | ) |   
---|---|---|---|---  
  
## ◆ isDockedToMainViewArea()

bool WebView::isDockedToMainViewArea  | ( | | ) |   
---|---|---|---|---  
  
## ◆ isFullScreen()

void WebView::isFullScreen  | ( | | ) |   
---|---|---|---|---  
  
## ◆ isMaximized()

void WebView::isMaximized  | ( | | ) |   
---|---|---|---|---  
  
## ◆ isMinimized()

void WebView::isMinimized  | ( | | ) |   
---|---|---|---|---  
  
## ◆ javascriptDone()

void WebView::javascriptDone  | ( | QString  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ offFocus()

void WebView::offFocus  | ( | | ) |   
---|---|---|---|---  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ onFocus()

void WebView::onFocus  | ( | | ) |   
---|---|---|---|---  
  
[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

## ◆ raise()

void WebView::raise  | ( | | ) |   
---|---|---|---|---  
  
Shows the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules.") on top of other windows. 

## ◆ removeAllowedExternalFilter()

bool WebView::removeAllowedExternalFilter  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
## ◆ setBackgroundColor()

void WebView::setBackgroundColor  | ( | long  | | ) |   
---|---|---|---|---|---  
  
## ◆ setCanClose()

void WebView::setCanClose  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Allows or disallows closing of the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."). 

Parameters
     bCanClose,true| to allow closing of the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."), false to disallow.   
---|---  
  
## ◆ setDockWidgetWindowTitle()

void WebView::setDockWidgetWindowTitle  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
## ◆ setGeometry()

void WebView::setGeometry  | ( | int  | ,   
---|---|---|---  
|  | int  | ,   
|  | int  | ,   
|  | int  |   
| ) | |   
  
Sets the window position and geometry of the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."). 

Parameters
     x,the| x-coordinate for the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules.").   
---|---  
y,the| y-coordinate for the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules.").   
width,the| width for the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules.").   
height,the| height for the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules.").   
  
## ◆ setHtml()

void WebView::setHtml  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Sets the HTML content of the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."). 

Parameters
     html,the| HTML content for the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules.").   
---|---  
  
## ◆ setMaximumHeight()

void WebView::setMaximumHeight  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the maximum height of the webview. 

## ◆ setMaximumSize()

void WebView::setMaximumSize  | ( | int  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Sets the maximum size of the web view. 

## ◆ setMaximumWidth()

void WebView::setMaximumWidth  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the maximum width of the webview. 

## ◆ setMinimumHeight()

void WebView::setMinimumHeight  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the minimum height of the webview. 

## ◆ setMinimumSize()

void WebView::setMinimumSize  | ( | int  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Sets the minimum size of the web view. 

## ◆ setMinimumWidth()

void WebView::setMinimumWidth  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Sets the minimum width of the webview. 

## ◆ setPreferredSize()

void WebView::setPreferredSize  | ( | int  | ,   
---|---|---|---  
|  | int  |   
| ) | |   
  
Sets the preferred size of the webview. 

## ◆ setUrl()

void WebView::setUrl  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Sets the URL of the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."). 

Parameters
     url,the| URL for the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules.").   
---|---  
  
## ◆ setWindowFlags()

void WebView::setWindowFlags  | ( | WindowFlags  | | ) |   
---|---|---|---|---|---  
      
    
        \brief Sets the window flags for the WebView.
    
        \param flags,   the window flags.
                        Window flags:
                            Widget = 0x00000000,
                            Window = 0x00000001,
                            Dialog = 0x00000002 | Window,
                            Sheet = 0x00000004 | Window,
                            Drawer = Sheet | Dialog,
                            Popup = 0x00000008 | Window,
                            Tool = Popup | Dialog,
                            ToolTip = Popup | Sheet,
                            SplashScreen = ToolTip | Dialog,
                            Desktop = 0x00000010 | Window,
                            SubWindow = 0x00000012,
                            ForeignWindow = 0x00000020 | Window,
                            CoverWindow = 0x00000040 | Window,
    
                            WindowType_Mask = 0x000000ff,
                            MSWindowsFixedSizeDialogHint = 0x00000100,
                            MSWindowsOwnDC = 0x00000200,
                            BypassWindowManagerHint = 0x00000400,
                            X11BypassWindowManagerHint = BypassWindowManagerHint,
                            FramelessWindowHint = 0x00000800,
                            WindowTitleHint = 0x00001000,
                            WindowSystemMenuHint = 0x00002000,
                            WindowMinimizeButtonHint = 0x00004000,
                            WindowMaximizeButtonHint = 0x00008000,
                            WindowMinMaxButtonsHint = WindowMinimizeButtonHint | WindowMaximizeButtonHint,
                            WindowContextHelpButtonHint = 0x00010000,
                            WindowShadeButtonHint = 0x00020000,
                            WindowStaysOnTopHint = 0x00040000,
                            WindowTransparentForInput = 0x00080000,
                            WindowOverridesSystemGestures = 0x00100000,
                            WindowDoesNotAcceptFocus = 0x00200000,
                            MaximizeUsingFullscreenGeometryHint = 0x00400000,
    
                            CustomizeWindowHint = 0x02000000,
                            WindowStaysOnBottomHint = 0x04000000,
                            WindowCloseButtonHint = 0x08000000,
                            MacWindowToolBarButtonHint = 0x10000000,
                            BypassGraphicsProxyWidget = 0x20000000,
                            NoDropShadowWindowHint = 0x40000000,
                            WindowFullscreenButtonHint = 0x80000000,
    

The following enums have overlapping values with other enums. This was not intentional, but it's too late to change now. WindowOkButtonHint = 0x00080000, // WindowTransparentForInput WindowCancelButtonHint = 0x00100000 // WindowOverridesSystemGestures 

## ◆ setWindowModality()

void WebView::setWindowModality  | ( | WindowModality  | | ) |   
---|---|---|---|---|---  
  
Sets the window modality for the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."). 

Parameters
     modality,the| window modality. Window flags: Qt::NonModal = 0, Qt::WindowModal = 1, Qt::ApplicationModal = 2,   
---|---  
  
## ◆ setWindowTitle()

void WebView::setWindowTitle  | ( | QString  | | ) |   
---|---|---|---|---|---  
  
Sets the window title of the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."). 

Parameters
     title,the| title for the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules.").   
---|---  
  
## ◆ setZoomFactor()

void WebView::setZoomFactor  | ( | double  | | ) |   
---|---|---|---|---|---  
  
## ◆ show()

void WebView::show  | ( | | ) |   
---|---|---|---|---  
  
Shows the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."). 

## ◆ showFullScreen()

void WebView::showFullScreen  | ( | | ) |   
---|---|---|---|---  
  
## ◆ showMaximized()

void WebView::showMaximized  | ( | | ) |   
---|---|---|---|---  
  
## ◆ showMinimized()

void WebView::showMinimized  | ( | | ) |   
---|---|---|---|---  
  
## ◆ showNormal()

void WebView::showNormal  | ( | | ) |   
---|---|---|---|---  
  
## ◆ undockFromMainViewArea()

void WebView::undockFromMainViewArea  | ( | | ) |   
---|---|---|---|---  
  
* * *

The documentation for this class was generated from the following file:

  * [WebView.pki](_web_view_8pki.html)


