from time import sleep

def successor(a):
    '''Returns the successor of a'''
    return a + 1

def add(a,b):
    '''Returns a + b'''
    return a + b

def double(a):
    '''Returns a + a'''
    return add(a,a)

def sgn(n):
    '''
    Returns 1 if n is postive
    Returns 0 if n is zero
    Returns -1 is negative
    '''

    if n > 0:
        return 1
    elif n == 0:
        return 0
    else:
        return -1
'''
favoriteChampion = input("What is your favorite champion? ")
print(favoriteChampion, " is OP!")

name = input("What's your Summoner name? ")
print(name, " deserves Challenjour")

favColor = input("What is your favorite color? ").lower()
validColor = ['red', 'blue', 'green', 'yellow', 'black']

isValidColor = False #favColor is in validColor array


for color in validColor:
    if favColor == color:
        isValidColor = True

if isValidColor:
    print('Correct.')
if not(isValidColor):
    print('Incorrect.')
'''

def findabc(string):
    '''
    Returns true if abc is anywhere in the string.
    abc may be in any order and be separated by anything.
    '''
    string = string.lower()
    if "a" in string and "b" in string and "c" in string:
        return True
    else:
        return False

assert findabc('abc') == True
assert findabc('ab') == False
assert findabc('rrrrarrrrbrrrrcrrrr') == True
assert findabc('ABC') == True

testStr = input("Easy mode abc ")

if findabc(testStr) == True:
    print("abc is in ", testStr)
else:
    print("abc is not in ", testStr)

#hard mode

def hardModeFindabc(string):
    '''
    Returns true if abc or ABC is anywhere in the string.
    abc or ABC may be in any order and be separated by anything.
    '''
    if "a" in string and "b" in string and "c" in string:
        return True
    elif "A" in string and "B" in string and "C" in string:
        return True
    else:
        return False

assert hardModeFindabc("ABc") == False
assert hardModeFindabc("aBc") == False
assert hardModeFindabc("A_B_Ceeeeelllab") == True
assert hardModeFindabc("a c b sCssEssD") == True


