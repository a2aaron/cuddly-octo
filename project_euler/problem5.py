'''
2520 is the smallest number that 
can be divided by each of the numbers from 1 to 10
without any remainder.

What is the smallest positive number
that is evenly divisible by all of the numbers from 1 to 20?
'''

def lcm(*nums):
    result = max(nums)
    while allDivisibleBy(result, *nums) == False:
        if result % 1000000 == 0:
            print(result)
        result = result + 1
    print(result)

def allDivisibleBy(dividend, *divisors):
    '''
    First argument is our number to check,
    All other arguments are the numbers to check.
    '''
    for divisor in divisors:
        if dividend % divisor != 0:
            #if any divisor isn't divisible
            return False
    #every divisor is divisible
    return True

def all_divisible_by(dividend, divisors):
    return all(dividend % d == 0 for d in divisors)
    
lcm(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)