class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        size = len(nums)

        result = 0
        for left in range(size):
            multi = 1
            for right in range(left, size):
                multi = lcm(multi, nums[right])
                if multi >= k:
                    if multi == k:
                        result += 1
                    else:
                        break # multi > k

        return result
