class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        lost  = 0
        delta = 0
        for cost, cashback in transactions:
            # branch-free code
            lost += max(0, cost - cashback)
            delta = max(delta, min(cashback, cost))

        return lost + delta
