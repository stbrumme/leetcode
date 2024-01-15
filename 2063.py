class Solution:
    def countVowels(self, word: str) -> int:
        result = 0
        for i, c in enumerate(word):
            if c in "aeiou":
                left  = i + 1          # prefix
                right = len(word) - i  # suffix
                result += left * right # all combinations of prefix and suffix
        return result
