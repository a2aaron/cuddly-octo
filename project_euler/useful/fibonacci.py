def nth_fibo_recur(n):
    '''Return the nth fibonacci number recurisvely. Not recommended for large values.'''
    if n < 0: #there are no -1st fibonacci numbers
        raise ValueError

    elif n == 0: #zeroth fibonacci number = 0
        return 0

    elif n == 1: #first fibonacci number = 1,
        return 1

    else:
        return nth_fibo_recur(n-1) + nth_fibo_recur(n-2)


def nth_fibo_iter(n):
    '''Return nth fibonacci number iteratively.'''
    if n < 0: #there are no -1st fibonacci numbers
        raise ValueError

    elif n == 0: #zeroth fibonacci number = 0
        return 0

    elif n == 1: #first fibonacci number = 1,
        return 1

    else:
        currVal = 1 #starts as 2nd fib number
        parentVal = 1 #starts as 1st fib number
        grandParentVal = 0 #starts as 0th fib number
        for currIter in range(1,n):
            currVal = parentVal + grandParentVal #n -> n+1th
            grandParentVal = parentVal #n-2th -> n-1th
            parentVal = currVal #n-1th -> nth
        return currVal