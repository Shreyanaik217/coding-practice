#The solution set must not contain duplicate subsets. Return the solution in any order.
#bit manipulation ,array


 class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lst = [[]]
        for i in range(1, len(nums) + 1):
            ans = list(itertools.combinations(nums, i))
            lst.extend([list(comb) for comb in ans])
        return lst
