# Memory Management

    Register -- cache memory  -- Main Memory  --  Magnetic Disk/optical Disk
capacity (left to right increase)
access time (left to right increase)
per unit cost (left to right decrease)


## Diagram:

CPU  -----Cache ---  Main/Primary/Physical memory /RAM  -- Seconday / logical/virtual/auxiliary memory.
    ----------------

CPU will fetch the data from Cache or RAM not from seconday because secondary is very slow which affect the CPU process.
Cache has L1 (~768 KB), L2 (~4MB), L3 (~16 MB). 

## locality of Reference (LOR)
If CPU 7 maain memory is that small then how does it gets maximum data from cache or main memory That is because of LOR.
It lets fetches the nerby useful memory toc current memory. this way Cache hit is > 90% as well as RAm hit is > 90%.  
2 type of locality:
- Spatial Locality: Refers to the use of data elements in the near by locations. Like program execute in seq, so when asked for a location then its next few data is also pulled.
- Temporal Locality: refers to use of specific data / resources within a relatively small duration or most frequent used item. LRU is used for it.

Cache Hit: If program find the required data in Cache. 

Hit ratio: The cache hit rate is the ratio of data access requests that are being satisfied by the cache. This Ratio is impacted by various factors, such as the size of the cache, the behaviour of the program using cache etc.

Hit Latency: time taken to get the data from cache if cache hit occurred.

Cache Miss: When data is not found in Cache memory. to reduce cache miss and improve performance, we use strategies like increase the size of cache, optimize the cache replacement algorithms, more efficient data storage strategy.

Miss Latency: time taken to get the data from main/disk storage if cache miss occurred.


Computer work flow:
CPU generate address called logical address according to Seconday memory as CPU assumes we can use full disk memory. But CPU should not use seconday memory as it will make it slow.

Operating System comes into picture and convert Logical Address to physical Address. 
OS => 
    LA from sec memory --> PA of RAm after putting data in main memory

COA => convert physical Address to cache address.
    PA from main memory --> Cache Address of Cache after putting data in Cache.


As we saw, data is moving from secondary to main to cache meory, we need a specific size sections so that data can be fit in. Like we cannot fetch and store data of 2KB in 1KB Cache or main mory. 

We divide secondary memory in equal size like 1Kb, these are called "Pages".
We create same size (1 KB) partition in main memory called Blocks in COA and frame in OS. 
We create same size (1 KB) partition in cache memory called Cache Line or Cache Block. 

1 kilo = 10^3 == 2^10
1 Mega = 10^6 == 2^20
1 Giga = 10^9 == 2^30
1 Tera = 10^12 == 2^40
1 Peta = 10^15 == 2^50


Memory Size: 
    -- Address length in bits = n
    -- no of address/locations we can generate = 2^n
    -- Memory Size = (number of Locations) * (Size of each location)
    -- Ex:
        -- Size of each location = 1 Byte (default)
        -- Number of Locations = 2^17 if n = 17
        -- MS = 2^17 * 1 Byte =2^7 * 2^10 * 1 byte = 2^7 KB

Address length in bits = UpperBound(Log2(n)) where n is no of locations.
    -- memory size = 32 GB.
    -- location size = 1 Byte
    -- no of locations = (memory size) / (location size) = 32GB/1B = 32G = 2^35 
    -- address length = 35.


## Cache Mapping:
It is relationship of main memory and cache memory.
### Memory
 Computer has 1D memory. Generally we use "Word" for locations. 
 For ex if we have 64 locations (W0, W1, ... , W63), we divide it into 16 blocks/pages (B-0, B-1, ..., B-15). Each block will handle 4 locations/Words. When we want to fetch the data of a location/Word then instead of that only we pull the respective block, as we may need the next sequential data.
 

