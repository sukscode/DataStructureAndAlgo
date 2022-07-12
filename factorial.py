def factorial(n):
    assert n>=0 and int(n)==n, 'number must be positive integer'
    if n in [0,1]:
        return 1
    else:       
        return n * factorial(n-1)

print(factorial(1.5))