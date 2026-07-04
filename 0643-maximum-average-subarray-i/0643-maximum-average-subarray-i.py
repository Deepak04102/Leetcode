class Solution(object):
    def findMaxAverage(self, nums, k):
        window_sum=sum(nums[:k])
        current_sum=window_sum
        
        for i in range(k,len(nums)):
            window_sum+=nums[i]-nums[i-k]
            current_sum=max(current_sum,window_sum)

        return float(current_sum)/k
        