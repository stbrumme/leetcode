class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        result = 0

        have  = defaultdict(int)
        total = 0
        for right, n in enumerate(nums):
            if right >= k:
                # remove on left side of sliding window
                left = right - k
                x = nums[left]
                have[x] -= 1
                if have[x] == 0:
                    del have[x]
                total -= x

            # add on right side of sliding window
            have[n] += 1
            total   += n

            # yes, almost unique
            if len(have) >= m:
                result = max(result, total)

        return result
