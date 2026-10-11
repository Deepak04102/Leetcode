class Solution(object):
    def sumOfSquares(self, nums):
        result=[]
        n=len(nums)
        for i in range(n):
            if n%(i+1)==0:
                result.append(nums[i]*nums[i])
        return sum(result)

        