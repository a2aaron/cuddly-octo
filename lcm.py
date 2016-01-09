def lcm(*nums):
    result = max(nums)
    while allDivisibleBy(result, *nums) == False:
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
    
