class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        for i in range(len(s)):
            y, x = startPos
            for j in range(i, len(s)):
                if   s[j] == "L": x -= 1
                elif s[j] == "R": x += 1
                elif s[j] == "U": y -= 1
                else:             y += 1

                if not (0 <= x < n) or not (0 <= y < n):
                    j -= 1 # failed to make last step
                    break  # off the grid

            yield j - i + 1 # steps
