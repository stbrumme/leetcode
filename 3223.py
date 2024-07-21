class Solution:
    def minimumLength(self, s: str) -> int:
        # each step removes a letter twice if it exists at least 3 times
        freq = [ 0 ] * 26
        for c in s:
            c = ord(c) - 97 # ord("a") = 97
            if freq[c] >= 2:
                freq[c] -= 1 # same as += 1 plus -= 2
            else:
                freq[c] += 1

        return sum(freq)
