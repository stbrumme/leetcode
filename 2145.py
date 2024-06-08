class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        high = low = 0
        diff = 0
        for d in differences:
            diff += d
            high  = max(high, diff)
            low   = min(low,  diff)

        low  = lower - low
        high = upper - high

        return max(high - low + 1, 0)
