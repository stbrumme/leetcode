class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        low  = [ inf ] * len(nums)
        # lowest element between nums[i] and nums[k]
        have = nums[k]
        for i in range(k, -1, -1):
            have = min(have, nums[i])
            low[i] = have
        # lowest element between nums[k] and nums[j]
        have = nums[k]
        for j in range(k + 1, len(nums)):
            have = min(have, nums[j])
            low[j] = have

        result = len(low) * min(low[0], low[-1]) # the whole array could be a good subarray, too
        i = j = k
        while i > 0 or j < len(low) - 1:
            # same minimum, try to maximize the width
            while i > 0     and low[i] == low[i - 1]:
                i -= 1
            while j < k - 1 and low[j] == low[j + 1]:
                j += 1

            width  = j - i + 1
            result = max(result, width * min(low[i], low[j]))

            # reached border
            if i == 0:
                j += 1
                continue
            if j == len(low) - 1:
                i -= 1
                continue

            # extend the side with the higher minimum
            if low[i - 1] > low[j + 1]:
                i -= 1
            else:
                j += 1

        return result
