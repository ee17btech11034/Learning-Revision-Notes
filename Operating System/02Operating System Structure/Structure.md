# OS
## Structure of OS
    - A common approach is to partition the task into small components, or modules, rather than have one monolithic system. Each of these modules should be a well defined portion of the system, with carefully defined inputs, outputs, and functions.
    - Simple Structure:
        - manay OS do not have well-defined structures. Frequently, such systems started as small, simple, and limited systems and then grew beyond their original scope. MS-DOS is an example of such a system.
        - Not divided into modules. its interface, levels and functionality are not well seperated.
        ```bash
        MS-DOS Layer Structure:==>
        
                                Application Program
                                    |           |
                                    |           |
                                    V           |
                    Resident System Program   |
                                    |       |   |
                                    |       |   |
                                    V       |   |
                    MS-DOS device drivers   |   |
                                    |       |   |
                                    |       |   |
                                    V       V   V
                            ROM BIOS device drivers 
        ```
    - Layered Approach:
        - With proper hardware support, OS can be broken into peices. The OS can then retain much greater control over the computer and over the applications tat make use of that computer. A layer can only communicate with either its just above layer of just below layer.
        1. Implementers have more freedom in changing the inner workings of the system and in creating modular OS.
        2. Under a top-down approach, the overall functionality and features are determined and are seperated into components.
        3. Information hiding is also important, because it leaves programmers free to implement the low-level routines as they see fit.
        4. A system can be made modular in many ways. One method is the layered approach, in which the OS is broken into a number of layers (levels). The bottom layer (layer 0) is the hardware; the highest (layer N) is the user interface.
        
    - Micro-Kernal Approach
        - in the mid-1980s, researches at Carnegie Mellon University developed an OS called Mach that modularized the kernal using the microkernal approach.
        - This method structures the OS by removing all non-essential components from the kernel and implementing them as system and user-level programs. The result is a smaller kernel.
        ```bash
                Application Program             File System       Device Driver                 ===> these are pulled from kernel and put in "user mode"
                                ^                 ^      ^            ^
                                |                 |      |            |
            ____________________|_________________|______|____________|___________
            |                   |                 |      |            |          |
            |                   `----messages-----`      `--messages--`          |
            |    Interprocess                      Memory              CPU       |             ===> Kernel Mode
            |   Communication                     management         Scheduling  |
            |________________________micro kernel________________________________|
                                   ^              ^
                                   |              |
                                   V              V
                                       Hardware
        
        ```
        - One benefit of microkernel approach is that it makes extending the OS easier. All new services are added to user space and consequently do not require modification of the kernel.
        - When the kernel does have to be modified, the changes tend to be fewer, because the microkernel is a smaller kernel.
        - The MINIX 3 microkernel, for example, has only approximately 12000 lines of code. Developer Andrew S. Tanenbaum.

    - User and OS Interface:
        - OS = Kernel (actual management) + Interface (communication with user).
        - There are several ways for users to interface with OS. Here, we discuss two fundamental approach"
            1. Command-line Interface / Command Interpreter
                - SOme OS include the command interpreter in the kernel. Others, such as Windows adn UNIX, treat the command interpreter as a special program that is running when a job is initiated or when a use first logs on (on interactive systems).
                - On System with multiple command interpreters to choose from, the interpreters are known as shells. FOr example, on UNIX and LINUX systems, a user may choose among several different shells, including the Bourne shell, C Shell, Bourne-Again Shell, Korn Shell, and others.
            2. Graphical User interfaces.
                - A secondary startegy for interfacing with the OS is through a user-friendly graphical user interface, or GUI. Here, users employ q mouse-based window and menu system characterized by a desktop.
                - The user moves the mouse to position its pointer on images, or icons, on the screen (the desktop) that represent programs, files, directories, and system functions. Depending on mouse pointer's location, clicking a button on the mouse can invoke a program, select a file or dir (folder), etc that contains commands.
                - For most mobile systems, we use touchscreen interface.
         
    - System Call
        - System calls provide the means for a user prgram to ask the operating system to perform the task reserved for the OS on the user program's behaviour.
        - System calls provide an interface to the services made available by an OS. These calls are generally available as routines written in C/C++.
        - The API specifies a set of functions that are available to an application programmer, including the parameters that are passed to each function and the return values the programmer can expect.
        ```bash
                            User Programs
                                |
                                |
                            System Calls
                                |
                                |
                                V
                              Kernel
                                |
                                |
                                V
                            Hardware
        
        Simply, when user want to do some task then "System calls" helps user to provide the task to Kernel on user's behalf. 
        Ex is code written by us is not useful to kernel but compiler reads it and provide the task to kernel. 
        ```
        - type of System Calls:
            1. Process Control
                a. end, abort
                b. load, execute
                c. create process, terminate process
                d. get process attributes, set process attributes
                e. wait for time
                f. wait even, signal event
                g. allocate and free memory.
            2. file manipulation/management
                a. create file, delete file
                b. open, close
                c. read, write, reposition
                d. get file attributes, set file attributes.
            3. device manipulation
                a. request device, release device
                b. read, write, reposition
                c. get device attributes, set device attributes
                d. logically attach or detach devices.
            4. information maintenance
                a. get time or date, set time or date
                b. get system data, set system data
                c. get process, file or device attributes
                d. set process, file or device attributes
            5. Communications
                a. create, delete communication connection
                b. send, receive messages transfer status information
            6. Protection
        
        - Mode:
            - We need two seperate mode of operation: User Mode and Kernel Mode (supervisor mode/ system mode / privileged mode). A bit, called the mode bit, is added to the hardware of the computer to indicate the current mode: Kernel (0) or user (1).
            - When the computer system is executing on behalf of a user application, the system is in user mode. When a user app requests a service from the OS (via a system call), the system must transition from user to kernel mode to fulfill the request.