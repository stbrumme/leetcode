class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        all = []
        for v, l in zip(values, labels):
            heappush(all, (-v, l)) # max-heap: negate value

        have   = defaultdict(int)
        result = 0
        count  = 0
        while all and count < numWanted:
            v, l = heappop(all)
            if have[l] == useLimit:
                continue

            v = -v # was negated to convert min-heap to max-heap

            have[l] += 1
            count   += 1
            result  += v

        return result
