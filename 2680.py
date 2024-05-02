class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        result = 0

        # always apply all shifts to one element, pretty often it's max(nums)
        # but not always !

        have = [  0   ] * 32 # count how often each bit is used
        last = [ None ] * 32 # most recent number having that bit set
        all  = 0             # ORing all numbers
        for n in nums:
            all |= n

            reduce = n
            while reduce > 0:
                i = reduce.bit_length() - 1 # position of highest bit
                reduce  ^= 1 << i           # clear highest bit
                have[i] += 1
                last[i]  = n

        # remove unused high bits
        while len(have) > 1 and have[-1] == 0:
            have.pop()
            last.pop()
        bits = len(have)

        for n in nums:
            # shift
            current = n << k
            # basic test to reject small values
            if (current | all) <= result:
                continue

            # add bits from other elements (= not unique to current value)
            for i in range(bits):
                if have[i] > 1 or (have[i] == 1 and last[i] != n):
                    current |= 1 << i

            result = max(result, current)

        return result
