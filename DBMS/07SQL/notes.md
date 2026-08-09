# SQL (Structured Query Language)

## Intro to SQL
    - Domain specific language used in programming and design for managing data held in a relational db management system (RDBMS).
    - it can define the structure of DB, modify the data and specify the security constraints, etc.

## Classification of DB languages
    1. Data Definition Language(DDL):
        - DDL is set of SQL commands used to CREATE, modify and delete database structures but not data.
        - DDL Commands: CREATE, ALTER, DROP, TRUNCATE, COMMENT, GRANT, REVOKE statement.
    2. Data Manipulation Language(DML):
        - DML is a language that enables users to access or manipulates data as organized by the appropriate data model.
        - 2 types:
            - Procedural
            - Declarative/non-preocedural
        - commands: INSERT, UPDATE, DELETE statement.
    3. Data Control Language (DCL):
        - it is a component of SQL statement that control access to data and to the datbase.
        - Commit, rollback command are used in DCL. GRANT, REVOKE.
    4. Data Query Language (DQL):
        - This comp of SQL allows getting data from the db and imposing ordering upon it.
        - SELECT statement.
    5. View Definition Language (VDL):
        - used to specify user view and their mapping to conceptual schema.
        - specifies user interfaces.
    
    - SQL is a DML language.

## DDL Commands:
    - create Table:
        ```bash
            # Blueprint:
                CREATE TABLE table_name (
                    column1 data_type [constraints],
                    column1 data_type [constraints],
                    ...
                )

            # Eg:
                CREATE TABLE Students (
                    StudentID INT PRIMARY KEY,
                    FirstName VARCHAR(50),
                    LastName VARCHAR(50),
                    Age INT
                )
        ```
        # Data Types:   
            - Numeric: 
                - INT, SMALLINT, BIGINT, DECIMAL(p,s), FLOAT, REAL.
            - String:
                - VARCHAR(n), CHAR(n), TEXT.
    
    - Adding a new column:
        ```bash
            ALTER TABLE Employees
            ADD PhoneNumber VARCHAR(15);
        ```
    - Dropping/Delete a column:
        ```bash
            ALTER TABLE Employees
            DROP COLUMN PhoneNumber;
        ```
    - Modifying a column:
        ```bash
            ALTER TABLE Employees
            MODIFY COLUMN PhoneNumber VARCHAR(20);

            OR

            ALTER TABLE Employees
            ALTER COLUMN PhoneNumber VARCHAR(20);
        ```
    - Renaming a Column:
        ```bash
            ALTER TABLE Employees
            RENAME COLUMN PhoneNumber TO ContactNumber;
        ```
    - Renaming a Table:
        ```bash
            ALTER TABLE Employees
            RENAME TO Staff;
        ```
    
    - Drop/ Delete Table
        ```bash
            DROP TABLE table_name;
        ```

    - Create table with Foreigh Key:
        ```bash
            CREATE TABLE Orders (
                OrderID INT PRIMARY KEY,
                CustomerID INT,
                OrderDate DATE,
                FOREIGN KEY (CUSTOMERID) REFERENCES Customers (CustomerID)
            );
        ```
    
    - Add foreign key:
        ```bash
            ALTER TABLE Orders
            ADD FOREIGN KEY (CUSTOMERID) REFERENCES Customers (CustomerID);
        ```




    ==== Commands for Instance====

    - Insert Values:
        ```bash
            BluePrint:
                INSERT INTO table_name (col1, col2, col3, ...)
                VALUES (val1, val2, val3, ...)

            Eg:
                INSERT INTO Students (StudentID, FirstName, LastName, Age)
                VALUES
                (1, 'Raj', 'Asiwal', 26),
                (2, 'Raja', 'Asiwal', 26);
        ```
    - Delete from table:
        ```bash
            DELETE FROM table_name
            WHERE condition;


            DELETE FROM Students
            WHERE StudentID=1;

            DELETE FROM table_name; --> isse sirf content delete hota hai means no change in schema.
        ```


