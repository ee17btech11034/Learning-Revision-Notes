# Input/Output Management
- To comunicate with outside world (display, internet, etc) we need IO devices also called Peripheral Devices that allow the system to receive and transmit the data/information.
- When design the IO system for computer, it is essential to:
    - Conside the number of IO devices
    - understand the capacity and capabilities of each device.

## Interface
Directly connecting an IO device to a computer is not feasible due to several reasons given below. We use Interface b/w CPU and IO device.:
    - Speed: The CPU and IO device operate at different speeds. CPU = 2GHz = 2G operations per sec.
    - Format: The data format used by the CPU (ASCII, Unicode) may differ from that of the peripheral devices. Like We do not need any specific IO device (mouse/keyboard) for a specific CPU. Interface will handle all the work
    - Physical Orientation: IO devices use various technologies like optical, magnetic, or electrochemical mechanism, unlike CPU, which uses electronic signals.
    - Signal Conversion: Since IO devices are electromagnetic or electrochemical in nature, their signals need to be converted to be compatible with the electronic signals of the CPU memory.

## Bus:
1. Address Bus:
    - The CPU uses the address bus to identify the correct IO device among many. The CPU sends the address of the target device, and all devices monitor the bus. When a device matches the addres, it activates its control and data lines.
2. Control Bus:
    - After selecting a device, the CPU sends functional codes via the control bus. The selected device reads these codes and performs the corresponding actions (IO command,  control command, or status command).
3. Data Bus: 
    - Based on the operation, either: The CPU sends data to the device, or The device sends data to the CPU via the data bus.

```bash
            |-------------------------------- Data
  Processor |------------------------------- Address
            |-------------------------------- Control

3 parts of each interface is connected to these buses parallely. 
Address bus gets the address from CPU that it wants to connect to and respective IO Interface match the address and tgets ready. Then DATA bus is used to send data, control bus for controls. 
```

## How a computer (CPU) deals with Memory and I/O devices 
### Memory Mapped I/O
    - In Memory Mapped I/O, there are no seperate I/O instructions. The CPU uses the same instructions to access both memory and IO devices. This means IO data in interface registers can be manipulated just like memory words. 
    - Advantage: in typical systems, there are more memory instructions that IO instructions. In memory-mapped IO, all memory instructions can be used for IO operations, increasing efficiency. As we can use same instructions (we using with memry) with IO devices, so no extra load.
    - Disadvantage: The total address space is divided between memory and IO devices, reducing the addressable memory range.
    - Ex: 8085 processor. 

### Isolated I/O
    - In this, a common bus is used to transfer data between the CPU, Memory, and IO devices. The distinctions b/w memory and IO transfers is managed through seperate control lines:
        - IO Read/Write Lines: Enable during IO transfers.
        - Memory Read/Write Lines: Enabled during memory transfers.
    - Address Bus and Data bus will be common for allIO and main memory. But CPU will be connected to Main memory using 2 lines (READ and WRITE). And CPU will be connected to all IO devices using  2 lines (differnet than line of main memory) (READ and WRITE).
    - When address matches with any IO or main memory then only one will get the data.
    - Advantages: Efficient memory usage, as the same address can be used for both memory and IO operations.
    - Disadvantages: Requires seperate control lines for memory and IO devices, increasing complexity.
    - Ex: 8086 processor.

### I/O Processor
    - in above 2, CPU was interacting with IO devices directly but we do not want that. 
    - In I/O Processor (IOP), the computer uses independent sets of data, address, and control buses for memory and I/O operations. This allows for better parallelism in data transfers.
    - Memory bus: Connects the CPU and memory, allowing both the CPU and IOP to communicate with memory. 
    - I/O Bus: The IOP communicates with input and output devices through a seperate I/O bus, which has its own address, data, and control lines.
    - Purpose: The I/O processor provides an independent pathway for transfering data b/w external devices and internal memory, offloading I/O operations from the CPU and improving efficiency.
