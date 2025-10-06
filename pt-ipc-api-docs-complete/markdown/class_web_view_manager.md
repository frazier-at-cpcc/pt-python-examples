# Cisco Packet Tracer Extensions API: WebViewManager Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_web_view_manager.html

---

[WebViewManager](class_web_view_manager.html "WebViewManager manages all WebViews.") manages all WebViews. [More...](class_web_view_manager.html#details)

##  Public Member Functions  
  
---  
[WebView](class_web_view.html) | [createWebView](class_web_view_manager.html#a5edb6b833209fa1dd33817877e6e8055) (QString, QString, int, int)  
| Creates a [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."). [More...](class_web_view_manager.html#a5edb6b833209fa1dd33817877e6e8055)  
  
[WebView](class_web_view.html) | [getWebView](class_web_view_manager.html#a7d480765fdd070aaff95a086330c31f6) (uuid)  
| Returns the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules.") with the specified UUID. [More...](class_web_view_manager.html#a7d480765fdd070aaff95a086330c31f6)  
  
bool | [closeWebView](class_web_view_manager.html#a2b25c74ad9b3f5be7249648f712c77b4) (uuid)  
| Closes the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules.") with the specified UUID. [More...](class_web_view_manager.html#a2b25c74ad9b3f5be7249648f712c77b4)  
  
void | [closeAll](class_web_view_manager.html#aa3ebff72e2de9a5f933c962a2dad7eb7) ()  
| Closes all WebViews. [More...](class_web_view_manager.html#aa3ebff72e2de9a5f933c962a2dad7eb7)  
  
void | [tookWebViewOwnership](class_web_view_manager.html#af3e28bf0bd6e3b8ae9f1da9518b4ca6f) (uuid, QString)  
| This event is emitted when a custom interface takes ownership of a [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."). [More...](class_web_view_manager.html#af3e28bf0bd6e3b8ae9f1da9518b4ca6f)  
  
  
## Detailed Description

[WebViewManager](class_web_view_manager.html "WebViewManager manages all WebViews.") manages all WebViews. 

## Member Function Documentation

## ◆ closeAll()

void WebViewManager::closeAll  | ( | | ) |   
---|---|---|---|---  
  
Closes all WebViews. 

## ◆ closeWebView()

bool WebViewManager::closeWebView  | ( | uuid  | | ) |   
---|---|---|---|---|---  
  
Closes the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules.") with the specified UUID. 

Parameters
     id,the| UUID of the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules.") of interest.  
---|---  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ createWebView()

[WebView](class_web_view.html) WebViewManager::createWebView  | ( | QString  | ,   
---|---|---|---  
|  | QString  | ,   
|  | int  | ,   
|  | int  |   
| ) | |   
  
Creates a [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."). 

Parameters
     title,the| title for the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules.").   
---|---  
url,the| URL for the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules.").   
width,the| width for the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules.").   
height,the| height for the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules.").  
  
Returns
    [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."), the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules.") object that is created. 

## ◆ getWebView()

[WebView](class_web_view.html) WebViewManager::getWebView  | ( | uuid  | | ) |   
---|---|---|---|---|---  
  
Returns the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules.") with the specified UUID. 

Parameters
     id,the| UUID of the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules.") of interest.  
---|---  
  
Returns
    [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."), the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules.") object with the specified UUID. 

## ◆ tookWebViewOwnership()

void WebViewManager::tookWebViewOwnership  | ( | uuid  | ,   
---|---|---|---  
|  | QString  |   
| ) | |   
  
This event is emitted when a custom interface takes ownership of a [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."). 

  * webViewId, the UUID of the [WebView](class_web_view.html "WebView allows manipulation of WebViews such as the Instruction dialog and Script Modules."). 
  * customInterfaceUrl, the URL of the custom interface that took ownership.



[IPC](class_i_p_c.html "IPC is the main entry point for all IPC functionality.") event. 

* * *

The documentation for this class was generated from the following file:

  * [WebViewManager.pki](_web_view_manager_8pki.html)


