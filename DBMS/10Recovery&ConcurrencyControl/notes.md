# Recovery

## Log based Recovery:
    - We log all the steps in a book.
    -  2 Ways:
        - Deffered DB Modification
            - We keep the changes and do commit at last only.
        - Immediate DB Modification
            - Commit changes as we are doing it.


## Shadow Paging Recovery Technique:
    - we create a copy of page table. 
    - we make changes in new copy.
    - If all good then update is new table.

## Data Fragmentation:
    - Horizontal Fragmentation:
        - Row wise divide. Few rows are store somewhere and other few on different.
    - Vertical Fragmentation:
        - Col wise divide. Few columns are store somewhere and other few on different.
    - hybrid Fragmentation:
        - Dono divide.


# Concurrency Control
    - We need protocols which create transaction that follow properties automatically on runtime. 

## Time Stamping Approach:
    - We provide serial no (timestap at which it entered the system) and if conflict happens then we resolve by looking at both.
    - We associate Read and Write timestapmp (serial No of transaction) for data item as well.

## Lock based method:
    - Lock the db so other one can not access it.
    - Modes:
        - Shared mode:
            - Read operation can be done by multiple Ts.
        - Exclusive mode:
            - If T_i want to write anything.
    - Isme System Dead-lock me ja sakta hai. 
    - 2 Phase Locking:
        - Each Transaction has 2 phases:
            - Growinf phase:
                - Here Ts may obtain locks, but not release them
            - Shrinking Phase
                - Here Ts may release locks, but not obtain them
    - Here multiple issues can occur.
    - We have multiple variants to solve these.

## Validation based protocol:
    - It assumes that conflict does not happen generally.
    - Max read only Transactions hi hote hai.
