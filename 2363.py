class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        all = defaultdict(int)
        for v, w in items1 + items2:
            all[v] += w

        for a in sorted(all):
            yield a, all[a]
