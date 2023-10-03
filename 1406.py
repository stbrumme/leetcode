class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @cache
        def deeper(pos):
            if pos >= len(stoneValue):
                return 0

            take = stoneValue[pos]
            best = take - deeper(pos + 1)

            for i in range(pos + 1, pos + 2+1):
                if i < len(stoneValue):
                    take += stoneValue[i]
                    best  = max(best, take - deeper(i + 1))

            return best

        result = deeper(0)
        if result == 0:
            return "Tie"
        return "Alice" if result > 0 else "Bob"
