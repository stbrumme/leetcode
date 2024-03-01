class Solution:
    def appealSum(self, s: str) -> int:
        result = 0

        # 1) adding a new character to a string of length n creates n new substrings

        # 2) adding an already known character to a string, doesn't change its appeal
        # 3) but adding a new character, increases it by one

        # that means that when adding characters,
        # only the substrings since the last appearance of that character are relevant:
        # they all increment their appeal by one

        prev = [ -1 ] * 26 # previous index of that character
        diff = 0
        for i, c in enumerate(s):
            index = ord(c) - ord("a") # a => 0, b => 1, etc.

            # get and update distance to previous occurence of the same character
            distance    = i - prev[index]
            prev[index] = i

            diff   += distance
            result += diff

        return result
