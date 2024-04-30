class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        # prepare sliding window, ignore positive numbers
        have  = [ 0 ] * 51 # negative index is fine in Python ...
        for n in nums[ : k - 1]:
            if n < 0:
                have[n] += 1
        total = sum(have)

        previous = 0
        for left, right in zip(nums, nums[k - 1 : ]):
            if right < 0:
                have[right] += 1
                total       += 1
                if right < previous:
                    previous = 0

            if   previous < 0:
                # order didn't change
                yield previous
            elif total < x:
                # too few negative numbers
                yield 0
            else:
                # count negative numbers
                negative = 0
                for i in range(-50, 0):
                    # enough
                    if negative + have[i] >= x:
                        break
                    negative += have[i]

                yield i
                previous = i

            if left < 0:
                have[left] -= 1
                total      -= 1
                if left <= previous:
                    previous = 0
