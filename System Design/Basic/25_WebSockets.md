# Web Sockets:

## 1. HTTP:
    - Client ask first.
    - Server responds back.
    - Best in published documents / blog articles.
    - But issue is if information is updated on server then it will not be updated on client sie until refresh.

## 2. Polling (Short polling):
    - Here to solve the above problem, client continuouslypol server that "any new data?". 
    - Best in Weather apps.
    - Too many wasted req if freq requests are happening.
    - But if gap is too big then it migh be delayed.

## 3. Long Polling:
    - Client make a request and server will respond after some time. 
    - Best when user req to complete payment and screen shows "do not refresh page" as it is saying to not make anoher request. Once payment is done then server send the response.
    - There will be many open connections on server side.
    - If no new info is there then it is worst.

## 4. Server Sent Events (SSE):
    - Client open a single connection and leaves it open.
    - Server pushes a stream of events down it as they happen.
    - AI apps as they send the ans to client and client can not send data in midway. Once that is done then only a new connection is stablished and client ask next/new que.

## 5. Web Sockets:
    - Both sides can send the data on full duplex persistent mode.
    - Because of persistent connection, hard to scale.
    - We use Pub/Sub model.
    - Upgrade req to web sockets from HTTP req (to check if server is available).