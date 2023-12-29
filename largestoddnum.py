#find the largest odd number in the given number

class Solution(object):
    def largestOddNumber(self, num):
        return num[:next((i for i in range(len(num)-1, -1, -1) if ord(num[i]) &1==1), -1) + 1]