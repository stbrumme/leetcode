class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        @cache
        def deeper(pos):
            value = arr[pos]
            best  = 1
            # go left
            for i in range(1, d + 1):
                if pos - i < 0 or arr[pos - i] >= value:
                    break
                best = max(best, 1 + deeper(pos - i))
            # go right
            for i in range(1, d + 1):
                if pos + i == len(arr) or arr[pos + i] >= value:
                    break
                best = max(best, 1 + deeper(pos + i))

            return best

        result = 0
        for i in range(len(arr)):
            result = max(result, deeper(i))
        return result
