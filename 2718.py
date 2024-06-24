class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        result = 0

        # skip these because they were overwritten
        skipRow    = set()
        skipColumn = set()

        for type, index, value in reversed(queries):
            if type == 0: # row
                if index not in skipRow:
                    remaining = n - len(skipColumn) # note: it's not len(skipRow)
                    result   += remaining * value
                    skipRow.add(index)
            else:         # column
                if index not in skipColumn:
                    remaining = n - len(skipRow)
                    result   += remaining * value
                    skipColumn.add(index)

        return result
