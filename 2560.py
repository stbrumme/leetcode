class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # greedily steal up to "limit" money, return visited houses
        def steal(limit):
            robbed = 0
            skip   = False # don't rob the next house
            for n in nums:
                # rob this house
                if n <= limit and not skip:
                    robbed += 1
                    skip = True
                else:
                    skip = False

            return robbed

        high = max(nums) # at most 10^9
        return bisect_left(range(high + 1), k, key = steal)
