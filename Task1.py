def fact(n):
    if n<2:
        return 1
    else:
        return n*(fact(n-1))

n=int(input('Enter a number:'))
print('factorial of ',n,' is ',fact(n))
