class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        for i in range(m):
            yield original[i * n : (i + 1) * n]
