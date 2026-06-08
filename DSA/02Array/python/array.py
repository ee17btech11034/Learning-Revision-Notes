''' 
- Python has list that can contain haterogrnous elements. 
- Arrays can be created using 2 methods:
    1. Python array module (but multi dimention array can not be created, but add type safety)
    2. Python Numpy module (best choice for multi-dimention, but no type safety in default)

'''

######################## 1.  Array module

'''
import array
# val = array.array('Typecode', [x, y]) ->  typecode is like Data Type in python
# val = array.array('Typecode', []) ->  empty arr
val = array.array('i', [1, 2, 3, 4, 5])
print(val)
for i in range(0, len(val)):
    print(i, end=" ")
'''


'''
# import array as arr  --> but again arr.array()
from array import *
# val = array('Typecode', [x, y]) ->  typecode is like Data Type in python
# val = array('i', [1, 2, 3, 4, 5.6]) # error throw 
val = array('i', [1, 2, 3, 4, 5])
val = array('u', ['a', 'b', 'c'])
for i in val:
    print(i, end=" ")

print(val.typecode) # to get the typecode
val.reverse() # reverse the arr

# val.insert(ind, value) -> right shift
val.insert(1, 15)
val.append(15) # insert at end

# val[ind] = newVal -> modify / update the array

copyArr = array(val.typecode, (x*3 for x in val)) # create new arr

# copyArr.pop(ind) # remove ind th element
copyArr.pop() # remove last element
# copyArr.remove(element) # remove specific elemtn
copyArr.remove(element)

# slicing
# newArr = val[start_ind : end_ind] # create new arr with [start_ind, end_ind)
newArr = val[1, 4]
newArr = val[1, -3] # from ind 1 to (remove last 3)

rev_arr = val[::-1] # reverse the arr

# ind = val.index(elemtn) # return the ind of element
ind = val.index(5)

'''



######################################  2. Numpy module

# -> install numpy       `pip install numpy`

from numpy import *

# val = array([x, y]) # No need for typecode as it has haterogenous
# val = array([]) # empty arr
# val = array([1, 2, 3])
val = array([1, 2, 3], float) # type safety


# arr2 = linspace(start_num, end_num, chunk) # [start-num, end_num] ko chunk parts me equal divide krke un nums ka arr banao
arr2 = linspace(10, 20, 10)
arr3 = linspace(10, 20, 11)

# arr4 = arange(start_num, end_num, difference)  # [start-num, end_num) ko difference ke hisab se nums ka arr banao
arr4 = arange(10, 20, 1)

# arr5 = logspace(start, end, p) # log me e^ ki form me banta hai


# arr5 = zeros(length) # arr of zeros
arr5 = zeros(10)
arr5 = ones(10)
arr6 = full(10, 7) # 10 length ka 7 val as default


# Dimension array
zero_dim_arr = array(10) # single element arr
one_dim_arr = array([1,2,3,4]) 
two_dim_arr = array([ [1, 2], [3, 4] ])