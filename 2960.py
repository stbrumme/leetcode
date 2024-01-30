class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        result   = 0
        subtract = 0
        for b in batteryPercentages:
            b = max(0, b - subtract)
            if b > 0:
                result   += 1
                subtract += 1
        return result
