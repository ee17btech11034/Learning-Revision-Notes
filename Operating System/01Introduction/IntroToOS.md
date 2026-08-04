# Operating System
## Definitions:
    1. Intermediary: 
        - Acts as intermediary b/w user and h/w.
    2. Resource manager/Allocator: 
        - OS controls and coordinates the use of system resources among various application programs in an unbiased fashion.
    3. Platform: OS provides a platform on which other application program can be installed, provides the environment within which programs are executed.

## Goals of OS
    1. Primary Goal:=> Convenience / User Friendly
    2. Secondary Goal:=> Efficiency (Using resources in efficient manner), Reliability, Maintainability.

## Functions of OS
To achieve the goal we need some steps these are called Functions.
    1. Process Management
        - involves handling the creation, scheduling, and termination of processes, which are executing programs.
    2. Memory Management
        - Manages allocation and deallocation of physical and virtual memory spaces to various programs.
    3. I/O Device Management
        - Handles I/O operations of peripheral devices like disks, keyboards, etc., including buffering and caching.
    4. File Management
        - manages files on storage devices, including their information, naming, permissions, and hierarchy.
    5. Network Management
        - manages network protocols and functions, enabling the OS to establish network connections and trasfer data.
    6. Security Management
        - Ensures system protection against unauthorized access and other security threats through authentication, authorization, and encryption.

## Major Components of OS
    1. Kernal:
        - Centraol Component --> manages the system's resources and communication b/w hardware and software.
    2. Process Management
        - Processor Schedular --> Determines the execution of processes.
        - Process Control Block (PCB) --> Contains process details such as process ID, priority, status, etc.
        - Concurrency Control --> Manages simultaneous execution.
    3. Memory Management
        - physical memory management --> manages RAM allocation
        - Virtual memory Management --> Simulates additional memory using disk space.
        - Memory Allocation --> Assigns memory to different processes.
    4. File System management
        - File Handling --> manages the creation, deletion, and access of files and directories.
        - File Control Block --> Stores file attributes and control information.
        - Disk Scheduling --> Organizes the order of reading or writing to disk.
    5. Device Management
        - Device Drivers --> Interface b/w the hardware and the OS
        - I/O Controllers --> Manage data transfer to and from peripheral devices.
    6. Security and Access Control
        - Authentication --> Verifies user creds.
        - Authorization --> Control access permissions to files or directories
        - Encryption --> Ensures data confidentiality and integrity.
    7. User Interface
        - Command Line Interface (CLI) --> Text based user interaction. 
        - Graphical user Interface (GUI) --> Visual, user-friendly interaction with the OS
    8. Networking
        - Network Protocol --> Rules for communication b/w devices on a network
        - Network Interface --> manages connection b/w the computer and the network. 

## Classification of OS
1. Batch OS:
    - Early computers were not interactive device, there users used to prepare a job which consist three parts 
        a. Program
        b. Control information
        c. Input data
    - Only one job is given input at a time as there was no memory, computer will take the input then process it and then generate output.
    - Common input/output device were punch card or tape drives. So there devices were very slow, and processor remain ideal most of the time.
    - To speedup the processing job with similar types ( for eg FORTRAN jobs, COBOL jobs, etc.) were batched together and were run through the processor as a group/batch.
    - in some system grouping is done by the operator while some systems it is performed by the  'Batch Monitor' resided in the low  end of main memory.
    - then jobs (as deck of punched cards) are bundled into batches with similar requirement. 
    ```bash
                  ___________
        User --> |          |                 ________
        User --> |          |------ Jobs---> | Batch |              __________
        User --> | Operator |                |_______|------------>|
        User --> |          |                 ________             | Computer
                 |__________|------ Jobs---> | Batch |------------>|___________
                                             |_______|
    ```

