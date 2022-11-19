import random


def display_prime(n):

    if n!=int(n):
        { 'It is not a prime number' }
    n=int(n)

    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return { 'It is not a prime number' }

    if n==2 or n==3 or n==5 or n==7:
        return { 'It is a prime number' } 
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)

    def trial_composite(a):
        if pow(a, d, n) == 1:
            return { 'It is not a prime number' }
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return { 'It is not a prime number' }
        return { 'It is a prime number' } 
 
    for i in range(8):#number of trials 
        a = random.randrange(2, n)
        if trial_composite(a):
            return { 'It is not a prime number' }
 
    return { 'It is a prime number' } 