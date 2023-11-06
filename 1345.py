class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # positions with same arr[]
        same = defaultdict(set)
        for i, a in enumerate(arr):
            same[a].add(i)

        # bfs
        todo  = set([ 0 ])
        seen  = set([ -1 ]) # avoid checking for negative numbers
        last  = len(arr) - 1
        steps = 0
        while todo:
            if last in todo:
                return steps

            next = set()
            for t in todo:
                if t in seen:
                    continue
                seen.add(t)

                if t + 1 not in seen:
                    next.add(t + 1)
                if t - 1 not in seen:
                    next.add(t - 1)

                next |= same[arr[t]]
                same[arr[t]].clear() # crucial to handle cases with many repeated numbers

            todo   = next
            steps += 1
