# Data
## Definitions:
    - Data:
        - Any fact or figures about an entity is called as Data.
    - Information:
        - Analysed and processed data is called Information.
    - Database:
        - Structured collection of data, facilitating easy access, management, and updates.
    - Database Management System (DBMS):
        - DBMS is software facilitating efficient data storage, retrieval, and management in database.
        - Ensures data safety and integrity, while offering accessibility and concurrency control.
        - Support functions like data quering, reporting, analytics for informed decision making.


## File System
    - Slower data retrieval due to unstructured querying capabilities.
    - Challenges in correlating data across seperate files leading to data isolation.
    - Risk of inadvertent data alterations or deletions creating integrity problems.
    - Potential for data inconsistency due to incomplete operations, leading to atomicity problems.
    - Conflict and inconsistencies from simultaneous data access/modifications, causing concurrent access anomalies.


## View of DB (data Abstraction)
    - View Level
    - Logical Level / Conceptual Level
    - Physical Level

### Physical Level:
    - The internal schema details data storage and access on hardware, featuring the lowest level of data abstraction with complex structures, predominantly managed by the database administrator.

### Logical Level / Conceptual Level:
    - Above the Physical Level, this level showcases data as entity sets and their relationships, detailing the types and connections b/w stored data in db.

### View level:
    - This is pinnacle of data abstraction, displaying only a portion of the entire database focusing on user-interest areas. 
    - it can represent multiple views of same data.

## Data independence
    - Capacity to change the schema at one level of a database system without having to change the schema at the next higher level.
    - 2 types:
        - Physical Data Independence
        - Logical Data Independence

## Instance and Schemas
    - Instance of the DB:
        - The collection of info stored in the db at a specific moment is called. 
        - 
    - DB Schema:
        - Overall design of the DB, illustrating the logical structure and organization of data.
        - It defines relationships and how data is organized.

## OLAP Vs OLTP
### OLAP (Online Analytical Processing)
    - deals with historical data
### OLTP (online Transaction Processing)
    - Current CRUD data.


## Types of DB
    - Commercial Database:
        - Used in business sector to handle large vol of transactions and customer data.
    - Multimedia DB:
        - Stores data types such as images, audio, video files. 
    - Deductive DB:
        - utilizes logic programming to derive information from data stored in database, allowing more complex and analytical queries.
    - Temporal DB:
        - Keeps track of changing data over time, allowing for queries concerning time-based data.
    - Geological Information System (GIS): 
        - Stores, Organizes, and analyzes geographical data, ...


## DBA (database Administrator)
    - DBA hold authority over data and the programs facilitating data access. 
    - Functions:
        - Schema Definition:
            - It outlines the original database schema. 
            - read about DDL Compiler
        - Storage Structure and Access Method Definition:
            - Responsible for forming appropriate storage structures and access methods.
        - Schema and Physical Organization modification:
            - Involves altering the db schema or physical storage organization.
        - Granting of Authorization for Data Access:
            - provides various types of data access for different users.
        - Integrity Constraint Specification:
            - maintain constraints.

