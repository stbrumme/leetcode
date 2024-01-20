class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        result = 0
        for w in text.split(" "):
            result += 0 if any(b in w for b in brokenLetters) else 1
        return result
