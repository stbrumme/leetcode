class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0

        have = defaultdict(int)
        # sliding window
        left = 0
        for right, c in enumerate(s):
            # find most frequent character
            have[c] += 1
            dominant = max(have.values())

            # replace any other character
            length   = right - left + 1
            other    = length - dominant

            # shrink window if too many other characters
            if other > k:
                have[s[left]] -= 1
                left   += 1
                length -= 1

            result = max(result, length)

        return result
