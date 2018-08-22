# -*- coding: utf-8 -*-

def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n

def _not_divisible(n):
    return lambda x:x%n>0

def primes():
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(n),it)

for n in primes():
    if n<1000:
        print(n)
    else:
        break


def num(x):
    n=1
    while n<=x:
        if n>=10:
            yield n
        n=n+1

def is_palindrome(num):
    return str(num)==str(num)[::-1]

output=filter(is_palindrome,num(1000))
print(list(output))

