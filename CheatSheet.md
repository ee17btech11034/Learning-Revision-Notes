# Interview Prep: Ultimate CS Basics, HLD, & LLD Cheat Sheet

This comprehensive cheat sheet focuses on practical, high-level engineering choices, trade-offs, and frequently asked interview topics, bypassing long academic lectures.

---

## 🌐 Part 1: Computer Networks (CN)
*Focus on how data moves across the internet and how services talk to each other.*

### Core Concepts
*   **TCP vs. UDP:** 
    *   **TCP:** Reliable, connection-oriented, guarantees packet delivery, and handles congestion control. Used for HTTP, WebSockets, and database connections.
    *   **UDP:** Fast, connectionless, lightweight, and allows packet loss. Used for real-time video streaming, VoIP, and gaming.
*   **The 4-Way Handshake:** The standard sequence used to safely and gracefully close an established TCP connection from both sides.
*   **HTTP Evolution:**
    *   **HTTP/1.1:** Suffers from Head-of-Line (HoL) blocking (one slow request blocks all subsequent ones on that connection).
    *   **HTTP/2:** Introduced multiplexing over a single TCP connection, allowing concurrent requests and responses.
    *   **HTTP/3:** Moves from TCP to QUIC (built on UDP). Eliminates TCP-level HoL blocking and allows faster connection migration across networks.
*   **DNS Resolution:** The process of turning a domain name into an IP address. It traverses a hierarchy: Root server ➡️ Top-Level Domain (TLD) server ➡️ Authoritative Name Server.
*   **Load Balancers:**
    *   **Layer 4 (L4):** Operates at the transport layer. Routes raw bytes based on IP and TCP ports. Fast but blind to packet content.
    *   **Layer 7 (L7):** Operates at the application layer. Routes traffic based on actual HTTP content, URLs, headers, and cookies. Smart but CPU-intensive.

---

## 💻 Part 2: Computer Organization & Architecture (COA)
*Focus on memory hierarchy and concurrency traps.*

### Core Concepts
*   **Memory Hierarchy:** 
    *   `CPU Registers` ➡️ `L1/L2/L3 Cache` ➡️ `RAM` ➡️ `SSD/HDD`.
    *   **Trade-off:** Faster memory is physically closer to the CPU, smaller, and highly expensive; slower memory is distant, massive, and cheap.
*   **Cache Locality:**
    *   **Spatial Locality:** Accessing memory items physically close together (e.g., looping sequentially through a contiguous array).
    *   **Temporal Locality:** Re-accessing the exact same memory item or variable repeatedly within a short timeframe.
*   **Cache Misses:** Occur as a cold start (compulsory), capacity limitation, or conflict. High cache misses drop application throughput significantly as the system falls back to slow RAM or disk.

---

## ⚙️ Part 3: Operating Systems (OS)
*Focus on resource management and multi-threading, which are vital for backend performance.*

### Core Concepts
*   **Process vs. Thread:**
    *   **Process:** An isolated, running instance of a program with its own dedicated memory space.
    *   **Thread:** A lightweight unit of execution inside a process. Threads share the parent process's memory space. Context switching between threads is cheap, but shared memory introduces race conditions.
*   **Concurrency vs. Parallelism:**
    *   **Concurrency:** Managing and making progress on multiple tasks by interleaving their execution over time (can happen on a single CPU core).
    *   **Parallelism:** Executing multiple tasks at the exact same physical instant (requires multiple CPU cores/hardware).
*   **Deadlocks:** Occur when threads are permanently blocked waiting for each other. Requires **four simultaneous conditions**:
    1.  *Mutual Exclusion* (resource cannot be shared).
    2.  *Hold and Wait* (holding a resource while waiting for another).
    3.  *No Preemption* (resources cannot be forcibly taken away).
    4.  *Circular Wait* (Thread A waits for B, B waits for A).
    *   *Prevention:* Always acquire locks in a strict, globally consistent order.
