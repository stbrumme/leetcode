class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        size   = 2 * n - 1
        result = [ None ] * size

        def deeper(pos):
            # done
            if pos == size:
                return True

            # slot occupied, go deeper
            if result[pos] is not None:
                return deeper(pos + 1)

            # larger digits first (9,8,7,...,2)
            for digit in reversed(range(2, n + 1)):
                if digit in result:
                    continue

                # secondary position needs to be empty, too
                other = pos + digit
                if other >= size or result[other] is not None:
                    continue

                # fill in and go deeper
                result[pos] = result[other] = digit
                if deeper(pos + 1):
                    return True

                # failed, reset
                result[pos] = result[other] = None

            # no digit fits, try 1 (only once)
            if 1 not in result:
                result[pos] = 1
                if deeper(pos + 1):
                    return True
                result[pos] = None
            return False

        deeper(0)
        return result
