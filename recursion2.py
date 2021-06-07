def fact2(n):
    if n <= 1:
        return 1
    return n + fact2(n-1)

print(fact2(5))