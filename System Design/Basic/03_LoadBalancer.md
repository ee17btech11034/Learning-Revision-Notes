# Load Balancer

    - When a lots of req comes then a single server could go overwhelem.
    - Single server will delay in response time.

    - We can have multiple machines as server. 
    - But we need something that sends requests to these machines/servers. This job is handled by Load Balancer.


# Types of Load Balancing:
    - Lease Connection:
        - Request will go to server which has least no of requests.
    - Round Robin Scheduling:
        - We can keep aloting the requests to servers in round/circular fashion.
        - If heavy req bundles on a single machine then it becomes issue.
    - Weighted Round Robin:
        - If a machine is more capable then we alot multiple requests to that machine, rest gets the same.
    - IP Hashing:
        - When we want clients from a region with similar IP to connect with a particular machine. 
        - It is useful in premium services for premium clients


# Advantages:
    - Traffic is distributed and processed in parallel
    - Easy to scale.
    - High Availabiliy (If one server machine is down, still we will be up)

# Disadvantages:
    - A load balancer can get very complex and not easy to setup (like what if machine is down, server not responding, stuck like this)
    - Load Balancer is a single point of failure
    - If load balancer is compromised then system can go down (if hackers divert all traffic to single server).