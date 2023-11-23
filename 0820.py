class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # if two words share the same suffix, then their reverse representation shares the same prefix
        reverse = [ w[::-1] for w in words ]

        result = 0
        prev = "STOP" # words are only lowercase, so I need an "invalid" string for bootstrapping
        for r in sorted(reverse):
            # add string
            result += len(r) + 1
            # merge with previous if possible
            if len(prev) <= len(r) and r.startswith(prev):
                result -= len(prev) + 1
            prev = r

        return result
