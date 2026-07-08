# 02 Memory Hierarchy & Interfacing

## 1. Understanding Hierarchy in Memory Systems
* **Concept**: A hierarchy represents a ranking system based on chosen parameters (similar to ranking movies by release date versus critical scores).
* **The Balancing Act**: In computer engineering, different physical memory storage devices are ranked against each other to bridge the speed gap between a fast processor and slow storage at an affordable cost.

### The Core Mismatch Hierarchy Spectrum
As you move **up** the structural pyramid (from Secondary Storage to Registers):
* ⬆️ **Cost per bit** increases drastically.
* ⬆️ **Frequency of usage** by the CPU increases.
* ⬇️ **Access time** decreases (it gets much faster).
* ⬇️ **Physical storage size/capacity** decreases.

```text
                        /\  
    [Registers (Embedded Flip-Flops - Fastest/Smallest)]
                       /   \  
                      /=====\ 
            [Cache Memory (SRAM Layers)]
                    /==========\ 
            [Main Memory (DRAM Workspace)]
                  /===============\ 
        [Secondary Storage (HDD/SSD - Slowest/Largest)]
```

---

## 2. Foundational Interfacing Metrics
Memory interfacing defines how various levels of memory components physically and logically connect to the processor and input/output (I/O) peripherals.

* **Processor Performance Indicator**: Measured in **MIPS** (Million Instructions Per Second). The ultimate design goal is to feed instructions fast enough to sustain the CPU's maximum MIPS capacity.
* **Inclusion Property**: Information located at a faster level ($n$) is structurally treated as a smaller subset of the larger, slower level beneath it ($n + 1$).
* **Hit**: Occurs when the processor requests data or an instruction, and it is successfully found in the target level ($n$).
* **Miss**: Occurs when the requested item is absent in level $n$, forcing the processor to look down into level $n + 1$.
* **Hit Ratio ($H$)**: The mathematical probability of finding a required instruction in a specific memory level.
  $$\text{Hit Ratio} = \frac{\text{Instructions found in that layer}}{\text{Total instruction requests made by the program}}$$
  * *Example*: If a program has $100$ instructions total, and $80$ are successfully fetched from Main Memory, the main memory hit ratio ($H$) is $\frac{80}{100} = 0.8$ ($80\%$). 
  * *Note*: The final permanent secondary storage layer inherently maintains a $100\%$ ($1.0$) hit ratio; if a file does not exist there, the system cannot run it at all.

---

## 3. Memory Interfacing Configurations & Access Formulas

The system's overall **Average / Effective Memory Access Time ($T_{\text{avg}}$)** depends entirely on how the physical memory chips are wired to the CPU. There are two core configurations:

### Way 1: Parallel Interfacing (Simultaneous Connection)
* **Architecture**: Every individual level of memory ($M_1, M_2, M_3$) is wired directly and simultaneously to the processor. 
* **Operation**: When searching for information, the processor probes all levels side-by-side at the exact same time. 
* **Mathematical Formula**: For a 3-level setup where $T_1 < T_2 < T_3$ represent the individual layer access times, and $H_1, H_2$ represent the hit ratios:
  $$T_{\text{avg}} = H_1 \cdot T_1 + (1 - H_1)H_2 \cdot T_2 + (1 - H_1)(1 - H_2) \cdot T_3$$
* **Formula Breakdown**:
  * There is an $H_1$ chance it hits immediately in $M_1$, taking $T_1$ time.
  * There is a miss chance $(1 - H_1)$ in $M_1$. If it misses, it checks $M_2$ with an $H_2$ success rate, taking $T_2$ time.
  * If it misses both layers—represented by $(1 - H_1)(1 - H_2)$—it defaults to recovering it from the final layer ($M_3$) in $T_3$ time.

### Way 2: Level-Wise Interfacing (Hierarchical Connection)
* **Architecture**: The memory arrays are connected sequentially in a chain. The processor is only directly wired to the fastest layer ($M_1$).
* **Operation**: If a miss occurs in $M_1$, the hardware must sequentially traverse into $M_2$, and onward downstream if misses continue. 
* **The Penalty**: Because access isn't parallel, looking into a lower level means you have already wasted time searching through the higher, failed levels.
* **Mathematical Formula**:
  $$T_{\text{avg}} = H_1 \cdot T_1 + (1 - H_1)H_2 \cdot (T_1 + T_2) + (1 - H_1)(1 - H_2) \cdot (T_1 + T_2 + T_3)$$
  *(Notice how the access times accumulate additively inside the miss paths because the system searches through each gate sequentially).*

## Questions:
* **Q1** A cache memory needs access time of 30ns, main memory 150ns. find the avg access time of CPU (assume hit ratio = 80 %)?

    * Cache => T1 = 30 ns, H1 = 0.8
    * Main memory => T2 = 150 ns
    * If they are parallely attached then $$T_{\text{avg}} = H_1 \cdot T_1 + (1 - H_1) \cdot (T_2)$$
    * If they are seq attached then $$T_{\text{avg}} = H_1 \cdot T_1 + (1 - H_1) \cdot (T_1 + T_2) $$
* **Q2** Assume that for a certain processor, a read req takes 50 ns on a cache misss and 5 ns on cache hit. It was was observed that 80% of the processor's read request result in a cache hit. The avg read access time ?

    * It is level wise. 
    * T1 + T2 = 50 ns
    * T1 = 5 ns
    * H1 = 80% = 0.8
    * avg Time $$T_{\text{avg}} = H_1 \cdot T_1 + (1 - H_1) \cdot (T_1 + T_2) $$


Default is always level wise.