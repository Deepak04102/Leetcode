class Solution(object):
    def heightChecker(self, heights):
        a=sorted(heights)
        count=0
        for i in range(len(heights)):
           

               if heights[i]!=a[i]:
                count+=1
        return count
                

        