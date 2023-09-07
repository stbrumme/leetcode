class Solution:
    def partitionString(self, s: str) -> int:
        result = 1
        have = set()
        for c in s:
            if c in have:
                result += 1
                have.clear()

            have.add(c)

        return result
