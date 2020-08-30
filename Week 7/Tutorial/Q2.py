def sumDigits(x):
    # Assuming x >= 1
    # Complete this function recursively
    if x == 0:
        return 0
    else:
        return (x % 10 + sumDigits(int(x/10)))


result = sumDigits(368)
print(result)
