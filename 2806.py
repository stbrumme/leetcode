class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # let's write the most obscure formula
        return ((10 - (((purchaseAmount + 5) >> 1) // 5)) * 5) << 1
