class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1

        # impossible ?
        if freq["a"] < k or freq["b"] < k or freq["c"] < k:
            return -1
        # nothing to do
        if k == 0:
            return 0

        # assume to always take from the right side
        result = len(s)
        right  = -len(s) # Python's minus-notation => take from right side
        for left in range(len(s)):
            # one less from the right side until k-requirement is violated
            while right < 0 and freq[s[right]] > k and freq["a"] >= k and freq["b"] >= k and freq["c"] >= k:
                freq[s[right]] -= 1
                right          += 1

            result = min(result, left - right) # remember: right has Python's minus-notation

            # one more from the left side
            freq[s[left]] += 1

        return result
