# CPU Scheduling
    1. It is the process of determining which process in the ready queue is allocated to the CPU.
    2. Various scheduling algorithms can be used to make this decision, such as First-come-first-serve(FCFS), Shortest Job Next (SJN), Priority and Round Robin (RR).
    3. Different algorithm support different class of process and favor different scheduling criterion.

## Type of Scheduling
    1. Non-pre-emptive: 
        - Under non-pre-emptive scheduling, once the CPU has been allocated to a process, the process keeps the CPU until it releases the CPU willingly.
        - A process will leave the CPU only:
            - When a process completes its execution (Termination state).
            - When a process wants to perform some i/o operations (Blocked state).
    2. Pre-emptice:
        - Under this, once the CPU has been allocated to a process, A process will leave the CPU willingly or it can be forced out. 
        - So it will leave the CPU:
            - When a process completes its execution
            - When a process leaves CPU voluntarily to perform some i/o operations.
            - If a new process enters in the ready states (new, waiting), in case of high priority
            - When process switches from running to ready state because of time quantum expire.

## Scheduling Criteria
    - Different CPU-scheduling algorithms have different properties, and the choice of a perticular algorithm may favour one class of processes over another. So, in order to efficiently select the scheduling algorithms following criteria should be taken into consideration:
        1. CPU Utilization:-->s Keeping CPU as busy as possible.
        2. Throughput:--> If the CPU is busy executing processes, then work is being done. One measure of work is the number of processes that are completed per time unti, called throughput.
        3. Waiting Time:--> It is sum of the periods spent waiting in the ready queue.
        4. Response Time:--> RT is the time it takes to start responding, not the time it takes to output the response.
    - Note:==> The CPU Scheduling algorithm does not affect the amount of time during which process executes or perform I/O, it affects only the amount of time that a process spends waiting in the ready queue. It is desirable to maximize CPU utilization and throughput and to minimize turnaround time, waiting time, and response time.
    - Terminology:
        - Arrival Time (AT):--> Time at which process enters a ready state.
        - Burst Time (BT):--> Amount of CPU time required by the process to finish its execution.
        - Completion Time (CT):--> Time at which process finishes its execution.
        - Turn Around time (TAT):--> Completion Time (CT) - Arrival Time (AT), Waiting Time (WT) + Burst Time(BT)
        - Waiting Time (WT):--> TAT - BT

## Scheduling Algorithms
### FCFS (First Come First Served)
    - FCFS is the simplest scheduling algorithm, as the name suggest, the process that requests the CPU first is allocated the CPU first.
    - Implementation is manage by FIFO Queue.
    - It is always non pre-emptive in nature. Matlab sab puri tarah execute honge tabhi leave krenge, apne aap hi.
    - Advantage:
        - Easy to understand, and can easily be implemented using Queue data structure.
        - Can be used for background processes where execution is not urgent.
    - Disadvantage:
        - If initial process is taking too long and later comming process are of small time then waiting time will increase. It is called Convoy Effect.
        - Convoy Effect:
            - If a smaller process have to wait more for the CPU because of Larger process then this effect is called Convoy Effect, it result into more average waiting time.
            - Solution, smaller process have to be executed before longer process, to achieve less avg waiting time.
        - It is thus troublesome for time sharing system (due to its non-pre-emptive nature), where it is important that each user get a share of the CPU on regular intervals. 

### Shortest Job First (SJF) (non-pre-emptive)
    - Shortest remaining time first (SRTF) / Shortest Next CPU Burst (Pre-emptive)
    - Whenever we make a decision of selecting the next process for CPU execution, out of all available process, CPU is assigned to the process having smallest burst time requirement. When the CPU is available, it is assigned to the process that has the smallest next CPU burst. If there is a tie, FCFS is used to break the tie.
    - it supports both version non-pre-emptive and pre-emptive (purely greedy approach).
    - In SJF (non-pre-emptive) once a decision is made and among the available process, the process with smallest CPU burst is scheduled on the CPU, it can not be pre-empted even if a new process with the smaller CPU burst requirement then the remaining CPU burst of the running process enter in the system.
    - Isme hai ki P1 ka BT = 7 hai and t=2 par hi P2 with BT = 2 aa gayi to CPU nikal dega with saying ki p1 ka BT = 7 - 2 = 5 hai and P2 ka 2 hai so P2 ko run kro.
    - Advantage:
        - Pre-emptive version gurantees minimal average waiting time so some time also reffered as optimal algorithm. Provide a standard for other algo in terms of average waiting time. 
        - Provide a better average response time compare to FCFS.
    - Disadvantage:
        - Here process with the longer CPU burst requirement goes into starvation and have response time.
        - This algo can not be implemented as there is no way to know the length of the next CPU burst. As SJF is not implementable, we can use the one technique where we try to predict the CPU burst of the next coming process.

