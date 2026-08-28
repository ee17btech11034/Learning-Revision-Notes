# Design Quick Commerce Service

## Flow:
    - Nearby Service:
        - First we collect the location of client (long, lat)
        - Then we find the Centers nearby within x km range. Locations for Centres are stored in DC_Locations db.

        - Instead of direct distance find the actual distance. Like if centre is in front but it is river and no road then it is of no use. So find the lowest distance by travel
        - We take the list of some centres so that we can find the items in any of those.
    
    - Availability Service:
        - It will tell that are items available on a particular centre.
        - Distribution centre will have its own db for items. It must be with ACID properties like PostgreSQL. (as 2 users can not oder same item if only one item is remaining. with low level locking)

    - Order Service:
        - After we ientify the centers, we make transactions (ACID) and confirm the order.

    
    - We would not make it fault tolerant as if consistency is break and other db does not have the updated itms then we may make order that is not available. 
    - We want to make it consistent

## Improvements:
    - Can we cache DC locations for a particular area. 