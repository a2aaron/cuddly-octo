stuff = [1,2,3,4,5,6,7,8,9]

'''
#keep element values inside the range (3,8)
results = []
for i in stuff:
    if 3 < stuff[i] < 8:
        result = stuff[i]


#keep element values outside the range (3,8)
results = []
for i in stuff:
    if 3 > stuff[i] or 8 < stuff[i]:
        results.append(i)

#keep even element values
results2 = []
for i in stuff:
    if stuff[i] % 2 == 0 
        results2.append(i)

#keep odd element values
results3 = []
for i in stuff:
    if stuff[i] % 2 == 1
        results3.append(i)

'''


def keep(stuff, reason):
    '''
    Returns all values that satify the reason
    reason should be a function
    '''
    result = []
    for i in stuff:
        if reason(i):
            result.append(i)
    return result


items = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

print(keep(items, lambda x: x in [3, 5, 7]))


def length(x):
    l = 0
    for i in x:
        l += 1
    return l

assert length([1,2,3]) == 3
assert length([1,2,3,4]) == 4
assert length("1234") == 4
assert length({4,3,6,4}) == 3
assert length((1,2,3,4)) == 4
assert length(range(10)) == 10
assert length(i + 1 for i in range(10)) == 10






