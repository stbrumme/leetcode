class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(dict)
        for t in times:
            edges[t[0]][t[1]] = t[2]

        have = { k : 0 }
        todo = set([ k ])
        while todo:
            next = set()
            for t in todo:
                for e in edges[t]:
                    duration = have[t] + edges[t][e]
                    if e not in have or have[e] > duration:
                        have[e] = duration
                        next.add(e)
            todo = next
                    
        if len(have) != n:
            return -1
        return max(have.values())