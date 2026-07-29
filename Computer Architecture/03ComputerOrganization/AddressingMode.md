# Addressing Mode

- Operand Reference: Operand addressing specifies the various methods for referencing the location of an operand.
- Effective Address/Absolut Address: This refers to the final address where the operand is located in memory. 
- Address Calculation:
    - Non-computable Addressing: Direct reference without the need for arithmatic calculations
    - Computable Addressing: Involves the use of arithmatic operations to compute the final address of the operand.
- Criteria for selecting Addressing Modes: Speed, Instruction Length, Pointer Support, Looping and Indexing Support, Program Relocation.


## Modes:
### Immediate Mode Addressing
The Operand embedded directly within the instruction.

### Direct Mode Addressing (Absolute Address Mode)
It involves the instruction containing the address of the memory location where the data is present(effective address). Only one memory reference operation is required to access the data.

### Indirect mode addressing
In this mode, the instruction stores the address where the effective address (the address of the variable) is stored. 2 references are required:
    - The first reference retrieves the effective address.
    - The second, accesses the actual data.

### Implied mode addressing
in this mode, operands are not explicitly stated, they are implicitly defined by the instruction itself. This is commonly used when operationsinvolves registers like an accumulator, where the operand location is predetermined by the CPU.
    - Implied Mode Instructions
    - Zero Address Instruction

### Register Mode Addressing
in this mode, variables are stored directly in the CPU's registers instead of memory. the instruction will specify which register contains the data by providing the register number.

### Register Indirect mode addressing
in this mode, the instruction specifies a register containing the memory address (effective address) of the variable. The CPU uses the content of the register to determine where the actual data is stored.

### Base Register (Off Set) Mode / Based Indexed Addressing
We just store the base or start address of memory for program. When data changes its location then only register will update the base values stored. We can access below code using base. (Base + offset)

### Index addressing mode

### Relative Addressing mode