```bash
_____________________________________________________________
       |        |                 |
       |        |                 |------------------------------ data line
  CPU  |        |   I/O Processor |------------------------------ Address Line
       |        |                 |------------------------------ Control Line
-------         |_________________|
    |                   |
    |                   |
    |                   |
    --------------------
            |
            |
        Memory Unit

CPU interact with Memory or IO processor. 
IO processor deals with IO interfaces.   
```

## Modes of Data Transfer
We deal with "how data communication will take place CPU and I/O device.
There are 3 methods of Data Transfer:
    1. Programmed I/O
        - In this, the I/O device can not directly access memory, and the CPU is responsible for transferring data between the device and memory. The processor follows steps:
            a. data Bus Signaling: The IO device places data on the data bus and signals its validity
            b. Interface Handling: The interface monitors for the valid data signal, copies the data to its internal register, and setsa flag indicating that the data has been accepted (we need flag as we do not know if that val is garbag or data).
            c. CPU Monitoring: The CPU continously checks the status register, and when the flag is set. It retrieves the data from Interface register and clears the flag.
            d. Ready for new transfer: The interface disables the data accepted line, signaling the IO device that it's ready for the next data transfer.
        - Conclusion: It forces the CPU to operate in busy-wait mode (CPU constantly checks if dta is availabe or not by looking at flag bit), which can waste CPU cycles. it is inefficient for handling multiple or high speed I/O devices simultaneously, making it less suitable for modern, high-performance system.
        ```bash
        ____________                   ______________Interface_______                    _________
                    |                 |                              |                  |
                    |<----Data bus----|    Data Register             |<----I/O Bus------|
            CPU     |---Address bus-->|                              |<---Data Valid----|I/O Device
                    |----I/O Read---->|  Status Registor (Flag Bit)  |--Data Accepted-->|
                    |----I/O Write--->|                              |                  |
        ____________|                 |_____________Interface________|                  |_________
        ```
        - It is still used in certain areas today, where simplicity is preferred over efficiency, like Washing Machine Controlling Buttons and display, Temperature Loggers polling sensors, Simple digital clock checking time updates.
    
    
    2. Interrupt initiated I/O
        - In this, the I/O device notifies the CPU when it's ready for data transfer by sending an interrupt. The CPU, while executing instructions, checks for interrupts b/w instructions. If an interrupt occurs, the CPU decides whether to handle it or continue execution. (Code is set of instructions, pahle current running instruction ko complete krta hai and then decides).
        - ISR (Interrupt Service Routine): Each device has its own ISR, which tells the CPU how to manage the interrupt, saving CPU time.
        - Type of Interrupts:
            a. non-vectored interrupt: the CPU and device have a pre-agreed memory location for the interrup service routine.
            b. Vectored Interrupt: The device provides the address of the interrupt service routine when interrupting.
            
            If multiple devices interrupt simultaneously, the CPU prioritize which interrupt to handle first based on predefined rules. 
        - We use Daisy Chaining for this. 
            - Daisy chaining is a hardware solution used to establish priority among multiple I/O devices in a system, commonly known as a Serial solution.
                -- Advangat: Simple, easy to implement; Fast & efficient for small systems
                -- Disadvantage: Fixed priority, devices earlier in the chain always gets priority. Priority can not be dynamcally changed even when required. 
        - Conclusion: This method improves efficiency as the CPU is not constantly polling I/O devices, unlike programmed I/O. Keyboard input in modern computers, Mouse movement or clicks, Hard disk I/O, USB devices.
    
    3. Direct Memory transfer /Direc Memory Access (DMA)
        - In traditional I/O operations, CPU manages and controls data transfer b/w I/O devices and memory. 
        - however, In DMA, a DMA Controller is used to handle the data transfer, allowing the CPU to delegate the task. 
        - the DMA Controller takes control of the system buses to directly transfer data between the I/O device and memory, bypassing the CPU. This frees up the CPU for other tasks, improving overall system efficiency.

## 