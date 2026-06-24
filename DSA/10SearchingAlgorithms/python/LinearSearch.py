'''
Linear Search: 
    - Search an key through each element
    - TC => Ω(1) -> Θ(1) -> O(1)
    - SC => Ω(1) -> Θ(1) -> O(1)
'''

def linearSearch(arr, n, key):
    for i in range(n): # 0 -> n traverse; All TC => O(n) 
        if (arr[i] == key):
            return i
    return -1

if __name__=="__main__":
    arr = [3, 52, 24, 6, 7, 10]

    key = [3, 5, 6, 8]
    n = len(arr)

    print("Arr is: ", end=" ")
    print(arr)
    for val in key:
        key_ind = linearSearch(arr, n, val)
        if (key_ind > -1):
            print(f"{val} is present in arr at ind: {key_ind}")
        else:
            print(f"{val} is not present in arr.")