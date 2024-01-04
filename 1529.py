class Solution:
    def minFlips(self, target: str) -> int:
        result = 0
        use = 0
        for c in target:
            if int(c) != use:
                result += 1
                use    ^= 1

        return result
