class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        result = 1
        size   = len(nums)

        skip = 0
        for i in range(size):
            # if there's a known mismatch, then skip
            if skip > 0:
                skip -= 1
                continue

            # each subarray with length 1 is always size
            nice = True

            # try longer subarrays
            for last in range(i + 1, size):
                if nums[last] != 0: # x AND 0 is always 0
                    for scan in range(i, last):
                        if nums[scan] & nums[last]:
                            nice = False
                            skip = scan - i
                            break

                # mismatch, abort
                if not nice:
                    break

                length = last - i + 1
                result = max(result, length)

        return result