*   **Virtual Memory & Paging:** The OS maps application-level virtual memory addresses to physical RAM using fixed-size blocks called pages. 
    *   **Thrashing:** A critical failure state where the OS spends more time swapping pages in and out of disk storage than executing actual application code.

---

## 💾 Part 4: Databases & Storage Internals
*Understand how storage engines manage data consistency, indexing, and isolation levels.*

### Core Concepts
*   **ACID Properties:**
    *   **Atomicity:** All operations in a transaction succeed, or the entire transaction is rolled back (All-or-Nothing).
    *   **Consistency:** A transaction moves the database from one valid, constraint-compliant state to another.
    *   **Isolation:** Concurrent execution of transactions leaves the database in the same state as if they were executed sequentially.
    *   **Durability:** Once a transaction is committed, its changes survive system crashes or power failures.
*   **Transaction Isolation Levels (Crucial):**
    1.  **Read Uncommitted:** Lowest level. Allows *Dirty Reads* (reading uncommitted data from other transactions).
    2.  **Read Committed:** Prevents dirty reads, but allows *Non-Repeatable Reads* (re-reading the same row gives different data because another transaction committed changes mid-way).
    3.  **Repeatable Read:** Prevents non-repeatable reads, but allows *Phantom Reads* (queries returning range matches see new rows inserted by another transaction).
    4.  **Serializable:** Highest isolation level. Transactions executed completely in a conceptual line. Drastically drops write performance due to locking.
*   **Index Internals:**
    *   **B-Trees / B+ Trees:** Self-balancing trees optimized for disk-read systems. Used heavily in relational databases (MySQL, PostgreSQL) because they excel at point lookups and range queries (`WHERE age BETWEEN 20 AND 30`).
    *   **LSM Trees (Log-Structured Merge-Trees):** Append-only structures optimized for incredibly high write throughput. Used in NoSQL databases (Cassandra, RocksDB).

---

## 🌍 Part 5: Distributed Systems Core Concepts
*The core architectural trade-offs you must call out explicitly in High-Level Design rounds.*

### Core Concepts
*   **CAP Theorem:** In a distributed system face-to-face with a Network Partition (**P**), you must choose between Consistency (**C** - every node returns the latest write or an error) or Availability (**A** - every healthy node returns a non-error response without guarantee it contains the latest write).
*   **PACELC Theorem:** Extends CAP. If there is a Partition (**P**), choose Availability (**A**) or Consistency (**C**); Else (**E**), when the system is running normally, trade off between Latency (**L**) or Consistency (**C**).
*   **Replication Strategies:**
    *   **Synchronous:** Master waits for replicas to confirm write before responding to the user. High consistency, high latency, risk of blocking if a replica dies.
    *   **Asynchronous:** Master responds immediately after writing locally; replicas copy data in the background. Low latency, but risks data loss if the master crashes before sync finishes.
*   **Split-Brain Problem:** Occurs when a distributed cluster fractures into two isolated halves, and both sub-clusters elect their own master node. Avoided using **Quorum Sensing** (requiring a strict majority of nodes like $N/2 + 1$ to elect a leader).

---

## 🗺️ Part 6: High-Level Design (HLD) Microservices Patterns
*How to use architectural design patterns to scale real-world applications.*

### Core Concepts
*   **Network Protocol Choices:**
    *   **WebSockets:** Best for bidirectional, persistent, low-latency communication (e.g., Live chat apps, collaborative docs). Operates over TCP.
    *   **gRPC:** Ideal for internal microservice-to-microservice communication. Leverages HTTP/2 for multiplexing and Protocol Buffers for fast, binary serialization (saves major network bandwidth and CPU cycles).
    *   **Polling vs. Long-Polling:** Use Long-Polling only when updates are sparse and setting up persistent WebSockets is overkill.
