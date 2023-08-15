class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1

        all = defaultdict(str)
        for f in freq:
            all[freq[f]] += f

        result = ""
        high = max(freq.values())
        for i in range(high + 1, 0, -1):
            for j in all[i]:
                result += j * i

        return result