## SQl Queries:
    - In case of operations on multiple Tables we take 2 and complete that and take 3 , and so on. 
    - At any time at max we take 2 and perform.
    - Structure:
        ```bash
            Select A1, A2, ..., An     (Column name)
            from r1, r2, ..., r_m      (Relation/table name)
            Where P;                   (Condition) 
        ``` 
    - By default SQL support Duplication, we can use DISTINCT to remove it.

    - 'Select *' ==> means need all the columns
    - 'Select distinct col_x' ==> remove duplication
    - 'Select col_x*1.5' ==> no change in main DB.

    - We need Where clause to filter the rows.
    - ' Select acc_no from account Where balance > 1000;
    - ' Select acc_no from account Where balance between 1000 and 10000; [inclusion range]
    - ' Select acc_no from account Where balance > 1000 and city='delhi;
    - we can use '<, >, <=, >=, <>, and, or, not, between, not between.

    - Set Operations:
        - Select customer_name from depositor
            Union                      ---> (we canuse Intersect or Except)
            Select customer_name from borrower
        - By default it removes duplicates. If we want duplicates then use 'union all / intersect all / except all


    
    +++++++++++ Queries on Multiple Relations +++++++++++++++++++

    - Select cust_name, balance
        from account, depositor
        where account.acc_num = depositor.acc_num  --> we need something for mapping for lossy / lossless as it will create all possible combinations. It is called Cartisian Product.

    - Natural Join / Inner Join:
        - It automatically identifies the common attribute and handles it. 
        - represent by 'infinite box sign'
        ```bash
            Select cust_name, balance
            from account natural join depositor
        ```
        - in cases where some data is only in one table, then it won't consider it. Sometimes it is lossy operator.
        - To resolve it we need Outer Join.

    - Outer Join:
        - It is extension of Inner join.
        - 1. Left Outer Join:
            - It does not let any loss at left side. 
            - It takes all from left table.
            - If nothing found on right then it puts 'null' there. 
        - 2. Right Outer Join:
            - It does not let any loss at right side. 
            - It takes all from right table.
            - If nothing found on left then it puts 'null' there. 
        - 3. Complete / Full Outer join:
            - It does not allow loss on any side.

    - Alias operations / Rename:
        - It does rename Db. Just rename on the copy we see.
        - It is useful in self comparison as well.
        - 'Select acc_num, balance*1.06 as total_balance from account'
        - Complex query as copy:
            ```bash
                Select balance
                from account
                Except
                Select A.balance
                from account as A, account as B
                where A.balance < B.balance;

                ==> First it will create 2 copy of account table as A, B. 
                    - Find where A.Balance < B. balance
                    - Except that from first table.
            ```

    - Aggregate Functions:
        - Functions that take collection of values as input and return a single val.
        - 5 inbuilt function:
            - avg
            - min
            - max
            - sum
            - count

        - ```bash
            Select count(*)
            from account


            Select avg(balance)
            from account
            Where branch_name='delhi'
        ```

        - suppose a val is null for balance in table. Sum and ag will ignore it but count it will count. 
        - avg = sum(balance) / count(*) ==> Not always.********************************************************************************

    - Ordering the Display of Tuples:
        - 
        ```bash
            Select distinct branch_name
            from branch
            where branch_city='delhi'
            Order by branch_name aesc; ==> display the name in ascending order can use 'desc' for descending; default is aesc.
        ```

    - String Operaions:
        - by default SQL is case sensitive but we can change this.
        - like operator can use '_' or '%'.
            ```bash
                Select branch_name
                from branch
                where branch_name like '_____' ==> that branch name must have n character in it (n dash means n chars).



                Select branch_name
                from branch
                where branch_name like '%jaipur%' ==> that branch name must contain this string it (start/mid/end)
            ```

    - Group by Clause:
        - We can divide table in group and then run the query. 
        - Beneficial in cases like branch wise avg.
        ```bash
            Select branch_name, avg(balance)
            from account
            Group by branch_name
        ```

        - Some times we want to add conditions on groups:
        ```bash
            Select branch.branch_name, avg(balance)
            from branch, account
            where branch.branch_name = account.branch_name and branch_city='delhi'
            Group by branch_name
            Having avg(balance) > 1500
        ```
        - 'Where' works only on table on single run but "Having' works on groups as well.
        - Chalne ka flow ==>
            from ==> Where ==> Group by ==> Having ==> Select.

    - Trigger:
        - automated transition. Like OTP for transaction.


    
- Embedded SQL:
    - It is incorporated directly into a procedural language like C or java.

- Dynamic SQL:
    - It can run dynamically at runtimeas well.