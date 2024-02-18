class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)
        candidates = set()

        # check second condition
        right = 1
        for i in reversed(range(size)):
            if i + 1 < size and nums[i] <= nums[i + 1]:
                right += 1
            else:
                right  = 1

            if right >= k:
                candidates.add(i)

        # check first condition
        left = 1
        for i in range(size):
            if i > 0 and nums[i] <= nums[i - 1]:
                left += 1
            else:
                left  = 1

            if left >= k and i + 2 in candidates:
                yield i + 1 # good index
