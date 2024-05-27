class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        result  = +inf

        # avoid huge loops/repetitions
        size    = len(nums)
        total   = sum(nums)
        loops   = target // total
        target %= total

        prefix = [ 0 ]
        have   = 0
        left   = 0
        for n in nums + nums: # doubling trick
            # prefix sum
            have += n
            prefix.append(have)

            need = have - target
            # a few shortcuts ...
            if need < 0:
                continue
            if need > total:
                break

            # binary search
            left = bisect_left(prefix, need, lo = left)
            if left < len(prefix) and prefix[left] == need:
                right  = len(prefix) - 1
                result = min(result, loops * size + right - left)

        return result if result < +inf else -1
