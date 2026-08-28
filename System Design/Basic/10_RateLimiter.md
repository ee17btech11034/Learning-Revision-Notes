# Design Rate Limiter

## Requirements Gather
    - 1. Is this rate limiter client side or server side?
        - Server side.
    - 2. How should I throttle the request?
        - We want system to throttle a req on multiple coonditions like (multiple request from same ip, same username or other parts)
    - 3.  Do we want to inform user that their request gor throttled/denied?
        - Yes, we want to inform.
    - 4. Do you want to design a distributed system or a single machine system?
        - Distributed
    - 5. 


## What kind of Implementation is possible:
    - Client Side:
        - not a good idea, as they can install fotware to manipulate the request.
        - We can manage servers, so better to put it that way.
    - Server Side:
        - Here we can put everything like server, Rate limiter in same server. This is not a good idea. As it will increase the load.
        - Better to put a API gateway b/w client and API server.
        - We will implement Rate Limiter in API Gateway.

## Algorithms to implement:
    - 1. Token Bucket Algorithm
        - we have a bucket and a fe-filler.
        - Each sec refiller puts n token (accepting n req/sec) in bucket.
        - A req come and take the token if available else denied or put in retry queue. 
        - Advantages:
            - Very easy to implement
            - Memory Efficient
            - Allows bursts of traffic
        - Disadvantages:
            - Tuning the refill rate & bucket size is tricky (as what if no req in last 5 sec and suddenlt 20 req came how will we handle tokens and size capping and all).
    
    - 2. Fixed Window Counter
        - At each sec we will accept only n req. 
        - At start of each sec wie will take the n req. If next sec is counted then we will come to zero. 
        - Advantage:
            - Very easy to implement
            - Memory Efficient
            - Allows us to dynamically manage quota.
        - DisAdvantage:
            - We get get n req in last few milisec of sec and n req in first few milisec at next window. If we see from that time window percepective we got 2n req. 
    
    - 3. Sliding Window log Algorithm
        - We log all the request coming to us.
        - We keep track of all coming requests in that time frame. If it exceed n req then we drop that but we keep the entry in log
        - As time passes that 1 req then older entries are getting deleted.
        - Advantages:
            - Very accurate, and requests are handled correctly in a rolling window
        - Disadvantage:
            - Not memory efficient as we need to keep entry.

## Basic high-Level Design
    - To make it faster we store in Redis. 
    - We want to throttle based on multiple rules, we will have to store those rules as well.
    - We can have a Rules Database and we can use a Cached Rules. Tgis way we don't have to query the Rules-db again and again.
    - Rate limiter will either drop the request or provide the denied message to user or retry it using Queue.

## Handling a Distributed Scenario
    - If Different Rate limiters are in different regions.
    - we use single redis store for all rate limitors, so we know everything about each user. 
    - Like if user is connected to limiter1 and then connected to limiter2. This way user is using resources.