class Solution(object):
    def minimumPushes(self, word):
        n=len(word)
        res=0
        for i in range(n):
            res=res+(i/8+1)
        return res
        