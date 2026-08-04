# Semaphores

## OS Solution (Semaphores)
    1. Semaphores are synchronization tools using which we will attempt n-process solution.
    2. A semaphore S is a simple integer variable that, but apart from initialization it can be accessed only through two standard tomic operations:
        - Wait(S)
        - Signal(S)
    3. The wait(S) operation was originally termed as P(SP and signal(S) was originally called V(S).
    ```bash
        Wait(S){
            while(S <= 0>);
            S--;
        }

        Signal(S){
            S++;
        }
    ```
    3. Peterson's solution was confined to just two processes, and since in a general system can have n processes, Semaphores provides n-processes solution.
    4. While solving critical section problem only we initialize semaphore S=1.
    5. Semaphores are going to ensure Mutual Exclusion and Progress but does not ensures bounded waiting.
    ```bash
        P_i(){
            while(T){
                intial state
                wait(s)
                critical section
                signal(s)
                remainder section
            }
        }
    ```
    - Next process will run that will be next in CPU, not that came first. Here Bounded wait is not resolved but it was not mendatory. 


## Classic Problems on Synchronization
    - There are number of actual industrial problem we try to solve in order to improve our understand of Semaphores and their power of solving problems.
    - Here in this section we will discuss a numbe of problems like 
        - Producer consumer problem / Bounder Buffer Problem
        - Reader-Writer Problem
        - Dining Philosopher problem
        - The Sleeping Barber Problem

### Producer consumer problem
    - There are two process Producer and Consumers, producer produces information and put it into a buffer which have n cell, that is consumed by a consumer. Both Producer and Consumer can produces and consume only one article at a time.
    - A producer needs to check whether the buffer is overflowed or not after producing an item, before accessing the buffer.
    - Similarly, a consumer needs to check for an underflow before accessing the buffer and then consume an item.
    - Also, the producer and consumer must be synchronized, so that once a producer and consumer it accessing the buffer the other must wait.
    - Solution using Semaphores
        - we will be using 3 semaphores:
            -Semaphore S = 1 //CS(critical section) --> it will ensume that Producer and consumer do not access Buffer at same time
            -Semaphore E = n //Count Empty Cells --> Ensures Consume do not access if all cells are empty. (prevent Underflow)
            -Semaphore F = 0 //Count Filled Cells --> Ensures Producer does not put a new job in buffer if it is full. (prevent Overflow)
        ```bash
            wait(x) => x = x-1
            signal(x) => x = x+1


            Producer(){
                while(T){
                    //Produce an Item
                    wait(E) // overflow
                    wait(S)
                    //Add item to buffer
                    signal(s)
                    signal(E)
                }
            }
            Consumer(){
                while(T){
                    wait(F) // underflow
                    wait(S)
                    //Pick item from buffer
                    signal(s)
                    signal(F)
                    //Consume Item
                }
            }
        ```

### Reader-Writer Problem
    - Suppose that a database is to be shared among several concurrent processes. Some of these processes may want only to read the database (readers), whereas others may want to update (that is, to read and write) the database(writers).
    - If two readers access the shared data simultaneously, no adverse effects will result. But, if a writer and some other process (either a reader or a writer) access the databse simultaneously, chaos may ensue.
    - To ensure that these difficulties do not arise, we require that the writers have exclusive access to the shared database while writing to the database.
    - Solutions Conditions:
        - if a writer is accessing then neither writer nor reader can access.
        - if reader is accessing then multiple reader can access this.
    - Solution using Semaphores
        - The reader processes share the following data structures:
            - Semaphore mutex = 1, wrt = 1; // two semaphores
            - int readcount = 0; //variable
        - Resources are used for:
            - Wrt is used for synchronization b/w WW, WR, RW.
            - Semaphore reader (mutex) is used to synchrinize b/w RR. like no 2 readers update readers variable Readcount at same time
            - Readcount is simple int variable which keep counts of number of readers.
        ```bash
            Writer(){
                wait(wrt)
                CS // Write
                Signal(wrt)
            }

            Reader(){
                wait(mutex)
                Readcount++
                if (readcount == 1){
                    wait(wrt) // first
                }
                signal(mutex)
                CS//Read
                wait(mutex)
                Readcount--
                if (readcount == 0){
                    signal(wrt) // last
                }
                signal(mutex)
            }
        ```

### Dining Philosopher Problem
    - Philosophers are sitting on circular table, they need 2 chosticks to each but on table n chopsticks are there for n philosophers. 
    - Each can either eat or think.
    - Solution for this with n = 5:
        ```bash
            Void Philosopher(void){
                while(T){
                    Thinking();
                    wait(chopstick[i])
                    wait(chopstick[(i+1)%5]); //n= 5
                    Eat()
                    signal(chopstick[i])
                    signal(chopstick[(i+1)%5])
                }
            }
        ```
    - Context switch ho right after "wait(chopstick[i])" then deadlock will occur as each philosopher will have one chopstick.
    - Solutions from Deadlock prevent:
        - Allow at most four philosophers to be sitting simultaneously at the table.
        - Allow 6 chopsticks to be used simultaneously at the table.
        - Allow a philosopher to pick up her chopstick only if both chopsticks are available (do do this, she must pick them up in a critical section).
        - One phlosopher picks up her right chopstick first and then left chopstick, ie reverse the sequence of any philosopher.
        - Odd philosopher picks up first her left chopstick and then her right chopstick, whereas an even philosopher picks up her right chopstick and then her left chopstick.

### The Sleeping Barber Problem
    - Barbershop:-->
        A barbershop consists of a waiting room with n chairs and a barber room with one barber chair.
    - Customer:-->
        Customers arrive at random intervals. If there is an available chair in the waiting room, they sit and wait. If all chairs are taken then they leave.
    - Barber:-->
        The Barber sleeps if there are no customers. If a customer arrives and the barber is asleep, they wake the barber up.
    - Synchronization:-->
        The challenge is to coordinate the interaction b/w the barber and the customers using concurrent programming mechanisms.
    - Solution:-->
        - Semaphore barber = 0 //indicates if the barber is available
        - Semaphore customer = 0 //counts the waiting customers
        - Semaphore mutex = 0 //Mutex for critical section int
        - waiting = 0 //number of waiting customers
        ```bash
            Barber(){
                while(T){
                    wait(customer)
                    wait(mutex)
                    waiting -= 1
                    signal(barber)
                    signal(mutex)
                    //cut hair
                }
            }

            Customer(){
                wait(mutex)
                if (waiting < n){
                    waiting += 1
                    signal(customer)
                    signal(mutex)
                    wait(barber)
                    //Get hair cut
                }
                else{
                    signal(mutex)
                }
            }
        ```

### Harware Type Solution Test and Set
    - Software-based sol such as Peterson's are not guranteed to work on modern computer architectures. In the following discussions, we explore several more solutions to the critical selection problem using techniques ranging from hardware to software, all these solutions are based on the premise of locking -- that is, protecting critical regions through the use of locks.
    - The critical section problem could be solved simply in a single processor environment if we could prevent interrupts from occuring while a shared variable was being modified.
    ```bash
        Boolean test and set(Boolean * target){
            Boolean rv = *target
            *target = true
            return rv
        }

        while(1){
            while(test and set(&lock));
            /* critical section */
            lock = false
            /* remainder section*/
        }
    ```