# ER Diagram
    - Entity Relationship Diagram.
    - It is Easy to draw and understand
    - Easy to convert in tables

## Entity:
    - An entity is a thing or an object in the real world that is distinguishable from other object based on the values of the attributes it possesses.
    - It may be:
        - Concrete such as person or book
        - abstract such as course
    - 2 Types:
        - Tangible: Entities which physically exist in real world eg Car, Pen, locker
        - intangible: Entities which exist logically eg Account, Video.
    - Each row is entity (no duplicate rows). 
    - We can not represent entity in ER.
    - Attributes are shown in columns. 
    - Multiple Entites of same type with same properties or attributes are called Entity Set/Table. Table is a relation.
    - We present it using Rectangle shape box in ER.

## Attributes:
    - Attributes are the units defines and describe properties and characteristic of entities.
    - These are represented by ellipse or oval connected to rectangle. 
    - types:
        - Single Valued:
            - Attributes having single val at any instance of time for an entity. Eg Aadhar no. DOB.
        - MultiValued:
            - It can have more than one val for an entity at same time. Eg phone no, email, address
            - represented by doule ellipse or independent table in a relational model.
        - Simple:
            - Can not be divide further such as Age.
        - Composite:
            - Attributes which can be further divided into sub parts, as simple attributes. 
            - it is represented by ellipse connected to an ellipse and in relational model by a seperate column.
        - Stored:
            - Main attribute whose val is permanently stored in db eg DOB.
        - Derived:
            - value is derived from other attributes. Eg Age can be derived from DOB.
            - we can have a column but calculated during runtime
        - Descriptive:
            - Attribute of relationship (not entity) is called descriptive attribute.
            - It takes 'null' val when entity does not have a val for it.
            - We want an attribute that will be calculated from 2 entities Employee and Department. Then we represent it by connecting it to relationship of both entity.
        
## Relationship / Association:
    - Relationship is an association b/wtwo or more entities of same or different entity set.
    - in ER, we cannot represent individual relationship as it is an instance or data.
    - Represented by a diamond box.
    ```bash


                                        /\
                                       /  \
                                    __/    \____
                                      \    /
                                       \  /
                                        \/
    ```
    - Every Relationship type has 3 components:
        - Name:
            - Every relationship must have a unique name.
        - Degree:
            - number of entities set (relationship/tables) associated(participate) in the relationship set.
            - unary relationship:-->
                - one single entity set participate in a relationship, means two entities of the same entity set are related to each other.
                - also called self-referential relationship set.
                - Eg monitor of class is also student of the class. 
                - Class ---- two parallel lines--- Relation/monitoring
            - binary:-->
                - two entities in a relationship
                - mostly are binary
            - ternary:-->
                - 3 entities in relationship.
            - Quaternary:-->
                - 4 entities in relationship.
            - N-ary relationship:-->
                - When n number of entity set are associated.
        - Structural Constraints (Cardinalities ratios, participation)
            - Mapping Cardinalities /  Cardinality Ratio:
                - Express the number of entities to which another entity can be associated via a relationship set. 
                - 4 Categories:
                    - 1. One to One (1 : 1) Relationship:
                        - An entity in A is associated wit atmost one entity in B, and an entity in B is associated with at most one entity in A. 
                        - If we represent an arrow edge at entity then it means 1. Or we can write at line as well.
                        - Instructor <--- Advices (Relation) ---> Student
                        - Instructor --1-- Advices (Relation) --1-- Student
                        - If no relationship it is fine but if present then at most one. Eg not necessary that all students take advices from teacher.
                    - 2. One to Many (1:m) Relationship:
                        - An entity in A is associated with any number (zero or more) of entities in B. An entity in b, however, can be associated with at most one entity in A.
                        - Instructor --1-- Advices (Relation) --m-- Student
                        - Instructor <---- Advices (Relation) ---- Student
                    
                    - 3. Many to One (m:1) Relationship:
                        - An entity in A is associated with at most number one entity in B. An entity in b, however, can be associated with any number (zero or more) of entities in A.
                        - Instructor --m-- Advices (Relation) --1-- Student
                        - Instructor ----- Advices (Relation) ----> Student
                    - 4. Many to Many (n:m) Relationship:
                        - An entity in A is associated with any number (zero or more) of entities in B. An entity in b is associated with any number (zero or more) of entities in A.
                        - Instructor --n-- Advices (Relation) --m-- Student
                        - Instructor ---- Advices (Relation) ---- Student
                        - Participation Constraints:
                            - it defines participations of entities of an entity type in a relationship.
                            - Partial Participation
                                - at one relation from A to B is not done. 
                                - Like Each Author may not have a Book
                                - Represented by single line
                                - Author ---N:M---Book
                            - Total Participation
                                - at one relation from A to B. 
                                - Like Each book must have a Author
                                - represented by double line
                                - Book ---N:M---Author. (These are double lines as we can not show here.)
                        - We generally will have to create seperate table to present it.

                    - Strong And Weak Netity Set:
                        - An entity set is called Strong if it has a Primary Key, all tuples in the set are distinguishable by that key.
                        - Strong key is represent by underline of attribute
                        - An entity set is called Weak if it does not have a Primary Key. represent by double rectangular. Relationship with it shows weak with double layer diamond. Wek has a total participation.
                        - As weak does not have a primary key, it uses Partial Key called discriminaator attributes. Key will be primary of relation + partial key.
                        - Weak partial key is represented by under dash line.


## Generalization:
    - Involved merging two lower-level entities to create a higher level entity.
    - 
    ```bash
                            Account
                 ^              |
                 |              |
                 |          diamond(IS A)
                 |            /    \
                 |           /      \
                            /        \
                        Saving      Current
    ```

## Specialization
    - A process where a higher level entity is broken down into more specific, lower-level entities.
    ```bash
                            Person
                 |              |
                 |              |
                 |          diamond(IS A)
                 |            /    \
                 V           /      \
                            /        \
                        Employee    Customer
    ```


## Aggregation
    - Relationship with a block where block has multiple relationships.