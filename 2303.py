class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        result = 0
        prev   = 0 # "upper" from previous iteration
        for upper, percent in brackets:
            applicable = min(upper, income) - prev  # income in that bracket
            result    += applicable * percent / 100 # taxes

            # continue with next bracket (if needed)
            prev       = upper
            if prev >= income:
                break

        return result
