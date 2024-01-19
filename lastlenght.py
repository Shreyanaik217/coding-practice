#length of the last word in the given string

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.split()
        if word:
            return len(word[-1])
