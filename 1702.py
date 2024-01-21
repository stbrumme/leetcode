class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        # a sequence "00...00" can become "11...10" (operation 1)
        # zeros at the end can be shifted left      (operation 2)
        # in the end only one zero will remain

        # keep all 1's on the left side, then count all zeros
        left = 0
        while left < len(binary) and binary[left] == "1":
            left += 1

        zeros = binary.count("0")
        if zeros == 0:
            return binary

        left += zeros - 1
        right = len(binary) - left - 1
        return "1" * left + "0" + "1" * right
