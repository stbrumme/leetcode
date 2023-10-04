class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def deeper(left, right):
            if left == right:
                return nums[left]

            l = nums[left]  - deeper(left + 1, right)
            r = nums[right] - deeper(left, right - 1)
            return max(l, r)

        return deeper(0, len(nums) - 1) >= 0
