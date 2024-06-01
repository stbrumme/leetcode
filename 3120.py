class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        return sum([ chr(ord(c) + 32) in word for c in set(word) ])
