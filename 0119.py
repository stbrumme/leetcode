class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # see 118
        prev = [ 1 ]
        for i in range(1, rowIndex + 1):
            row = []
            for j in range(1, i):
                row.append(prev[j - 1] + prev[j])
            prev = [ 1 ] + row + [ 1 ]
        return prev
