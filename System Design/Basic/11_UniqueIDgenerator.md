# Design a Unique ID Generator

## unique IDs usefulness:
    - Imgs/social media posts
    - video for yt
    - songs on spotify
    - order id for e-commerce
    - comments on social network
    - cash transactions for banking
    - IOT devices identification
    - Message and event driven architecture

- We see users post many pics/post comments and each is associated with ID. We need a system that generate these many unique IDs faster.

## A Very Simple Solu:
    - We can keep a counter and auto increment. 
    - But this only valid for single server architecture as it may clash (same id for different users) with distributed system.

## Requirements for Distributed Systems:
    - All IDs mmust be unique
    - Do we need IDs to be sortable as well ( may be they need it for something)
    - How fast you want these IDs (n ids/sec) to be.
    - What should be the length of IDs (32 bit, 64-bit, 128bit long id).

## Methods:
    - 1. Multi master replication:
        - if we have k servers, then we give counting 1 to k to each server.
        - Counter will increase by k for each new user.
        - Easy to implement
        - Not easy to scale as we will have to provide the new nums and rearrange ids.
    - 2. Using UUIDs:
        - It is 128 bits. 
        - Each server will have ID geerator. 
        - Simple way to generate unique IDs.
        - No coordination b/w servers needed
        - easy to scale

        - IDs are of 128 bits (too long) we will hvae to store it
        - UUIDs are alphanumeric
        - not sortable.

    - 3. Ticket Server Approach
        - This is done by flickr.
        - We use a central ticket server to generate.
        - We can choose the id types like alphanumeric, numeric etc.
        - We can ask like different IDs for users, img, videos, etc.
        - We can deploy multiple server for ticket generator.
        - Easy to implement

        - Not good for a huge system
        - Single point of failure
    
    - 4. Twitter Snowflake Approach
        - They used 64 bits for id.
            - 1 bit ==> 0
            - 41 bits ==> timestamp
            - 5 bits ==> datacenter ID
            - 5 bits ==> machine ID
            - 12 bits ==> sequence number
        - unique ids without collision
        - Fast, sortable IDs (also has timestamp info)
        
        - time Synchronization across servers is important
        - the implementation is tricky.
        - using this length time stamp we can go for 69 years.