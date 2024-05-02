class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        size = len(nums)

        all  = iter(sorted(range(size), key = lambda x : nums[x]))

        marked = [ False ] * size
        total  = sum(nums)

        for index, k in queries:
            # optional: mark at index
            if not marked[index]:
                marked[index] = True
                total -= nums[index]

            # required: mark up to k small numbers
            for _ in range(k):
                # no unmarked items left
                if total == 0:
                    break

                # pick smallest unmarked
                while marked[index]:
                    index = next(all)
                marked[index] = True
                total -= nums[index]

            yield total
