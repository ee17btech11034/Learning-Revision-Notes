# Transaction
    - Here we want whole program to be atomic in nature.
    ```bash
        Transaction T1:

            Read(A)
            A = A - 100
            Write(A)
            Read(B)
            B = B + 100
            Write(B)
    ```
    - Atomic in nature means if failure occurs in mid way then revert all above steps.


## ACID property:
    - Atomicity:
        - atomic in nature. 
    - Consistency:
        - DB should be consistent before and after execution.
    - Isolation:
        - A transaction should appear as though it is being executed in isolation from other transactions, even though many transactions are executing concurrently.
    - Durability:
        - Commit transaction must persist in the DB.


## Transaction States:
    - Active:
        - It is initial state. 
        - Transaction remains in this state whle it is executing operations.
    - Partially Commit:
        - Once all the instructions are completed in "Active" state then it comes here. 
        - Changes are handles in buffer/locally.
    - Commited:
        - Here we make changes in main DB from buffer.
    - failed:
        - If it failes either in "Active" or "partially Commited" state.
        - It goes to failed state.
    - Aborted:
        - All changes are reverted that were done in Active state.

## Need of Concurrent execution:
    - it leads to good DB performance, less waiting time.
    Overlapping I/O activity with CPU increases throughput and response time.

    - To handle the issues in it we need 'Scheduling".

### Schedule:
    - Serial Schedule:
        - T1 runs after T0. 
    - Non-Serial:
        - Some part of T1 runs and some part of T2 runs. 
        - But we check if they are interdependent. Like both are trying to update same val.
        - We divide this in 2 parts, Conflicting and independent. 
        - Independent like both transactions are reading either same or independent. 
        - Problem occurs where atlease one instruction is write and common.

        - Conflict Equivalent:
            - Conflict serialization
        - view serialization



## Recorverability:
### non-recoverability Vs Recoverability Schedule
    - Dirty Read. 
        - T1 made changes and we read that in T2 but we commited T2 first and before commit for T1 was happening. A failure opccured. Now What T2 read is a dirty read.
        - Top solve it we want that if we do dirty read then commit after that.

### Cascading Rollback Vs Cascadeless Schedule
    - Ek agar fail hua to rollback kr rha hai to usse read krne walle bhi kre, this is costly.
    - cascadeless me ham commit T1 ke pura hote hi krte hai like serialization.

### Strict Schedule:
    - If a transaction has updated a val then we will neither read nor write on that untill it is commited.