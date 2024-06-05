class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        result = 0

        # track each letter in a bitmask:
        # the i-th bit is 0 if the i-letter was encountered an even number of times
        # 10 letters => at most 2^10 = 1024 combinations
        have = defaultdict(int)

        # empty string => even count for each letter
        mask = 0
        have[mask] = 1

        for c in word:
            mask ^= 1 << (ord(c) - 97) # ord("a") == 97

            # a string between two identical masks:
            # difference = 0, therefore even count for all letters
            result += have[mask]

            # string between masks which differ by exactly one bit:
            # even count for all letters except one
            for odd in range(10):
                outlier = 1 << odd
                result += have[mask ^ outlier]

            have[mask] += 1

        return result
