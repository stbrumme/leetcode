class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        result = []
        for g in grid:
            for i, n in enumerate(g):
                size = len(str(n))
                if i == len(result):
                    result.append(size)
                else:
                    result[i] = max(result[i], size)
        return result
