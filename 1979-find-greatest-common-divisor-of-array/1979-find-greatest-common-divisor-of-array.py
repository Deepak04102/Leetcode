class Solution(object):
    def findGCD(self, nums):
        mx=max(nums)
        mn=min(nums)

        while mx:
            mn, mx = mx, mn % mx

        return mn
        