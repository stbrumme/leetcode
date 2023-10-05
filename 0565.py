class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        result = 1
        todo = set(nums)
        for n in nums:
            if n not in todo:   # already part of another cycle
                continue

            have = set([ n ])
            while True:
                n = nums[n]
                if n in have:   # cycle complete
                    break

                have.add(n)     # current cycle
                todo.discard(n) # numbers are part of exactly one cycle

            result = max(result, len(have))

        return result
