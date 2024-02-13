class Solution:
    def minimumCost(self, s: str) -> int:
        result = 0

        size = len(s)
        for i in range(size - 1):
            if s[i] != s[i + 1]:
                left    = i + 1
                right   = size - left
                result += min(left, right) # flip left or right side, whatever is cheaper

        return result
