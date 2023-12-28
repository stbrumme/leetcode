class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        # generic Gray-Code (as strings)
        have = [ "" ]
        for bits in range(n):
            more = []
            for h in have:
                more.append("0" + h)
            for h in have[::-1]:
                more.append("1" + h)
            have = more

        # convert to ints
        binary = [ int(h, 2) for h in have ]

        # rotate such that it starts with "start"
        pos    = binary.index(start)
        return binary[pos : ] + binary[ : pos]
