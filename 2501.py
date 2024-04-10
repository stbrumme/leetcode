class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        result = -1

        have = set(nums)
        skip = set() # already part of another streak

        limit = max(have)

        for h in sorted(have):
            if h in skip:
                continue

            length = 1
            next   = h * h
            skip.add(next)

            while next in have:
                length += 1
                next   *= next
                result  = max(result, length)

            # upcoming streaks can't be any longer
            if next >= limit:
                break

        return result
