class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # moving by 2 is essentially free
        # therefore always move by 2 and at most once by 1
        # the final position doesn't matter:
        # we only have to decide whether it's an odd or even position
        odd = even = 0
        for p in position:
            if p & 1:
                even += 1
            else:
                odd  += 1

        return min(odd, even)
