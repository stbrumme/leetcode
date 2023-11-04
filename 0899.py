class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # brute forcing test data showed that if k > 1 then s will be sorted
        if k > 1:
            return "".join(sorted(s))

        # and if k == 1 then s will be rotated
        result = s
        high, low = max(s), min(s)
        if high == low:
            return s # only one letter that is repeated
        for i in range(len(s)):
            if s[i] == low:
                rotated = s[i:] + s[:i]
                result  = min(result, rotated)
        return result
