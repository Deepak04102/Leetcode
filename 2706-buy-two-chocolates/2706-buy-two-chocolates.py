class Solution(object):
    def buyChoco(self, prices, money):
        first=float('inf')
        second=float('inf')

        for price in prices:
            if price<first:
                second=first
                first=price
            elif price<second:
                second=price

        cost=first+second

        if cost<=money:
            return money-cost

        return money

        
        