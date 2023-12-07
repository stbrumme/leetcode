class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        result = 0 # empty string has an even number of vowels

        # position of vowels in our state "have"
        mapping = { "a": 0, "e": 1, "i": 2, "o": 3, "u": 4 }
        have    = [ 0, 0, 0, 0, 0 ] # number of vowels a/e/i/o/u
        state   = 0
        first   = { state: -1 }     # before the first characters we have zero vowels

        for i, c in enumerate(s):
            # new vowel
            if c in mapping:
                # update counter
                have[mapping[c]] += 1

                # update state
                state = 0
                # merge lowest bits (0 if even)
                for h in have:
                    state <<= 1
                    state  |= h & 1

                # first time we encounter this state
                if state not in first:
                    first[state] = i


            # find longest substring which starts and end with the same state
            # => inbetween those we have an even number of each vowel
            distance = i - first[state]
            result   = max(result, distance)

        return result
