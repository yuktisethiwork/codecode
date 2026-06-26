# Problem: 121. Best Time to Buy and Sell Stock
# Approach: Solution
# Language: python3
# Time: O(n)
# Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=1
        n=len (prices)
        maxp=0
        while j<=n-1:
            buy=prices[i]
            sell=prices[j]
            profit=sell-buy
            print(profit)
            if profit>maxp:
                maxp=profit
            if prices[j]<prices[i]:
                i=j
                j+=1
            else:
                j+=1
            print(i,j)
        return maxp
        
            


        



            

            