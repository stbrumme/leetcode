class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        result = 0

        banned = set(banned) # faster lookup
        last = 1
        have = 0
        while have + last <= maxSum and last <= n:
            if last not in banned:
                have   += last
                result += 1
            last += 1
        return result
