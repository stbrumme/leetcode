class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result = 0

        prev = ""
        high = 0
        for c, t in zip(colors, neededTime):
            result += t # remove balloon

            if c == prev:
                high = max(high, t)
            else:
                result -= high # keep balloon with longest removal time
                # start new color group
                high = t
                prev = c

        return result - high # adjust final group, too
