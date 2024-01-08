class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        result = 0

        diffs = [ abs(ord(s[i]) - ord(t[i])) for i in range(len(s)) ]
        cost = 0
        left = 0
        for right in range(len(diffs)):
            # make string longer
            cost += diffs[right]
            # make string shorter
            while cost > maxCost:
                cost -= diffs[left]
                left += 1

            result = max(result, right - left + 1)

        return result
