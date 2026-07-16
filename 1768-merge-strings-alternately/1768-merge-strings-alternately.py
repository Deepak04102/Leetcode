class Solution(object):
    def mergeAlternately(self, word1, word2):
        a=len(word1)
        b=len(word2)
        i=0
        j=0

        ans=[]
        while i<a and j<b:
            ans.append(word1[i])
            ans.append(word2[j])
            i+=1
            j+=1

        while i<a:
            ans.append(word1[i])
            i+=1
        while j<b:
            ans.append(word2[j])
            j+=1

        return "".join(ans)
        