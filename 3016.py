class Solution:
    # same as problem 3014
    def minimumPushes(self, word: str) -> int:
        result = 0

        # count letters (even those that are unused)
        freq = [ 0 ] * 26
        for c in word:
            freq[ord(c) - ord("a")] += 1
        freq.sort()

        for pushes in range(1, 4+1):    # at most four letters per key
            for digit in range(2, 9+1): # 8 keys (2...9)
                if freq:
                    result += pushes * freq.pop()

        return result
