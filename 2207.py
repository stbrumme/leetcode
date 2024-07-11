class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        # prepend pattern[0] or append pattern[1]
        one = pattern[0]
        two = pattern[1]

        prepend1 = 1 # prepend pattern[0]
        prepend2 = 0
        append1  = 0
        append2  = 0

        for c in text:
            # order of these ifs is important if pattern[0] == pattern[1]
            if c == two:
                prepend2 += prepend1
                append2  += append1
            if c == one:
                prepend1 += 1
                append1  += 1

        append2 += append1 # append pattern[1]

        return max(prepend2, append2)
