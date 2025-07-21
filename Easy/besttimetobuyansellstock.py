class Solution(object):
    def maxProfit(self, prices):

        # greedy method just buy and sell whenever you can hold highest_number youve come
        # across for reference wrong greedy approach 

        # greedy gets minmum price and compares it to highest 
        # was doing a square peg in a round hole 

        profit = 0
        lowest_price = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < lowest_price:
                lowest_price = prices[i]
            
            profit = max(profit,prices[i]-lowest_price)

    
        return(profit)



        """
        :type prices: List[int]
        :rtype: int
        """

# trolled for 20 minutes and then smartened up