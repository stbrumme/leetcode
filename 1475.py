class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # brute force
        for i in range(len(prices)):
            pay = prices[i]
            for j in range(i + 1, len(prices)):
                if  pay >= prices[j]:
                    # discount
                    pay -= prices[j]
                    break
            yield pay
