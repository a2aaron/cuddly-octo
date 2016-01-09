import math

def is_factor(n, factor):
    '''Return true if n is a factor, false otherwise'''
    if n % factor == 0:
        return True
    return False


def is_prime(n):
    '''Return true if n is a prime, false otherwise'''
    if n == 0 or n == 1: #0 and 1 aren't primes
        return False

    #testing from 2 to sqrt(n) + 1 (+1 guarrentees a non empty range)
    for factor in range(2, math.floor(n ** 0.5 + 1)):
        if is_factor(n, factor): #if divisible
            return False
    return True

def nth_prime(n):
    '''Return the nth prime'''
    if n <= 0: #there is no zeroth prime
        raise ValueError
    currN = 0 #currN is zero so the function runs atleast once
    currVal = 0
    while currN != n:
        currVal = currVal + 1
        if is_prime(currVal):
            currN = currN + 1
    return currVal

def prime_list(a, b):
    '''Return a list of primes starting at
    the ath prime and ending at the bth prime (b not included)'''
    returnedList = []
    for n in range(a,b):
        returnedList.append(nth_prime(n))
    return returnedList

#PRECOMPUTED_PRIME_LIST = prime_list(1,1000) #first 1000 primes to aid in factoring

def factors(n):
    '''Return a list of ALL the factors of an input n. This includes 1 AND n.'''
    if n == 0:
        return [None]
    if n == 1:
        return [1]

    factor_list = list()
    curr_factor = 1
    while curr_factor <= n: #includes curr_factor = n
        if is_factor(n, curr_factor):
            factor_list.append(curr_factor)
        curr_factor = curr_factor + 1

    return factor_list


def prime_factors(n):
    '''
    Return a list of all the prime factors.
    Repeated factors are inserted again (ex: 4 -> [2,2])
    Includes n if n is a prime.
    '''
    