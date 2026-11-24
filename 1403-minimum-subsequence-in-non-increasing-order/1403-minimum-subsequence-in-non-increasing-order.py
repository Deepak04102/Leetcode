class Solution(object):
    def minSubsequence(self, nums):
        nums.sort(reverse=True)
        total=sum(nums)
        ans=[]
        curr=0

        for num in nums:
            curr+=num
            ans.append(num)

            if curr>total-curr:
                return ans

        