class Solution(object):
    def totalMoney(self, n):
        sum=0
        for i in range(n):
            week=i//7
            day=i%7
            sum+=week+day+1
        return sum

        