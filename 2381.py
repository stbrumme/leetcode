class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        result = ""

        size  = len(s)
        delta = [ 0 ] * (size + 1) # last index isn't used
        for start, end, direction in shifts:
            d = 2 * direction - 1 # 0 => -1, 1 => +1
            delta[start]   += d
            delta[end + 1] -= d

        a = ord("a")
        have = 0 # accumulated delta
        for c, d in zip(s, delta):
            have   += d
            ascii   = ord(c) - a
            ascii  += have
            ascii  %= 26
            result += chr(ascii + a)

        return result
