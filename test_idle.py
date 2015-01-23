def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print [fib(i) for i in range(1,20)]
#testing github integration
