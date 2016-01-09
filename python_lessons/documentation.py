#Removing things!

#=====
a = ["apple", "kahn", 4, 99, "last element", True, None]

#does not remove "last element"
#instead removes the element w/ the value of 4
a.remove(4)

print(a) #["apple", "kahn", 99, "last element", True, None]
#=====

#=====
a = ["apple", "kahn", 4, 99, "last element", True, None]

#removes the 2nd element ("kahn")
del a[1]

print(a) #["apple", 99, "last element", True, None]
#=====

#=====
a = ["apple", "kahn", 4, 99, "last element", True, None]

#sets a = None
#a no longer is a varible with a value
del a

#print(a) #None
#=====

#=====
a = ["apple", "kahn", 4, 99, "last element", True, None]

#returns + removes the value at the index
#if no index, then it defaults to the last element
a.pop([0])

print(a) ["kahn", 4, 99, "last element", True, None]
#=====


a = [1,3,5,1,7,5,3]

a != 2

while not a == 0:
while a != 0
