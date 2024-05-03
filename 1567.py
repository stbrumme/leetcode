class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        result = 0

        # process an array without zeros
        def check(sub):
            best = 0

            # first and last time a negative number was observed
            first = None
            last  = None
            sign  = +1
            for i, s in enumerate(sub):
                # process only negative numbers
                if s < 0:
                    sign = -sign
                    if first is None:
                        first = i
                    last = i

            # whole subarray is positive
            if sign == +1:
                return len(sub)

            # skip everything before (and including) the first negative number
            # or   everything after  (and including) the last  negative number
            return max(len(sub) - (first + 1), last)

        # partition into non-zero groups
        start = 0
        for end, n in enumerate(nums + [ 0 ]): # pad with zero to properly handle final partition
            if n == 0:
                result = max(result, check(nums[start : end]))
                start  = end + 1

        return result
