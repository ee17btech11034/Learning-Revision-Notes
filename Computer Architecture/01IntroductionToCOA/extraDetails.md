# Introduction to Computer Organization and Architecture (COA) Notes

## 1. Computer Architecture vs. Computer Organization
Understanding the distinction between these two terms is fundamental to COA.

* **Computer Architecture:** Refers to the attributes of a system visible to a programmer. It acts as the conceptual design and functional structure of the system.
    * *Focus:* **What** the computer does.
    * *Examples:* Instruction set architecture (ISA), number of bits used to represent data, addressing modes, and cache mechanisms.
* **Computer Organization:** Refers to the operational units and their interconnections that realize the architectural specifications.
    * *Focus:* **How** the computer does it.
    * *Examples:* Hardware details, peripheral interfaces, control signals, and the specific memory technology used.

---

## 2. Structure and Function of a Computer
A computer performs specific functions using a structured set of internal components.

### Core Functions
Every computer system performs four basic operations:
1. **Data Processing:** Manipulating data to produce useful information.
2. **Data Storage:** Retaining data temporarily or permanently for immediate or future use.
3. **Data Movement:** Transferring data between the computer and the outside world (I/O) or over long distances (data communications).
4. **Control:** Managing and coordinating the three functions above under the instruction of a program.

### Top-Level Structural Components
* **Central Processing Unit (CPU):** Controls the operation of the computer and performs its data processing functions.
* **Main Memory:** Stores data and executable programs currently in use.
* **Input/Output (I/O):** Moves data between the computer and its external environment.
* **System Interconnection (Bus):** Provides a communication pathway for the CPU, main memory, and I/O.

---

## 3. The Von Neumann Architecture
Most modern computers are based on the Von Neumann model, proposed by John von Neumann in 1945. Its defining feature is the **Stored-Program Concept**, meaning both data and instructions are stored together in the same read-write memory.

### Core Components
* **Memory Structure:** A unified memory space holding both instructions and data.
* **Arithmetic and Logic Unit (ALU):** The component that executes mathematical operations (addition, subtraction) and logical decisions (AND, OR, comparisons).
* **Control Unit (CU):** The "brain" that fetches instructions from memory, decodes them, and directs the flow of data signals.
* **Input/Output Equipment:** Interfaces operated by the control unit to interact with external devices.

### The Von Neumann Bottleneck
Because data and instructions share the same bus, the CPU cannot read an instruction and read/write application data at the exact same time. This throughput limitation is called the **Von Neumann Bottleneck**.

---

## 4. Inside the CPU: Registers and Components
The CPU contains ultra-fast internal storage cells called **registers** to manage immediate operations.

### Key Internal Registers
* **Program Counter (PC):** Holds the memory address of the **next** instruction to be fetched and executed.
* **Instruction Register (IR):** Holds the instruction currently being decoded or executed.
* **Memory Address Register (MAR):** Holds the memory address from which data will be fetched or to which data will be written.
* **Memory Buffer Register (MBR) / Memory Data Register (MDR):** Holds the actual data contents read from memory or waiting to be written to memory.
* **Accumulator (AC):** A temporary holding register that stores the immediate results of ALU operations.

---

## 5. The Instruction Cycle (Fetch-Execute Cycle)
The instruction cycle is the continuous process by which a computer retrieves a program instruction from its memory, determines what actions the instruction requires, and carries out those actions.

### 1. Fetch Phase
* The CPU copies the address stored in the **PC** to the **MAR**.
* The CPU sends a read signal along the control bus.
* The memory contents at that address are placed onto the data bus and copied into the **MBR**.
* The instruction moves from the **MBR** to the **IR**.
* The **PC** is automatically incremented to point to the next instruction.

### 2. Decode Phase
* The **Control Unit** examines the instruction in the **IR**.
* It interprets the opcode (operation code) to figure out what hardware operation is required.

### 3. Execute Phase
* If the instruction requires data from memory, the relevant addresses are resolved.
* The **ALU** executes the decoded command (e.g., adding two numbers).
* The results are stored back into a register (like the Accumulator) or main memory.

---

## 6. Bus Interconnection Structures
A bus is a shared communication pathway consisting of multiple lines (wires). It connects the major components of the computer.

### The System Bus Types
1. **Data Bus:** Carries the actual data or instructions between system modules. It is bidirectional.
2. **Address Bus:** Specifies the source or destination of the data on the data bus. It is unidirectional (driven by the CPU).
3. **Control Bus:** Transmits control and timing signals to manage access to and use of the data and address lines.
