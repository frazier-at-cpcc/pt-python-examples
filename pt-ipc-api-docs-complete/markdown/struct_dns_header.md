# Cisco Packet Tracer Extensions API: DnsHeader Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/struct_dns_header.html

---

DNS header structure. [More...](struct_dns_header.html#details)

##  Public Attributes  
  
---  
int | [queryId](struct_dns_header.html#a2d9958c629e9ace853ed551119dd05f3)  
bool | [response](struct_dns_header.html#aaa6040aed6288dbfb3fd2cc4f5dfdc5d)  
int | [opCode](struct_dns_header.html#a193828233160a66d0a1050ad56afda04)  
bool | [isAuthoritative](struct_dns_header.html#adcc865797644a4a16a804b8da33c7902)  
bool | [isTruncated](struct_dns_header.html#a41d1f38aaeab103ec9a74b3d4d927fc4)  
bool | [isRecursionDesired](struct_dns_header.html#acb03428da8042aef56857bb890a6f8e4)  
bool | [isRecurionAvailable](struct_dns_header.html#ad153014230b8d2a22d6d1730fd0a1b29)  
int | [responseCode](struct_dns_header.html#aa3bbe648ebb25f58cd9f8ef4e0543c0e)  
int | [numQuestions](struct_dns_header.html#a6e3f8ad5d9e929672052481534a26d93)  
int | [numAnswerRecords](struct_dns_header.html#adfda8823469230d4015f8f9944f97640)  
int | [numAdditionalRecords](struct_dns_header.html#a6b11d4ffced6ed12b9e1a53c3f59ff7b)  
[DnsResourceRecord](struct_dns_resource_record.html) | [dnsQueryRr](struct_dns_header.html#adc262465ba5a1d8592669d5305ea6eaf)  
vector< [DnsResourceRecord](struct_dns_resource_record.html) > | [vectAnswerRrs](struct_dns_header.html#a9c1cbf48ac1d95d2010f078dca9c6ffa)  
vector< [DnsResourceRecord](struct_dns_resource_record.html) > | [vectAuthorityRrs](struct_dns_header.html#a91f8c8057bdc7e8b426e36c3e4637bca)  
vector< [DnsResourceRecord](struct_dns_resource_record.html) > | [vectAdditionalRrs](struct_dns_header.html#a5b2ce1c75bdddd867a1030fb63bdaa50)  
  
## Detailed Description

DNS header structure. 

## Member Data Documentation

## ◆ dnsQueryRr

[DnsResourceRecord](struct_dns_resource_record.html) DnsHeader::dnsQueryRr  
---  
  
## ◆ isAuthoritative

bool DnsHeader::isAuthoritative  
---  
  
## ◆ isRecurionAvailable

bool DnsHeader::isRecurionAvailable  
---  
  
## ◆ isRecursionDesired

bool DnsHeader::isRecursionDesired  
---  
  
## ◆ isTruncated

bool DnsHeader::isTruncated  
---  
  
## ◆ numAdditionalRecords

int DnsHeader::numAdditionalRecords  
---  
  
## ◆ numAnswerRecords

int DnsHeader::numAnswerRecords  
---  
  
## ◆ numQuestions

int DnsHeader::numQuestions  
---  
  
## ◆ opCode

int DnsHeader::opCode  
---  
  
## ◆ queryId

int DnsHeader::queryId  
---  
  
## ◆ response

bool DnsHeader::response  
---  
  
## ◆ responseCode

int DnsHeader::responseCode  
---  
  
## ◆ vectAdditionalRrs

vector<[DnsResourceRecord](struct_dns_resource_record.html)> DnsHeader::vectAdditionalRrs  
---  
  
## ◆ vectAnswerRrs

vector<[DnsResourceRecord](struct_dns_resource_record.html)> DnsHeader::vectAnswerRrs  
---  
  
## ◆ vectAuthorityRrs

vector<[DnsResourceRecord](struct_dns_resource_record.html)> DnsHeader::vectAuthorityRrs  
---  
  
* * *

The documentation for this class was generated from the following file:

  * [CDnsHeader.pki](_c_dns_header_8pki.html)


