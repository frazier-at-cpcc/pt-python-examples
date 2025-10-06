# Cisco Packet Tracer Extensions API: MailBox Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_mail_box.html

---

##  Public Member Functions  
  
---  
vector< [Mail](struct_mail.html) > | [getMails](class_mail_box.html#a3fe6c663a0a7103e537209bda8e56c34) ()  
| Returns all the mails in the mailbox. [More...](class_mail_box.html#a3fe6c663a0a7103e537209bda8e56c34)  
  
void | [deleteMailAt](class_mail_box.html#a734e1c8b4f433a62a65f0f109d002e2b) (int)  
| Deletes the mail at the given index. [More...](class_mail_box.html#a734e1c8b4f433a62a65f0f109d002e2b)  
  
  
## Member Function Documentation

## ◆ deleteMailAt()

void MailBox::deleteMailAt  | ( | int  | | ) |   
---|---|---|---|---|---  
  
Deletes the mail at the given index. 

Parameters
     index,index| of the mail entry to delete.   
---|---  
  
## ◆ getMails()

vector< [Mail](struct_mail.html) > MailBox::getMails  | ( | | ) |   
---|---|---|---|---  
  
Returns all the mails in the mailbox. 

Returns
    vector<Mail>, value is a list that contains all the mails. 

* * *

The documentation for this class was generated from the following file:

  * [CMailBox.pki](_c_mail_box_8pki.html)


