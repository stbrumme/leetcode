class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        streak  = 0
        padding = [ 0 ] * k
        for n in padding + nums + padding:
            if n == 0:
                streak += 1
            else: # n == 1
                if streak < k:
                    return False
                streak  = 0

        return True
