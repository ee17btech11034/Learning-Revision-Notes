# Network Layer
    - Source to Destination Delivery:
        - Delivers packets from source to destination, possibly over multiple networks.
    - Logical Addressing: 
        - Uses logical addresses to identify the sender and receiver.
    - Routing: 
        - Responsible for finding the best route to send packets using routing protocols.
    - Packetizing: 
        - Involves encapsulating payload at the source, adding a header with essential details, and preserving payload integrity during transit, barring fragmentation cases.
    - Error and Flow Control: 
        - Encompasses adding a checksum in the datagram header for detecting corruption (not covering the entire datagram), with limited direct involvement in flow control, and using ICMP for some error control activities (ICMP just inform about the error does not solve it).
    - Congestion Control: 
        - Manages network congestion, handling situations when too many datagrams crowd a network segment and addressing capacity exceedance issues in networks or routers.


## datagram:
    - Packets used by the Ip are called. 
    - Header size = 20 to 60 Bytes
    - total size = Header +  payload => 20 to 65,535 bytes.

## Internet Protocol
### IPv4:
    - treat each datagram independent.
    - IP ke header me TCP hota hai.
    - 4 bit version.
    - Version:
        - First 4 bits tells the version 4 or 6.
    - Header Length:
        - 4 bit can represent 0 to 15.
        - but header length is of 20 to 60 bytes. 
        - To represnet this in 4 bits we multiply with 4 and it will be 0 to 60 but of multiple of 4.
        - numbers < 20 are of no use for us, to get the numbers that are not multiple of 4 we use padding.
    - Service Type:
        - It has 8 bits.
        - first 3 bits are reserved for to generate priority(111). 
        - next 4 are for DTRC 
            - D: Minimize Delay
            - T: Maximize throughput
            - R: Maximize reliability
            - C: Minimize Cost.
        - we can choose only one out of 4.
        - last nit is of no use.
    - total length:
        - 16 bit = 65,535
    - identification:
        - agar data packets ka fragmentation hota hai (mid way bhi) to uska identification number same hoga. 
        - 16 bit.
    - fragmentation bit:
        - fragments ke pahle number ko hi ham offset maante hai 
        - lekin first number hi bada ho to uske liye ham inki marking ko store krne ke liye 3 bit me ham number/8 kr dete hai. 
    - Flag bits:
        - 3 bits are there. 
        - first is of no use.
        - second tells "Do not fragment" means do not open and reak it. If that can not send it then it will discard it.
        - third bit tell "More fragment" tell that if it has 1 that means more are comming, if it has 0 then it was last.
    - Time-to-live:
        - 8 bit
        - If we send any packets and each router is sending that to another. This type of data may float on internet like garbage. 
        - We put a timeline or lifespan for that packet generally we set to 8 to 20 (max 2^8 = 255) and each router will reduce one length of it. like 255 -> 254 -> 253 ....--> 0. It will discard it.
    - protocol:
        - 8 bit
        - ICMP (01), IGMP(02), TCP(06), UDP(17), OSPF(89).
        - we just check this and find the protocol.
    - Header Checksum:
        - 16 bits
        - We run this checksum for header on each router.
        - no impact on payload.
    - Source and Destination Address:
        - each 32 bits).
    - Variable part:
        - 0 to 40 bytes.
        - 1 byte for padding
        -Record Route:
            - each address is of 32 bits (4 byte to store)
            - we can remember 9 routers. (9 * 4 = 36 byte)


### IPv6:
    - 128 bit (16 byte)
    - 2 parts:
        - Base header
        - payload

### Addreess Resolution Protocol:   
    - 

### RARP:


### Casting:
    - Unicast (one to one)
    - Broadcast (one to everyone)
        - limited:
            - locally connections ko broadcast, not on internet
        - direct
            - different group of network, not on whole internet.
    - multicast (one to many but not everyone)

### Subnet
    - subnetworks in a network.
    - wifi share in multiple people.
    - 2 types: 
        - Fixed length:-> all subnets are of same size.
        - Variable
    - Subnet Mask:
        - Subnet Mask of class A = 255.0.0.0
        - Subnet Mask of class B = 255.255.0.0
        - Subnet Mask of class C = 255.255.255.0

## classless:
    - a.b.c.d/x tells that first x bits tells the network Id. can not touch them
    - total = 32 bits
    - combinations = 32 - x
    - no of address = 2^(32 - x)
    - first when all last (32-x) bits are 0 then it is network id.
    - if all last (32 - x) bits are 1 then it is host id.
    - last 8 bits ko lekar range nikal sakte hai network block.


## Routing
    - Router has a routing table.
    - Ways:
        - 1. Flooding:
            - Send it to all, no routing mechanism equired.
        - 2. Routing:
            - static:-> fixed router table with paths
            - Dynamic:-> automaticallu update table.
    - Link state Routing:-> Dijikstra's algo is used.