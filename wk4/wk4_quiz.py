import time

"""
Q1: Write a recursive function that does the same thing
as the iterative function shown below:
"""

def add_numbers(upper):
    total = 0
    for number in range(upper + 1):
        total += number
    return total


def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + (recursive_sum(n - 1))


"""
Q2: Given the algorithm for calculating the factorial of a number 
write a recursive function that calculates a Fibonacci series
if n = 0, return 1
if n > 0, return n * (n-1)!
"""


# Function for nth Fibonacci number

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


"""
Q4: The recursive formula for computing the number 
of ways of choosing k items out of a set of n items, 
denoted C(n,k), is:

if k = 0: 1
if n < k: C(n, k) =   0
otherwise: C(n-1,k-1) + C(n-1,k)  
"""

def choosing(n, k):
    if k == 0 or k == n:
        return 1
    elif n < k:
        return 0
    else:
        return choosing(n-1, k-1) + choosing(n-1, k)

"""
Q5: Implement a recursive function reverse() that takes a nonnegative integer 
as input and prints its digits vertically, starting with the low-order digit.
"""

def reverse(n):
    if n < 10:
        return n
    else:
        print(n%10)
        return reverse(n//10)

"""
Q8: For the two implementations of fibonacci given below, 
explain why fibA is so much slower than fibB.
"""

def fibA(n):
    if n <= 1:
        return n
    else:
        return fibA(n-1) + fibA(n-2)

def fibB(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[i-1]+fibs[i-2])
    return fibs[n]

if __name__ == "__main__":
    # Q1
    #print(add_numbers(10))
    #print(recursive_sum(10))
    # Q2
    #print(fibonacci(10))
    # Q4
    #print(choosing(2,1))
    #print(choosing(1,2))
    #print(choosing(5,2))
    # Q5
    #print(reverse(312456))
    # Q8
    start = time.time()
    print(fibA(35))
    end = time.time()
    print(end-start)
    start = time.time()
    print(fibB(35))
    end = time.time()
    print(end-start)

