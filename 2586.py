class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        result = 0
        for i in range(left, right + 1):
            w = words[i]
            if w[0] in "aeiou" and w[-1] in "aeiou":
                result += 1
        return result
