class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        size = len(nums)

        # zeros don't change the result but simplify edge cases
        nums   = [ 0 ] + nums + [ 0 ]
        length = len(nums)

        # prefix sum, put positions in p slots, according to their modulo
        remain = defaultdict(list)
        have = 0
        for i, n in enumerate(nums):
            have += n
            remain[have % p].append(i)

        # sum(nums) % p == 0, remove nothing
        if have % p == 0:
            return 0

        result = size # without zeros
        have   = 0
        for i in reversed(range(length)): # including zeros
            n     = nums[i]
            have += n
            mod   = have % p

            # complementary number
            need  = p - mod if mod > 0 else 0

            # find closest position on the left
            # first remove everything on the right side
            while remain[need] and remain[need][-1] >= i:
                remain[need].pop()
            # need check that position which is on the left
            if remain[need]:
                remove = i - remain[need][-1] - 1
                result = min(result, remove)

        return result if result < size else -1
