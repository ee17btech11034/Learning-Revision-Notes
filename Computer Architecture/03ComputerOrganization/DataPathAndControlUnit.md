# 



## Historically, there have been 2 types of computers:
### Fixed Program Compuers (Dedicated Devices / Embedded Systems):
These have a specific function and can not be reprogrammed. Ex> Calculators, Washing Machine, radio, ATM, etc.

### Stored Program CComputers (General Purpose Computers/Von Neumann Architecture):
These can be programmed to perform various task, with applications stored within the system, which is why they are named as such.


## A CPU generally consists of three key components:
### 1. Control unit (CU)
    - Acts as the master generator of control sign als, directing the operations of all other components within CPU.
    - Manage Input/output flow, instruction fetching, and controls how data moves across the system, ensuring that instructions are executed in the correct order.

### 2. Registers
    - Few important registers are in every processor like program counter which contains address of the next instruction then instruction register which contain address of the current register and base register which contain base address of program.

### 3. ALU
    - It is a complex combination circuit which can perform arithmatic Operations, bit Shifting Operations, and logical operation eg Addition, Subtraction, Comparisons etc. 

### There are many other main components
    - Memory  --> Store a program
    - ALU --> perform operations
    - Register --> Fast Memory, sequence of flip-flop. (load, clear, increment pin)
    - timing Circuit --> Sequence Couter (to order certain operations like fetch, decode, execute), generate timing signals
    - control Unit --> generate control signals to select registers, select other circuit, to give inputs to registers. It gives signals to all components.
    - Flags --> one-bit information
    - Bus --> Using which we will connect differ component together, and perform data transfer using multiplexer.
    === Computer Flow ==> Memory --> Register --> ALU in Registerss--> Memory

## Types of Buses
1. Address Bus: is used to identify the correct i/o devices among the number of I/O device, so CPU put an address of a specific i/o device on the address line, all devices keep monitoring this address bus and decode it, and if it is a match then it activates control and data lines.

2. Control Bus : i/o commands, control command, ststus command, etc. --> It will say that type type of operation you need to perform, set of instructions

3. Data Bus: Once Control bus work is done, then data is provided.

## Bus Arbitration
1. Bus arbitration: Method to decide which device gets access to common bus when multiple devices request it simultaneously, ensuring data integrity and system stability.
    - Ways:
        - Daisy Chaining method:
            - Jab devices ko communicate krna hota hai CPU se to wo common bus par signal karte hai. 
            - JB common bus ka signal '1' hota hai to CPU pahle apne current instruction ko complete krta hai (pura code/program nahi). 
            - Yaha either CPU can reject or pull that. 
            - Agar pick krta hai to wo ab "Bus Grant" ka use krke signal deta hai Device-1 ko.
            - Device 1 check krta hai ki kya usne ye request ki thi, if yes then connect to CPU, if not requested then transfer to device 2. 
        - Polling
            - Controller unique address generate krta hai for each device based on their priority.
            - Master Bus will poll to device 1, to ask if he is interested in any operation. 
            - If so, it perform else device-1 will send that to device-2.
        - Fixed priority or independent request method
            - each device has its own busses/lines.

2. Conflict Resolution: Without Bus Arbitration, simultaneous access could result in data corruption and system malfunctions, making this mechanism essential for orderly and reliable data transfer.

## Booth's algorithm
- method to multiply
