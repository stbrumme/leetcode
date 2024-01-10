class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = list(range(1, m + 1))

        for q in queries:
            pos = p.index(q)
            yield pos
            p.pop(pos)
            p.insert(0, q)
