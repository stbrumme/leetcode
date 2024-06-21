class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        result = +inf

        # extract last value
        last1 = nums1[-1]
        last2 = nums2[-1]
        nums1.pop()
        nums2.pop()

        # trivial case
        if not nums1:
            return 0

        # pass 1: keep last value
        # pass 2: swap them (swapLast == 1)
        for swapLast in range(2):
            swaps = swapLast
            okay  = True

            for one, two in zip(nums1, nums2):
                # no swap
                if one <= last1 and two <= last2:
                    continue

                # do swap
                one, two = two, one
                swaps   += 1
                # condition violated ?
                if one >  last1 or  two >  last2:
                    okay = False
                    break

            if okay:
                result = min(result, swaps)

            # swap last
            last1, last2 = last2, last1

        return result if result < +inf else -1
