class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        size = len(nums1)
        k    = k1 + k2

        # reduce largest differences first
        deltas = [ 0 ] + sorted([ abs(n1 - n2) for n1, n2 in zip(nums1, nums2) ])
        total  = sum(deltas)
        if total <= k: # all differences become zero
            return 0

        last = deltas[-1]
        same = 0
        while k > 0 and deltas:
            diff = last - deltas[-1]

            # group identical deltas
            if diff == 0:
                deltas.pop()
                same += 1
                continue

            # apply k to the last number(s)
            remove = diff * same
            if remove > k: # can't make it identical, too few k left
                diff   = k // same
                remove = diff * same
                if diff == 0:
                    break
            last -= diff
            k    -= remove

        a = k        # last - 1
        b = same - a # last

        return sum( d**2 for d in deltas) + ((last - 1) ** 2) * a + (last ** 2) * b
