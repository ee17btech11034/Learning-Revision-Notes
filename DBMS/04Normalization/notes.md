# Normalization
    - this helps us to remove Redundancy.
## First Normal Form
    - 1NF is the initial step of database normalization.
    - Implication:
        - Atomic Vaues
        - Unique Colmns
        - Primary Key
        - Eliminating Duplicates

- Partial Dependency:
    - When non-prime attribute is dependent only on a part of candidate key. (PRIME > Non-Prime)
    - AB->D, A->c. 
- FUll Dependency:
    - When non-prime attribute is dependent on the entire candidate key. 

## Second NF:
    - It must be 1 NF.
    - It shopuld not have any partial dependency.
    - if we find any partial then we divide the table.

- Transitive Dependency:
    - A functional dep from non-prime attribute to non-prime attribute.
    - A->B, B->c, C->d, a is candidate key and last 2 are TD.

###  3rd NF:
    - It should be 2nd NF.
    - It must not have any Transitive Dependency.

    - Or direct if A-> B then A is super key or B is prime attribute.

### BCNF (Boyce Codd Normal Form)
    - A relational schema R is said to be BCNF if every functinal dependency in R form
        - A-> B; A must be a super key.


- Ideas beyond Functinal (above) Dependencies.

## Multivalues Dependency:
    - Denoted by, A->-> B, means for every val of A, there may exist more than one val of B. 
    - It cn be represented by A->-> OR A->> B.

## Trivial Multivalued Dependency:
    - Each table can have at max one trivial Dep 
## non-Trivial Multivalued Dependency:
    - col1 -->> col2, col1 -->> col3. Then we will have to break the table.


## 4 NF:
    - It must be BCNF
    - Must not exist any non-trivial multivalued dep.


## Lossy/lossless-dependency Preserving Decomposition
    - to ensure no data loss bcz of Normalization.
    - divide krte time wo common hoga jiske sare vlaues unique ho. Means common must be a Key.


## 5 NF:
    - it must be $ NF.
    - It can not be further non-loss decompossed.

- Dependency Preerving Decomposition:
    - Not mandatory.