# Proxy
    - Security is necessity.
    - It is an intermediate that sits b/w client and server, It is responsible for handling all req and res.
    - We want to give access to only certain users.

# Forward Proxy:
    - All clients connect to proxy server, 
    - Based on the connections Proxy can either allow to access it or refuse.
    - Eg Clients on private network and server is on internet, school network, workplace network, etc can only be accessed by connecting with VPN.
    - Advantages:
        - Logging:
            - Allows us to log each request made by user
        - Traffic Control:
            - We can govern what traffic to pass and which to block
            - not a single user try to busy the server
        - Encryption:
            - Make sure that all the traffic going through the proxy server is encrypted
        - Client Anonymity:
            - Servers do not know who clients are
            - For server, FP is the client.
    - Eg When we want to access the site that is banned in India, but that is on internet for others. We connect to FP and then access that.

# Reverse Proxy:
    - Eg Clients are on internet, Resources on private network.
    - Clients connect to RP and then it connects with server.
    - Advantages:
        - Server Anonimity:
            - Clients do not know what servers are they connecting to.
        - DDOS Attack Prevention:
            - DDoS is when sigle user put multiple req in small time frame to hiject server.
            - Without information about the server, we can't have a DDoS attack
            - As server's IP is not disclosed.
        - Optimization:
            - Caching:
                - We can implement some caching here.
            - load balancer:
                - this can act as load balancer as well
    - Again we have single point of failure, low latency b/z of middle step.