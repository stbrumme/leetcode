class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def bitmask(word):
            mask = 0
            for c in w:
                mask |= 1 << (ord(c) - ord('a'))
            return mask

        longest = defaultdict(set)
        for w in words:
            mask = bitmask(w)
            longest[mask].add(w)

        result = 0
        for w in words:
            me   = len(w)
            mask = bitmask(w)
            for l in longest:
                if mask & l == 0:
                    for o in longest[l]:
                        if o != w:
                            other = len(o)
                            result = max(result, me * other)

        return result
