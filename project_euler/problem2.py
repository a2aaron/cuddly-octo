'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
'''

def nthFibonacci(n):
    if n == 0: #nthFibonacci(0) = 0
        return 0
    elif n == 1: #nthFibonacci(1) = 1,
        return 1
    else:
        return nthFibonacci(n-1) + nthFibonacci(n-2)

n = 0
totalSum = 0

while nthFibonacci(n) < 4000000:
    if nthFibonacci(n) % 2 == 0:
        totalSum += nthFibonacci(n)
    n += 1

print(totalSum)