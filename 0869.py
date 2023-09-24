class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        nn  = str(n)
        two = 1
        while len(str(two)) <  len(nn):
            two <<= 1

        while len(str(two)) == len(nn):
            if sorted(str(two)) == sorted(nn):
                return True

            two <<= 1

        return False
