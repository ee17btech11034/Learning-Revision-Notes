# Indexing in Databases

    - To retrieve the data we can  upgrade the hardware but that is also it a extent.
    - We use indexing to make it faster.

    - We create seperate table that store the pointers to Db.
    - An index table acts like a map to store the memory address.


## Methods to create:
    - B Tree:
        - small child in left side, greater are in right side.


## Types of Indexing Methods:
    - 1. Primary:
        - Main values for uniqueness and fast access.
        - We have only one key as identifier, using that we devide the data.
        - Generally if we have Date col then it is useful.
    - 2. Secondary:
        - Use another column with primary key.
    - 3. Composite:
        - Indexing based on multiple columns to identify the results.
    - 4. Hashing:
        - Using a function to store the data in a calculated bucket #.
        - We create a bucket to store key as Hash function and values as pointer to the memory address block. 
        - This way it is faster.
        - We can use this in "log user visits" as theey will be similar entries, so easier to create hash.


## CHallenges:
    - The number of write operations will increase as we need to update index table too.
    - Adding indexes is not free, we need more space --> more cost incurred.
    - Cleanup unused indexes periodically (Audit regularly).
    
    
- Like we may need indexing to store student table  pointer for student class wise. But no need to keep indexing table for teachers as they won't be much and we will be using space unnecessarily.