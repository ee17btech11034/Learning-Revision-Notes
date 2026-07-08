# 📚 3. Classifications of Computer Architecture 

## 1. Primary Classification Models of Computer Architecture
Computer architectures are primarily categorized using two popular analytical frameworks:
* **Memory-Access Classification**: Groups systems based on memory structure layout and bus configurations (e.g., Von-Neumann vs. Harvard models).
* **Flynn's Taxonomy**: Formally proposed by Michael J. Flynn in 1966. It classifies systems based on concurrent data processing behaviors, computing streams, and processor counts.

---

## 2. Memory-Access Architecture Classifications

### I. Von-Neumann (Princeton) Architecture
* **Origins**: Named after John von Neumann's professorship at Princeton University.
* **Hardware Subsystems**: Formed by three core units: the Central Processing Unit (CPU), Main Memory, and Input/Output (I/O) system.
* **Stored-Program Concept**: A singular, unified main memory system simultaneously holds both the active program instructions and data items. The computer can manipulate its own internal program code like data.
* **Execution Style**: Carries out instructions sequentially. The CPU processes exactly one operation at a time.
* **The Von-Neumann Bottleneck**: 
  * A single physical path connects the main memory to the processor.
  * Because data and instructions share the same bus, the processor cannot simultaneously read an instruction and read/write data.
  * This severe execution constraint was formally highlighted by John Backus during his 1977 ACM Turing Award lecture.

### II. Harvard Architecture aka Non-Von Neumann Architecture
* **Origins**: Developed by researchers at Harvard University. It retains most architectural behaviors of the Princeton model but introduces crucial structural parallelism.
* **Memory Separation**: Uses two physically distinct memory units: one dedicated strictly to storing program instructions called `Instruction Memory`, and another separate unit for data items called `data memory`.
* **Execution Advantage**: The processor can fetch an instruction and perform a data memory access simultaneously. It eliminates bus competition, allowing systems to process instructions faster.
* **Diagram:** Instruction Memory <----> Processor <----> Data Memory

### III. Modified Harvard Architecture
* **Core Design**: A hybrid compromise that balances both the Harvard and Princeton architecture schemes.
* **Relaxed Division**: It removes the strict physical division of the primary instruction and data memory units.
* **Cache Integration**: Incorporates a small, high-speed internal storage unit called a cache. 
* **Dynamic Operation Modes**: 
  * When the processor executes instructions directly out of its internal cache, it operates like a pure Harvard architecture.
  * When accessing information from the backing main memory layer, it shifts to operate like a pure Von-Neumann machine. This design is widespread across modern consumer processors.
* **Diagram:** [Instruction Memory & Secondary data] <----> Processor (Cache) <----> Data Memory

---

## 3. Parallel Processing Classification (Flynn's Taxonomy)
Flynn’s Taxonomy classifies computing hardware based on the relationship between Instruction Streams (the sequence of instructions executed by the CPU) and Data Streams (the sequence of data items called by the instructions).

```text
DATA STREAMS
Single  Multiple
+---------------+---------------+
Single    | SISD          |  SIMD  |
I         | (Von-Neumann) | (Array Proc.) |
S         +---------------+---------------+
T Multiple|     MISD      |     MIMD      |
R         | (Theoretical) | (Multiproc.)  |
+---------------+---------------+
```


### I. SISD (Single Instruction, Single Data)
* **Characteristics**: Features a single CPU executing exactly one machine instruction at a time on a single data item.
* **Mapping**: Standard uniprocessor Von-Neumann architecture models fall directly into this category.

### II. SIMD (Single Instruction, Multiple Data)
* **Characteristics**: Driven by a single main control unit that handles a single instruction stream, but drives multiple Arithmetic Logic Units (ALUs) working in parallel.
* **Execution Style**: The control unit broadcasts identical control signals to all ALUs simultaneously. Each ALU performs the exact same operational task on its own distinct data set in lockstep.
* **Mapping**: Processor arrays and modern vector engines belong to this category.

### III. MISD (Multiple Instruction, Single Data)
* **Characteristics**: A theoretical class where multiple separate instruction streams (different programs) run concurrently on a single, shared data stream.
* **Mapping**: This class has no specific, pure practical implementation in computing history, though certain MIMD setups can simulate it.

### IV. MIMD (Multiple Instruction, Multiple Data)
* **Characteristics**: Built with multiple, completely independent processors. Each processing element fetches its own distinct set of instructions to manipulate its own assigned data streams.
* **Mapping**: Modern multi-core processors and multiprocessor supercomputers fall into this group.

---

## 4. Companion Topics
To maximize your understanding of these classification structures, study the following adjacent concepts:

### ⚡ Cache Coherency Protocols (Extending Modified Harvard)
* **The Problem**: In systems with separate L1 instruction and data caches, if a program writes new instructions into memory as data (self-modifying code), the instruction cache can become out of sync.
* **Key Solutions**: Study the MSI (Modified, Shared, Invalid) and MESI cache snooping protocols used to keep memory uniform.

### 📊 Vector Processing vs. SIMD
* **Data Width**: How vector processors differ from standard SIMD. Vector processors use very long registers to loop through arrays, while SIMD uses sub-word parallelism (like Intel's AVX or ARM's NEON extensions) to split a single 256-bit register into multiple 32-bit floats.

### 🌐 Interconnection Networks in MIMD Systems
* **Shared Memory (UMA)**: Uniform Memory Access systems where all processors share a central memory pool via a common system bus.
* **Distributed Memory (NUMA)**: Non-Uniform Memory Access systems where each processor has its own local memory, communicating with other processors over a dedicated network grid.