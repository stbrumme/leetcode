class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        need = set(range(left, right + 1))
        for l, r in ranges:
            for i in range(l, r + 1):
                need.discard(i)
        return not need
