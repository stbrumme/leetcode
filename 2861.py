class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        def impossible(alloys):
            # look at each machine
            for c in composition:
                paid = 0
                # create alloys as requested
                for metal, have, price in zip(c, stock, cost):
                    need = alloys * metal - have
                    if need > 0:
                        paid += need * price

                # within budget ?
                if paid <= budget:
                    return False
            # that's inflation ...
            return True

        # look for smallest number that's impossible, choose its predecessor
        return bisect_left(range(budget + min(stock) + 1), True, key = impossible) - 1
