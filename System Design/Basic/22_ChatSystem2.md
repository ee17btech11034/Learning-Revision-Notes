# Chat System:

- Previous was for client side. Here we will discuss for millions users.

## Sending a message:
    - We need a proper structure to send msg.

### Message_id:
    - we need msg_id unique for all msgs. We need unique id generation on massive scale that it should generate unique ids for all msgs. 
    - This id will be helpful in telling me that this msg came first (handy in sorting).
    - We can not fully rely n created timestamp bcz:
        - there are different timezones
        - user can alter time for a machine
        - if we want to use it then we will have to store till miliseconds/ nanoseconds. That will be extra memory consumption.
    - There are 3 ways to generate:
        - 1. Auto increment:
            - Suitable for SQL dbs but not for NoSQL.
        - 2. Global Sequence Generator:
            - Ensures uniqueness and sortability across systems. (Similar to twitter approach and takes UTC timezone)
        - 3. Local Sequence Generator:
            - Simpler implementation but limited uniqueness (work for small systems).

## User Journey: Connection
    - Once user gets a server from server pool and stablish a web-socket connection, ready to send msg.

### Service DIscovery:
    - User Login:-> User initiates login process
            |
            V
    - Authentication:-> Backend authenticates user
            |
            V
    - Server Selection:-> Service discovery selects server
            |
            V
    - Server Connection:-> User connects to selected server


### Sending a message:
    - This chat server will connect to an id generator.
    - As soon as we hist 'Send' button then this id generator gets triggered and grab an id and put it in message template.
    - this id will be unique in entire system. 
    - Chat server will take this message and places in 2 different locations:
        - 1. Message sync queue (send msg to their respective clients)
            - we can have single queue for multiple users.
            - we can have single queue for single chat system or there are many ways possible.
        - 2. Databases (useful to retrieve the older messages).

### Receive:
    - When B is connected to 'chat server' then it subscribe to the channel that if any message for 'B' then send that.
    - subscribe to 'Message sync queue'.
    - If user B is online then it fetches and deliver to B.
    - If B is offline then it will notify "Push Notification Service".

## Group Messages:
    - We use pub-sub model as eache user can not maintain one queue for each.

## Synchronize against Devices:
    - Each device has the msg id they have received. 
    - this way the can fetch all messages newer than that.

-- Offline telling service just checks status around every 30 sec to 60 sec. 