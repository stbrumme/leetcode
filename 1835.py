class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        # XOR of arr1
        one = reduce(xor, arr1)
        # AND that number with each of arr2
        two = map(lambda x: x & one, arr2)
        # XOR the results
        return reduce(xor, two)