### Priority Scheduling
    - Here a priority is associated with each process. At any instance of time out of all available process, CPU is allocated to the process which possess highest priority (may be higher or lower). 
    - Tie is brokern using FCFS order. No importance to senior or BT. It supports both pre-emptive and non-pre-emptive.
    - Advantage:
        - Gives a facility specially to system process.
        - Allow us to run important process even if it is a user process.
    - Disadvantage:
        - Here process with the smaller priority may starve for the CPU.
        - no idea of response time or WT.
    - Note:==> Specially use to support system process or important user process.
    - Ageing:--> a technique of gradually increasing the priority of processes that wait the system for long time. Eg Priority will increase after every 10 mins.

### Round Robin
    - This algo is designed for the time sharing systems, where it is not, the idea to complete one process and then start another, but to be responsive and divide time of CPU among the process in the ready state (Circular).
    - CPU scheduler goes around the ready queue, allocating the CPU to each process for a maximum of 1 time quantum say q. Up to which a process can hold the CPU in one go, with in which either a process terminates if process have a CPU burst of less than given time quantum or context switch will be executed and process must release the CPU voluntarily and enter the ready queue and wait for the next chance. 
    - Each process WT ==> (n-1)*q ==> n  process in ready queue and time quantum is q.
    - Advantage:
        - Perform best in term of avg response time.
        - Works well in case of Time sharing systems, client server architecture and interactive system.
        - Kind of SJF implementation.
    - Disadvantage:
        - Longer process may starve
        - Performance heavily depends on time quantum - if val of the time quantum is very less then it will give lesser avg response time (good but no of context switches will increase and CPU utilization will decrease)
        - no idea of priority.

### Multi Level Queue Scheduling (MLQS)
    - After all above approaches, non of them alone is enough. We need hybrid.
    - Here process are easily classified into different groups:
        - System Process (can implement it with Priority algo)
        - foreground (interactive) processes (can use RR algo)
        - background (batch) processes (can use FCFS algo)
    - A multilevel queue scheduling algorithm, partitions the ready queue into several seperate queues. The processes are permanently assigned to one queue, generally based on properties and requirement of the process.
    - there must be scheduling among the queues, which is commonly implemented fixed-priority pre-emptive scheduling or round robin with different time quantum.

### Multi-level Feedback Queue Scheduling (MLFQS)
    - Problem with MLQS is how to decide number of ready queue, scheduling algorithm inside the queue and between the queue and once a process enters a specific queue we can not change and queue after that.
    - MLFQS, allows a process to move between queues. The idea is to seperate process according to the characteristics of their CPU bursts. If a process uses too much CPU time, it will be moved to a lower-priority queue. In addition, a process that waits too long in a lower-priority queue may be moved to a higher-priority queue. This form of aging prevents starvation.
    - A process entering the ready queue is put in queue 0. A process in queue 0 is given a time quantum of 8 msec. If it does not finish within this time, it is moved to the tail of queue 1. If queue 0 is empty, the process at the head of queue 1 is given a quantum of 16 msec. If it does not complete, it is pre-empted and is put into queue 2. Processes in queue 2 are run on an FCFS basis but are run only when queue 0 and 1 are empty.
    - It has following parameters:
        - The number of queues
        - The scheduling algo for each queue
        - the method used to determine when to upgrade a process to a higher-priority queue
        - The method used to determine when to demote a process to alower-priority queue
        - the definition of MLFQS makes it the most general CPU-scheduling algorithm. It can be configured to match a specific system under design. unfortunately, it is also the most complex algorithm, since defining the best scheduler requires some means by which to select values for all the parameters.