class Solution:
    def sortString(self, s: str) -> str:
        result = ""

        freq = defaultdict(int)
        for c in s:
            freq[c] += 1

        alphabet = "".join(sorted(freq))
        while len(result) < len(s):
            for c in alphabet:
                if freq[c] > 0:
                    result += c
                    freq[c] -= 1

            for c in alphabet[::-1]:
                if freq[c] > 0:
                    result += c
                    freq[c] -= 1

        return result
