class Solution:
    def thousandSeparator(self, n: int) -> str:
        return f"{n:,}".replace(",", ".") # workaround: dot is a special symbol for F-strings
