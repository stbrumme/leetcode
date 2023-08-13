class Solution:
    def countSegments(self, s: str) -> int:
        s = re.sub(" +", " ", s)
        s = re.sub("(^ +| +$)", "", s)

        if len(s) == 0:
            return 0

        result = 1
        for c in s:
            if c == ' ':
                result += 1
        return result