### Cache Mapping
- Cache Mapping refers to the process of determining where data should be store in the Cache memory.
- The Cache mapping algorithm determines which cache lines are assigned to which main memory blocks. Like 4 blocks (CL0, Cl1, ..., CL3) are in Cache and main memory blocks (B0, b1,...B63) are there. 
- Types of Cache mapping algorithms
    1. Direct Mapping: Each main memory block can be stored in only one specific cache line. Here 
        CL0  <-- B0,   B4,    B8, .....
        CL1  <-- B1,   B5,    B9, .....
        CL2  <-- B2,   B6,    B10, .....
        CL3  <-- B3,   B7,    B11, .....
        Here B2, B6 will always go to CL2 even if above Cache blocks are free.
        - Cl Number = (Block number) % no of Cache Lines (remainder)
        - We need to store TAG as well to identify that which block is stored in cache. This way it is easier for look up. We use Block number as TAG but if we see last 2 bits will be enough to know for 4 bit word. No need to store 4 bit just store with 32 bit (last 2 bits of block).
        - Cl1 <--- B1 (0001), B5 (0101), B9 (1001), B13 (1101)
        - we can see last 2 bits are same for it. Means if a block has last 2 bits 01 then it will go to Cl1. 
        - Inside CL1 we know that only 4 blocks (B1, B5, B9, B13) will come to this means we need 2 bits to represet, we will give 
            00 to B1, 
            01 to B5, 
            10 to B9, 
            11 to B13, etc. this is like Hashing. It is helpul for look up.
        - disadvantage is Conflict miss like what is we need B0, B4, B8, only repetatively, then we will be removing and adding then removing and adding.
        -- main memory ( physical Address)
                <------------ block Number ---> |<--- Block Offset ---> 
                <--- Tag --->  Cache line ----> |<--- Block Offset ---> 
                            |--------------Cache ---------------------> 
            -- Assume Address were 64 means 6 bits.
            -- Each Block is refering to 4 Words. block Number = 4
            -- Block Offset = 6 - 4 = 2
            -- Means Representation of a Word in bits, first 4 bits will tell about the block number and last 2 will tell about offset means position in that block like 0-4.
            -- Cache has 4 line and each has 4 locations/Words. Total = 16 lines.
            -- Block Offset = 2
            -- To identify one of 16 lines, we need bit = 4 bit. Cache = 4
            -- Cache line = Cache - block offset = 4 - 2 = 2
            -- tag = bits - cache = 6 - 4 = 2.
            -- in easy language. 
                -- In main memory: 
                    -- It has 64 Words, we take 4 words and create a block. 
                    -- blocks = 16 (we need 4 bits to represet the block numbers) but better to use first 4 bits of word number as it will represent the same. Each block has 4 words that means we need 4 address / 2 bits to represet. Last 2 bits of Word is Offset.
                -- in Cache:
                    -- Assume we have 4 Cache Lines (CL0, CL1, CL2, CL3), each has 4 words. 
                    -- Total words = 16, we need 4 bits to represent the 16 words/addresses.
                    -- Out of 4 we can use first 2 for Cache Lines (0-4) and last 2 for offset for word position in cache.
                    -- To keep the tage we need 2 more bits in this case as only 2 addresses will come to this. 
                    -- Final conclusion is, representation of a word tells, first 2 bits will tell about tag, next 2 will tell about line, last 2 will tell about position in line.
    
    2. Associative Mapping: Any main memory block can be stored in any free cache line. It is also known as Many to Many Mappings.
        - To overcome the problem of Conflict-miss in direct mapping, we use this.
        - Tag will be same as block number, it is slow when searching.
        - Tag Directoy size = (Number of tags) * (tag size) = (Number of lines in cache) * (Number of bits in tag)
        - We can add comparator which check number in all Lines parallely and pass those to OR Gate this way we have fast output but to add this many comparator it will be costly.
        -- main memory ( physical Address)
                <------------ block Number ---> |<--- Block Offset ---> 
                <--- Tag = Block Number-------> |<--- Block Offset ---> 
                            |-- Cache line ---> |<--- Block Offset ---> 
                            |--------------Cache ---------------------> 

    3. Set-associative mapping: The cache is divided into sets, each of which contains several cache lines. A main memory block can be stored in any cache line within a set.
        - like Set-0 (CL-0, CL-1), set-1 (CL-2, CL-3).
            - Set-0  <--  B0, B2, B4
            - Set-1  <--  B1, B3, B5
        - In k-wat set associative mapping, cache lines are grouped into sets where each set cotains "k" number of lines. A particular block of main memory can map to only one particular set of the cache. Within that set, the memory block can map to any freely available cache line.
        -- main memory ( physical Address)
                <------------ block Number ---> |<--- Block Offset ---> 
                <--- Tag --->  set -----------> |<--- Block Offset ---> 
                            |--------------Cache ---------------------> 

### Cache Replacement Policies
- In direct mapped cache, each memory blockmaps to a single, predetermined cache location. Since each block has a fixed position, no replacement policy is needed. 
- in fully associative & set-associative caches, multiple blocks can map to the same set or cache position. When all possible positions are occupied, a decision must be made on which block to replace.

