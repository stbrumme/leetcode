class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        # build suffix in reverse ...
        suffix = []
        seen   = set()
        for n in reversed(nums):
            suffix.append(len(seen))
            seen.add(n)

        # because pop() is much faster than pop(0)
        seen.clear()
        for n in nums:
            seen.add(n)
            yield len(seen) - suffix.pop()
