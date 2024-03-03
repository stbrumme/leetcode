class Solution:
    def splitString(self, s: str) -> bool:
        # skip most leading zeros
        while len(s) > 2 and s[: 2] == "0":
            s = s[1 :]

        size = len(s)

        def deeper(pos, need):
            # end of string
            if pos == size:
                return True

            # skip leading zeros
            while pos < size and s[pos] == "0":
                pos += 1
            if pos == size:
                return need == 0

            # try every possible substring
            for stop in range(pos + 1, size + 1):
                have = int(s[pos : stop])
                if have == need:
                    return deeper(stop, have - 1)

                if have >  need: # abort, too large
                    return False

            return False

        # all strings of length [1, size - 1]
        for i in range(1, size):
            have = int(s[:i])
            if deeper(i, have - 1):
                return True

        return False
