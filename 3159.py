class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        pos = [ i for i, n in enumerate(nums) if n == x ]
        for q in queries:
            if q <= len(pos):
                yield pos[q - 1]
            else:
                yield -1
