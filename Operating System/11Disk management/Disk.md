# Disk
## Definition
    - Magnetic disks serve as the main secondary storage in computers. Each disk has a flat, circular platter with magnetic surfaces for data storage.
    - A read-write head hovers over these surfaces, moving in unison on a disk arm. Platters have tracks divided into sectors for logical data storage.
    - Disks spin at speeds ranging from 60 to 250 rotations per second, commonly noted in RPM like 5,400 or 15,000.

## Transfer Time
    - Total Transfer Time = Seek Time + Rotational Latency + Transfer Time
    - Seek Time: - It is a time taken by Read/Write header to reach the correct track.
    - Rotational Latency: - It is the time taken by read/Write header during the wait for the correct sector. In general, it’s a random value, so far average analysis, we consider the time taken by disk to complete half rotation. (0 -> 1 revolution)
    - Transfer Time: - it is the time taken by read/write header either to read or write on a disk. In general, we assume that in 1 complete rotation, header can read/write the either track, so 
        total time will be = (File Size/Track Size) * time taken to complete one revolution.

## Disk Scheduling
    - Goal: The operating system must use hardware efficiently, which for disks means minimizing seek and waiting times while maximizing data transfer rates. This is achieved by managing the order of I/O requests.
    - Process: 
        - When a process requires disk I/O, it issues a system call to the OS, which may include details such as the operation type (input/output), disk address, memory address, and the number of sectors to be transferred.
        - If desired disk drive and controller are available, the req can be serviced immediately. If the drive or controller is busy, any new req for service will be placed in the queue of pending req for that drive.
        - When one req is completed, the OS chooses which pending req to service next.

### 1. FCFS (First Come First Served)
    - in this, the req are addressed in the order they arrive in the disk queue. This algo is intrinsically fair but does not provide fastest service.
    - Advantage:
        - Easy to understand and use
        - Every req gets a fair chance
        - no starvation (may suffer from convoy effect)
    - Disadvantage:
        - Does not try to optimize seek time or waiting time.

### 2. SSTF(Shortest Seek Time First) Scheduling
    - Major component in total transfer time is seek time, in order to reduce seek time if we service all the requests close to the current head position, this idea is the basis for the SSTF algorithm. 
    - In SSTF, the request nearest to the disk arm will get executed first i.e. requests having shortest seek time are executed first. Although the SSTF algorithm is a substantial improvement over the FCFS algorithm, it is not optimal.
    - Advantages:
        - Reduces total seek movement
        - Increases system throughput
    - Disadvantage:
        - Overhead to calculate the closest req.
        - Can cause Starvation for a req which is far from the current of the header
        - High variance of response time and waiting time as SSTF favours only closest reqs.
    
### 3. SCAN/ Elevator Algorithm
    - The disk arm starts at one end of the disk and moves towards the other end, servicing requests as it reaches each track, until it gets to the other end of the disk.
    - At the other end, the direction of head movement is reversed, and servicing continues. The head continuously scans back and forth across the disk.
    - Yaha ham 0-> last track tak jo bhi req mili unko satisfy karo and trck ko last track -> 0 chalo and again aise hi chalta rahega.
    - Advantages:
        - Simple easy to understand and use
        - No starvation but more wait for some random process
        - Low variance and Average response time
    - Disadvantages:
        - Long waiting time for requests for locations just visited by disk arm. (last/start track ki taraf jate huye hi to req ko handle kiya hai hamne.)
        - Unnecessary move to the end of the disk, even if there is no request.

### 4. C-SCAN Scheduling
    - When the disk head reaches one end and changes direction, fewer requests are nearby since those cylinders were just serviced. Most pending requests are at the opposite end, having waited the longest.
    - Circular-scan is a variant of SCAN designed to provide a more uniform wait time. Like SCAN, C-SCAN moves the head from one end of the disk to the other, servicing requests along the way. When the head reaches the other end, however, it immediately returns to the beginning of the disk without servicing any requests on the return trip.
    - Yaha ham 0-> last track tak jo bhi req mili unko satisfy karo and track ko wapas 0 pr le jao (no req handle on this revert) and 0 -> last track par hi req ko handle karo.
    - Advantages:
        - Provides more uniform wait time compared to SCAN
        - Better response time compared to scan
    - Disadvantage:
        - More seeks movements in order to reach starting position

### 5. LOOK Scheduling
    - It is similar to the SCAN disk scheduling algorithm except the difference that the disk arm inspite of going to the end of the disk goes only to the last request to be serviced in front of the head and then reverses its direction from there only. Thus, it prevents the extra delay which occurred due to unnecessary traversal to the end of the disk.
    - Yaha ham 0-> last req (na ki last track tak) tak jo bhi req mili unko satisfy karo and trck ko last req -> start req tak chalo and again aise hi chalta rahega.
    - Advantage: 
        - Better performance compared to SCAN
        - Should be used in case to less load
    - Disadvantage: 
        - Overhead to find the last request
        - Should not be used in case of more load.

### 6. C LOOK
    - As LOOK is similar to SCAN algorithm, in similar way, C-LOOK is similar to C-SCAN disk scheduling algorithm. In C-LOOK, the disk arm in spite of going to the end goes only to the last request to be serviced in front of the head and then from there goes to the other end's last request. Thus, it also prevents the extra delay which occurred due to unnecessary traversal to the end of the disk.
    - Yaha ham 0-> last req tak jo bhi req mili unko satisfy karo and track ko wapas start req pr le jao (no req handle on this revert) and start -> last req par hi req ko handle karo.
    - Advantage: 
        - Provides more uniform wait time compared to LOOK
        - Better response time compared to LOOK
    - Disadvantage: 
        - Overhead to find the last request and go to initial position is more
        - Should not be used in case of more load.