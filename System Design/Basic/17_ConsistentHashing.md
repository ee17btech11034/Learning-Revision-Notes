# Consistent Hashing:
    - If our app is similar to ticket booking, where user login and book tickets.
    - Now we want this for more users. We create multiple db.
    - Now que is in which db we should keep the info / event track info for a user.
    - For this, we must evenly distribute the DB (Sharding). This is where Hashing comes into picture.

## Hashing
        - We take the db numbers = n.
        - We modulo user_id / event_id to find the exact db. 
        - It will always lead to the db for that user.

        - Now problem is what if we add 1 more db then this formula won't work, we will have to rearrange the existing data as well.

## Consistent Hashing
    - We place these db in circle
    - take modul with partitions we divided the circle in m. (m >= n)
    - by taking the modulo, we get the time or number at that clock. 
    - Go clockwise from there until we find the db with the data.
    - It saves time and memory by not checking all db.
    - If a db is removed then we can simply move its content to its next db in clockwise direction.

    - But here problem is like what if most/max events are in a particular region or for single db.
    - It will increase the load on that one.

    - To resolved it we add Virtual nodes.

    - Virtual Nodes:
        - On the ring in empty clock positions we put the virtual nodes to differnt dbs. like if val comes to this then go to this db that is in opposite dir or not nearby.
        - It will be hard to implement bcz now we will have many regions if we remove the db/node.

## Where we need this:
    - in distributed db
    - in distributed message broker