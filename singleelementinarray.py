#Problem: Given an array of integers, every element appears twice except for one. Find that single one.
#find the single elemet in the given array of element and display the element which is not repeated in the array
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
