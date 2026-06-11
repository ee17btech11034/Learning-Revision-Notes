# Part - 01 #

##################### Array Representation ##############
'''
We have 2  views:
    1. Logical View:
        - Diagram we draw on paper for tree is called logical view.
    2. Physical View:
        - The way it is stored in memory.
'''

'''
 To store tree in array form, we will have to make it ""Complete Binary tree"".

 Tree:==> 
Logical View:
                                                                        10
                                                                15             20
                                                                            30    18
                                                                         25

                                                                                

To make it CBT we will add dummy node (represent (DN)


                                                                             10(i=0)
                                                        15(i=1)                             20(i=2)
                                            DN(i=3)              DN(i=4)               30(i=5)    18(i=6)
                                      DN(i=7)     DN(i=8)    DN(i=9)   DN(i=10)      25(i=11)

Array: 
Physical View:
               [10, 15, 20, , , 30, 18, , , , , 25]  ==> length = 12 
                    - mid dummy node space is wastage.
                    - We do not prefer this to make tree.
'''


'''
index i's:=> (assuming 0 based index)
    Left child = (2*i + 1)
    Right child = (2*i + 2)

'''


########################## Linked List Representation ####################
'''
 We can use Doubly linked list Node style. [left child, data, right child]

 We will have to do traversal. 

'''