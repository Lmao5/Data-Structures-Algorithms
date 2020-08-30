# Sorts a sequence in ascending order using the
# optimized bubble sort algorithm
def bubbleSort_optimized(theSeq):
    n = len(theSeq)
    # Perform n-1 bubble operations on the sequence
    for i in range(n - 1, 0, -1):
        # Set boolean variable to check occurrence of swapping
        # in inner loop
        checkSwapped = True
        # Bubble the largest item to the end
        for j in range(i):
            if theSeq[j] > theSeq[j + 1]:
                # Swap the j and j+1 items
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
                # Set boolean variable value if swapping occurred
                checkSwapped = False
            # checks how many passes print(theSeq)

        # Exit the loop if no swapping occurred
        # in the previous pass
        if checkSwapped == True:
            print(theSeq)
            return theSeq

a = bubbleSort_optimized([ 11, 2, 3, 5, 4, 6, 7, 8, 9, 10])
print(a)
