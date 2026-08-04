# File System
## File Allocation Method
    - The main aim of file allocation problem is how disk space is utilized effectively and files can be accessed quickly. Three major methods of allocating disk space are in wide use:
        - Contiguous
        - Linked
        - Indexed
    - Each method has advantages and disadvantages. Although some systems support all three, it is more common for a system to use one method for all files.

### 1. Contiguous Allocation
    - It requires that each file occupy a set of contiguous blocks on the disk.
    - In directory usually we store three column file name, start dba, length of file in number of blocks.
    - Advantage:
        - Accessing a file that has been allocated contiguously is easy. Thus, both sequential and direct access can b supported by contiguous allocation.
    - Disadvantage:
        - Suffer from huge amount of external fragmentation
        - Another problem with contiguous allocation is file modification.
    
### 2. Linked Allocation
    - With this, each file is a linked list of disk blocks; the disk blocks may be scattered anywhere on the disk. 
    - The directory contains a pointer to the first and last blocks of the file. Or we can sat -1 represent as last block for file but it may face some issues as how to know about data lose. better to keep either length or last node.
    - Advantage: 
        - To create, read, write a new file is simply easy. The size of a file need not be declared when the file is created. A file can continue to grow as long as free blocks are available.
        - There is no external fragmentation with linked allocation, and any free block on the free-space list can be used to satisfy a request.
    - Disadvantage: 
        - Only sequential access is possible, To find the \(i^{\text{th}}\) block of a file, we must start at the beginning and follow the pointers until we get to the \(i^{\text{th}}\) block.
        - Another disadvantage is the space required for the pointers, so each file requires slightly more space than it would otherwise.

### 3. Indexed Allocation
    - It solves problems of contiguous and linked allocation, by bringing all the pointers together into one location: ==> the index block.
    - We do not store data directly, we store pointers to data sections. And if needed we can store pointer to another block which also have pointers to some code blocks.
    - This way we can jump to any section of code faster without full traverse of data blocks.


## Free-space Management
    - Since disk space is limited, we need to reuse the space from deleted files for new files, if possible. To keep track of free disk space, the system maintains a free-space list. The free-space list records all free disk blocks—those not allocated to some file or directory.
    - To create a file, we search the free-space list for the required amount of space and allocate that space to the new file. This space is then removed from the free-space list. When a file is deleted, its disk space is added to the free-space list.
    - Approaches to acquire empty blocks:

### 1. Linked List
    - A approach to free-space management is to link together all the free disk blocks, keeping a pointer to the first free block in a special location on the disk and caching it in memory.
    - This first block contains a pointer to the next free disk block, and so on.
    - This scheme is not efficient; to traverse the list, we must read each block, which requires substantial I/O time. However, operating system simply needs a free block so that it can allocate that block to a file, so the first block in the free list is used.

### 2. Bit Vector
    - Frequently, the free-space list is implemented as a bit map or bit vector. Each block is represented by 1 bit. If the block is free, the bit is 1; if the block is allocated, the bit is 0.
    - For example, consider a disk where blocks 2, 3, 4, 5, 8, 9, 10, 11, 12, 13, 17, 18, 25, 26, and 27 are free and the rest of the blocks are allocated. The free-space bit map would be001111001111110001100000011100000 ...
    - The main advantage of this approach is its relative simplicity and its efficiency in finding the first free block or n consecutive free blocks on the disk.
    
    - (Image Diagram text: Blocks 0 to 15 mapped to Bits, showing Block 0/1 as 0 "Block is allocated" and Block 2/3 as 1 "Block is free".)

    - Unfortunately, bit vectors are inefficient unless the entire vector is kept in main memory. Keeping it in main memory is possible for smaller disks but not necessarily for larger ones.
    - A 1.3-GB disk with 512-byte blocks would need a bit map of over 332 KB to track its free blocks.
    - A 1-TB disk with 4-KB blocks requires 256 MB to store its bit map. Given that disk size constantly increases, the problem with bit vectors will continue to escalate as well.

## File Organization
    - Definition & Importance: 
        - File organization dictates how data is stored, impacting access methods, efficiency, flexibility, and storage device selection.
    - Methods of Organization:
        - Sequential: 
            - Records are stored and accessed in a specific, sorted order based on a key field, requiring a sequential search to locate data.
        - Random/Direct: 
            - Records are stored in no particular order but accessed directly using a key to locate them on storage media, typically on magnetic or optical disks.
        - Serial file organization:
            - a. Records in a file are stored and accessed one after another.
            - b. This type of organization is mainly used on magnetic tapes.
        - Indexed-sequential file organization method:
            - Almost similar to sequential method only that, an index is used to enable the computer to locate individual records on the stage media
            - For example, on a magnetic drum, records are stored sequentially on the tracks. However, each record is assigned an index that can be used to access it directly.

## File Access Mechanisms
    - Sequential Access: 
        - Information is processed in order, one record after another, commonly used by editors and compilers.
    - Direct Access: 
        - Based on disk models, this method allows reading or writing blocks/records in any order, making it suitable for database management systems.
    - Indexed Access: 
        - An index containing key fields and pointers is used to locate specific records, enabling direct access to data after searching the index.

## Directory
    - A directory is similar to a "folder" in everyday terminology, and it exists within file system.
    - It's a virtual container where multiple files and other directories (often called subdirectories) can reside.
    - It organizes the file system in a hierarchical manner, meaning directories can contain subdirectories, which may contain further subdirectories, and so on.
    
    - (Image Diagram text: A tree structure showing Root directory D1, branching down to User directories D11, D12, D13, D14, and further down to Files and subdirectories F1, F2, Sd1, F3, Sd2, F4, F5, F6, F7).

    - Common Directory Operations
        - Management: 
            - Create (mkdir), delete (rmdir/rm -r), and rename directories to organize file systems.
        - Navigation & Inspection: 
            - List contents (ls/dir) and change the current working directory (cd).
        - File Manipulation: 
            - Copy or move directories and their contents to new locations.
        - Organization & Access: 
            - Sort files by attributes and manage access permissions (read, write, execute).
        - Search: 
            - Locate specific files or subdirectories based on criteria.

## File Protection System
    1. Reliability
    2. Security
    3. Controlled Access
    4. Access Control


## Acces Matrix
    - Ways to present info like which user has what permission for which files.