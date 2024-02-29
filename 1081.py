class Solution:
    def smallestSubsequence(self, s: str) -> str:
        result = ""

        # count chars
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1

        need = set(s)
        for c in s:
            # adjust counter
            freq[c] -= 1
            if c not in need:
                continue

            # check last char: if it's (lexicographically) larger and will appear again in s
            # then replace it by the current character
            while result and result[-1] > c and freq[result[-1]] > 0:
                need.add(result[-1])
                result = result[: -1]

            result += c
            need.discard(c)

        return result
