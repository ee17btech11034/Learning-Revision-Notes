# Indexing

## Flow:
    - ER Diagram --> Relation Model --> Normalization.
    - But after doing Normalization, Db gets slow as it is divided.
    - We do indexing to make retrieval fast.

## Sorted / ordered file:
    - Retrieval is fast O(log n) 
    - But append and deletion make go till O(n)

## Unsorted file:
    - Append is fast
    - retrieval or deletion is slow O(n)

## Indexing:
    - Index hamesh sorted hoga.
    - We divide main file in blocks and first element represent the block(sorted by that key)
    - indexes canbe established with key from table. 

### Primary Key:
    - Indexing is done on Primary Key.

### Clustered indexing:
    - If indexing is done on attribute which is sorted but not a key (means having multiple same values).
    - Yaha har block ke first ko rakhne ke bajay ham har block me distinct value ko provide krte hai.

### Secondary ndexing:
    - indexing is done on unsorted key. 
    - we keep each and every record in index file.
    - But indexing is sorted so waha wo fast ho jata hai.
    - example of dense. 


## Dense Vs Sparce:
    - When every value is present in indexing then it is dense. All distinct values are present
    - When only some values are present not all. Like we did in first element from block. Chances that more distinct values are in that block, they do not get entry.



## B-Tree:
    - A B tree of order m if non-empty is an m-way search tree in which:....
    - order means  this many max children a node can have. 
    - if a node can have n children then it can contain n-1 values. 
    - Think from a perspective like all values in mid of values will be in that range/children
    - middle wale ko upar push krte hai agar order full hota hai to.

## B+ Tree:
    -