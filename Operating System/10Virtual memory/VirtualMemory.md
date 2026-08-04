# Virtual Memory
    - To enable multiprogramming and optimize memory, modern computing often uses pure demand paging to keep multiple processes in memory.
    - Pure Demand Paging: 
        - A memory management strategy where a process begins execution with zero pages (no pages) in memory, loading them only upon explicit demand during execution. 
            1. Process starts with zero pages in memory, causing an immediate page fault.
            2. The necessary page is loaded, allowing execution to resume.
            3. Further page faults occur only when new, required pages are needed.
            4. Once all necessary pages are loaded, execution continues. The core principle is to load pages only upon demand.
        - We do not load on locality of reference. Only load the page that CPU asked for..
     - Advantage:
        - A program would no longer be constrained by the amount of physical memory that is available, Allows the execution of processes that are not completely in main memory, i.e. process can be larger than main memory.
        - More programs could be run at the same time as use of main memory is less.
    - Disadvantages
        - Virtual memory is not easy to implement.
        - It may substantially decrease performance if it is used carelessly (Thrashing)

## Implementation of Virtual memory
    - We add a new column in page table, which have binary value 0 or Invalid which means page is not currently in main memory, 1 or valid means page is currently in main memory.
    - Page Fault:
        - When a process tries to access a page that is not in main memory then a Page Fault Occurs.
    
    - Steps to handle Page Fault:
        1. If the reference was invalid, it means there is a page fault and page is not currently in main-memory, now we have to load this required page in main-memory.
        2. We find a free frame if available we can brought in desired page, but if not we have to select a page as a victim and swap it out from main memory to secondary memory and then swap in the desired page(situation effectively doubles the page-fault service time ).
    
    - We can reduce this overhead by using a Modify bit or Dirty Bit as a new column in page table.
        1. The modify bit for a page is set whenever the page has been modified. In this case, we must write the page to the disk.
        2. If the modify bit is not set: It means the page has not been modified since it was read into the main memory. We need not write the memory page to the disk: it is already there.
    - Performance of Demand Paging:
        - Effective Access time for demand paging:
            ==> (1 - p)*ma + p*page fault service time
            --> p -> page fault rate or probability of page fault
            --> ma is memory access time.

# Page Replacement Algorithms
It will decide which page to replace.
    1. FIFO:
        - First in first out page replacement algorithm.
        - oldest page will be replaced if itis full.
        - Its performance is not alays good.
        - Belady's Anomaly: 
            - For some page algorithms, the page-fault rate may increase as the number of allocated frames increases.
    2. Optimal:
        - Optimal Page Replacement Algorithm
        - Replace the page that will not be used for the longest period of time. 
        - It has lowest page-fault rate of all algos.
        - will never suffer from Belady's anomaly.
        - We need to know the future page eferences that is near to impossible. It is hard to implement.
        - It is used to compare/test other algos.
    3. LRU:
        - Least Recently Used Page replacement Algorithm
        - We check the page which has not been used for the longest time and replace it. 
        - When we need to replace a page then we check the backwards pages and find that is not used recently.
        - Does not suffer from Belady's Anomaly.

# Thrashing
    - Definition: Thrashing occurs when a process spends more time swapping pages than executing, often triggered when low CPU utilization leads to increasing the degree of multiprogramming.
    - Process: As processes demand more frames, they take them from others, causing a chain reaction of page faults and swapping, which empties the ready queue.
    - Result: The scheduler mistakenly adds more processes to combat low CPU activity, worsening the issue, resulting in skyrocketing page faults, plummeting system throughput, and, ultimately, no productive work.

## Solution => The Working Set Strategy
    - This model uses a parameter \(\Delta \), to define the working set window. The set of pages in the most recent \(\Delta \) page references is the working set.
    - If a page is in active use, it will be in the working set. If it is no longer being used, it will drop from the working set.
    - The working set is an approximation of the program's locality. The accuracy of the working set depends on the selection of \(\Delta \) . If \(\Delta \) is too small, it will not encompass the entire locality; if \(\Delta \) is too large, it may overlap several localities.