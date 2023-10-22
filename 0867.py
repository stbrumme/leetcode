class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        for i in range(len(matrix[0])):
            yield [ matrix[j][i] for j in range(len(matrix)) ]
