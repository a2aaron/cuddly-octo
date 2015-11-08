def collatz(n):
    if n == 0:
    	return 0
    numSteps = 0
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        numSteps += 1
    return numSteps
