class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        for _ in range(k):
            heappush(nums, -heappop(nums))
        return sum(nums)
