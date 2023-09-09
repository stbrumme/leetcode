class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return len(word) == 1 or word.isupper() or word[1:].islower()
