hList = []
otherList = []

def sortFlower(theSeq):
    n = len(theSeq)
    for i in theSeq:
        if i[0] == 'H':
            hList.append(i)
        else:
            otherList.append(i)
    print(sorted(hList) + sorted(otherList))

# Test Codes
flowerList = ['Bougainvillea', 'Orchids',
              'Hibiscus', 'Frangipani', 'Honeysuckle']

#print('Input List:', flowerList)
sortFlower(flowerList)
