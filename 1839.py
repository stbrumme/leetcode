class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        result = 0

        # next vowel
        next   = { "a": "e", "e": "i", "i": "o", "o": "u" }

        prev   = ""    # last vowel
        length = 0     # length of currently processed substring
        valid  = False # true if current character belongs to a sequence starting with "a"
        for c in word:
            # must start with "a"
            if not valid:
                if c == "a":
                    valid  = True
                    length = 1
            # same vowel or next vowel in alphabetical order
            elif c == prev or c == next.get(prev, ""):
                length += 1
            # abort
            else:
                if c == "a":
                    length = 1     # immediately restart new sequence
                else:
                    valid  = False # keep idling, wait for "a"

            prev = c

            # sequence complete (but there may be more "u")
            if valid and c == "u":
                result = max(result, length)

        return result
