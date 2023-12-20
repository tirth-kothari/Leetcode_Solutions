class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        total = prices[0]+prices[1]
        if money >= total:
            return (money-total)
        else:
            return money
