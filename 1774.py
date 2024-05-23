class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        # return difference but prefer cheaper price
        best = lambda paid : abs(target - paid - 0.1)

        @cache
        def deeper(paid, pos):
            # reach target or out of toppings
            if paid >= target or pos == len(toppingCosts):
                return paid

            # 0, 1 or 2 of each topping
            top = [ deeper(paid + i * toppingCosts[pos], pos + 1) for i in ( 0, 1, 2 ) ]
            return sorted(top, key = best)[0]

        desserts = [ deeper(b, 0) for b in baseCosts ]
        return sorted(desserts, key = best)[0]
