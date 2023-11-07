class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        # positions of all letters
        board = { }
        for letter in range(26):
            x = letter %  5
            y = letter // 5
            ascii = chr(ord("a") + letter)
            board[ascii] = ( x, y )

        result = ""
        x, y = 0, 0
        for c in target:
            bx = board[c][0]
            by = board[c][1]

            # can't go right if cursor is at "z"
            if y == 5 and x != bx:
                result += "U"
                y -= 1

            # left / right
            while x < bx:
                result += "R"
                x += 1
            while x > bx:
                result += "L"
                x -= 1
            # up / down
            while y < by:
                result += "D"
                y += 1
            while y > by:
                result += "U"
                y -= 1

            # found the letter
            result += "!"

        return result
