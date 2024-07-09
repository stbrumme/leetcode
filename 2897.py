class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        result = 0

        # idea:
        # all bits are independently affected by AND / OR
        # updating two values breaks down into just four cases:
        # 0, 0 => 0 AND 0 = 0, 0 OR 0 = 0    => nothing changed
        # 0, 1 => 0 AND 1 = 0, 0 OR 1 = 1    => nothing changed
        # 1, 0 => 1 AND 0 = 0, 1 OR 0 = 1    => (1, 0) becomes (0, 1)
        # 1, 1 => 1 AND 1 = 1, 1 OR 1 = 1    => nothing changed
        # when updating two values a and b where a <= b
        # then a gets potentially smaller and b potentially bigger

        # bigger is better because the square of large value gets even larger
        # in the end we combine numbers until as many bits as possible are set
        # in the selection of k values

        # count bits
        freq = defaultdict(int)
        for n in nums:
            while n:
                prev = n
                n   &= n - 1        # chop off lowest bit
                freq[prev ^ n] += 1 # increment its counter

        # convert to array
        have = [ 0 ] * 32 # counter per bit position
        for f, c in freq.items():
            have[f.bit_length() - 1] = c
        # remove high bits if unused
        while have and have[-1] == 0:
            have.pop()

        # build the k largest numbers
        for _ in range(k):
            n = 0
            for i, c in enumerate(have):
                if c > 0:
                    n |= 1 << i
                    have[i] -= 1

            result += n * n # fits in 64 bits, therefore is faster to delay modulo

        return result % 1_000_000_007
