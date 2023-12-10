class Solution:
    def secondHighest(self, s: str) -> int:
        digits = set()
        for c in s:
            if "0" <= c <= "9":
                digits.add(int(c))
        return sorted(digits)[-2] if len(digits) >= 2 else -1
