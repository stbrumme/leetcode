class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = defaultdict(int)
        last  = defaultdict(int)
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        result = -1
        for l in last:
            distance = last[l] - first[l]
            if distance > 0:
                result = max(result, distance - 1)
        return result
