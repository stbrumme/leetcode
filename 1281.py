class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [ int(d) for d in str(n) ]
        return reduce(mul, digits) - reduce(add, digits)
