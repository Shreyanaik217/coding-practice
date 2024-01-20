#valid palindrome or not in (true or false)
class Solution(object):
    def isPalindrome(self, s):
        s = [c.lower() for c in s if c.isalnum()]
        return all (s[i] == s[~i] for i in range(len(s)//2))

************************************************************************************************************************
#simplified

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal, Panama"))  # Output: True
print(sol.isPalindrome("race a car"))  # Output: False

#inbuild functions
