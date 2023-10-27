class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(0) # unlimited
        x  = int("".join([ str(n) for n in num ]))
        return [ int(c) for c in str(x + k) ]
