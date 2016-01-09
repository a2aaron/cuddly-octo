'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
'''
import math

def floorSqrtPlusOne(n):
    return  math.floor(math.sqrt(n)) + 1

def isFactor(n, factor):
    if n % factor == 0:
        return True
    return False

def isPrime(n):
    #testing from 2 to sqrt(n) + 1 (+1 guarrentees a non empty range)
    for factor in range(2,floorSqrtPlusOne(n)):
        if isFactor(n, factor): #if divisible
            return False
    return True

def returnHighestPrimeFactor(n):
    endOfRange = floorSqrtPlusOne(n)
    highestFactor = 0
    for factor in range(1, endOfRange):
        print("Current Factor:", factor, "/", endOfRange, "| Current Highest:", highestFactor)
        if isFactor(n, factor) and isPrime(factor):
            highestFactor = factor
    print("FINAL: ", highestFactor)

returnHighestPrimeFactor(600851475143)