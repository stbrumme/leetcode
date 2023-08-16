class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        y = 0
        delta = +1

        rows = defaultdict(str)
        for c in s:
            rows[y] += c
            y += delta

            if y < 0 or y == numRows:
                y -= 2*delta
                delta = -delta

        return "".join(rows.values())
