class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        result = 0

        size = len(nums)
        even = True
        for i in range(size - 1):
            # left number must be at an even index
            if even:
                # delete left number if equal
                if nums[i] == nums[i + 1]:
                    result += 1     # still even
                else:
                    even = False    # will be odd
            else:
                even = True

        # if final array has an odd length, remove one more element
        return result + (1 if even else 0) # note: i run until size - 1, therefore even is negated
