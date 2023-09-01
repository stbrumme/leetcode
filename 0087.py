class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def deeper(a, b):
            # early exit
            if a == b:
                return True
            if sorted(a) != sorted(b):
                return False

            for i in range(1, len(a)):
                # no swap
                if deeper(a[:i], b[:i]) and deeper(a[i:], b[i:]):
                    return True

                # swap
                swapped = a[i:] + a[:i]
                p = len(a) - i
                if deeper(swapped[:p], b[:p]) and deeper(swapped[p:], b[p:]):
                    return True

            return False

        return deeper(s1, s2)
