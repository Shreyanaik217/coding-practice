#count number of words in given string
class Solution(object):
    def countSegments(self, s):
        a=s.split()
        return len(a)