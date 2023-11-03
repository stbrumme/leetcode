class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        # brute-force
        result = ""
        for i, c in enumerate(number):
            if c == digit:
                compare = number[:i] + number[i + 1:]
                result  = max(result, compare)
        return result
