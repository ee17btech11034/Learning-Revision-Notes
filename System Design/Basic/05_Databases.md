# Databases

    - We store the data in db to store and retrieve the data in efficient manner.


## Advantages:
    - Efficient Data Retrieval:
        - Quick quries for any information that we need.
        - We do not need to scan entire storage.
    - Data Integrity & Consistency:
        - All operations make sure that records remain accurate.
    - Handle Complex queries:
        - Find out performance, usage matrics, correlation, advanced insights, data mining.
    
## Challenges:
    - Scalibility:
        - When multiple clients waant different services at same time and each is trying to access the Db, then it may be slow. 
        - We need to scale the DB by dividing it.
    - Consistency:
        - When we deploy DB in multiple regions then it is our responsibility that all other are consistent.
        - Means same query should be able to fetch the same output on any DB.
    - Availability:
        - If one DB is corrupted then we make copies of that and we atleast be available.
        - Backups are available.