1. FIFO Policy: 
    - In FIFO (First in, First Out), the block that entered the cache first is replaced first when cache is full. We start to full by 0 to n-1 line. available = i % n
    - this can lead to issue called Belady's Anamaly, where increasing the number of cache lines may unexpectedly result in more misses, which reduce efficiency.
        - Ex. 1, 2,3, 4, 1, 2, 5, 1, 2, 3, 4, 5 with Cache size = 3 miss = 9 then CS = 4 miss= 10. Sometimes it may increase. 

2. Optimal Algorithm:
    - The Optimal Page replacement Algorithm replaces the page that will not be used for the longest period in the future. This algorithm offers the best theoretical performance but is impractical to implement because it requires precise knowledge of future page references, which is geerally impossible.
        - jab replace krna ho to future dekho ki konse n-1 word wapas repeat honge unko leave krke remaining 1 line ko replace kr do. But agar futu me koi > 2 ki entry nahi hai to previous exist dekhte hai ki konsa recently used hua hai jo hua hai usko as it is rakho and jo bahut time se use nhi hua usko leave kr do.
    - Despite its limitations, the optimal algorithm serves as benchmark to evaluate the efficiency of the other cache replacement policyies.
    - We can not implement it because we do not know about the future code/part. But no algorithm is faster than this.

3. LRU (Least Recently Used):
    - LRU replacement policy replaces the page that has not been accessed for the longest period in the past. It uses past access patterns to predict which page is least likely to be needed soon.
    - While effective, implementing LRU can be computationally expensive in practice, as tracking the exact order of page usage requires additional overhead.

###  Type of Miss
- Compulsory Miss: 
    - When CPU demands for any block for the first time then definitely a miss is going to occur as the block needs to be brought into the cache, it is known as Compulsory Miss.
- Capacity Miss: 
    - Occur because blocks are being discarded from cache because cache can not contain all blocks needed for program execution. Happens only when cache is full with no space left.
    - It happens only in associative or set associative, not in direct mapping.
- Conflict Miss:
    - In the case of set associative or direct mapped block replacement strategies, conflict misses occur when several blocks are mapped to the same set or block frame; also called collision misses or interference misses.

## Memory Organization
- Memory is organized at different levels, CPU may try to access dfferent levels of memory in different ways. On this basis, the memory organization is broadly divided into two types
    1. Sequential/hierarchical :
        - Level-1 (L1): Directly connected to the CPU
        - Level-2 (L2): connected to L1
        - Level-3 (L3): connected to L2, and so on.
        - Memory Access Process:
            - CPU first searches for the required data in L1. 
            - If not found, it searches in l2.
            - if still not found, it continues searching in L3 and subsequent levels.
        - Memory Access Time: h- hit rate, T - time to look in level
            - Avg time required to access memory per operation =  (H1 * T1) +    (1- H1) * H2 * (T1 + T2)  +   (1 - H1)(1 - H2)H3 (t1 + T2 + T3) 
    2. Parallel:
        - Level-1 (L1): Directly connected to the CPU
        - Level-2 (L2): Directly connected to the CPU
        - Level-3 (L3): Directly connected to the CPU, and so on.
        - All levels are connected to the CPU, CPU starts searching for word in all the levels simultaneously.
        - Memory Access Time: h- hit rate, T - time to look in level
            - Avg time required to access memory per operation =  (H1 * T1) +    (1- H1) * H2 * (T2)  +   (1 - H1)(1 - H2)H3 (T3) 
- We assume that we will get the data in last level that means H3 = 1 here. 

## Cache Coherence Problem
- if multiple copy of same data is maintained at different level of memories then inconsistency may occur, this problem is known as cache coherence problem. Like when data is copied from Main memory to cache then data also persist in main memory as it is copy-paste operation not cut-paste. When CPU update the data in Cache then we can say that same data copy has different values one copy at cache level and another one at main memory, it is called Data consistency. Cache coherence problem can be resolved using the following techniques: Write Through. Write Back.
    1. Write Through
        - Write through is used to maintain the consistency between the cache and main memory. According to it if the cache copy is updated, at the same time main memory is also updated.
        - Advantages: It provides the highest level of consistency.
        - Disadvantages: It requires more number of memory access as we have to update main memory again and again.
        - As data is updated parallely so we do not need Dirty bit here.
    2. Write Back:
        - It is also used to maintain the consistency between the cache and main memory.
        -- According to it all the changes performed on cache are reflected back to main memory in the end.
        - Advantages: Less number of memory access and less write operations.
        - Disadvantages: inconsistency may occuras it is updated in the end when we are removing that data from cache.
        - To know or mark that this data has been updated, we use a bit to mark it that is called "Dirty Bit", 0-> no updated, 1-> updated.