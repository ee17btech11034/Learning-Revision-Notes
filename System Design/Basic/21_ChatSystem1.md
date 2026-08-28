# Design a chat System

## Basic Design:
    - A server stores messages from A and transmit messages to B, in both direction.


## Requirmeents:

## Features:
    - We can add broadcast as well.
    - We can add 'upload attachments' as well.

## Communication Techniques:
    - 1. Polling:
        - Client periodically check for new messages from the server.
        - Here client create a connection and close it repeatitive that consume server bandwidth.
        - not good as it bombard server with req msg. And there will be so many connections open . 
    
    - 2. Long Polling:
        - Client sends a request, server receives it and wait for some time (3 sec / 5 sec).
        - Client wait for a server response before checking again.
        - Then after sometime server response. 
        - Then again client sends a req.
        - connection duration increases, as server will not close connection immediatly.
        - but is is not real time response. It may face some delay.
    
    - 3. WebSocket:
        - A persistent connection for real time communication.
        - A bi-directional message b/w A & B.
        - client will send 'HTTP Handshake' to server.
        - server will send 'ACK' to client. And this will be converted to web-sockets connection.
        - This connection will stay. 
        - A & B can chat.

## Systems:
### Stateless System:
    - In each req we do not remember anything from previous request.
    - We may store some cache, but that is different.

### Stateful System:
    - It stablish a web-socket connection for A & B to server. 
    - It is real-time communication.
    - Harder to scale so we use 'Sticky connection', etc.
    - Usages: Live Gaming, colleborative online work, chat app.


## High Level Design:
    - Presence Service:
        - Used to notify the status of 2 different individual.
        - it ois stateful as then only we may know. 
    - Read-Receive Service:
        - Tells users that msg is received  or read.