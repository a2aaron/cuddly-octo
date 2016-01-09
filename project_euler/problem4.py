'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

import math


    
def isPalindrome(string):
    if type(string) is not str:  #conversion to str so we can extract slices
        string = str(string)

    stringLen = len(string)
    stringHalfLen = math.floor(stringLen/2)
    #using floor because string length must be an int
    #and because we don't care about the middle number
    #works the same with ceil and trunc

    for i in range(0, stringHalfLen):
        if string[i] != string[stringLen - 1 - i]:  #arrays are zero indexed
            return False
    return True

def largestPalindromeOverRange(start, end):
    largestPalindrome = 0
    a = start
    b = start
    while b != end:
        product = a * b
        if isPalindrome(product) and largestPalindrome < product:
            largestPalindrome = product

        if a == end:
            a = start
            b = b + 1 

        a = a + 1
        print(b, "/", end," | Largest Palindrome: ", largestPalindrome)
    print("FINAL: ", largestPalindrome, "| a = ", a, " | b = ", b)

largestPalindromeOverRange(0,999)