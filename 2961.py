class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        for i, (a, b, c, m) in enumerate(variables):
            inner = pow(a, b, 10)
            outer = pow(inner, c, m)
            if outer == target:
                yield i
