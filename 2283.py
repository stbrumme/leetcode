class Solution:
    def digitCount(self, num: str) -> bool:
        freq = [ 0 ] * 10
        for n in num:
            freq[int(n)] += 1

        return all(int(n) == f for n, f in zip(num, freq))
