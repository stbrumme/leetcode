class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        maxheap = [ -int(n) for n in nums ]
        heapify(maxheap)

        for _ in range(k - 1):
            heappop(maxheap)
        return str(-maxheap[0])
