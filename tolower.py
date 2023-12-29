#to convert uppercase to lowercase
class Solution(object):
    def toLowerCase(self, s):
        answerString = ""
        for i in s:
            if 'A' <= i <= 'Z':
                answerString = answerString + chr(ord(i)+32)
            else:
                 answerString = answerString + i

        return answerString