# Sorts a Python list in ascending order using
# the merge sort algorithm

def mergeSort( theList ):
    # Check the base case - the list contains a single item
    if len(theList) <= 1:
        return theList
    else:
        # Compute the midpoint
        mid = len(theList) // 2
        
        # Split the list and perform the recursive step
        leftHalf= mergeSort( theList[ :mid ] )
        rightHalf = mergeSort( theList[ mid: ] )
        # Merge the two sorted sublists

        newList = mergeSortedLists( leftHalf, rightHalf)
        return newList
