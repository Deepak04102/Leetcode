class Solution(object):
    def sequentialDigits(self, low, high):
        ans=[]
        for start in range(1,9):
            num=start
            for next in range(start+1,10):
                num=num*10+next
                if low<=num<=high:
                    ans.append(num)

        ans.sort()
        return ans        