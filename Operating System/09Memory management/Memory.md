# Memory
## Memory Hierarchy
Memory is architected hierarchically to resolve the physical engineering trade-offs between processing speed, capacity limitations, and manufacturing costs.

```bash
[ Registers ]
        │
        V
[ Cache Memory  ────► (L1, L2, L3)]
        │
        V
[ Main Memory   ────► (RAM / Primary Physical Memory)]
        │
        V
[ Secondary Storage ────► (SSD / HDD / Logical / Virtual / Auxiliary Disk)]
───────────────────────────────────────────────────────────────────────────►
► Capacity Increases
► Access Time / Latency Increases
► Per-Unit Cost Decreases
```

## Locality of Reference
    - The references to memory at any given interval of time tend to be confined within a few localized areas in memory. This phenomenon is known as the property of locality of reference. There are two types of locality of reference.
        1. Spatial Locality: Use of data elements in the nearby locations.
        2. Temporal Locality: Temporal locality refers to the reuse of specific data or resources, within a relatively small-time duration, i.e. Most Recently Used. LRU works on this method.

## Duty of OS
     - Operating systems manage memory through key functions:
        1. Address Translation: 
            Converting logical to physical addresses for data retrieval.
        2. Allocation/Deallocation: 
            Managing process loading and removal. Decide which processes or data segments to load or remove from memory as needed.
        3. Tracking: Monitoring memory usage. 
            Monitor which parts of memory are in use and y which processes.
        4. Protection: 
            Ensuring process isolation and data integrity. Implement safeguards to restrict unauthorized access to memory, ensuring both process isolation and data integrity.

## Memory Allocation
    - There can be two approaches for storing a process in main memory:
        - Contiguous allocation policy
        - Non-Contiguous allocation policy (use it in modern PCs)

### 1. Contiguous allocation policy
    - We know that when a process is required to be executed it must be loaded to main memory, by policy has 2 implications.
        - a. It must be loaded to main memory completely for execution
        - b. must be stored in main memory in contiguous fashion.

#### Address Translation in Contiguous Allocation
    - Here we use a Memory Management Unit(OS) which contains a relocation register, which contains the base address of the process in the main memory and it is added in the logical address every time.
    - In order to check whether address generated to CPU is valid(with in range) or invalid, we compare it with the value of limit register, which contains the max no of instructions in the process.
    - So, if the value of logical address is less than limit, then it means it's a valid request and we can continue with translation otherwise, it is a illegal request which is immediately trapped by OS.
    ```bash
    Diagram Workflow Breakdown
        - CPU Generates Address: The CPU outputs a logical address.
        - Boundary Check: The system compares the logical address against the limit register (\(Logical\ Address < Limit\)).
        - Valid Request (Yes): The logical address is added to the relocation register to produce the final physical address in memory.
        - Invalid Request (No): The system triggers an OS exception labeled "trap: addressing error".
    ```

#### Space Allocation Method in Contiguous Allocation
    - 1. Variable size partitioning: 
        - In this policy, in starting, we treat the memory as a whole or a single chunk & whenever a process request for some space, exactly same space is allocated if possible and the remaining space can be reused again.
    - 2. Fixed size partitioning: 
        - here, we divide memory into fixed size partitions, which may be of different sizes, but here if a process request for some space, then a partition is allocated entirely if possible, and the remaining space will be wasted internally.
    
    We have 3 policies which can be applicable on above 2 Schemes:
        - 1. First fi Policy:
            - it states searching the memory from the base and will allocate first partition which is capable enough.
            - Advantage:
                - Simple, easy to use, easy to understand
            - Disadvantage:
                - poor performance, both in terms of time and space.
        - 2. Best fit policy:
            - we search the entire memory and will allocate the smallest  partition which is capable enough.
            - Advantage:
                - perform best in fix size partitioning scheme.
            - Disadvantage:
                - difficult to implement, perform worst in variable size partitioning as the remaining spaces which are of very small size.
        - 3. Worst fit Policy:
            - It also searches the entire memory and allocate the largest partition possible.
            - Advantage:
                - perform best in variable size partitioning
            - Disadvantage:
                - perform worst in fix size partitioning, resulting into large internal fragmentation.
        - 4. Next fit policy:
            - It is the modified version of first fit. It says start searching from the point where last request satisfied.

    - External fragmentation:
        - External fragmentation is a function of contiguous allocation policy. The space requested by the process is available in memory but, as it is not being contiguous, cannot be allocated this wastage is called external fragmentation.
    - Internal fragmentation:
        - Internal fragmentation is a function of fixed size partition which means, when a partition is allocated to a process. Which is either the same size or larger than the request then, the unused space by the process in the partition is called as internal fragmentation.

    - How can we solve external fragmentation:
        - We can also swap processes in the main memory after fixed intervals of time & they can be swapped in one part of the memory and the other part become empty(Compaction, defragmentation). This solution is very costly in respect to time as it will take a lot of time to swap process when system is in running state.
        - Either we should go for non-contiguous allocation, which means process can be divided into parts and different parts can be allocated in different areas.

