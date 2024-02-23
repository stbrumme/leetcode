class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        width = len(mat[0])
        if k % width == 0: # full rotations
            return True

        for i, row in enumerate(mat):
            for x in range(width):
                if i & 1: # odd
                    if row[x] != row[(x + k) % width]:
                        return False
                else:     # even
                    if row[x] != row[(x - k) % width]:
                        return False

        return True
