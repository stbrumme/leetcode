class Solution:
    def reformat(self, s: str) -> str:
        # split
        digits  = []
        letters = []
        for c in s:
            if "0" <= c <= "9":
                digits .append(c)
            else:
                letters.append(c)

        # at most differ by one
        if abs(len(digits) - len(letters)) > 1:
            return ""

        # merge
        result = ""
        pickDigit = len(digits) >= len(letters)
        while len(result) < len(s):
            result += digits.pop() if pickDigit else letters.pop()
            pickDigit = not pickDigit
        return result
