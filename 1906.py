class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        size = len(nums)
        have = sorted(set(nums))
        high = max(have)
        low  = min(have)

        all  = [ [] for _ in range(high + 1) ]
        # store positions of all numbers
        for i, n in enumerate(nums):
            all[n].append(i)

        for l, r in queries:
            previous = -inf
            best     = +inf

            # try all numbers (only 0...100 are allowed)
            for i in have:
                pos = bisect_left(all[i], l)
                # test if exists between l and r
                if pos < len(all[i]) and all[i][pos] <= r:
                    best = min(best, i - previous)
                    if best == 1:
                        break
                    previous = i

            # all numbers are the same
            if best == +inf:
                best = -1

            yield best
