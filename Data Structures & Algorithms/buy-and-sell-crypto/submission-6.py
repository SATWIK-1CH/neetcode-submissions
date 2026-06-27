class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price= float('inf')
        max_diff=0
        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            max_diff=max(prices[i]-min_price,max_diff)
            print('the current diff is',max_diff)
        return max(0,max_diff)