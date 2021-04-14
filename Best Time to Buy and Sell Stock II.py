class Solution(object):
    def maxProfit(self, prices):
        max=0
        lowest=0
        total=0
        if len(prices)==0:
            return 0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                if lowest==0 and max==0:
                    lowest=prices[i]
                    max=prices[i+1]
                if max<prices[i+1]:
                    max=prices[i+1]
            else:
                print(max,lowest)
                total+=(max-lowest)
                max=0
                lowest=0
        if total==0 or max!=0 or lowest!=0:
            total+=max-lowest
        return total
                
            
        """
        :type prices: List[int]
        :rtype: int
        """
        
