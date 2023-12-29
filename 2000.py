class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        pos = word.find(ch)
        if pos < 0:
            return word

        prefix = word[ : pos + 1]
        suffix = word[pos + 1 : ]
        return prefix[::-1] + suffix
