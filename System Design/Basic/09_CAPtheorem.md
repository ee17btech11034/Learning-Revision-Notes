# CAP Theorem


## Parameters to evaluate a Distributed system
    - Consistenchy:
        - The system should deliver the same results no matter how and from where we query.

    - Availability:
        - The system should always return some response or result.
    
    - Partition Tolerance:
        - The system should be functional even if one partition is disconnected.

## CAP Theorem
    - We can not achieve all three at any time.

    - CP Systems:
        - It must be consistent and Partition tolerance; we can sacrifice the Availability. We can showw service not available if service is down.
        - Eg Banking Systems
    - CA:
        - It must be consistent and Availability tolerance; we can sacrifice the Partition tolerance.
        - Eg Ticket Booking Systems (Like if payment service is down then we have nothing to do in ticket booking system)
    - PA:
        - It must be Partition tolerance and Availability tolerance; we will get the consistency eventually.
        - Eg Social Networking Systems (No need to show the change immediately).

## Why not all 3:
    - We will have to sacrifice one of them. 
    - think like 2 servers are connected.
    - and their connection is lost. 
    - If we want tem to provide the response then we will not get the consistency as data may be different in both.
    - If we want tem to provide the consistency then we will not respond the client until it is fixed (not available).