*   **Storage & Caching Decisions:**
    *   **Applying Memory Hierarchy:** Deploying an in-memory cache like Redis (RAM-based) in front of a relational database (Disk-based) protects the primary database from heavy read loads and avoids slow disk I/O bottlenecks.
    *   **Sharding & Consistent Hashing:** Distributing massive datasets across multiple independent database nodes. **Consistent Hashing** ensures that when storage servers are added or removed, only a minimal fraction of keys need to be remapped or moved.
*   **Concurrency at Scale:**
    *   **Rate Limiters:** Protecting infrastructure from malicious traffic, brute-forcing, or accidental DDoS spikes. Know **Token Bucket** (allows bursts) vs. **Leaky Bucket** (smooths out traffic flow).
    *   **Message Queues (Kafka / RabbitMQ):** Implements asynchronous processing. Decouples a fast, write-heavy ingestion layer from slower down-stream data processing layers.
*   **Distributed Transactions (Saga Pattern):** You cannot use standard ACID database locks across independent microservices. Use the **Saga Pattern** instead: Break the business workflow into consecutive local microservice transactions. If step 3 fails, execute explicit **Compensating Transactions** backward to reverse steps 1 and 2 manually.
*   **Fault Tolerance (Circuit Breaker Pattern):** Prevents cascading failures. If a downstream microservice degrades or goes down, the Circuit Breaker trips **Open** and immediately fails fast (or serves a fallback response) rather than hanging and exhausting the caller's server thread pool.

---

## 🛠️ Part 7: Low-Level Design (LLD) & Concurrency
*How to express CS fundamentals cleanly through code structures, thread safety, and design patterns.*

### 1. Advanced Concurrency Primitives
* **Thread Pools & Thread Exhaustion:** Creating OS threads is incredibly heavy. Systems use Thread Pools to reuse a fixed number of threads. If all threads are stuck waiting for a database query, the server faces Thread Exhaustion, causing incoming requests to drop.
* **Virtual Threads / Coroutines:** Modern frameworks (like Java's Virtual Threads, Go Goroutines, or Node async/await) decouple software execution lines from heavy OS-level threads. Millions of virtual threads can map to just a few physical OS threads, drastically scaling LLD efficiency.

### 2. Thread Safety & Memory Control
* **The Singleton Pattern Trap:** Unprotected Singleton patterns cause race conditions where multiple threads initialize multiple distinct instances in memory. Fix this via `Double-Checked Locking` or `Eager Initialization`.
* **Producer-Consumer Pattern:** Used to pass tasks safely between multi-threaded workloads. Implement this utilizing native thread-safe data structures like BlockingQueue to handle lock coordination implicitly.
* **Optimistic vs. Pessimistic Locking:**
    - **Optimistic Locking:** Assumes conflicts are rare. Uses version numbers or timestamps (db_version). Fails the transaction if a conflict occurs. Great for read-heavy systems.
    - **Pessimistic Locking:** Assumes conflicts are highly likely. Explicitly locks the row or table (SELECT ... FOR UPDATE), blocking all other threads. Best for high-contention, high-risk operations (like banking transactions).

### 3. Essential Go-To Design Patterns
* **Strategy Pattern:** Defines a family of interchangeable algorithms and encapsulates each one (e.g., switching seamlessly between different payment vendors like Stripe, PayPal, or Razorpay without changing core client logic).
* **Observer Pattern:** Creates a subscription model to notify multiple listener objects automatically of any state changes (crucial for event-driven decoupled systems).
* **Factory Pattern:** Provides an interface for creating objects in a superclass, allowing subclasses to alter the type of objects created without exposing instantiation logic.

### 4. SOLID Principles Check
* **S - Single Responsibility:** A class should have one, and only one, reason to change.
* **O - Open/Closed:** Software entities should be open for extension, but closed for modification.
* **L - Liskov Substitution:** Objects of a superclass must be completely replaceable with objects of its subclasses without breaking the application.
* **I - Interface Segregation:** Clients should never be forced to depend on interfaces or methods they do not actually use.
* **D - Dependency Inversion:** Depend on abstractions (interfaces), not on concrete implementations.