Still Computer was using cards so it made some faster because of Batch method but still processor were reading data from input and output that are very slow than processor. To overcome this we found
2. Spooling (Simultaneous Peripheral Operations online):
    - In computer system input-output devices, such as printers are very sow relative to the performace of the rest of the system.
    - Spooling is a process in which data is temporarily held in memory or other volatile storage to used by a device or a program.
    ```bash

                        |     Disk     |
                        |______________|
                          ^  ^  |  |
                    ______`__`__V__`____
    Card Reader ---|------`        `---|------> Printer
                   |      Memory       |
    
    ```
    - First we read from card reader and put that data into Disk, then use disk to fetch the data. tis way disk is faster then card reader.
    - Most common iplementation is Keyboard, mouse, printer. In printer spooling, the file that are sent to printer are first stored in the memory of printer and then once done printer fetch and print it. Some time we see keyboard freeze, reason is it is stored but did not sent or was noy pulled by computer.


3. Multiprogramming OS:
    - Multiple jobs: keeps several jobs in main memory simultaneously, allowing more efficient utilization of the CPU.
    - Job Execution: The OS picks and begins to execute one of the jobs in memory.
    - Waiting Jobs: Eventually, a job may need to wait for a task, such as an I/O operation to complete.
    - Switch Job: CPU takes the next job as it is in waiting phase. It does not run jobs parallely but it feels like that.
    - This way, we utilize CPU effectively.
    - Non-multiprogrammed: CPU sits idle while waiting for a job to complete.
    - Advantages:
        - High CPU utilization, Less waiting time, multi-task handling, shared cpu time
    - Disadvantage:
        - Complex scheduling (Difficult to program), Complex memory management (intricate handling of memory is required).

4. Multitasking OS:
    - Also known as Multitasking OS, time sharing, multiprogramming with Round Robin, Fair-Share.
    - Time sharing is a logical extension of multiprogramming, it allows many users to share the computer simultaneously. The CPU executes multiple jobs (may belong to different user) by switchingg among them, but the switches occur so frequently that, each user is given the impression that the entire computer system is dedicated to his/her use, even though it is being shared among many users. 
    - In modern OS, we are able to run multiple apps parallely by context switching that creates illusion of parallelism.
    - It is multiprogramming + time sharing.
5. Multiprocessing OS/ Tightly Coupled System
    - It refers to the use of two or more Central processing unit (CPU) within a Single computer system. These multiple CPU's share system bus, memory and other peripheral devices. 
    - Multiple concurrent processes each can run on a seperate CPU, here we achieve true parallel execution of processes. 
    - Use in AI, image processing, weather forecasting, etc.
    - Processing Ways:
        - A. Symmetric:
            - All processors are treated equally and can run any task.
            - Any processor can perform any task
            - Generally SImpler as all processors are same
            - Easily scalable by adding more processors.
            - Load is evenly distributed, enhancing performance.
        - B. Asymmetric;
            - Each processors assigned a specific task or role.
            - Tasks are divided according to processor roles.
            - More complex due to the dedicated role of each processor.
            - May require reconfiguration as processors are added.
            - Performance may very based on the specialization of tasks.

6. Real time OS
    - It is a special purpose OS which has well defined fixed time constrints. Processing must be done within the defined time limit or system will fail.
    - valued more for how quickly or how predictably it can respond, without buffer delays that for the amount of work it can perform in a given period of time.
    - Ex -> Petroleum refinery, Airline reservation system, ATC, Stock price information, defence apps like Radar.
    - Categories
        - A. Hard real-time OS:
            - This is also a type of OS and it is predicted by a deadline. The predicted deadlines will react at a time t=0. Ex-> Air bag control in car.
        - B. Soft real-time OS:
            - It has certain deadlines, may be missed and they will take the action at a time t=0+. The critical time of this OS is delayed to some extent. 
            - Ex -> Digital Camera, mobile phones, online data.

7. Distributed OS
    - It is a software over a collection of independent, networked, communicating, loosely coupled nodes and physically seperate computational nodes.
    - The node communicate with one another through various networks, such as high speed buses and the internet. They handle jobs which are serviced by multiple CPUs. Each individual node holds a specific software subset of the global aggregate OS.
    - 4 major reasons to build it:
        - a. Resource sharing
        - b. Computation speed
        - c. Reliability
        - d. Communication.