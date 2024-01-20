#pass the array to the function using pointer
#find the sum of thr given array using pointer
def array_sum(arr):
    result = 0
    for i in arr:
        result += i
    return result

# Usage
arr = [1, 2, 3, 4, 5]
print(array_sum(arr)) # 15
