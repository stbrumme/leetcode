class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        x1 = ord(s[0]) - ord("A")
        y1 = int(s[1])
        x2 = ord(s[3]) - ord("A")
        y2 = int(s[4])

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                yield chr(x + ord("A")) + str(y)
