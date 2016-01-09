def iterate(n, numIter = 1):
    '''
    Iterate for the specified number of times (default 1).
    Return final value reached.
    '''
    if numIter == 0:
        return n
    for currIter in range(0, numIter):
        if n % 2 == 0: #n is even
            n = n/2
        else: #n is odd
            n = 3*n + 1        
    return int(n) #int not required but n is always an int and should stay as int

def path(n): 
    '''
    Return an array of the number's path to 1
    Array will start with n and end when it reaches 1
    '''
    path = [n]
    while n != 1:
        n = iterate(n)
        path.append(n) 
    return path

def iterations_taken(n):
    '''Return number of steps taken for some input n.'''
    if n == 0:
    	return 0
    numIter = 0
    while n != 1:
        n = iterate(n, 1)
        numIter += 1
    return numIter

def iterations_taken_range(start, end):
    '''Return an array of the steps taken for some range(start,end)'''
    numIterArray = [];
    for n in range(start, end):
        numIterArray.append(iterations_taken(n))
    return numIterArray

def max_value_reached(n, withNumIter=False):
    '''
    Returns highest value reached and optionally the number of steps.
    If withStepNumber is set then it is returned as a tuple of (highestValue, numIter)
    '''
    arrayPath = path(n)
    if withStepNumber:
        return (max(arrayPath), arrayPath.index(max(arrayPath)))
    else:
        return max(arrayPath)