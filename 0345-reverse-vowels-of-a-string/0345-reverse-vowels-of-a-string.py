class Solution(object):
    def reverseVowels(self, s):
        s=list(s)
        
        l=0
        n=len(s)
        r=n-1
        vowel=set("aeiouAEIOU")

        while l<r:
            while l<r and s[l] not in vowel:
                l+=1
            while l<r and s[r] not in vowel:
                r-=1
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1

        return "".join(s)

        