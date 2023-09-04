class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Kahn's algorithm
        start = set(range(numCourses))
        need  = defaultdict(set)

        # courses without any prerequisites
        for p in prerequisites:
            start.discard(p[0])
            need[p[0]].add(p[1])

        result = []
        done   = set()
        # pick next course
        while start:
            next = start.pop()
            if next not in done:
                result += [ next ]
            done.add(next)

            candidates = []
            for n in need:
                need[n].discard(next)
                if n not in done and len(need[n]) == 0:
                    candidates.append(n)

            for c in candidates:
                start.add(c)
                del need[c]

        # still some courses not taken ?
        if len(result) < numCourses:
            return []
        else:
            return result
