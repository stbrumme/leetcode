class Solution:
    def countOrders(self, n: int) -> int:
        # testcases 1,2,3,4,5,6 produce the sequence 1,6,90,2520,113400,7484400
        # which can be found in OEIS (https://oeis.org/A000680)
        return (factorial(2 * n) // 2**n) % (10**9 + 7)
