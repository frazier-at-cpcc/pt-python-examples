# Cisco Packet Tracer Extensions API: TcpConnection Class Reference

Source: https://tutorials.ptnetacad.net/help/default/IpcAPI/class_tcp_connection.html

---

[TcpConnection](class_tcp_connection.html "TcpConnection for TCP connections made from TcpProcess's listen\(\) and connect\(\).") for TCP connections made from [TcpProcess](class_tcp_process.html "TcpProcess handles and manipulates the TCP process.")'s listen() and connect(). [More...](class_tcp_connection.html#details)

##  Public Member Functions  
  
---  
ip | [getLocalIp](class_tcp_connection.html#a782661c1b2b3dbd85c7d5a12d99f4f64) ()  
| Get local Ip Address. [More...](class_tcp_connection.html#a782661c1b2b3dbd85c7d5a12d99f4f64)  
  
ipv6 | [getLocalIpv6](class_tcp_connection.html#acc92dec90932760a7e6c908897e61c21) ()  
| Get local Ipv6 Address. [More...](class_tcp_connection.html#acc92dec90932760a7e6c908897e61c21)  
  
int | [getLocalPort](class_tcp_connection.html#a53f35f2ddb263f83536d92be5f596063) ()  
| Get local [Port](class_port.html "Port holds and manipulates the ports on devices.") number. [More...](class_tcp_connection.html#a53f35f2ddb263f83536d92be5f596063)  
  
ip | [getRemoteIp](class_tcp_connection.html#a681d7ddbf862ca67a95220fddaacd824) ()  
| Get remote Ip Address. [More...](class_tcp_connection.html#a681d7ddbf862ca67a95220fddaacd824)  
  
ipv6 | [getRemoteIpv6](class_tcp_connection.html#a9115c620e160a4882311f7bd8bb0cd88) ()  
| Get remote Ipv6 Address. [More...](class_tcp_connection.html#a9115c620e160a4882311f7bd8bb0cd88)  
  
int | [getRemotePort](class_tcp_connection.html#a1afeb4abbc04065012a8de130425ed1b) ()  
| Get remote port number. [More...](class_tcp_connection.html#a1afeb4abbc04065012a8de130425ed1b)  
  
string | [getRemoteIpString](class_tcp_connection.html#afd42c1c72c0f1e875d8ff9db13339c64) ()  
| Get remote ip address in string format. [More...](class_tcp_connection.html#afd42c1c72c0f1e875d8ff9db13339c64)  
  
TcpConnectionState | [getState](class_tcp_connection.html#aa433cbbdf8c4eec38f149797c523489a) ()  
| get the tcp connection state [More...](class_tcp_connection.html#aa433cbbdf8c4eec38f149797c523489a)  
  
void | [accept](class_tcp_connection.html#abda4a7f88e6cec61999a78090b8da411) (bool)  
| Accept the connection request. [More...](class_tcp_connection.html#abda4a7f88e6cec61999a78090b8da411)  
  
bool | [close](class_tcp_connection.html#a71dd74c757a2b7b706e4cd8cb1cedc3a) ([FrameInstance](class_frame_instance.html))  
| Close the current connection. [More...](class_tcp_connection.html#a71dd74c757a2b7b706e4cd8cb1cedc3a)  
  
bool | [sendData](class_tcp_connection.html#a7a1d8a587d6c9956e2cfc4143311fe37) (QString, [FrameInstance](class_frame_instance.html))  
| Sends data over this custom TCP process. [More...](class_tcp_connection.html#a7a1d8a587d6c9956e2cfc4143311fe37)  
  
bool | [sendDataWithPduInfo](class_tcp_connection.html#ae1671ec827e5dc44e18505d0d6cc1b4f) (QString, [FrameInstance](class_frame_instance.html), QString, QString, QString)  
| Sends data over this custom TCP process. [More...](class_tcp_connection.html#ae1671ec827e5dc44e18505d0d6cc1b4f)  
  
  
## Detailed Description

[TcpConnection](class_tcp_connection.html "TcpConnection for TCP connections made from TcpProcess's listen\(\) and connect\(\).") for TCP connections made from [TcpProcess](class_tcp_process.html "TcpProcess handles and manipulates the TCP process.")'s listen() and connect(). 

## Member Function Documentation

## ◆ accept()

void TcpConnection::accept  | ( | bool  | | ) |   
---|---|---|---|---|---  
  
Accept the connection request. 

Parameters
     bAccepted,bool-| true to accept and false to reject   
---|---  
  
## ◆ close()

bool TcpConnection::close  | ( | [FrameInstance](class_frame_instance.html) | | ) |   
---|---|---|---|---|---  
  
Close the current connection. 

Parameters
     frameInstance,the| [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") object to send back   
---|---  
  
## ◆ getLocalIp()

ip TcpConnection::getLocalIp  | ( | | ) |   
---|---|---|---|---  
  
Get local Ip Address. 

Returns
    ip, local ip address 

## ◆ getLocalIpv6()

ipv6 TcpConnection::getLocalIpv6  | ( | | ) |   
---|---|---|---|---  
  
Get local Ipv6 Address. 

Returns
    ipv6, local ipv6 address 

## ◆ getLocalPort()

int TcpConnection::getLocalPort  | ( | | ) |   
---|---|---|---|---  
  
Get local [Port](class_port.html "Port holds and manipulates the ports on devices.") number. 

Returns
    int, port number 

## ◆ getRemoteIp()

ip TcpConnection::getRemoteIp  | ( | | ) |   
---|---|---|---|---  
  
Get remote Ip Address. 

Returns
    ip, remote ip address 

## ◆ getRemoteIpString()

string TcpConnection::getRemoteIpString  | ( | | ) |   
---|---|---|---|---  
  
Get remote ip address in string format. 

Returns
    string, remote ip address 

## ◆ getRemoteIpv6()

ipv6 TcpConnection::getRemoteIpv6  | ( | | ) |   
---|---|---|---|---  
  
Get remote Ipv6 Address. 

Returns
    ipv6, remote ipv6 address 

## ◆ getRemotePort()

int TcpConnection::getRemotePort  | ( | | ) |   
---|---|---|---|---  
  
Get remote port number. 

Returns
    int, remote port number 

## ◆ getState()

TcpConnectionState TcpConnection::getState  | ( | | ) |   
---|---|---|---|---  
  
get the tcp connection state 

Returns
    enum<TcpConnectionState> CLOSED = 0, // [Server](class_server.html "Server is Server device object with a terminal line.") received ACK from client and connection is closed. SYN_SENT = 1, // Indicates active open. SYN_RECEIVED = 2, // [Server](class_server.html "Server is Server device object with a terminal line.") just received SYN from the client. ESTABLISHED = 3, // Client received server's SYN and session is established. LISTEN = 4, // [Server](class_server.html "Server is Server device object with a terminal line.") is ready to accept connection. FIN_WAIT_1 = 5, // Indicates active close. TIMED_WAIT = 6, // Client enters this state after active close. CLOSE_WAIT = 7, // Indicates passive close. [Server](class_server.html "Server is Server device object with a terminal line.") just received first FIN from a client. FIN_WAIT_2 = 8, // Client just received acknowledgment of its first FIN from the server. LAST_ACK = 9, // [Server](class_server.html "Server is Server device object with a terminal line.") is in this state when it sends its own FIN. CLOSING = 10   


## ◆ sendData()

bool TcpConnection::sendData  | ( | QString  | ,   
---|---|---|---  
|  | [FrameInstance](class_frame_instance.html) |   
| ) | |   
  
Sends data over this custom TCP process. 

Parameters
     data,the| data to send to the destination.   
---|---  
frameInstance,the| [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") object. Use createFrameInstance() to create the [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") object.  
  
Returns
    bool, true if successful, otherwise false. 

## ◆ sendDataWithPduInfo()

bool TcpConnection::sendDataWithPduInfo  | ( | QString  | ,   
---|---|---|---  
|  | [FrameInstance](class_frame_instance.html) | ,   
|  | QString  | ,   
|  | QString  | ,   
|  | QString  |   
| ) | |   
  
Sends data over this custom TCP process. 

Parameters
     data,the| data to send to the destination.   
---|---  
frameInstance,the| [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") object. Use createFrameInstance() to create the [FrameInstance](class_frame_instance.html "FrameInstance holds traffic details such as PDUs, ports, etc.") object.   
customProtocol,the| custom protocol name   
customPduType,the| custom PDU type   
jsonFields,the| fields in JSON string representation:  
  
Returns
    bool, true if successful, otherwise false. 

* * *

The documentation for this class was generated from the following file:

  * [CTcpConnection.pki](_c_tcp_connection_8pki.html)


