class Solution:
    def maxPower(self, s: str) -> int:
        result = 1

        prev = ""
        same = 0
        for c in s + "!":
            if c == prev:
                same += 1
                result = max(result, same)
            else:
                same = 1
                prev = c
        return result
