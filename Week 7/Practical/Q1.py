def Fibnacci(n):
    if n <= 1:
        return n
    else:
        return(Fibnacci(n-1) + Fibnacci(n-2))

for i in range(7):
    print(Fibnacci(i), end=" ")
