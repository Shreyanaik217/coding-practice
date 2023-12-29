#Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
import collections


class Solution(object):
    def longestPalindrome(self, s):
        res = 0
        for i in collections.Counter(s).values():
            res += i // 2 * 2
        return min(res+1, len(s))