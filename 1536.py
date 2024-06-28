class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        result = 0

        size = len(grid)

        # count trailing zeros
        zeros = []
        for row in grid:
            trailing = 0
            while trailing < size and row[-(trailing + 1)] == 0:
                trailing += 1

            zeros.append(trailing)

        for need in reversed(range(size)):
            pos = 0
            # find first row with enough trailing zeros
            while zeros[pos] < need:
                # nope, not good enough, need to swap
                result += 1
                pos    += 1
                # failed
                if pos == len(zeros):
                    return -1

            del zeros[pos]

        return result
