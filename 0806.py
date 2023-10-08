class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        pixels = 0
        lines  = 1
        for c in s:
            add = widths[ord(c) - ord("a")]
            if pixels + add > 100:
                pixels = 0
                lines += 1

            pixels += add

        return [ lines, pixels ]
