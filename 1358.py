class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        result = 0

        freq = { "a": 0, "b": 0, "c": 0 }

        right = 0
        for left in range(len(s)):
            # find minimal string starting at "left"
            while right < len(s) and freq["a"] * freq["b"] * freq["c"] == 0: # zero if at least one counter is zero
                freq[s[right]] += 1
                right          += 1

            # no more valid strings
            if freq["a"] * freq["b"] * freq["c"] == 0:
                break

            # all strings from "right" to the end are valid
            result += len(s) - right + 1
            freq[s[left]] -= 1

        return result
