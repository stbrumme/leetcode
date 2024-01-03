class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        pos = +inf
        for i, n in enumerate(nums):
            if n == target:
                old = abs(pos - start)
                new = abs(i   - start)
                if new < old:
                    pos = i
        return abs(pos - start)
