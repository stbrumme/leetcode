class Solution:
    def largestInteger(self, num: int) -> int:
        s = str(num)

        parity = [ int(c) & 1 for c in s ]
        digits = { 0: [], 1: [] }
        for i in range(len(s)):
            digits[parity[i]].append(s[i])

        # reverse order makes more sense, but popping the last item in the following loop is faster
        digits[0].sort()
        digits[1].sort()

        result = ""
        for p in parity:
            result += digits[p].pop()
        return int(result)
