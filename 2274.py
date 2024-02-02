class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        result = 0

        last = bottom - 1
        for s in sorted(special) + [ top + 1 ]:
            result = max(result, s - last - 1)
            last   = s

        return result
