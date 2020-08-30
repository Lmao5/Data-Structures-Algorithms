def last_element(tuple):
    return tuple[-1]

def sortNumber(tuples_list):
    return sorted(tuples_list, key=last_element)
    
#Test Code
tuples_list = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]

print(sortNumber(tuples_list))
