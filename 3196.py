class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        size = len(nums)

        # our own caching, @cache is slow
        cache = [ +inf ] * (2 * size)

        def deeper(i): # positive parameter: add, negative: subtract
            pos = abs(i)
            if pos == size:
                return 0

            if cache[i] != +inf:
                return cache[i]

            # restart
            best = nums[pos] + deeper(pos + 1)

            # flip sign
            if i > 0:
                best = max(best, -nums[pos] + deeper(-(pos + 1)))
                # no need for else-branch:
                # it would be identical to a resatart

            cache[i] = best
            return best

        return deeper(0)
