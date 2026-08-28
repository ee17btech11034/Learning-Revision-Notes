# Api Gateway

## Intro:
    - Things like:
        - rate flow, 
        - authentication
        - how to respond
        - gate keeper.
    are handled by it.
    - We should introduce it only if we have defined the high level system

## Basic Architecture:
    - we have a server with services like payments, users, subscription.
    - As this server itself handle authentication then it becomes heavy for single server as client increase.

    - We divide these services in Microservices.
    - If we create direct connection to these microservices then it will create a security threat,
    - we will have to authenticate user everytime for each service that will increae redundancy.
    - Cost and latency will increase.
    - Monitoring is also costly.

    - We need API Gateway to handle all this.

## API Gateway:
    - It validate the request
    - Run middleware
    - Re-route
    - Transform response


    - Filtering Visualizations:
        - 1. TLS Termination:
            - Server gets many request from users.
            - In this step we block the users that are not using HTTPS.
        - 2. Authentication:
            - We can authenticate user based on many filters like people from particular region can access. 
        - 3. Routing:
            - route the req to proper server
            - it is helpful in load balance.
        - 4. Transformation:
            - If some users are asking for request that we can combine in one. then it will be helpful for us.
            - Results will be faster.
        - 5. Aggregation:
            - we can collect different outputs from different services and put them in json. 
            - can send the single json now.

    
    - Request Validation Process:
        - ```bash

                    Receive Request
                          |
                          V
                    Validate URL
                          |
                          V
                    Check Headers
                          |
                          V
                    Validate Body
                          |
                          V
                    Reject Invalid Request
                          |
                          V
                    Send Error Message
        ```


    - Middleware:
        - we have:
            - Monitoring
            - Compliance
            - Security
            - Performance

    
    - Pros:
        - Centralized Security
        - Reduced Coupling
        - Improved Performance
        - Scalability
        - Fault Tolerance

    - Cons:
        - Operational Complexity
        - Cost
        - Latency (as a service b/w client nd server)

    
    - API Gateways we can use:
        - Managed Services:
            - Amazon API Gateway (better for AWS)
            - Azure API
        - Open Source:
            - Tyk
            - Kang
            - These provides better control.