# Process Synchronization & Race Condition
    - As we understand in multiprogramming environment a good number of processes compete for limited number of resources. Concurrent access to shared data at some time may result in data inconsistency eg.
        ```bash
            P(){
                read(i); --> assume i is stored in sga==hared location 
                i = i+1; --> assume here context switch happened, so below write condition will run in next but if this time any other process tries to read i then it will find old val ad write is not executed.
                write(i);
            }
        ```
    - Race Condition is a situation in which the output of a process depends on the execution sequence of process. ie if we change the order of execution of different process with respect to other process the output may change.

## General Structure of  aProcess:
        - initial Section:--> Where process is accessing private resources.
        - Entry Section:--> It is that part of code where, each process request for permission to enter its critical section.
        - Critical Section:--> Where process is access shared resources
        - Exit Section:--> It is the section where a process will exit from its critical section.
        - Remainder Section:--> Remaining Code.

## Criterion to solve Critical Selection Problem
    - Mututal Exclusion:
        -No two process should be present inside the critical section at same time, ie only one process is allowed in the critical section at an insance of time.
    - Progress:
        - If no process is executing in its critical section and some processes wish to enter their critical sections, then only those processes that are not executing in their remainder sections can participate in deciding which will enter its critical section next (means other process will participate which actually wish to enter), there should be no deadlock.
    - Bound Waiting:
        - There exists a bound or limit on the number of times a process is allowed to enter its critical section and no process should wait indefinitely to enter the CS.
    Note==> Mutual Exclusion and Progress are mendatory requirements for solution. Bounded waiting is optional. 

## Solutions to Critical Section Problem
We generally have following solutions:
    1. Two Process Solution (write for 2 process and then generalize it for n)
        a. Using Boolean variable turn
        b. Using Boolean array flag
        c. Peterson's Solution
    2. OS Solution
        a. Counting Semaphore
        b. Binary Semaphore
    3. Hardware Solution
        a. Test and Set Lock
        b. Disable interrupt

1. Two Process Sol:
    a. Using Boolean variable turn
        ```bash
            P0(){
                while(1){
                    while(turn != 0);
                    critical section
                    turn = 1
                    remainder section
                }
            }
            P1(){
                while(1){
                    while(turn != 1);
                    critical section
                    turn = 0
                    remainder section
                }
            }

            Here we maintain turn variable. But it will loop like P0 --> P1 --> P0 --> P1, etc.
            It has Mututal exclusion but progress is failed as they are not moving and what if P1 do not want to run the critical section but still because of tun var it will have to go to critical section.
            Invalid algorithm.
        ```
    
    b. Using Boolean array flag
        ```bash
            P0(){
                while(1){
                    flag[0] = T
                    while(flag[1]);
                    critical section
                    flag[0] = F
                    remainder section
                }
            }
            P1(){
                while(1){
                    flag[1] = T
                    while(flag[0]);
                    critical section
                    flag[1] = F
                    remainder section
                }
            }

            Here we maintain 2 cell flag array, initialized with False. 
            It has Mututal exclusion and progress but what if before while(flage[]) (line 2 ) it has a context switch then it will become deadlock as both arr will be True and nobody can enter.
            Invalid algorithm.
        ```
    
    c. Peterson's Solution
        ```bash
            P0(){
                while(1){
                    flag[0] = T
                    turn = 1
                    while(turn == 1 && flag[1] == T);
                    critical section
                    flag[0] = F
                    remainder section
                }
            }
            P0(){
                while(1){
                    flag[1] = T
                    turn = 0
                    while(turn == 1 && flag[0] == T);
                    critical section
                    flag[1] = F
                    remainder section
                }
            }

            It satisfy all 3. 
        ```

    ## Dekker's Algorithm
        just a version of peterson's sol.