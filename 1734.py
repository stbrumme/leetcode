class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        # this is a pure math problem, not a programming problem
        size = len(encoded) + 1

        # XOR of 1...size
        all  = reduce(lambda a, b: a ^ b, range(1, size + 1))

        # encoded is: a^b, b^c, c^d, d^e, e^f, f^g, ... so that each value appears twice
        # except for the first and the last value
        # skipping every odd element/pair of encoded, each value appears only once:
        #             a^b,      c^d,      e^f, ...
        have = reduce(lambda a, b: a ^ b, encoded[::2])       # XOR of encoded
        # the only missing element is the final number
        # (it took me some time to note that n is always odd, so encoded has always an even length)
        result = [ all ^ have ]
        # now we have all we need and
        # let's build the whole result in reverse
        while encoded:
            result.append(result[-1] ^ encoded.pop())

        return reversed(result)
