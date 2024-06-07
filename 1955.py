class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        modulo = 1_000_000_007
        # number of sequences ending with 0, 1 or 2
        zero = 0
        one  = 0
        two  = 0

        for i, n in enumerate(nums):
            if   n == 0:
                zero += zero + 1
            elif n == 1:
                one  += one  + zero
            elif n == 2:
                two  += two  + one

            # modulo every now and then ... (it's slow)
            if (i & 15) == 0:
                zero %= modulo
                one  %= modulo
                two  %= modulo

        return two % modulo
