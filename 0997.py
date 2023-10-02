class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # convert edges to sets
        all = defaultdict(set)
        for a, b in trust:
            all[a].add(b)

        # AND all those sets
        common    = set(range(1, n + 1))
        candidate = None
        numEmpty  = 0
        for i in range(1, n+1):
            if not all[i]:
                numEmpty += 1
                continue

            common &= all[i]
            if not common: # early exit: noone left who is trusted by everybody
                return -1

        # persons who trust noone
        if numEmpty != 1:
            return -1

        # a unique person must be left
        if len(common) != 1:
            return -1
        for c in common: # weird syntax to extract the only element from a set
            return c
