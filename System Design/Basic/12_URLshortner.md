# URL Shortner

    - we can see bitly.com, tinyurl.com
    - It gets redirected to actual URL.

## Requirements:
    - What is the Volume of URLs that we want to handle
        - 100 million / day
    - How short the URL should be
        - length of short url (keep as short as we can)
    - what kind of characters do you need
        - Numeric, alphanumerc, or with symbols.
    - do we want 'i' and 'l' letter to be removed top increase the readibility.
    - can short URL be deleted or updated
        - no (for simplicity)
    
## System Requirements:
    - We need o know what the memory we need, what rea/write speed we need.
    
    - Back of the Envelope calculations:
        - Assuming 100 million URL / day generate = 10^8
        - Write operations per sec = 10^8 / (24 * 60 * 60) = 1160 op/sec
        - If we run this service for nxt 10 yrs = 10^8 * 365 * 10 = 365 * 10^9 records
        - assume 100 bytes per record => 365 * 10^9 * 100 bytes = 365 * 10^11 bytes = 36.5 TB

    - Redirection  cab be in 2 ways:
        - 301 ==> permanent redirect
            - We will cache the result in client ans do not need to go to site for re-attempt.
        - 302 ==> temporarily moved
            - we can use for clickes for a particular url 

## URL Shortening (High Level View)
    - Long URL ==> f(x) ==> shorturl/charcters.

    - Assume we allow alphanumeric 0-9, a-z, A-Z. ==> 62 chars. 
    - if length is 7 then 62^7 combinations.
    - in distribution system, we can not maintain the Hash Table. Because Hash Table is in memory, when we have system around the world, they need to be connected but memory can not be connected.
    - So, we store that in DB, with ID, short URL, Long URL.

    - Functions to generate Tiny URL:
        - 1. Hash:
            - Take a hash and generate hash number
            - take first 7/8 characters
            - issue is theses first 7/8 characters may be same but whole str is different.
            - Methods:
                - MD5:
                    - Will convert that into exact 7/8 characters
                - SHA-1:
                    - We take first 7/8 chars
                - CRC-32:
                    - We take first 7/8 chars
        
        - 2. Hash + Collision Resolution:
            - Here we check the first 7/8 chars in db and if it is not present add it.
            - If present then we append a temp predefined string in input url and generate a new short.

        - 3. ID Based Approach (Base 62)
            - We have characters with mapping:
                - 0-9 ==> 0 -> 9
                - a-z ==> 10 -> 35
                - A-Z ==> 36 -> 61
            - We take a num = 11157 that is nothing but the ID.
                - char1 = num % 62; num = num // 62
                - char2 = num % 62; num = num // 62

                ...
                - Read it in reverse from bottom to top. (2TX)
            - Flow:
                - long url ==> is url in db ==yes==> return the short url
                                            ==no==> generate new id ==> create shorturl for ID ==> Save ID, short url, long url. 

            - Security concerns like we can guess next number if we can find the ID.
            - Inconsistent in short url like some will be of length 3, some of 4, 5 , etc.

    - We can cache the some inputs.


# Features:
    - We can put the length to 7 fr all but with p[remium we can provide the length to be 8 or 9. 
    - Premium users can choose the prefix or suffix of their choice