class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        # check if sorted without duplicates
        def increasing(data):
            return all(data[i - 1] < data[i] for i in range(1, len(data)))

        # find first mismatch
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                # remove left  element
                if increasing(nums[:i - 1] + nums[i:]):
                    return True
                # remove right element
                if increasing(nums[:i] + nums[i + 1:]):
                    return True

                # more than one misplaced element
                return False

        # already strictly increasing, can remove any element
        return True
