class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        indices = [ [ i, sum(mat[i]) ] for i in range(len(mat)) ]
        indices.sort(key = lambda x : x[1])
        return [ i[0] for i in indices ][:k]