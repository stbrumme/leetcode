class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False

        freq = defaultdict(int)
        for d in deck:
            freq[d] += 1

        g = freq[deck[0]]
        # same greatest common divisor
        for f in freq.values():
            if f != g:
                g = gcd(g, f)
        return g > 1
