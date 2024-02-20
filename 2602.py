class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        size = len(nums)
        nums.sort()

        # prefix sum
        prefix = []
        total  = 0
        for n in nums:
            total += n
            prefix.append(total)

        for q in queries:
            # smaller than any number
            if q <= nums[0]:
                yield total - size * q
                continue
            # bigger  than any number
            if q >= nums[-1]:
                yield size * q - total
                continue

            # increment on the left  side to match q
            pos   = bisect_left(nums, q)
            lower = prefix[pos - 1]
            same  = q * pos
            left  = same - lower

            # decrement on the right side to match q
            higher = total - lower
            same   = q * (size - pos)
            right  = higher - same

            yield left + right
