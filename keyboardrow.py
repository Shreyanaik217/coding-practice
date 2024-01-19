#keyboard row

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        #
        s1 = {'q','w','e','r','t','y','u','i','o','p'}
        s2 = {'a','s','d','f','g','h','j','k','l'}
        s3 = {'z','x','c','v','b','n','m'}
        
        res = []
        for i in words:
            wordset = set(i.lower())
            if (wordset&s1 == wordset) or (wordset&s2 == wordset) or (wordset&s3 == wordset):
                res.append(i)
        return res