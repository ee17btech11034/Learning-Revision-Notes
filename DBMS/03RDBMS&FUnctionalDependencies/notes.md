# Functional Dependency
## Relational DataBase Management System
    - A relational database management system (RDBMS), conceptualized.
    - Central to its design is the utilization of tablets for data storage where it maintains and enforces specific data relationships, marking a significant evolution in database design.
### Basics of RDBMS:
    - Domain:
        - It is also called Field/Column/Arity/Degree.
        - Domain (set of permissible value in particular column) is a set of atomic values.
    - Table (Relation):
        - A relation is a set of tuples/rows/entities/records
    - Tuple:
        - Each row of a Relation/Table is called Tuple.
    - Arity/Degree:
        - number of Columns/attributes of a Relation. 
    - Cardinality:
        - Number of rows/tuples/record of Relational instance. 

### Properties of Relational Table:
    - Cells contain atomic values
    - same kind of values in a column
    - Each row is unique
    - No two tables can have the same name in relational Schema.
    - Each column has a unique name
    - Seq or row/col in insignificant.

### Problems in Relational Database:
    - Update Anomalies:
        - Anomalies that cause redundant work to be done during insertion into and Modification of a relation and that may cause accidental loss of info during deletion from a relation
    - Insertion Anomalies:
        - Like branch name is stored with students. Isme agar koi branch me koi student hi nhi hai to wo table nhi hogi.
        - Us branch ke liye me koi another table me entry nahi kar sakta because branch is dependent on students. Like branches are that have students.
    - Modification Anomalies:
        - Agar hame branch name change krna hai to kitni jagah change karna hoga.
    - Deletion Anomalies:
        - Agar single student hi tha koi branch ka tab again same problems.

    - These all problems came because of Redundency (repeat of same data). 
    - To over these we divide tables. Like Student ki table alag and branch ki table alag. branch code ki Primary key can behave like Foreign key of Student.

### Purpose of Normalization:
    - It is refinement process.
    - 1NF >>> 2NF >>> 3NF >>> BCNF.
    - Each table must represnt one idea.


## Functional Dependency (FD)
    - If we give one information then we must be able to find another information based on that.
    - col1 -> col2 is FD if for each val in col1, we can find exact one value in col2. 
    - T1(a) = T2(a) ==> Tuple value of col1 (a) for tuple 1 and tuple 2 is same then
    - t1(b) = T2(b) it must be this.

    - Trivial FD:
        - if b is a subset of a, then the FD a -> b will always hold.
        - xy->y does not make much sense. Like by giving xy we get y, here all are cols.

    - Attributes Closure / Closure on Attribute Set / Closure set of Attributes:
        - Attribute closure of an attribute set can be defined as set of attributes which can be functionally determined from F.
        - Denoted by F^+.
        - Like R(ABCDEFG)
            A->B
            BC->DE
            AEG->G
            (AC)^+ = ?
            Ans:+++++++++++
                - (AC)+ -> AC
                        -> ABC (Here A-> se B ko find kr skte hai)
                        -> ABCDE (BC-> DE)
        - Armstrong's axioms:
            - Stnadard ways to calculate Closures.
            - Reflexivity :=> AB -> B
            - Augmentation :=> if A-> B then AC-> BC
            - transitivity :=> if A->B and B->C then A->C.
            - These are RAT Rules.
            - More rules are below:
            - Union :=> if x->y and x->z then x->yz
            - Decomposition :=> if x->yz then x->y and x->z
            - Pseudo Transitivity :=> If x->y and wy->z, then wx->z
            - Composition :=> If x->y and z->w, then xz->yw.
        
        - Canonical Cover:
            - Remove any dependency if we can. like without that also we can get all attributes by other paths.

## Keys:
    - No such thing as key in DB. But generally Super key is called Key.

### Super Key:
    - set of attributes using which we can identify each tuple uniquely is called Super Key.
    - It can have multiple super keys.
### Candidate Key:
    - Minimal set of attributes using which we can identify each tuple uniquely. 
    - Also called MINIMAL SUPER KEY
    - There must be atleast one Candidate Key.
    - like A->BCD, BCD->A. Here both are candidate key as none of them is subset of another.
### Prime Attributes:
    - Attributes that are member of at least one candidate keys are callled Prime Attributes.
### Primary Key:
    - One of the candidate key is selected by DBA as Primary key. 
    - Primary key val can not be null.
    - Candidate keys that are not choosen are callled Alternate Key.
### Foreign Key:
    - A foreigh key is a column or group of columns in a relational Database table that refers the primary key of the same table or some other table to represent relationship.
    - the concept of referential integrity is derived from foreign key theory.
    - Same table like student table me monitor id ho to studentid hi use hogi. 
### Composite Key:
    - It is a key composed of more than one column sometimes it is also known as concatenated key.
### Secondary Key:
    - It is a key used to speed up the search and retrieval contrary to primary key. 
    - It is not necessary to contain unique values.
    - Like age or income se sort/search krke fir primary key search use kro to faster resut milte hai.