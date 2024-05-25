class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        result = 0

        size = len(s)
        for i in range(size):
            have = defaultdict(int)
            for j in range(i, size):
                c = s[j]
                have[c] += 1
                if have[c] > 2:
                    break

                result = max(result, j - i + 1)

        return result
