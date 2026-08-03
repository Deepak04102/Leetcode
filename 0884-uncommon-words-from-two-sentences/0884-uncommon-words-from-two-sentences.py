class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        words=(s1+" "+s2).split()
        count={}
        for word in words:
            count[word]=count.get(word,0)+1

        ans=[]

        for word in count:
            if count[word]==1:
                ans.append(word)

        return ans

        
        