class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        size = len(arr)

        # reject if impossible
        total = sum(arr)
        if total % 3 != 0:
            return [ -1, -1 ]

        # only zeros
        if total == 0:
            return [ 0, size - 1 ] # [ 0, 1 ] should be valid, too, but is rejected

        # number of 1s per part
        need = total // 3

        have    = 0
        pattern = ""
        # extract a substring such that it start and ends with "1" and has one third of all "1"
        for pos in range(size):
            x = arr[pos]
            have += x
            if pattern or have == 1:
                pattern += str(x)
            if have == need:
                break

        # trailing zeros
        last = len(arr) - 1
        while arr and arr[last] == 0:
            last    -= 1
            pattern += "0"

        # find pattern three times
        all = "".join(str(a) for a in arr)
        pos = -len(pattern)
        split = []
        for _ in range(3):
            pos = all.find(pattern, pos + len(pattern))
            if pos == -1: # not found
                return [ -1, -1 ]

            split.append(pos + len(pattern))

        return [ split[0] - 1, split[1] ]
