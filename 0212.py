class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = []

        m = len(board[0])
        n = len(board)

        prefix = set()
        for w in words:
            for i in range(1, len(w)):
                prefix.add(w[:i])

        hashed = set(words) # faster lookups

        def deeper(x, y, have):
            current = board[y][x]
            if current == ".": # letter already in use
                return

            have   += current
            board[y][x] = "."  # tombstone to avoid using a letter multiple times

            # found a word
            if have in hashed:
                result.append (have)
                hashed.discard(have)
                # note: do not return here because a word might be a prefix of another word

            # left, right, up, down
            if have in prefix:
                if x > 0:
                    deeper(x - 1, y, have)
                if x < m - 1:
                    deeper(x + 1, y, have)
                if y > 0:
                    deeper(x, y - 1, have)
                if y < n - 1:
                    deeper(x, y + 1, have)

            board[y][x] = current # restore

        # scan full board
        for y in range(n):
            for x in range(m):
                deeper(x, y, "")

        return result
