class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        best = 0 
        for p in prices :
            best = max(best, p - mini)
            mini = min(mini, p)
        return best
        