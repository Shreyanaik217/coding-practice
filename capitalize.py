#capitalized the given string
class Solution(object):
    def capitalizeTitle(self, title):
        li = title.split()
        for i,l in enumerate(li):
            if len(l) <= 2:
                li[i] = l.lower()
            else:
                li[i] = l[0].upper() + l[1:].lower()
        return ' '.join(li)