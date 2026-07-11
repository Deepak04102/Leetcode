from fractions import gcd
class Solution(object):
    def isGoodArray(self, nums):
        good=nums[0]
        for num in nums[1:]:
            good=gcd(good,num)
        return good==1
        