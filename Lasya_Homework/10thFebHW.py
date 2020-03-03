'''
 Find unique triplets whose three elements gives the sum of zero from an array of n integers
'''

# function to print triplets with 0 sum
def findTriplets(arrInput , n):
    found = False
    for i in range(n - 1):
        # Find all pairs with sum
        # equals to "-arrInput [i]"
        s = set()
        for j in range(i + 1, n):
            x = -(arrInput [i] + arrInput [j])
            if x in s:
                print(x, arrInput [i], arrInput [j])
                found = True
            else:
                s.add(arrInput [j])
    if found == False:
        print("No Triplet Found")
arrInput = [0, -1, 2, -3, 1]
n = len(arrInput)
findTriplets(arrInput , n)