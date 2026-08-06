# OSI Model
## All Layer Duies

### 1. Physical Layer:
    - It defines the characteristics of the interface b.w the devices and the trnsmission medium.
    - Responsinilities;
        - 1. Representation of bits:
            - To be trnasmitted, bits must be encoded into signals-elctrical or optical or wave (sound),  based on medium.
        - 2. Data rate:
            - The transmission rate (the number of bits sent each second) is also defined by physical layer.
        - 3. Line Configuration:
            - This layer is concerned with the connection of devices to the media.
        - 4. Physical Topology:
            - This handles this as well to choose the best topology.
        - 5. Transmission Mode:
            - This layer also defines the direction of transmission b/w two devices: 
                - Simplex, hald-duplex, or full-duplex.

### 2. Data Link Layer:
    - packet is called "Frame".
    - Responsinilities:
        - 1. Framing:
            - This layer divides the stream of bits received from the network layer into manageable data units called frames.
            - If needed then we divide the dtaa got from network layer in parts and add header and trailer and send them.
        - 2. Physical addressing:
            - If frames are to be distributed to different systems on the network, the data link layer adds a header to the frame to define the sender and/or receiver of the frame.
        - 3. Access Control:
            - When two or more devices are connected to the same link, data link layer protocols are necessary to determine which device has control over the link at any given time.
        - 4. Flow Control:
            - If the rate at which the data are absorbed by the receiver is less than the rate at which data are produced in the sender, the data link imposes a flow control mechanism to avoid overwhelming the receiver.
        - 5. Error Control:
            - To detect and retramsmit damaged or lost frames. 
            - Uses a mechanism to recognize duplicate frames. 
            - Error control is achieved through a trailer added to the end of the frame.

### 3. Network Layer:
    - It is responsible for the source-to-destination delivery of a packet, possibly across multiple networks (links).
    - Here packet is called "Datagram".
    - Responsinilities:
        - 1. Logical addressing:
            - If a packet passes the network boundary, we need another addressing system to help distinguish the source and destination systems.
            - This alyer adds a header to the packet coming from the upper layer that, ampong other things, includes the logical addresses of the sender and receiver.
        - 2. Routing:
            - Mechanism to find the way to send the packets to final destination.

### 4. Transport Layer:
    - packet is called "Segment".
    - Responsinilities:
        - 1. Service-point Addressing:
            - Inside a computer ther an many processes are running. 
            - This layer is used to stablish a connection between process of source and process of destination.
            - Such as Port Addressing or Socket Addressing.
        - 2. Segmentation and reassembly:
            - Divide data got from application layer into segments. 
        - 3. Connection Control:
            - this layer can be connectionless or connection oriented.
                - A connectionless transport layer treats each segment as an independent packet and delivers it to the transport layer at the destination machine.
                - A connection-oriented transport layer makes a connection with transport layer at the destination machine first before delivering the packets. 
            - After all packets are transferred, the connection is terminated.
        - 4. Flow Control:
            - Flow control at this layer is performed end to end rather than across a single link.
        - 5. Error Control:
            - Error control at this layer is performed process-to-process rather than across a single link.

### 5. Session layer:
    - It is Network Dialog Controller. 
    - It establishes, maintain and synchronizes the interaction among communicating systems. 
        - Dialog Control:
            - this alayer allows two systems to enter into a dialog
            - start communication in half or full duplex.
        - Synchronization:
            - this layer allows a process to add checkpoints, or  synchronization points, to a stream of data.

### 6. Presentation L:ayer:
    - 1. translation:
        - The processes (running programs) in tow systems are usually exchanging information in the form of character string, numbers, and so on.
        - the info is changed in bit stream befote trnsmitted. Bcz different systems use different encoding, this layer is responsible for interoperability b/w these different encoding.
    - 2. Encription:
        - To carry sensitive info, a system must be able to ensure privacy. 
    - 3. Compression:
        - Reduces the number of bits contained in the information
        - Useful in text, audio and video transmit.

### 7. Application Layer:
    - This layer enable the user to access the network.
    - Services:
        - 1. Network Virtual Terminal:
            - 
        - 2. File Transfer, access, and management:
            - 
        - 3. Mail Services:
            - 
        - 4. Directory Services:
            - 



## Transmission Media:
    - (layer-0) can broadly defined anything that can carry info from src to dest.
        - Wired/ guided:
            - Twisted Pair Cable
            - Coaxial Cable
            - Fibre Optic Cable
        - Wireless/Unguided:
            - Radio Waves
            - Microwaves
            - Infrared Waves.

## Switching:
    - It is a technique by which nodes control or switch data to transmit it b/w specific points on a network. 
    - Methods:
        - Circuit Switching
            - properly switches ko use krke connection stablish krna. Very old approach.
        - Packet Switching
            - Datagram Approach:
                - Different packets may take different paths and may reach at different time. Then we re-arrangethem.
            - Virtual Approach:
                - We select a path virtually first and then send all packets through that path. Path is not reserved for this. It is just that ths is the path we need to take. 

## ISDN (Integrated Services Digital Network) 