class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        # state transitions:
        # x => y
        # y => x or z
        # z => x or z

        @cache
        def deeper(wasDoubleA, aa, bb, ab):
            result = 0
            if wasDoubleA: # "AA"
                if bb > 0:
                    result =             1 + deeper(False, aa, bb - 1, ab)
            else: # "AB" or "BB"
                if aa > 0:
                    result =             1 + deeper(True,  aa - 1, bb, ab)
                if ab > 0:
                    result = max(result, 1 + deeper(False, aa, bb, ab - 1))

            return result

        result = 0
        if x > 0:
            result =             1 + deeper(True,  x - 1, y, z)
        if y > 0:
            result = max(result, 1 + deeper(False, x, y - 1, z))
        if z > 0:
            result = max(result, 1 + deeper(False, x, y, z - 1))

        return 2 * result # algorithm counted chunks, each chunk has two letters
