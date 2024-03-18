class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        # all positions where "a" is found in "s"
        one = []
        for pos in range(len(s)):
            if s[pos : pos + len(a)] == a:
                one.append(pos)

        o = 0 # index in one[]

        # all positions where "b" is found in "s"
        for pos in range(len(s)):
            if s[pos : pos + len(b)] == b:
                # skip matches too far away
                while o < len(one) and pos - one[o] > k:
                    o += 1

                # found a match (or multiple)
                while o < len(one) and abs(pos - one[o]) <= k:
                    yield one[o]
                    o += 1
