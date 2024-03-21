class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        a = b = 0
        for c in seq:
            left  = a < b    # 1 if True else 0
            right = left ^ 1 # same as 1 - left

            if c == "(":
                a +=  left
                b +=  right
                yield right
            else:
                a -=  right
                b -=  left
                yield left
