# 🐧 Linux Systems & Fundamentals: SDE Interview Guide

This guide covers core Linux concepts, OS-level fundamentals, and production commands frequently tested in SDE interviews and system design rounds.

---

## 🏗️ 1. Linux Architecture & CS Fundamentals

### The Kernel vs. User Space
*   **Kernel**: The core abstraction layer of the OS that has unrestricted access to the underlying hardware (CPU, Memory, Disk, I/O devices). It manages processes, memory, and hardware resources.
*   **User Space**: The restricted environment where user applications, daemons, and shells execute. This separation prevents user applications from accidentally corrupting the system or other running programs.

### System Calls (Syscalls)
*   **Definition**: A system call is a programmatic interface that allows a user-space application to request a privileged service or resource from the Linux kernel.
*   **Common Examples**: `fork()` (create process), `exec()` (execute binary), `open()`, `read()`, `write()` (file I/O), `mmap()` (memory mapping).

### The Everything is a File Philosophy
*   In Linux, almost all resources are abstracted as data streams through the virtual filesystem (VFS). 
*   Physical storage, directories, hardware devices (`/dev/`), kernel statistics (`/proc/`), and network sockets are handled using standard file operations (`read`, `write`, `open`, `close`).

---

## ⚙️ 2. Process Management & Concurrency

### Processes vs. Threads
*   **Process**: An independent executing program instance with its own isolated virtual memory address space, file descriptors, security context, and environment variables.
*   **Thread**: The smallest unit of execution scheduled by the kernel. Multiple threads run inside a single process, sharing its memory space, heap, and open files, but maintaining their own stack registers and program counters.

### Process Lifecycle & States
*   **Running/Runnable (R)**: The process is currently executing on a CPU core or waiting in the CPU run-queue.
*   **Interruptible Sleep (S)**: The process is blocked waiting for an event (e.g., user input, network packet, storage I/O).
*   **Zombie (Z)**: A terminated process whose resource allocations are freed, but its entry remains in the kernel process table because the parent process hasn't read its exit status code via `wait()`.

### Key Commands for Process Management
```bash
# 1. View all running processes with resources (Snapshot)
ps aux

# 2. View process hierarchies (Excellent for spotting orphaned paths)
ps -ef --forest

# 3. Kill a process gracefully (Sends SIGTERM - Signal 15)
kill <PID>

# 4. Kill a process immediately and forcefully (Sends SIGKILL - Signal 9)
kill -9 <PID>

# 5. Check what process is binding to a specific network port (e.g., 8080)
sudo lsof -i :8080
```

---

## 🧠 3. Memory & File System Internals

### Virtual Memory & Paging
*   **Virtual Memory**: An architectural abstraction that gives each running process the illusion of having a vast, contiguous block of RAM. It protects processes from reading/writing into each other's spaces.
*   **Paging**: The system maps virtual addresses into physical memory in fixed-size blocks (typically 4KB) called "Pages".
*   **Page Fault**: An interrupt triggered when a program tries to access a memory page that isn't mapped into physical RAM. The kernel catches this and pulls the page from disk/swap or allocates it dynamically.

### Inodes & Hard vs. Symbolic Links
*   **Inode (Index Node)**: A database entry on the disk structure that describes a file's metadata (size, permissions, owner, timestamps, and data block pointers). Crucially, the inode *does not* store the file name.
*   **Hard Link**: A secondary directory entry pointing directly to an existing file's exact Inode number. Deleting the original file entry does not destroy the data until all hard links are unlinked.
*   **Symbolic Link (Symlink/Soft Link)**: A distinct shortcut file containing a path string targeting another file or directory. If the target is deleted, the symlink breaks.

### Key Commands for Memory & Storage Diagnostics
```bash
# 1. View physical memory allocations and swap space in human units
free -h

# 2. Check disk space usage across active partitions
df -h

# 3. Analyze disk space consumption of a directory (max-depth 1)
du -h --max-depth=1 /var/log

# 4. Monitor continuous virtual memory, swapping, and system I/O updates
vmstat 2
```

---

## 🌐 4. Networking & IPC (Inter-Process Communication)

### Inter-Process Communication (IPC) Mechanisms
When separate processes need to exchange state or data, they rely on kernel-mediated IPC channels:
*   **Pipes (`|`)**: Unidirectional data streams connecting `stdout` of one command to `stdin` of another.
*   **Sockets**: Network endpoints allowing processes to communicate across different machines (TCP/IP) or locally on the same host (Unix Domain Sockets).
*   **Shared Memory**: The fastest IPC mechanism. Multiple processes map the exact same physical memory block into their virtual spaces, eliminating copy overhead.

### File Descriptors (FDs)
*   A non-negative integer index assigned by the kernel tracking an open input/output resource.
*   By default, every process starts with three basic file descriptors:
    *   `0`: Standard Input (`stdin`)
    *   `1`: Standard Output (`stdout`)
    *   `2`: Standard Error (`stderr`)

### Key Networking & Troubleshooting Commands
```bash
# 1. Check all network interfaces and active assigned IP addresses
ip a

# 2. View all listening TCP and UDP sockets with process identities
sudo ss -tulnp

# 3. Trace network packet routing hops targeting an external domain
traceroute google.com

# 4. Perform an authoritative DNS lookup to pull a domain's A records
dig github.com

# 5. Test raw port connectivity and TCP handshakes to a remote server
nc -zv 192.168.1.50 443
```

---

## 🛠️ 5. Log Analysis & Text Processing (Crucial for Interviews)

In interviews, you are often asked how to scan production application logs to find exceptions, error rates, or top IP addresses. Master these tools:

```bash
# 1. Search for specific text patterns inside a log file (Case Insensitive)
grep -i "exception" application.log

# 2. Follow log entries in real-time as an application writes to it
tail -f /var/log/nginx/access.log

# 3. Find files larger than 100MB modified in the last 24 hours
find /var/log -type f -size +100M -mtime -1

# 4. Advanced SDE Challenge: Find the top 5 most frequent IP addresses in an access log
# (Assuming the IP is the first space-separated item in the file)
awk '{print \$1}' access.log | sort | uniq -c | sort -rn | head -n 5
```
