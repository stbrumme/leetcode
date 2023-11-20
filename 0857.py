class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        result = inf

        # sort by quality per wage
        candidates = [ ( q/w, q, w ) for q, w in zip (quality, wage) ]
        # the worker with lowest quality per wage determines the total cost according to rule 1
        candidates.sort(reverse = True)

        current = []
        sum     = 0
        for ratio, q, w in candidates:
            sum += q
            heappush(current, -q) # max-heap, use negative values

            # too many workers, remove those with high quality because they cost the most
            # (when adjusted for rule 1)
            if len(current) > k:
                remove = -heappop(current)
                sum   -= remove

            # current ratio is the lowest quality per wage
            if len(current) == k:
                result = min(result, sum / ratio)

        return result
