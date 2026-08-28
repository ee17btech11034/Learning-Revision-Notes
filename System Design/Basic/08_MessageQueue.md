# Message Queue & CDN

## Message Queue:
    - If reqsts and then our service may get overwhelemend and may get slower.
    - We provide them a token and pull the service token wise ans serve the request.
    - We have 2 components "Producer" and "Consumer". Producer puts the req in queue and cunsumer pulls the req from queue an serves it.
    - Lot of implementations are there like RabbitMQ, Apache Kafka, Amazon SQS, etc.
    - Advantages:
        - Decoupling:
            - It allows us to seperate components and make them free sooner.
            - We do not need a constant connection with server or client.
        - Security:
            - We can check the req in queue if any security threat is exist.
        -Scalibility:
            - The system becomes more scalable as more clients can send in req asynchronously.
        - Fault Tolerance:
            - We can process the message again, if the first attempt fails. This makes the system fault tolerant.
    
    - We should not use this in chatbot message service. Like we do not want delay.
    - Challenges:
        - Making sure that the ordering of messages remains same in the order they were received. OR we want to give priority to any client.
        - Handling duplicate messages to avoid redundency and processing cycles.
        - Adding something in the middle introduces latency. The benefits should outweigh the lag.


## CDN (Content Delivery Network):
    - When server is in one continent and users are accessing that from all around the world. It will increast the latency.
    - We deploy server or main parts centrally.
    - We can stablish CDN networks in different regions.
    - It stores, cache the content we need for our application.
    - Request goes to nearby CDN and if it is available there then it will respond or if not available then it will ask for server.
    - Pros & Cons:
        - Faster Load Time
        - Reduces latency
        - Caching STatic content (like images or something static to load the site).

        - We must make sure that data should always be fresh
        - All the CDN insfrastructure is costly.