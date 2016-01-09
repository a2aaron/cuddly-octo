from collatz import collatz

def collatz_range(start, end):
    stepsTaken = [];
    for n in range(start,end):
        stepsTaken.append(collatz(n))
    print(stepsTaken)
    return stepsTaken

collatz_range(1,5)

