class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        modulo = 1_000_000_007

        # number of sequences ending with zero or one
        zero = 0
        one  = 0
        both = 0 # zero + one
        null = 0 # 1 if at least one "0" was found

        for c in binary:
            if c == "0":
                zero = both
                null = 1
            else:
                one  = both + 1 # and start a new sequence

            both = (zero + one) % modulo

        return (both + null) % modulo
