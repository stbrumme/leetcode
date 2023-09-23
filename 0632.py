class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        start, end = 0, 999999

        pos = [0] * len(nums)
        lower = [ (n[0], i) for i,n in enumerate(nums) ]
        heapify(lower)
        upper = max(lower)[0]

        while True:
            # min/max
            a = lower[0]
            smallest = a[1]

            if upper - a[0] < end - start:
                start, end = a[0], upper

            # remove/replace smallest
            if pos[smallest] == len(nums[smallest]) - 1:
                break
            pos[smallest] += 1
            heapreplace(lower, (nums[smallest][pos[smallest]], smallest))
            upper = max(upper, nums[smallest][pos[smallest]])

        return [ start, end ]