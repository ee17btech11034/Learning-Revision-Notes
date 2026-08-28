# Caching
    - Client put a req, server takes it and then fetch the data from Database. This is costly and slow process.
    - We store the data in Cache and if client re then we check in cache and if found then we return it.
    - Caching:
        - Kind of a memory or small database that is fast
        - Very fast
        - Usually small in Capacity

    - Cache Hit:
        - Able to find the resource in cache.
    - Cache Miss:
        - Not able to find the resource in cache.

    - Better system ==> higher val of (Cache Hit / Cache Miss)


## Cache Eviction Methods:
    - Methods to replace the Cache.
        - 1. Random Evicton:
            - Remove any random Eviction.
            - Here Any frequently accessed may get out.
        - 2. First in First Out:
            - Olver one will be replaced.
            - Here also frequently accessed may get out.
        - 3. LFU (Least Frequently Used):
            - Replace the cache that is least frequently accessed.
            - Chances that we remove something that we did not need much in past but in future we may need it.
        - 4. LRU (Lease Recently Used):
            - Replace the cache that is least recently accessed.
            - Chances that we remove something that we did not need in near past time but in future we may need it.

## Careful around:
    - Consistency:
        - If resource is updated in Database and we still kep copy of older data.
        - We will be providing Stale data. 
        - We should be refreshing to updte the cache with latest data.
    - Coherence:
        - Caches in different regions could get out of sync
    - Security:
        - We do not want user to put their credentials everytime. 
        - Sessions and credentials should be cached with caution.


## Shared Storage:
    - To store the session ids, or some important ids we need this No-SQl DB.
    - Think like we have multiple server-db mchines for different region.
    - Server for one region is gone. Then if we store session ids on that then we will be needing to re-login user again.
    - Shared DB just redirect the client as it already has the session id.