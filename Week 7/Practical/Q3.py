def recursiveSort(numList, low, high):
    if low < high:
        if numList[high] % 2 == 0:
            """
            temp = numList[low]
            numList[low] = numList[high]
            numList[high] = temp  
            """
            numList[low], numList[high] = numList[high], numList[low]

            recursiveSort(numList, low + 1, high)
        else:
            recursiveSort(numList, low, high - 1)


numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numList)
recursiveSort(numList, 0,len(numList)-1)
print(numList)
