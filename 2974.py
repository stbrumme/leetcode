class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapify(nums)
        while nums:
            alice = heappop(nums)
            bob   = heappop(nums)
            yield bob
            yield alice
