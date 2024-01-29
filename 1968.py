class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # rearrange such that
        # 1) nums[i] is larger  than nums[i - 1] and nums[i + 1]
        #    - OR -
        # 2) nums[i] is smaller than nums[i - 1] and nums[i + 1]

        nums.sort()
        prev = 0
        for i, n in enumerate(nums):
            if i & 1:
                yield n
                yield prev
            else:
                prev = n

        if len(nums) & 1:
            yield prev
