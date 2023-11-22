class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        piles  = sorted([ -g for g in gifts ]) # turn into max-heap
        for _ in range(k):
            heappushpop(piles, -int(sqrt(-piles[0])))
        return -sum(piles)
