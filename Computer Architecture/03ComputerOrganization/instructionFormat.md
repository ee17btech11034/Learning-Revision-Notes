# Instruction Format
    - Instructions in a computer system can be classified according to the number of operands or references made within the instruction. The main types are:
        - 3-Address Instruction => Mode/opCode  Destination   Source1     Source2   ==> ADD R1 R2 R3
        - 2-Address Instruction => Mode/opCode  Destination/Source1     Source2   ==> ADD R2 R3   ==> R2 = R2 + R3
        - 1-Address Instruction => Mode/opCode  Destination/Source   ==> ADD R2   ==> It uses Accumulator Register to put the result. AC = AC + R2
        - 0-Address Instruction: => Mode/opCode    PUSH/ADD  ==> Used in stack based architectures, PUSH A means A ko push kro stack me, ADD B means stack ki top val me B add kro and stack me dump kr do