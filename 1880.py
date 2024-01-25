class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def value(s):
            result = 0
            for c in s:
                result *= 10
                result += "abcdefghij".index(c)
            return result

        return value(firstWord) + value(secondWord) == value(targetWord)
