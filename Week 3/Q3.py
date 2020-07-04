import math
def binarySearch( theValues, target ): 
     # Start with the entire sequence of elements      
    low = 0 
    high = len(theValues) - 1  
    count = 0
    # Repeatedly subdivide the sequence in half 
    # until the target is found      
    while high >= low: 
         	# Find the midpoint of the sequence          	
        mid = int((low + high)/2)
         	# Does the midpoint contain the target? 
         	# If yes, return midpoint (i.e. index of the list)          	
        if theValues[mid]==target:
            first_occurance = mid
            cont = True 

            #Checks the first occurance of the number
            while first_occurance > 0 and cont:
                if theValues[first_occurance - 1] == target:
                    first_occurance -= 1
                    count += 1
                else:
                    cont = False    
            return first_occurance, count         
            # Or is the target before the midpoint? 
 
        elif target < theValues[mid]: 
            high = mid -1         
         	# Or is the target after the midpoint? 
        else: 
         	low = mid + 1 
        # If the sequence cannot be subdivided further, 
    # target is not in the list of values     
    return -1 
        
a = binarySearch([1,2,3,5,5,5,5,6,7,8,9,10], 5)
print(a)
