#Reverse Bits:
#Problem: Reverse bits of a given 32 bits unsigned integer.

def reverseBits(n):
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
