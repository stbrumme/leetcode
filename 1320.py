class Solution:
    def minimumDistance(self, word: str) -> int:
        # +inf is a placeholder indicating the initial hand positions

        def distance(x1, y1, x2, y2):
            if x1 == +inf:
                return 0
            return abs(x1 - x2) + abs(y1 - y2)

        @cache
        def deeper(x1, y1, x2, y2, pos):
            if pos == len(word):
                return 0

            c = ord(word[pos]) - ord("A")
            # 6x5 grid
            x = c  % 6
            y = c // 6

            # use left or right hand, whatever is cheaper/faster
            left  = deeper(x,  y,  x2, y2, pos + 1) + distance(x1, y1, x, y)
            right = deeper(x1, y1, x,  y,  pos + 1) + distance(x2, y2, x, y)
            return min(left, right)

        return deeper(+inf, +inf, +inf, +inf, 0)
