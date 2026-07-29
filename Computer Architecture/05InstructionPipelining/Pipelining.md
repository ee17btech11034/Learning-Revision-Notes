# Pipelining

## Uniprocessing
    - When we actually execute an instruction, it is executed into number of phases, like --- 
        --> Instruction Fetch (get the data from memory),  -->  Instruction Decode (find what code wants to perform), --> Instruction Execute, --> Instruction Store.
    - If system has only one processor then at most one instruction can be executed at a time.

## Multiprocessing
    - To execute multiple instruction together or concurrently we must have multiple processors.


## Pipelining
    - Idea is to make a special processor (pipelined processor), where the circuit of every phase is different and buffers are placed in between stages. Like If 
        - phase1 (instruction 1) has completed fetching and now passed the datat to Decode part. 
        -- Fetch part is free for phase 2 instructions. 
    - Structural Hazards: Read about it. 
    - Control Hazards: 
        - All stages use memory or shared resources like system bus, CPU but parallely 2 can not access same memory untill we create duplicate that willl be costly. 
        - If branching is there. Like 2 types of branching can happend (if-else, goto statement). When Instruction I3 is in execute state and there we find switch/jump to statement to I7. Now parallely when I3 was on execute, we did some stages completed for I4, I5. But now we want I7 to load. So, whatever we did for I4, I5 we will have to remove it.
    - Solutions to Control Hazards:
        - Flushing/Stalling or NOP (no-operations): It is the worst case scenario either we remove the computed data or we do not work at all. which means compiler do not need to execute any instructions here. If we find any conditional statement in Decode stage then do not load any more instructon until execution is completed.
        - Code rearrangement or delayed load: Here with smart compilers we can first execute some instruction which are independent from the current logic. Only theoritically possible. It says when we find conditional statement in Decode then wait and complete the independent tasks. 
        - Estimation Method/ predictive method: Here we use either 2 stage prediction, then policy change or 1 stage prediction then policy change. 
            - k = 1 or 2 stage prediction. 
            - Like initially we say, jump will not happen, if this is true then we got it right. 
                - but jump happend so if jump happened k times in continous(in I3, I4) then it will point that "jump will happend". 
                - again if k consecutive time jump did not happend then we set it "jump will not happen".
    - Data Hazards:
        - This occurs when instructions that exhibit data dependence, modify data in different stages of a p[ipeline. Hazard causes delay in the pipeline.
        ```bash
        4 stages [IR (Fetch)   -->    Decode (DE)   --> EX (Execte)    --> WB (Write)]  


                Instructions             Meaning of Instructions                 4 Stages
                I0: MUL R2, R0, R1          R2 = R0 * R1                IR  -->  DE  -->  EX  -->  WB
                I1: DIV R5, R3, R4          R5 = R3 / R4                         IR  -->  DE  -->  EX  -->  WB
                I2: ADD R2, R5, R2          R2 = R5 + R2                                  IR  -->  DE  -->  EX  -->  WB
                I3: SUB R5, R2, R6          R5 = R2 - R6                                           IR  -->  DE  -->  EX  -->  WB

            Here in T2 step we need value of R2, which we will get after completion of I0. 
        ```
        - There are 3 types of Data Hazards: This condition is called Bemstein Condition. 
            - RAW (Read after write)[Flow/True data Dependency] occurs when instruction J tries to read data before Instructions I write it. (I < J)
            - WAR (write after Read)[Anti data Dependency] occurs when instruction J tries to write data before Instructions I read it it. (I < J)
            - WAW (Write After Write)[Output data dependency] occurs when instruction J tries to write output before nstruction, I write it.

            == WAR and WAW hazards occur during the out-of-order execution of the instructions.
        
        - Solution of data Dependency
            - We can use code movement or code relocation and can execute the dependent instruction after some time.
            - We use 5 stages [IR (Fetch)   -->    Decode (DE)   -->   Operand Fetch (oF) -->  EX (Execte)    --> WB (Write)]
                - in OF, we fetch all the operands and then perform the next stage.
            - Here we can use operator forwarding using which we can directly access the result after execution instead of waiting that it gets store in memory.
                - Operator Forwarding: 
                        - When Execution happens then it happens in ALU, then write in memory.
                        - Next Instruction read from memory and then perform some execution. 

                        - If Data is available in ALU for next instruction then why wait till it is not updated in memory. Just pull the data from ALU and perform the action.
                        - here OF is not needed as we directly pull from EX of last instruction.
