class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        # hash(pos - 1) = p * hash(p) minus the last element

        result = ""

        # a = 1, ..., z = 26
        ascii2num = lambda c : ord(c) - ord("a") + 1
        pk = pow(power, k, modulo) # precomputed constant

        size = len(s)
        have = 0 # length of sliding window
        hash = 0
        for i in reversed(range(size)):
            # add character (left side)
            hash *= power
            hash += ascii2num(s[i])
            have += 1

            # remove character (right side)
            if have > k:
                last  = ascii2num(s[i + k])
                hash -= last * pk
                have -= 1

            hash %= modulo
            if hash == hashValue:
                result = i

        return s[result : result + k]
