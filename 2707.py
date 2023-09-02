class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        @cache
        def deeper(pos):
            if pos == len(s):
                return 0

            # immediate match
            result = len(s) - pos
            for d in dictionary:
                if s[pos:].startswith(d):
                    result = min(result, deeper(pos + len(d)))

            # gap
            return min(result, 1 + deeper(pos + 1))

        return deeper(0)
