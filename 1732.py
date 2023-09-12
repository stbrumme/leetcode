class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = 0
        alt = 0
        for g in gain:
            alt += g
            result = max(result, alt)

        return result
