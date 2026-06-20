'''
Q1. A thief has a knapsack (bori) of weith W. an arr is given with weight with value (price). maximum picked item.

Sol:
    - Find the per kg price. 
    - sort on decresasing order on per kg price. 
    - now do the loop and add item.
'''




if __name__=="__main__":
    #[price, weight]-> weight available
    # arr = [[21, 7], [24, 4], [12, 6], [40, 5], [30, 6]]
    arr = [[24, 7], [21, 3], [12, 4], [10, 5]]
    knapSackWeight = 20

    weightPerKg = []

    arr.sort(key=lambda x: (x[0] / x[1]), reverse=True) # sort on decresasing order on per kg price. 

    # print(arr)

    totalValues = 0
    for [price, weight] in arr:
        takenWeight = min(knapSackWeight, weight)
        totalValues += ((price * takenWeight) / weight)
        knapSackWeight -= takenWeight
    
    print(totalValues)
