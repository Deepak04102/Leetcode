class Solution(object):
    def maxProduct(self, nums):
        largest=second=0

        for num in nums:
            if num>largest:
                second=largest
                largest=num
            elif num>second:
                second=num

        return (largest-1)*(second-1)
        