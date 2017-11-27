from functools import lru_cache


def fib1(n):
    """Simple fibonacci"""
    if n in [1, 2]:
        return 1
    else:
        return fib1(n-1)+fib1(n-2)


@lru_cache()
def fib2(n):
    """Added caching with python magic - this is now really fast"""
    if n in [1, 2]:
        return 1
    else:
        return fib2(n-1)+fib2(n-2)


def fib3(n):
    """Iterative fibonacci"""
    n1, n2 = 1, 1
    for i in range(n):
        n1, n2 = n2, n1+n2
    return n1

print(fib1(20))
print(fib2(20))
print(fib3(20))
