# Dead-Lock
## Basics of Dead-Lock
    - In a multiprogramming environment, several processes may compete for a finite number of resources.
    - A process requests resources; if the resources are not available at that time, the process enters a waiting state. Sometimes, a waiting process is never again able to change state, because the resources it has requested are held by other waiting processes. This situation is called Deadlock.
    - A set of processes is in a deadlock state when every process in the set is waiting for an event that can be caused only by another process in the set.

## Necessary conditions for deadlock
    - It needs all 4 conditions:
        1. Mutual Exclusion
            - At least one resource must be held in a non-sharable mode; that is, only one process at a time can use the resource.
            - if another process requests that resource, the requesting process must be delayed until the resource has been released. And the resource must be desired by more than one process.
        2. Hold and Wait
            - A process must be holding at least one resource and waiting to acquire additional resource that are currently being held bu other processes. Eg Plate and Spoon.
        3. No pre-emptive
            - Resources can not be pre-empted; that is , a resource can be released only voluntarily by the process holding it, after that process has completed its task.
        4. Circular Wait
            - A set P0, P1, ..., Pn of waiting processes must xist such that P0 is waiting for a resource held by P1, P1 is waiting for a resource held by P2, ..., and  Pn is waiting for a resource held by P0. 
    
        
## Deadlock Handling Methods
    1. Prevention:
        - Design such protocols that there is no possibility of deadlock by removing atleast one deadlock condition out of 4. 
    2. Avoidance:
        - Try to avoid deadlock in run time so ensuring that the system will never enter a deadlock state.
    3. Detection:
        - We can allow the system to enter a deadlocked state, then detect and recover.
    4. Ignorance:
        - We can ignore the problem altogether and pretend the deadlocks never occur in the system.

### 1. Prevention
Remove one condition.
    - Mutual Exclusion:
        - we can not remove it as two process can not share the resource. 
        - In prevention approach, there is no solution for mutual exclusion as resource can't be mae sharable as it is a hardware property and process also can't be convinced to do some other task.
    - Hold and Wait:
        It has 3 approaches
            1. Conservative Approach: 
                - Process is allowed to run if & only if it has acquired all the resources. It is costly.
            2. Alternative protocol:
                - A process may request some resources and use them. Before it can request any additional resources, it must release all the resources that it is currently allocated. Starvation may happen as P1 may come after completing all processes.
            3. Wait time out:
                - We place a max ime outs up to which a process can wait. After which process must release all the holding resources and exit.
    - No pre-emptive:
        If a process requests some resources
            - We first check whether they are available. if they are, we allocate them.
            - if they are not,
                - We check whether they are allocated to some other process that is waiting for additional resources. if so, we pre-empt the desired resources from the waiting process and allocate them to the requesting process (Considering Priority).
                - If the resources are neither available nor held by a waiting process, the requesting process must wait, or may allow to pre-empt resource of a running process Considering Priority.
    - Circular Wait:
        - We can eliminate it by giving a natural number mapping to every resource and then any process can request only in the increasing order and if a process wants a lower number, then process must first release all the resource larger than that number and then give a fresh request.
    

Problem with prevention
    - Different deadlock Prevention approach put different type of restrictions or conditions on the processes and resources Because of which system becomes slow and resources utilization and reduced system throughput.


### 2. Avoidance
    - So, in order to avoid deadlock in run time, system try to maintain some books like a banker, whenever someone ask for a loan(resource), it is granted only when the book allow. Also Called Banker's Algorithm.
    - To avoiding deadlock we require additional information about how resources are to be requested. Which resources a process will request durin its lifetime. 
    - With this additional knowledge, the OS can decide for each request whether process should wait or not.
    - Explaination: 
        - We have "max Need" table with resource to process. "Allocation" table to tell this procees hold this many resource at that time. "system max" table is given of max resources available of types. Create "Current Need" table by (max need - allocation). create "Available" by (system max - allocation). Now just check the procees in "current need" that can be completed by taking resources from Available.
        - Sequence we get is called "Safe Sequence".
    - Safe Sequence:
        - some seq in which we can satisfies demand of every process without going into deadlock, if yes, this seq is called safe sequence.
    - Safe State:
        - If their exist at least one possible safe seq.
    - unsafe State:
        - If their exist no possible seq. Then there are chances of deadlock (not surity).

    - Read more about Banker's algorithm and safety algorithm.
    - Resource Allocation Graph
        - Deadlock can also be described in terms of a directed graph called a system resource-allocation graph. This graph consists of a set of vertices V and a set of edges E.
        - If cycle then means it can have deadlock but not necessary. 

### 3. Deadlock Detection and Recovery
    - Once a deadlock is detected there are two options for recovery from a deadlock
        1. Process Termination
            - Abort all deadlocked processes
            - Abort one process at a time until the deadlock is removed.
        2. Resourse pre-emption
            - Selecting a victim
            - Partial or Complete Rollback. 

### 4. Ignorance (ostrich Algorithm)
    1. OS behaves like there is no concept of deadlock.
    2, Ignoring deadlocks can led lead to system performance issues as resources get locked by idle processes.
    3. Despite this, many OS opt for this approach to save on the cost of implementing deadlock detection.
    4. Deadlocks are often rare, so the trade-off may seem justified. Manual restarts may be required when a deadlock occurs.