### 2. Non-contiguous Memory allocation (Paging)
    - Paging is a memory management scheme that permits the physical address space of a process to be non-contiguous.
    - Paging avoids external fragmentation.
    
    - Secondary memory is divides into fixed size partition(because management is easy) all of them of same size called pages(easy swapping and no external fragmentation).
    - Main memory is divided into fix size partitions (because management is easy), each of them having same size called frames(easy swapping and no external fragmentation).
    - Size of frame = size of page
    - In general number of pages are much more than number of frames (approx. 128 time) 

#### Translation process
    - CPU generate a logical address is divided into two parts - p and d 
        where p stands for page no and d stands for instruction offset.
    - The page number(p) is used as an index into a Page table
    - Page table base register(PTBR) provides the base of the page table and then the corresponding page no is accessed using p.
    - Here we will finds the corresponding frame no (the base address of that frame in main memory in which the page is stored)
    - Combine corresponding frame no with the instruction offset and get the physical address. Which is used to access main memory.

    Page Table:
        - Page table is a data structure not hardware.
        - Every process have a separate page table.
        - Number of entries a process have in the page table is the number of pages a process have in the secondary memory.
        - Size of each entry in the page table is same it is corresponding frame number.
        - Page table is a data structure which is it self stored in main memory.
    
    - Advantage:
        - Removal of External Fragmentation
    - Disadvantage:
        - Translation process is slow as Main Memory is accessed two times(one for page table and other for actual access).
        - A considerable amount of space a wasted in storing page table(meta data).
        - System suffers from internal fragmentation(as paging is an example of fixed size partition).
        - Translation process is difficult and complex to understand and implement.
    - Page Table Size = No of Entries in Page Table * size of each entry(f)
    - Process Size = No of pages * size of each page.

#### Solutions to Paging problems
    - A serious problem with page is, translation process is slow as page table is accessed two times (one for page table and other for actual access).
        - to solve the problems in paging we take the help of TLB. the TLB is associative high speed memory.
        - Each entry in the TLB consists of two parts: 
            a key (Page no) and a value (frame no). 
        - When the associative memory is search for page no, the page no is compared with all page no simultaneously. If the item is found, the corresponding frame no field is returned.
        - The search is fast; the hardware, however, is expensive, TLB Contains the frequently referred page numbers and corresponding frame number.

        - The TLB is used with page tables in the following way. The TLB contains only a few of the page-table entries. When a logical address is generated by the CPU, its page number is presented to the TLB. If the page number is found, its frame number is immediately available and is used to access memory.
        - If the page number is not in the TLB (known as a TLB Miss), then a memory reference to the page table must be made.
        - Effective memory Access time:
            hit [TLB + main memory] + (1 - hit)[TLB + 2 main memory]
    - Size of Page:
        - If we increase the size of page then internal fragmentation increase but size of page table decreases.
        - If we decrease the size of page then internal fragmentation decrease but size of page table increases.
        - So we have to find what should be the size of the page, where both cost are minimal.

#### Multilevel Paging / Hierarchical Paging
    - Modern systems support a large logical address space (2^32 to 2^64).
    - In such cases, the page table itself becomes excessively large and can contain millions of entries and can take a lot of space in memory, so cannot be accommodated into a single frame.
    - A simple solution to this is to divide page table into smaller pieces.
    - One way is to use a two-level paging algorithm, in which the page table itself is also paged.

### 3. Non-contiguous Memory allocation (Segmentation)
    - Paging is unable to separate the user's view of memory from the actual physical memory. Segmentation is a memory-management scheme that supports this user view of memory.
    - A logical address space is a collection of segments. Each segment has a name and a length. The addresses specify both the segment name and the offset within the segment. The user therefore specifies each address by two quantities: a segment name and an offset.
    - Segments can be of variable lengths unlike pages and are stored in main memory.
    
    - Segment Table: 
        - Each entry in the segment table has a segment base and a segment limit. The segment base contains the starting physical address where the segment resides in memory, and the segment limit specifies the length of the segment.
        - The segment number is used as an index to the segment table. The offset d of the logical address must be between 0 and the segment limit. If it is not, we trap to the operating system.
        - When an offset is legal, it is added to the segment base to produce the address in physical memory of the desired byte. Segmentation suffers from External Fragmentation.
    
### 4. Segmentation with Paging
    - Since segmentation also suffers from external fragmentation, it is better to divide the segments into pages.
    - In segmentation with paging a process is divided into segments and further the segments are divided into pages.
    - While similar to multilevel paging, this approach is superior because it allows for varying partition sizes, matching the different sizes of segments. It shares the same core properties as multilevel paging.

### 5. Inverted Page Table
    - The drawback of paging is that each page table may consist of millions of entries. These tables may consume large amounts of physical memory just to keep track of how other physical memory is being used. To solve this problem, we can use an Inverted Page Table.
    - An inverted page table has one entry for each real page (or frame) of memory. Each entry consists of the virtual address of the page stored in that real memory location, with information about the process that owns the page. Thus, only one page table is in the system, and it has only one entry for each page of physical memory.
    - Thus number of entries in the page table is equal to the number of frames in the physical memory.