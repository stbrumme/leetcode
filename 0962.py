class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        result = 0

        # sorted in reverse
        low = [ ( nums[0], 0 ) ]
        for i in range(1, len(nums)):
            n = nums[i]
            if n < low[-1][0]:
                # lower than anything seen before
                low.append( ( n, i ) )
            else:
                # measure longest ramp
                left  = 0
                right = len(low) - 1
                # binary search for largest number not exceeding n
                while left != right:
                    mid = (left + right) // 2
                    value, pos = low[mid]
                    if value > n:
                        left  = mid + 1
                    else:
                        right = mid

                length = i - low[left][1]
                result = max(result, length)

        return result
