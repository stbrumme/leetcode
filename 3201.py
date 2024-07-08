class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # only the lowest bit matters:
        # odd:  1 + 0 or 0 + 1
        # even: 0 + 0 or 1 + 1
        size = len(nums)
        for i in range(size):
            nums[i] &= 1

        def odd(target):
            best = 0
            for n in nums:
                if n == target:
                    best   += 1
                    target ^= 1
            return best

        even1 = sum(nums)    # = nums.count(1)
        even0 = size - even1 # = nums.count(0)

        return max(odd(0), odd(1), even0, even1)
