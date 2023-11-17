class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        result = inf

        # step 1: maximize elements (second operation, can only be applied once)
        for i in range(len(nums)):
            if (nums[i] & 1) == 1:
                nums[i] *= 2
        # all elements are now even

        low = min(nums)

        # step 2: minimize elements, beginning with the largest => max-heap
        maxheap = [ -n for n in nums ] # max-heap means negated sign
        heapify(maxheap)
        while (maxheap[0] & 1) == 0: # second operation, can be applied multiple times
            smaller = -maxheap[0] // 2
            heappushpop(maxheap, -smaller)

            low    = min(low, smaller)
            high   = -maxheap[0]
            result = min(result, high - low)

        return result
