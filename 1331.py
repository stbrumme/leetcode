class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique = list(sorted(set(arr)))
        rank   = {}
        for i, u in enumerate(unique):
            rank[u] = i + 1

        for a in arr:
            yield rank[a]
