class Solution(object):
    def minimumFlips(self, n):
        s=bin(n)[2:]
        ans=0

        i=0
        j=len(s)-1
        while i<j:
            if s[i]!=s[j]:
                ans+=2
            i+=1
            j-=1

        
        return ans
        