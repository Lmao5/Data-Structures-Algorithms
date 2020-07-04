def sequentialSearch( theValues, target ): 
    n = len( theValues ) 
    for i in range(n): 
        # If the target is in the ith element, return True         
        if theValues[i] == target: 
            return True 
        elif theValues[i] > target:
            return False
            
    return False    
    # If not found, return False 

a = sequentialSearch([1,2,3,4,5,6,7,8,9], 10)
print(a)
