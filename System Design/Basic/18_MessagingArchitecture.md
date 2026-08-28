# Distributed Messaging Architecture
    - Queue, Streams
    - Kafka

    - To transmit messages b/w producer and consumer, with surity that data/msg will reach. Even with million of msgs.

    - Kafka is open source, distributed event streaming platform which we can either use as a stream or message queue.


## Simple Single Queue:
    - We have q single queue with producer and a consumer. Consumer can be human, app, website, etc.
    - Producer put the event in queue
    - Consumer consumes sequenceally.

    - It is ood for very small system.
    - We can handle multiple type of events in it but limited. 
    - 
    - but if we have thousand / millions of message then we could nt even process it. and Memory can get full.

## Multiple Queues:
    - Instead of single queue, we can get multiple queues but problem here is we will have to take the events according to time.
    - We will havr to compare the time for all queues and then pick the oldst event. 
    - this will be waste of CPU cycles and resources as well as memory.

## Multiple queues but one queue for one type of event:
    - Like One queue for Game like Cricket, another for football, etc.
    - This way we can get the events in sorted manner for particular type of event (game). 
    - But issue here is, what if we have multiple games of same type, like 2 cricket matches are live at same time. similarly n different events of same type. This will be harder to manage.

## Kafka:
    - Here we have topics and each topic can have n partitions. 
        - topics can be similar to "Games" and partitions means n games of same type are live.
    - We can have multiple producers and Consumers.

    - Terminpology:
        - Broker:
            - Individual servers that make up the cluster and store information
            - It is a server that handles the data.
            - we can have k number of brokers
            - We can scale it and broken can be of different capacity
            - All brokers combined behaves like a single System
        - Partitions:
            - Ordered immutable sequence of messages that are continually appended to.
            - We can make pertitions in each broker (each broker can have different partitions). Partitons are just like allotin a memory block for some calculations.
            - All these details are handled in Matadata that is handled in Kafka.
        - Topics:
            - Logical grouping of partitions. You publish and subscribe to topics.
            - Game of Criket can be called Topic.
            - Single topic is not only on single broker.
            - Kafka points topic to partitions in brokers.
            - Data is distributed on different brokers.
        - Leader:
            - Handles all incoming data.
        - Follower:
            - Passively replicate leader.

    - Fault tolerance:
        - What if we store data of topic on a single broker and that broker is out of reach then we will be unable to access.
        - Kafka maintain a Leader and some followers on different brokers. Followers have the same data as Leader.
        - If eader broker is down the follower in another broker will take place and become leader. 
        - Then either kafka will restore the broken broker or create a new partition and make follower if available.

    - Sending & Receiving Messages:
        - Topic:
            - Based on this, kafka decide where to put the info.
        - key-val:
            - key-val pairs. 
            - Key is helpful to decide the partition inside the Topic.
            - If key is not given, kafka will consider it as single partition in topic and can put in any.
        - Timestamp:
            - helpful to keep track of incming event in order.
            - If any event came later but timestaamp is old then Kafka arranges it accordingly and treat it old.
        

    - Kafka as Stream Vs queue:
        - When want to process messages asynchronously (eg processing yt videos) --> Message queue. Like when ever server will be available then it will pick from queue
        - When we need system for live event (eg live yt comments, live fb comments) --> stream

    
    - Once a msg is in kafka then we can not delet it.