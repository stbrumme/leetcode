class Solution:
    def minChanges(self, s: str) -> int:
        # count "01" / "10" (starting at even offsets in s)
        sys.set_int_max_str_digits(0)
        a = int(s[0::2], 2)
        b = int(s[1::2], 2)
        return (a ^ b).bit_count()
