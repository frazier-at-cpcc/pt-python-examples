# Cisco Packet Tracer Extensions API: PaletteDialog Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_palette_dialog.html

---

[PaletteDialog](class_palette_dialog.html "PaletteDialog allows for UI manipulation of the Palette Dialog.") allows for UI manipulation of the Palette Dialog. [More...](class_palette_dialog.html#details)

##  Public Member Functions  
  
---  
void | [setVisible](class_palette_dialog.html#a1f4ab3db466a032853dd7c01c2f536e8) (bool)  
| Shows or hides this widget from view. [More...](class_palette_dialog.html#a1f4ab3db466a032853dd7c01c2f536e8)  
  
void | [setWidgetVisible](class_palette_dialog.html#abd7de8955b208c2024fd8254361eacba) (string, bool)  
| Shows or hides the specified child widget. [More...](class_palette_dialog.html#abd7de8955b208c2024fd8254361eacba)  
  
void | [setDisabled](class_palette_dialog.html#a96b2f5181093790ecea63f1b3f6b2400) (bool)  
| Enables or disables input events to this widget. [More...](class_palette_dialog.html#a96b2f5181093790ecea63f1b3f6b2400)  
  
void | [setWidgetDisable](class_palette_dialog.html#a9a20d7bafc255f151fba8d280960a3c4) (string, bool)  
| Enables or disables the specified child widget. [More...](class_palette_dialog.html#a9a20d7bafc255f151fba8d280960a3c4)  
  
  
## Detailed Description

[PaletteDialog](class_palette_dialog.html "PaletteDialog allows for UI manipulation of the Palette Dialog.") allows for UI manipulation of the Palette Dialog. 

## Member Function Documentation

## ◆ setDisabled()

void PaletteDialog::setDisabled  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Enables or disables input events to this widget. 

Parameters
     bDisabled,true| to disable input events to this widget, false to enable input events.   
---|---  
  
## ◆ setVisible()

void PaletteDialog::setVisible  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Shows or hides this widget from view. 

Parameters
     bVisible,true| to show this widget, false to hide it.   
---|---  
  
## ◆ setWidgetDisable()

void PaletteDialog::setWidgetDisable  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Enables or disables the specified child widget. 

Parameters
     widgetName,where| widgetName can be one of the following: OutlineCheckBox, ColorFilledBtn, NoFillRB, FillColorRB, EllipseBtn, LineBtn, RectangleBtn, FreeformBtn.   
---|---  
bDisabled,true| to disable input events to this child widget, false to enable input events.   
  
## ◆ setWidgetVisible()

void PaletteDialog::setWidgetVisible  | ( | string  | ,   
---|---|---|---  
|  | bool  |   
| ) | |   
  
Shows or hides the specified child widget. 

Parameters
     widgetName,where| widgetName can be one of the following: OutlineCheckBox, ColorFilledBtn, NoFillRB, FillColorRB, EllipseBtn, LineBtn, RectangleBtn, FreeformBtn.   
---|---  
bVisible,true| to show this child widget, false to hide it.   
  
* * *

The documentation for this class was generated from the following file:

  * [PaletteDialog.pki](_palette_dialog_8pki.html)


