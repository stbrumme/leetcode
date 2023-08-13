class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = { "a", "e", "i", "o", "u", "A", "E", "I", "O", "U" }
        v = []
        for c in s:
            if c in vowels:
                v.append(c)

        result = ""
        for c in s:
            if c in vowels:
                result = result + v.pop()
            else:
                result = result + c

        return result
