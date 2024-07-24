class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        # 0 OR 0 == 0,   0 XOR 0 == 0
        # 0 OR 1 == 1,   0 XOR 1 == 1
        # 1 OR 0 == 1,   1 XOR 0 == 1
        # 1 OR 1 == 1,   1 XOR 1 == 0

        # if target contains "0" but source is "1" at the same index,
        # then we need at least one "1" in source to convert it to "0"
        # (with 1 XOR 1 == 0), there's no other way

        # any other bit pattern can be easily created
        return ("1" in s and "1" in target) or s == target
