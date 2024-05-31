class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        result = 0

        have   = defaultdict(int)
        total  = 0
        unique = 0

        for i, n in enumerate(nums):
            # add new value
            total   += n
            have[n] += 1

            # unique
            if have[n] == 1:
                unique += 1
            if have[n] == 2:
                unique -= 1

            # remove old value
            if i >= k:
                old = nums[i - k]
                total     -= old
                have[old] -= 1

                if have[old] == 1:
                    unique += 1
                if have[old] == 0:
                    unique -= 1

            # if all value are unique, then check subarray sum
            if unique == k:
                result = max(result, total)

        return result
