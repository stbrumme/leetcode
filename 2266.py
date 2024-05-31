class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        size = len(pressedKeys)

        # convert to ints, so that comparisons are much faster
        keys = [ int(c) for c in pressedKeys ]
        keys.append(+inf) # stop marker

        @cache
        def deeper(pos):
            if pos == size:
                return 1

            # each number has 3 letters, but numbers 7 and 9 have 4
            num = keys[pos]

            # press the same number 1 to 3/4 times
            result = 0
            for repeat in range(1, 4 + 1):
                if repeat < 4 or num == 7 or num == 9:
                    next    = pos + repeat
                    result += deeper(next)
                    if next > size or keys[next] != num:
                        break

            return result % 1_000_000_007

        return deeper(0)
