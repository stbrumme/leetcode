class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        result = inf

        # sliding window is more efficient but needs more code ...
        for i in range(len(blocks) - k + 1):
            white = 0
            for j in range(k):
                if blocks[i + j] == "W":
                    white += 1

            result = min(result, white)

        return result
