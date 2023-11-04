class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @cache
        def deeper(start, coins):
            # pick coins from pile "start" and/or its right neighbors
            if start == len(piles):
                return 0

            total = 0 # value  of picked coins
            have  = 0 # number of picked coins
            best  = deeper(start + 1, coins) # pick nothing from current pile
            for p in piles[start]:
                # pick coins and find optimal choice
                total += p
                have  += 1
                if have > coins:
                    break
                best   = max(best, total + deeper(start + 1, coins - have))

            return best

        return deeper(0, k)
