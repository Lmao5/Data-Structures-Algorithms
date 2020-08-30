def isPalindrome(aStr):
    # Complete this function recursively
    x = len(aStr)
    if x <= 1:
        return True
    elif aStr[0] == aStr[(x-1)]:
        return isPalindrome(aStr[1:len(aStr)-1])
    else:
        return False
    


a = isPalindrome('madam')
print(a)
