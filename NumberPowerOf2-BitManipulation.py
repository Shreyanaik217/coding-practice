#The is_power_of_two function checks whether a given number n is a power of two. It utilizes bitwise operations to efficiently perform this check.

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Usage
print(is_power_of_two(8)) # True
print(is_power_of_two(9)) # False
