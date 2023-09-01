class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # modified binary search
        def deeper(left, right):
            if nums[left] == target or nums[right] == target:
                return True

            if left >= right:
                return False

            pivot = (left + right) // 2
            if nums[pivot] == target:
                return True

            if nums[left] < nums[right]:
                # basic binary search
                if nums[pivot] > target:
                    return deeper(left, pivot - 1)
                else:
                    return deeper(pivot + 1, right)
            else:
                # full search
                return deeper(left, pivot - 1) or deeper(pivot + 1, right)

        return deeper(0, len(nums) - 1)
