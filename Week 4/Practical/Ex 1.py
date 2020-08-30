# Sort a sequence in ascending order using the selection sort
# algorithm
def selectionSort(theSeq, choice):
    n = len(theSeq)
    choice.upper() #Capitalise the letter

    for i in range(n - 1):
        # Assume the ith element is the smallest.
        smallNdx = i

        if choice == 'A': #ascending choice

        # Determine if any other element contains a smaller value.
            for j in range(i+1, n):
                if theSeq[j] < theSeq[smallNdx]:
                    smallNdx = j
        
        elif choice == 'D': # descending choice
            for j in range(i+1, n):
                if theSeq[j] > theSeq[smallNdx]:
                    smallNdx = j
            
        else:   #if user put nonsensical answer
            print("Please enter 'D' or 'A'.")
        # Swap the ith value and smallNdx value only if the
        # smallest value is not already in its proper position.
        if smallNdx != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[smallNdx]
            theSeq[smallNdx] = tmp


# Test codes
list_of_numbers = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
choice = input("Enter 'D' for descending order or 'A' for ascending order: ")

print('Input List:', list_of_numbers)
selectionSort(list_of_numbers, choice)
print('Sorted List:', list_of_numbers)
