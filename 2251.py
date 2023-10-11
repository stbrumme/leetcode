class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # heap for flowers beginning to bloom
        earliest = [ (a, b) for a, b in flowers ]
        heapify(earliest)

        # heap indicating last day of bloom
        bloom = []

        reorder = {} # map back from sorted to unsorted
        for p in sorted(set(people)):
            # add new flowers
            while earliest:
                start, end = earliest[0]
                if start > p:
                    break

                heappop (earliest)
                heappush(bloom, end)

            # remove old flowers
            while bloom and bloom[0] < p:
                heappop(bloom)

            # number of blooming flowers
            reorder[p] = len(bloom)

        return [ reorder[p] for p in people ]
