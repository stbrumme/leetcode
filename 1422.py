class Solution:
    def maxScore(self, s: str) -> int:
        result = 0

        left  = 0 # count 0s
        right = s.count("1")
        for c in s[:-1]:
            if c == "0":
                left  += 1
            else:
                right -= 1

            result = max(result, left + right)
        return result
