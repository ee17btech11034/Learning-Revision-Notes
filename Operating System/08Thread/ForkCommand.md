# Fork
## Requirement of Fork Command
    - In number of applications specially in those where work is of repetitive nature, like web server ie with every client we have to run similar type of code. Have to create a seperate process every time for serving a new request.
    - So, it must be better solution that instead to creating a new process everytime from scratch we must have a short command using which we can do this logic.

## Idea of Fork Command
    - Here fork command is a system command using which the entire image of the process can be copied and we create a new process, this idea help us to complete the creation of the new process with speed.
    - After creating a process, we must have a mechanism to identify wether in newly created process which one is child and which is parent.

## Implementation of fork command
    - in general, if fork return 0 then it is child and if fork return 1 then it is parent, and then using a programmer level code we can change the code of child process to behave as a new process.

## Advantages of using fork commands
    - now it is relatively easy to create and manage similar type of process of repetitive nature with the help of fork command.

## Disadvantage
    - To create a new process by fork command we have to do system call as, fork is system function
        - Which is slow and time taking
        - Increase the burden over OS

Different img of the similar type of task have same code part which means we have the multiple copy of the same data waiting the main memory. If we run fork command n times then it will generate (2^n -1) copies.

To reslve this we need Thread.
