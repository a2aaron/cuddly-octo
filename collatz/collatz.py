def iterate(n, numIter = 1):
    '''
    Iterates for the specified number of times (default 1).
    Returns final value reached.
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
    Returns an array of the number's path to 1
    Array will start with n and end when it reaches 1
    '''
    path = [n]
    while n != 1:
        n = iterate(n, 1)
        path.append(n) 
    return path

def iterationsTaken(n):
    '''Return number of steps taken for some input n.'''
    if n == 0:
    	return 0
    numIter = 0
    while n != 1:
        n = iterate(n, 1)
        numIter += 1
    return numIter

def iterationsTakenRange(start, end):
    '''
    Returns an array of the steps taken for some range (inclusive)
    '''
    numIterArray = [];
    for n in range(start, end + 1): #inclusive range
        if len(range(start, end + 1)) > 1000: #progress checker
            print("Current Value: ", n, "/", end)
        numIterArray.append(iterationsTaken(n))
    return numIterArray

def highestValueReached(n, withNumIter=False):
    '''
    Returns highest value reached and optionally the number of steps.
    If withStepNumber is set then it is returned as an array of
    [highestValue, numIter]
    '''
    arrayPath = path(n)
    if withStepNumber:
        return [max(arrayPath), arrayPath.index(max(arrayPath))]
    else:
        return max(arrayPath)

def demo():
    '''
    Runs a demo printing values with the longest path.
    '''
    n = 1
    longestPathValue = 1
    longestPathLength = 0
    while True:
        if n % 100000 == 0: #every 100,000 give a status update
            print("Current Value: ", n, " | Steps Taken: ", iterationsTaken(n))
        if iterationsTaken(n) > longestPathLength:
            print("Longest Path: ", longestPathValue, " | Most Steps Taken: ", longestPathLength)
            longestPathValue = n
            longestPathLength = iterationsTaken(n)
        n = n + 1
demo()