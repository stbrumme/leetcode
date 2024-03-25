class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        result = 0
        last   = [ 0 ] * 26 # longest substring ending with that letter
        expect = -1         # random number outside 0...25
        length = 0
        for c in s:
            # map "a"..."z" to 0...25
            c = ord(c) - ord("a")
            # continue or reset
            if c == expect:
                length += 1
            else:
                length  = 1

            # next letter in alphabet incl. wraparound
            expect = c + 1
            if expect == 26: # same as mod 26
                expect = 0

            # even longer than before ?
            last[c] = max(last[c], length)

        return sum(last)
