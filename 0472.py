class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # faster lookup
        all = set(words)

        @lru_cache(maxsize = 10000)
        def deeper(w, first):
            if w in all and not first: # prevent self-match
                return True

            for i in range(1, len(w)):
                if w[:i] in all and deeper(w[i:], False):
                    return True
            return False

        return [ w for w in words if deeper(w, True) ]