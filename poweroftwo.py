#Power of Two (231):
#Problem: Given an integer n, write a function to determine if it is a power of two.

def isPowerOfTwo(n):
    return n > 0 and (n & (n - 1)) == 0
