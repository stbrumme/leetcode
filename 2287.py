class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        # required letters
        need = defaultdict(int)
        for c in target:
            need[c] += 1

        # available letters
        have = defaultdict(int)
        for c in s:
            if c in need: # count only those letters we actually need
                have[c] += 1

        result = +inf
        for c in need:
            if c not in have:
                return 0
            result = min(result, have[c] // need[c])
        return result
