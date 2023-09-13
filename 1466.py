class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        okay = defaultdict(list)
        bad  = defaultdict(list)
        for c in connections:
            bad [c[0]].append(c[1])
            okay[c[1]].append(c[0])

        result = 0

        done = set()
        todo = [ 0 ]
        while todo:
            next = [ ]
            for t in todo:
                if t in done:
                    continue
                done.add(t)

                for o in okay[t]:
                    if o not in done:
                        next   += [ o ]
                for b in bad[t]:
                    if b not in done:
                        next   += [ b ]
                        result += 1

            todo = next

        return result
