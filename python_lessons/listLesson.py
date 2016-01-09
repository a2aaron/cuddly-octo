a = [1,5,6,4,1,3,7,3,5,7]

#Oh good, a long list

'''
runningTotal = 0 #our total starts at zero
for i in a:
    runningTotal = runningTotal + a[i]

print(runningTotal)

'''
'''
for i in [1, 2, 3, "Hello", ["inner list", 9]]:
    #we loop through, each time
    #setting i to a different value
    #first loop, i = 1
    #second loop, i = 2
    #third loop, i = 3
    #fourth loop, i = "Hello"

    print(i)

for i in range(0,5)
    #note how the end value (5) is NOT included
    print(i)


'''

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("nerf", end=" ")
    elif i % 5 == 0:
        print("fizz", end=" ")
    elif i % 3 == 0:
        print("rito", end=" ")
    else:
        print("plz", end=" ")