#fibonacci series using Memoization using decorators
def memoization_func(t):
    dict_one = {}
    def h(z):
        if z not in dict_one:
            dict_one[z] = t(z)
        return dict_one[z]
    return h

@memoization_func
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(20))