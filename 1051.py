class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum( h != e for h, e in zip(heights, sorted(heights)) )
