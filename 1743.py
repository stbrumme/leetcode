class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # faster lookup
        next = defaultdict(list)
        for a, b in adjacentPairs:
            next[a].append(b)
            next[b].append(a)

        # first and last element
        start = None
        stop  = None
        for n in next:
            if len(next[n]) == 1:
                if not start:
                    start = n
                else:
                    stop  = n

        yield start

        have  = set([ start ])
        pick, = next[start]
        # walk the line ...
        while pick != stop:
            yield pick

            have.add(pick)
            a, b = next[pick]
            pick = a if b in have else b

        yield stop
