# Thread
## Definition
    - A thread is a basic unit of CPU utiization, consisting of a program counter, a stack, and a set of registers, (and a thread ID).
    - traditional (heavyweight) processes have a single thread of control - There is one program counter, and one seq of instructions that can be carried out at any given time.
    - Multi-threaded applications have multiple threads within a single process, each having their own program counter, stack and set of registers, but sharing common code, data, and certain structures such as open files.

## Models
### Many to One Model
    - In the many-to-one model, many user-level threads are all mapped onto a single kernel thread.
    - however, if a blocking system call is made, then the entire process blocks, even if the other user threads would otherwise be able to continue.
    - Because a single kernel thread can operate only on a single CPU, the many-to-one model does not allow individual processes to be split across multiple CPUs.
    - Green threads for Solaris implement the many-to-one model in the past, but few systems continue to do so today.
    - Explain:
        - Kernel create a single process. Inside that process we manage many threads. Itis good as kernel does not have much load.
        - But if machine is of multi process then we can not run threads in multiple process format.
        - If any thread is found doing some illegal work then kernel will kill the whole rocess as it does not know about the thread.
        - if a thread needs more resources then it can not communicate to OS or kernel.

### One To One Model
    - The one to one model creates a seperate kernel thread to handle each user thread. It overcomes the problems listed above involving blocking system calls and the splitting of processes across multiple CPUs.
    - however, the overhead of managing the one-to-one model is more significant, involving overhead and slowing down the system. Most implementations of this model place a limit on how many threads can be created. 
    - Linux and windows from 95 to XP implement the one-one model for threads.

### Many to Many Model
    - The many-to-many model multiplexes any number of user threads onto an equal or smaller number of kernel threads, combining the best features of the one-to-one and many-to-one models.
    - Users have no restrictions on the number of threads created. Blocking kernel system calls do not block the entire process.
    - Processes can be split across multiple processors. Individual processes may be allocated variable numbers of kernel threads, depending on the number of CPUs present and other factors.