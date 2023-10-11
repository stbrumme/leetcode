class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        result = 0
        for left in range(len(nums)):
            if nums[left] > threshold or nums[left] % 2 != 0:
                continue

            # not very efficient but good enough ...
            length = 1
            expect = 1 # now look for pattern 0,1,0,1,0, ...
            for right in range(left + 1, len(nums)):
                if nums[right] > threshold or nums[right] % 2 != expect:
                    break

                length += 1
                expect ^= 1

            # we could adjust the variable "left" to speed up

            result = max(result, length)

        return result
