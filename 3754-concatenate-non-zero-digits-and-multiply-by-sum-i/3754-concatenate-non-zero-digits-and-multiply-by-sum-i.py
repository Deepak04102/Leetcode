class Solution(object):
    def sumAndMultiply(self, n):
        digit_sum=0
        num=0
        
        for ch in str(n):
            digit=int(ch)
            if digit!=0:
                num=num*10+digit
                digit_sum+=digit
        return num*digit_sum
        