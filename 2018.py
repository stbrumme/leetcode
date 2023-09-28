class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        width  = len(board[0])
        height = len(board)

        patterns = [ "" ]
        for y in range(height):
            patterns.append("")
            for x in range(width):
                if   board[y][x] == "#":
                    patterns.append("")
                else:
                    patterns[-1] += board[y][x]

        for x in range(width):
            patterns.append("")
            for y in range(height):
                if   board[y][x] == "#":
                    patterns.append("")
                else:
                    patterns[-1] += board[y][x]

        for p in set(patterns):
            if len(p) != len(word):
                continue

            p = p.replace(" ", ".")
            if re.search(p, word):
                return True
            if re.search(p, word[::-1]):
                return True

        return False
