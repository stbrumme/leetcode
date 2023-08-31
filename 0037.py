class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def simplify(solution):
            changes = 0
            for x in range(9):
                for y in range(9):
                    # solved cell
                    if len(solution[x][y]) == 1:
                        continue

                    avoid = set()
                    for i in range(9):
                        # same column
                        if len(solution[x][i]) == 1:
                            avoid.add(solution[x][i][0])
                        # same row
                        if len(solution[i][y]) == 1:
                            avoid.add(solution[i][y][0])
                        # same box
                        xx = (x // 3) * 3 + i % 3
                        yy = (y // 3) * 3 + i // 3
                        if len(solution[xx][yy]) == 1:
                            avoid.add(solution[xx][yy][0])

                    for a in avoid:
                        if a in solution[x][y]:
                            solution[x][y].remove(a)
                            changes += 1
                    if len(solution[x][y]) == 0:
                        return -1

            return changes


        def validate(solution): # only checks if one candidate per cell, no further validation
            for x in range(9):
                for y in range(9):
                    if len(solution[x][y]) > 1:
                        return False
                    me = solution[x][y][0]
                    for i in range(9):
                        if i != x and me == solution[i][y][0]:
                            return False
                        if i != y and me == solution[x][i][0]:
                            return False
                        xx = (x // 3) * 3 + i % 3
                        yy = (y // 3) * 3 + i // 3
                        if (x != xx or y != yy) and me == solution[xx][yy][0]:
                            return False
            return True


        def isFinished(solution): # only checks if one candidate per cell, no further validation
            for x in range(9):
                for y in range(9):
                    if len(solution[x][y]) > 1:
                        return False
            return True


        def solve(deeper):
            # deep copy (why so weird in Python ?)
            attempt = []
            for x in range(9):
                r = []
                for y in range(9):
                    r.append(deeper[x][y].copy())
                attempt.append(r)

            if simplify(attempt) < 0:
                return None

            if isFinished(attempt):
                return attempt if validate(attempt) else None

            for x in range(9):
                for y in range(9):
                    if len(deeper[x][y]) > 1:
                        guess = deeper[x][y]
                        for c in guess:
                            attempt[x][y] = [ c ]
                            complete = solve(attempt)
                            if complete != None:
                                return complete
                        return None
            return attempt


        # 9 strings, each 9 bytes
        candidates = []
        for row in board:
            r = []
            for cell in row:
                if cell == ".":
                    r.append([ 1,2,3,4,5,6,7,8,9 ])
                else:
                    r.append([ int(cell) ])
            candidates.append(r)

        s = simplify(candidates)
        while s > 0:
            s = simplify(candidates)

        # let's go
        final = solve(candidates)

        # convert to Leetcode format
        result = []
        for x in range(9):
            r = []
            for y in range(9):
                board[x][y] = str(final[x][y][0])
