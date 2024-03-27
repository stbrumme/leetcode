class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        result = 0

        # remove duplicates and sort
        nums   = set(nums)
        # highest actually set bit
        high   = max(nums)
        maxbit = high.bit_length()

        # can't get any better than this
        optimal = 1 << (maxbit + 1) - 1

        # begin with highest bits
        mask = 0
        most = 2 # at most 2 candidates in first round, then 4, 8, 16, ...
        for bit in reversed(range(maxbit)):
            current = 1 << bit
            mask   |= current
            limit   = result | current

            one = set()
            for n in nums:
                one.add(n & mask)
                if len(one) == most: # early exit: all possible bitmasks
                    break
            most <<= 1

            for candidate in one:
                if limit ^ candidate in one:
                    result = limit

                    # early exit: perfect pair found
                    if result == optimal:
                        return result

        return result
