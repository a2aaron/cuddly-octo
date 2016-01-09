def nthRowPascal(row):
    '''
    Return the nth row of Pascal's Triangle as an array.
    The zeroth row is defined as 1.
    '''
    resultArray = [1]
    workingArray = resultArray #our array that we use operations on
    for iteration in range(1,row):
        for i in range(0, len(workingArray)):
            workingArray[i + 1] = workingArray[i + 1] + workingArray[i]
    return resultArray

for i in range(0,5):
    print(nthRowPascal(i), " i = ", i)


assert nthRowPascal(0) == [1]
assert nthRowPascal(1) == [1,1]
assert nthRowPascal(2) == [1,2,1]
assert nthRowPascal(3) == [1,3,3,1]
assert nthRowPascal(4) == [1,2,1]
