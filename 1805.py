class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        clean = ""
        for c in word:
            clean += c if c >= "0" and c <= "9" else " "

        # note: two consecutive spaces => empty string after split, do not convert to zero
        return len(set([ int(n) for n in clean.split(" ") if n != "" ]))
