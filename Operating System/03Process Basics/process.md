# Process
## Definition
in general, a process is a program in execution.
    - A program is not a process by default. A program is a passive entity, i.e. a file containing a list of instructions stored on disk (secondary memory) (often called an executable file).
    - A program becomes a Process when an executable file is loaded into main memory and when its PCB is created.
    - A process on the other hand is an Active Entity, which require resources like main memory, CPU time, registers, system buses, etc.
    ```bash
        PCB: Process Control Block
            When we execute a file then OS create a Data Structure PCB for that program. PCB stores data related to that program like metadata, process number etc. 
            PCB has ==> Process state, process number, process counter, registers, memory limits, list of open files. 

    ```
    - Even if two processes may be associated with same program, they will be considered as twop seperate execution sequences and are totally different process. 
    - For instance, if a user has invoked many copies of web browser program, each copy will be treated as seperate process. even though the text section is same but the data, heap, and stack sections can vary.
    - A Process consists of following sections:
        1. Text Section:-> Also known as Program Code.
        2. STack:-> Which contains the temporary data (Function Parameters, return addresses and local variables).
        3. Data Section:-> Containing global variables.
        4. Heap:-> Which is memory dynamically allocated during process runtime.
        ```bash
                                Stack
                                  |
                                  | grow this side
                                  V

                                  ^
                                  | grow this side
                                  |
                                 Heap
                                _______
                                 data
                                ______
                                 text
        ```

## PCB (Process Control Block)
    - Each process is represented in the OS by a process control block (PCB) - also called a task control block.
    - PCB simply serves as the repository for any information that may vary from process to process. It contains many pieces of information associated with a specific process, including these:
        1. Process State:-> The state may be new, ready, running, waiting, halted, and so on. 
        2. Program Counter:-> The Counter indicates the address of the next instruction to be executed for this process. 
        3. CPU Registors:-> The registers vary in number and type, depending on the computer architecture. They include accumulators, index registers, stack pointers, and general-purpose registers, plus any condition-code information. Along with the program counter, this state information must be saved when an interrupt occurs, to allow the process to be continued correctly afterwards.
        4. CPU-scheduling information:-> This information includes a process priority, pointers to scheduling queues, and any other scheduling parameters. 
        5. Memory Management information:->  This info may include such items as the values of the base and limit registers and the page tables, or the segment tables, depending on the memory system used by the OS. 
        6. Accounting information:-> this info includes the amount of CPU and real time used, time limits, account numbers, job or process numbers, and so on.
        7. I/O status information:-> this info includes the list of I/O devices allocated to the process, a list of open files, and so on.

## Process States
A process changes states as it executes. The state of a process is defined in parts by the current activity of that process. A process may be in one of the following states:
    - New:--> The process is being created.
    - Running:--> Instructions are being executed.
    - Waiting (Blocked):--> The process is waiting for some event to occur (such as an I/O completion or reception of a signal).
    - Ready:--> The process is waiting to be assigned to a processor.
    - Terminated:--> The process has finished execution.
    ```bash
            New
             |
             | admitted
             |
             V         
            Ready<----------interrupt-----Running-----------------Exit-----> Terminate
             ^  `---schedular dispatch----->`   |
             |                                  |
         I/O or event completion            I/O or event waiting
             |                                  |
              `----------Waiting------<--------<`
    ```


## Schedulers
    - A process migrates among the various scheduling queues throughout its lifetime. The OS must select, for scheduling purposes, processes from these queues in some fashion. The selection process is carried out by the appropriate scheduler.
    - Types:
        - Long Term Scheduler (LTS)/ Spooler:
            LTS determine which processes enter the ready queue from the job pool. Operating less frequently than short-term schedulers, they focus on long term system goals such as maximizing throughput.
        - Medium-term scheduler:
            This swaps processes in and out of memory to optimize CPU usage and manage memory allocation. By doing so, it adjusts the degree of multiprogramming and frees up memory as needed. Swapping allows the system to pause and later resume a process, improving overall system efficiency.
        - Short Term Scheduler (STS)/ CPU Schedulers:
            This selects from among the processes that are ready to executer and allocates the CPU to one of them.

## Dispatcher
    - It is the module that gives control of the CPU to the process selected by the short term scheduler.
    - This function involves the folloeing: switching context, switching to user mode, jumping to the proper location in the user program to restart that program.
    - The dispatcher should be as fast as possible, since it is invoked during every process switch. The time it takes for the dispatcher to stop one process and start another running is known as the dispatch latency.
    - PCB ke data ko save karna and new process ke data ko load krna and uska PCB data pull karna.

## CPU Bound and I/O Bound Process
    - A process execution consists of a cycle of CPU execution or wait and i/o execution or wait. Normally a process alternates between two states.
    - Process execution being with the CPU burst that may be followed by a i/o burst, then another CPU and i/o burst and so on. Eventually in the last will end up on CPU burst. So, process keep switching b/w the CPU and i/o during execution.
    - I/O Bound Processes:-->
        This is one that spends more of its time doing I/O that it spends doing calculations.
    - CPU Bound Processes:-->
        This generates I/O requests infrequently, using more of itstime doing computations.
    - It is important that the long-term scheduler select a good process mix of I/O bound and CPU bound processes all processes are I/O bound, the ready queue will almost always be empty, and the short-term scheduler will have little to do. Similarly, if all processes are CPU bound, the I/O waiting queue will almost always be empty and devices will go unused, and again the system will be unbalanced. 

## Context Switch
    - Switching the CPU to another process requires performing a state save of current process and a state restore of a different process. This task is known as a context switch.
    - When a context switch occurs, the Kernel saves the context of the old process in its PCB and loads the saved context of the new process scheduled to run. Context-switch time is pure overhead, because the system does no useful work while switching.