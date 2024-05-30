class Solution:
    def numberOfWays(self, s: str) -> int:
        result = 0

        # only "010" or "101"
        nil010 = nil101 = 1
        one010 = one101 = 0
        two010 = two101 = 0
        for c in s:
            if c == "0":
                one010 += nil010
                two101 += one101
                result += two010
            else:
                one101 += nil101
                two010 += one010
                result += two101

        return result
