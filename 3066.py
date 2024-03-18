class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        result = 0

        heapify(nums) # min-heap
        while len(nums) >= 2:
            x = heappop(nums)
            if x >= k:
                break

            y = nums[0]
            heapreplace(nums, 2 * x + y) # faster than pop + push
            result += 1

        return result
