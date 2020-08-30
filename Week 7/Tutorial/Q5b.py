def exp_recursion(x, n):
    if n == 1:
        return x
    else:
        return (x* exp_recursion(x,n -1))


print(exp_recursion(2, 8))
