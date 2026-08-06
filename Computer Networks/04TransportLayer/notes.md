# Transport Layer
## Transport Layer Services
    - Handle process to process.
    - Port addressing used to identify process.
    - 3 transport layer protocols:
        - UDP is connectionless and unreliable
        - TCP and SCTP are connection oriented and reliable.

### Port Numbering:
    - 16 bit number (0 to 65535)
        - 0 to 1023 ==> well known  port numbers
        - 1024 to 49,151 ==> Registered port numbers
        - 49,152 to 65535 ==> Dynamic or private port numbers.

    - Socket Address = Ip Address + port Number


### TCP (Transmission Control Protocol)
    - TCP creates a virtual connection b/w two TCPs to send data. 
    - TCP has 6 flags.

    - TCP Connection:
        - It is called Three Way Handshaking.
        - The client program issues a request for an active open. A client that wishes to connect to an open server tells its TCP to connect to a particular server. TCP can now start the three way handhske process.
        - client create packet with randon numbers and SYN flag ko 1 karta hai and send it with SeqNo = 8000 (random).
        - Server was Passive open Mens ready to accept mode.  
        - now server will respond "ACK" with  AckNo = 8001 and SeqNo = 15000 (random).  Here "SYN" and "ACK" flag bit will be 1.
        - Now client will receive and respond with "ACK" with SeqNo = 8001 and Ackno = 15001.


### UDP (User DataGram Protocol)
    - It does not add anything to the services of IP except for providing process-to-process commuication instead of host-to-host communication.
    - Used for multicasting, DNS management proceess such as SNMP, RIP. 

### RTP (Real time protocol):
    - can tolerate packets data
    - used match stream.